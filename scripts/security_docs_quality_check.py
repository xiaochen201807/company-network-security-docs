#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Security Program documentation quality checker.

Pure Python standard library. Suitable for local runs and Jenkins/CI.

Exit codes:
  0: no blocking findings
  1: ERROR findings exist
  2: strict mode and WARNING findings exist
  3: checker runtime/configuration failure
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional


BACKTICK_FENCE = chr(96) * 3
CONTROL_ID_RE = re.compile(r"\bSEC-[A-Z][A-Z0-9]{1,7}-\d{3}\b")
CORE_FILE_RE = re.compile(r"^(\d{2})-.*\.md$")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
H1_RE = re.compile(r"^#\s+\S")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
UNCHECKED_RE = re.compile(r"^- \[ \]\s+", re.M)

EXPECTED_CORE_RANGE = range(0, 31)

REQUIRED_GOVERNANCE = (
    "docs/governance/README.md",
    "docs/governance/security-control-catalog.md",
    "docs/governance/security-current-target-profile.md",
    "docs/governance/security-raci.md",
    "docs/governance/company-security-parameters-register.md",
    "docs/governance/document-hierarchy-and-maintenance.md",
)

REQUIRED_NAVIGATION = (
    "docs/knowledge-map.md",
    "docs/obsidian-usage.md",
)

REQUIRED_HIERARCHY_ARTIFACTS = (
    "docs/policies/information-security-policy.md",
    "docs/procedures/critical-vulnerability-sop.md",
    "docs/procedures/employee-offboarding-sop.md",
    "docs/playbooks/account-compromise-playbook.md",
    "docs/playbooks/secret-leak-playbook.md",
)

REQUIRED_TEMPLATES = (
    "docs/templates/asset-inventory-template.md",
    "docs/templates/access-request-and-review-template.md",
    "docs/templates/vulnerability-record-template.md",
    "docs/templates/vulnerability-exception-template.md",
    "docs/templates/penetration-test-authorization-template.md",
    "docs/templates/monthly-vulnerability-report-template.md",
    "docs/templates/security-incident-report-template.md",
    "docs/templates/backup-recovery-exercise-template.md",
    "docs/templates/audit-finding-remediation-template.md",
    "docs/templates/security-baseline-check-template.md",
    "docs/templates/threat-model-template.md",
    "docs/templates/product-security-release-checklist.md",
    "docs/templates/psirt-case-template.md",
    "docs/templates/crypto-inventory-template.md",
    "docs/templates/ai-security-review-template.md",
    "docs/templates/mobile-security-checklist.md",
    "docs/templates/privacy-impact-assessment-template.md",
    "docs/templates/third-party-security-assessment-template.md",
    "docs/templates/business-impact-analysis-template.md",
    "docs/templates/email-phishing-incident-template.md",
)

EXPECTED_SPLITS = {
    "08": {
        "index": "docs/08-devsecops-and-supply-chain.md",
        "archive": "docs/08-devsecops/reference-full-v1.md",
        "dir": "docs/08-devsecops",
        "minimum_subdocs": 7,
    },
    "09": {
        "index": "docs/09-vulnerability-and-penetration-testing.md",
        "archive": "docs/09-vulnerability/reference-full-v1.md",
        "dir": "docs/09-vulnerability",
        "minimum_subdocs": 6,
    },
}

STALE_ACTIVE_MARKERS = (
    "V0.1 文档骨架",
    "V1.0 基础体系完成版",
    "V1.1 进阶安全体系版",
    "00～24 已形成",
)


@dataclass
class Finding:
    severity: str
    check: str
    message: str
    path: Optional[str] = None
    line: Optional[int] = None
    remediation: Optional[str] = None


@dataclass
class Control:
    control_id: str
    requirement: str
    level: str
    owner: str
    evidence: str
    frequency: str
    metric: str
    source: str
    line: int


class QualityChecker:
    def __init__(self, root: Path, max_active_lines: int = 1000) -> None:
        self.root = root.resolve()
        self.docs_dir = self.root / "docs"
        self.readme = self.root / "README.md"
        self.max_active_lines = max_active_lines
        self.findings: list[Finding] = []
        self.metrics: dict[str, object] = {}
        self.controls: list[Control] = []
        self._texts: dict[Path, str] = {}

    def add(
        self,
        severity: str,
        check: str,
        message: str,
        path: Optional[Path | str] = None,
        line: Optional[int] = None,
        remediation: Optional[str] = None,
    ) -> None:
        if isinstance(path, Path):
            try:
                path = str(path.resolve().relative_to(self.root))
            except ValueError:
                path = str(path)
        self.findings.append(
            Finding(
                severity=severity,
                check=check,
                message=message,
                path=path,
                line=line,
                remediation=remediation,
            )
        )

    def rel(self, path: Path) -> str:
        return str(path.resolve().relative_to(self.root))

    def read(self, path: Path) -> str:
        path = path.resolve()
        if path not in self._texts:
            self._texts[path] = path.read_text(encoding="utf-8")
        return self._texts[path]

    def markdown_files(self) -> list[Path]:
        files: list[Path] = []
        if self.readme.exists():
            files.append(self.readme)
        if self.docs_dir.exists():
            files.extend(sorted(self.docs_dir.rglob("*.md")))
        return files

    @staticmethod
    def is_archive(path: Path) -> bool:
        return path.name.startswith("reference-full-") or "references" in path.parts

    @staticmethod
    def is_template(path: Path) -> bool:
        return "templates" in path.parts

    def run(self) -> dict[str, object]:
        if not self.readme.exists() or not self.docs_dir.exists():
            raise RuntimeError("README.md or docs/ not found; root must point to project root.")

        files = self.markdown_files()
        self.metrics["markdown_files"] = len(files)
        self.metrics["total_lines"] = sum(len(self.read(p).splitlines()) for p in files)

        self.check_markdown_structure(files)
        self.check_internal_links(files)
        self.check_wikilinks(files)
        self.check_obsidian_metadata(files)
        self.check_core_docs()
        self.check_required_artifacts()
        self.check_readme_navigation()
        self.check_knowledge_map()
        self.check_document_size(files)
        self.check_split_architecture()
        self.check_metadata()
        self.check_control_catalog(files)
        self.check_current_target_profile()
        self.check_parameters_register()
        self.check_stale_markers(files)
        self.check_open_items(files)
        self.check_orphans(files)

        counts = Counter(f.severity for f in self.findings)
        self.metrics["findings"] = dict(counts)
        self.metrics["errors"] = counts["ERROR"]
        self.metrics["warnings"] = counts["WARNING"]
        self.metrics["infos"] = counts["INFO"]
        self.metrics["documentation_quality"] = self.quality_summary()

        return {
            "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "project_root": str(self.root),
            "metrics": self.metrics,
            "findings": [asdict(f) for f in self.findings],
        }

    def check_markdown_structure(self, files: Iterable[Path]) -> None:
        invalid_h1 = 0
        unbalanced = 0
        heading_jumps = 0

        for path in files:
            text = self.read(path)
            lines = text.splitlines()
            h1s = [i for i, line in enumerate(lines, 1) if H1_RE.match(line)]
            if len(h1s) != 1:
                invalid_h1 += 1
                self.add(
                    "ERROR",
                    "markdown.h1",
                    f"Expected exactly one H1, found {len(h1s)}.",
                    path,
                    remediation="Keep exactly one document title using H1.",
                )

            for fence in ("~~~", BACKTICK_FENCE):
                count = sum(1 for line in lines if line.lstrip().startswith(fence))
                if count % 2:
                    unbalanced += 1
                    self.add(
                        "ERROR",
                        "markdown.fence",
                        f"Unbalanced code fence: {count} fence lines.",
                        path,
                    )

            previous = 0
            in_fence = False
            fence_token: Optional[str] = None
            for lineno, line in enumerate(lines, 1):
                stripped = line.lstrip()
                token = None
                if stripped.startswith("~~~"):
                    token = "~~~"
                elif stripped.startswith(BACKTICK_FENCE):
                    token = BACKTICK_FENCE
                if token:
                    if not in_fence:
                        in_fence, fence_token = True, token
                    elif token == fence_token:
                        in_fence, fence_token = False, None
                    continue
                if in_fence:
                    continue
                match = HEADING_RE.match(line)
                if not match:
                    continue
                level = len(match.group(1))
                if previous and level > previous + 1:
                    heading_jumps += 1
                    self.add(
                        "WARNING",
                        "markdown.heading_level",
                        f"Heading jumps from H{previous} to H{level}.",
                        path,
                        lineno,
                    )
                previous = level

        self.metrics["markdown_invalid_h1"] = invalid_h1
        self.metrics["markdown_unbalanced_fences"] = unbalanced
        self.metrics["markdown_heading_jumps"] = heading_jumps

    def check_internal_links(self, files: Iterable[Path]) -> None:
        broken = 0
        for path in files:
            text = self.read(path)
            for match in MD_LINK_RE.finditer(text):
                target = match.group(1).strip()
                if (
                    not target
                    or target.startswith("#")
                    or "://" in target
                    or target.startswith("mailto:")
                    or target.startswith("tel:")
                ):
                    continue
                local_target = target.split("#", 1)[0].split("?", 1)[0]
                if not local_target:
                    continue
                candidate = (path.parent / local_target).resolve()
                if not candidate.exists():
                    broken += 1
                    line = text[: match.start()].count("\n") + 1
                    self.add(
                        "ERROR",
                        "link.broken",
                        f"Broken relative link: {target}",
                        path,
                        line,
                    )
        self.metrics["broken_links"] = broken

    def resolve_wikilink(self, source: Path, target: str) -> Optional[Path]:
        target = target.split("|", 1)[0].split("#", 1)[0].strip()
        if not target:
            return None
        if target.startswith(("http://", "https://", "mailto:", "obsidian://")):
            return None

        raw = Path(target)
        candidates = []
        if raw.suffix:
            candidates.extend([self.root / raw, source.parent / raw])
        else:
            candidates.extend([
                self.root / (target + ".md"),
                source.parent / (target + ".md"),
            ])

        for candidate in candidates:
            if candidate.exists():
                return candidate.resolve()

        if "/" not in target:
            matches = list(self.root.rglob(target + ".md"))
            if len(matches) == 1:
                return matches[0].resolve()
        return Path("__MISSING__")

    def check_wikilinks(self, files: Iterable[Path]) -> None:
        broken = 0
        total = 0
        for path in files:
            text = self.read(path)
            for match in WIKI_LINK_RE.finditer(text):
                target = match.group(1)
                resolved = self.resolve_wikilink(path, target)
                if resolved is None:
                    continue
                total += 1
                if resolved == Path("__MISSING__"):
                    broken += 1
                    line = text[: match.start()].count("\n") + 1
                    self.add(
                        "ERROR",
                        "obsidian.wikilink_broken",
                        f"Broken Obsidian WikiLink: [[{target}]]",
                        path,
                        line,
                    )

        self.metrics["wikilinks"] = {
            "total": total,
            "broken": broken,
        }

    @staticmethod
    def extract_frontmatter(text: str) -> Optional[str]:
        if not text.startswith("---\n"):
            return None
        end = text.find("\n---\n", 4)
        if end == -1:
            return None
        return text[4:end]

    def check_obsidian_metadata(self, files: Iterable[Path]) -> None:
        docs_files = [p for p in files if self.docs_dir in p.resolve().parents]
        required_keys = {
            "aliases",
            "type",
            "domain",
            "phase",
            "priority",
            "status",
            "tags",
        }

        with_frontmatter = 0
        property_problems = 0
        core_relation_blocks = 0

        for path in docs_files:
            text = self.read(path)
            frontmatter = self.extract_frontmatter(text)
            is_core = bool(CORE_FILE_RE.match(path.name)) and path.parent.resolve() == self.docs_dir.resolve()

            if frontmatter is None:
                severity = "ERROR" if is_core else "WARNING"
                self.add(
                    severity,
                    "obsidian.frontmatter_missing",
                    "Obsidian YAML Properties frontmatter is missing.",
                    path,
                )
                property_problems += 1
                continue

            with_frontmatter += 1
            keys = {
                match.group(1)
                for match in re.finditer(r"^([A-Za-z][A-Za-z0-9_-]*):", frontmatter, re.M)
            }
            missing = sorted(required_keys - keys)
            if missing:
                severity = "ERROR" if is_core else "WARNING"
                self.add(
                    severity,
                    "obsidian.property_missing",
                    "Missing Obsidian Properties: " + ", ".join(missing),
                    path,
                )
                property_problems += 1

            if "security" not in frontmatter:
                self.add(
                    "WARNING",
                    "obsidian.security_tag",
                    "Frontmatter does not include the base security tag.",
                    path,
                )
                property_problems += 1

            if is_core:
                if "parent:" not in frontmatter or "[[docs/knowledge-map]]" not in frontmatter:
                    self.add(
                        "ERROR",
                        "obsidian.parent",
                        "Core document must point to docs/knowledge-map in parent property.",
                        path,
                    )
                    property_problems += 1

                start_count = text.count("<!-- obsidian-relations:start -->")
                end_count = text.count("<!-- obsidian-relations:end -->")
                if start_count == 1 and end_count == 1:
                    core_relation_blocks += 1
                else:
                    self.add(
                        "ERROR",
                        "obsidian.relation_block",
                        f"Core document relation block markers invalid: start={start_count}, end={end_count}.",
                        path,
                    )

        self.metrics["obsidian"] = {
            "docs_files": len(docs_files),
            "frontmatter_files": with_frontmatter,
            "frontmatter_coverage_percent": round(
                with_frontmatter / len(docs_files) * 100, 1
            ) if docs_files else 0.0,
            "property_problems": property_problems,
            "core_relation_blocks": core_relation_blocks,
            "core_relation_expected": len(list(EXPECTED_CORE_RANGE)),
        }

    def check_core_docs(self) -> None:
        by_num: dict[int, list[Path]] = defaultdict(list)
        for path in self.docs_dir.glob("*.md"):
            match = CORE_FILE_RE.match(path.name)
            if match:
                by_num[int(match.group(1))].append(path)

        missing: list[int] = []
        duplicates: list[int] = []
        for num in EXPECTED_CORE_RANGE:
            found = by_num.get(num, [])
            if not found:
                missing.append(num)
                self.add("ERROR", "core.missing", f"Missing core document {num:02d}-*.md.", "docs")
            elif len(found) > 1:
                duplicates.append(num)
                self.add(
                    "ERROR",
                    "core.duplicate",
                    f"Multiple core documents use prefix {num:02d}: "
                    + ", ".join(p.name for p in found),
                    "docs",
                )

        self.metrics["core_docs_expected"] = len(list(EXPECTED_CORE_RANGE))
        self.metrics["core_docs_present"] = len(list(EXPECTED_CORE_RANGE)) - len(missing)
        self.metrics["core_docs_missing"] = missing
        self.metrics["core_docs_duplicate_prefixes"] = duplicates

    def check_required_artifacts(self) -> None:
        groups = {
            "navigation": REQUIRED_NAVIGATION,
            "governance": REQUIRED_GOVERNANCE,
            "hierarchy": REQUIRED_HIERARCHY_ARTIFACTS,
            "templates": REQUIRED_TEMPLATES,
        }
        stats: dict[str, object] = {}
        for name, paths in groups.items():
            missing = []
            for relpath in paths:
                if not (self.root / relpath).exists():
                    missing.append(relpath)
                    self.add(
                        "ERROR",
                        f"required.{name}",
                        f"Required artifact missing: {relpath}",
                        relpath,
                    )
            stats[name] = {
                "expected": len(paths),
                "present": len(paths) - len(missing),
                "missing": missing,
            }
        self.metrics["required_artifacts"] = stats

    def check_readme_navigation(self) -> None:
        text = self.read(self.readme)
        missing_core = []
        for num in EXPECTED_CORE_RANGE:
            candidates = sorted(self.docs_dir.glob(f"{num:02d}-*.md"))
            if not candidates:
                continue
            relpath = self.rel(candidates[0])
            if relpath not in text:
                missing_core.append(relpath)
                self.add(
                    "WARNING",
                    "readme.navigation",
                    f"Core document is not linked from README: {relpath}",
                    self.readme,
                )
        for relpath in REQUIRED_GOVERNANCE:
            if relpath not in text:
                self.add(
                    "WARNING",
                    "readme.governance_navigation",
                    f"Governance artifact not linked from README: {relpath}",
                    self.readme,
                )
        self.metrics["readme_missing_core_links"] = missing_core

        for relpath in REQUIRED_NAVIGATION:
            if relpath not in text:
                self.add(
                    "ERROR",
                    "readme.knowledge_map",
                    f"Knowledge map is not linked from README: {relpath}",
                    self.readme,
                )

    def check_knowledge_map(self) -> None:
        path = self.root / "docs/knowledge-map.md"
        if not path.exists():
            self.add(
                "ERROR",
                "knowledge_map.missing",
                "Security knowledge map is missing.",
                path,
            )
            return

        text = self.read(path)
        mermaid_count = text.count("~~~mermaid")
        if mermaid_count < 3:
            self.add(
                "WARNING",
                "knowledge_map.visual_depth",
                f"Knowledge map contains only {mermaid_count} Mermaid diagrams; expected at least 3.",
                path,
            )

        missing_core = []
        for num in EXPECTED_CORE_RANGE:
            candidates = sorted(self.docs_dir.glob(f"{num:02d}-*.md"))
            if not candidates:
                continue
            relative_from_map = candidates[0].name
            if relative_from_map not in text:
                missing_core.append(relative_from_map)
                self.add(
                    "WARNING",
                    "knowledge_map.coverage",
                    f"Core document is not discoverable from knowledge map: {relative_from_map}",
                    path,
                )

        self.metrics["knowledge_map"] = {
            "mermaid_diagrams": mermaid_count,
            "core_links_expected": len(list(EXPECTED_CORE_RANGE)),
            "core_links_present": len(list(EXPECTED_CORE_RANGE)) - len(missing_core),
            "missing_core_links": missing_core,
        }

    def check_document_size(self, files: Iterable[Path]) -> None:
        oversized = []
        for path in files:
            if self.is_archive(path) or self.is_template(path):
                continue
            line_count = len(self.read(path).splitlines())
            if line_count > self.max_active_lines:
                oversized.append((self.rel(path), line_count))
                self.add(
                    "WARNING",
                    "maintainability.size",
                    f"Active document has {line_count} lines, threshold is {self.max_active_lines}.",
                    path,
                    remediation="Split into index plus Standard, SOP or Playbook documents.",
                )
        self.metrics["oversized_active_docs"] = oversized

    def check_split_architecture(self) -> None:
        split_metrics: dict[str, object] = {}
        for name, cfg in EXPECTED_SPLITS.items():
            index = self.root / str(cfg["index"])
            archive = self.root / str(cfg["archive"])
            directory = self.root / str(cfg["dir"])
            subdocs = (
                [p for p in directory.glob("*.md") if p.resolve() != archive.resolve()]
                if directory.exists()
                else []
            )

            if not index.exists():
                self.add("ERROR", "split.index", f"{name} index file missing.", index)
            elif len(self.read(index).splitlines()) > 200:
                self.add(
                    "WARNING",
                    "split.index_size",
                    f"{name} index is larger than 200 lines.",
                    index,
                )

            if not archive.exists():
                self.add(
                    "WARNING",
                    "split.archive",
                    f"{name} historical full reference is missing.",
                    archive,
                )

            if len(subdocs) < int(cfg["minimum_subdocs"]):
                self.add(
                    "ERROR",
                    "split.subdocs",
                    f"{name} split has {len(subdocs)} subdocs, expected at least {cfg['minimum_subdocs']}.",
                    directory,
                )

            split_metrics[name] = {
                "index_lines": len(self.read(index).splitlines()) if index.exists() else None,
                "archive_exists": archive.exists(),
                "subdocs": len(subdocs),
            }
        self.metrics["split_architecture"] = split_metrics

    def check_metadata(self) -> None:
        targets: list[Path] = []
        for folder in ("policies", "procedures", "playbooks"):
            directory = self.docs_dir / folder
            if directory.exists():
                targets.extend(sorted(directory.glob("*.md")))

        required_keys = ("Document ID", "Type", "Owner")
        document_ids: dict[str, list[str]] = defaultdict(list)
        problems = 0

        for path in targets:
            text = self.read(path)
            for key in required_keys:
                if key not in text:
                    problems += 1
                    self.add(
                        "WARNING",
                        "metadata.required",
                        f"Missing metadata key: {key}",
                        path,
                    )
            match = re.search(r"\|\s*Document ID\s*\|\s*([^|]+?)\s*\|", text)
            if match:
                document_ids[match.group(1).strip()].append(self.rel(path))

        for doc_id, paths in document_ids.items():
            if len(paths) > 1:
                problems += 1
                self.add(
                    "ERROR",
                    "metadata.document_id_duplicate",
                    f"Duplicate Document ID {doc_id}: {', '.join(paths)}",
                )

        self.metrics["metadata_docs_checked"] = len(targets)
        self.metrics["metadata_problems"] = problems

    @staticmethod
    def parse_pipe_row(line: str) -> list[str]:
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            return []
        return [cell.strip() for cell in stripped[1:-1].split("|")]

    def check_control_catalog(self, files: Iterable[Path]) -> None:
        catalog_path = self.root / "docs/governance/security-control-catalog.md"
        if not catalog_path.exists():
            return

        controls: list[Control] = []
        text = self.read(catalog_path)
        for lineno, line in enumerate(text.splitlines(), 1):
            row = self.parse_pipe_row(line)
            if len(row) < 8:
                continue
            if not re.fullmatch(r"SEC-[A-Z][A-Z0-9]{1,7}-\d{3}", row[0]):
                continue
            controls.append(
                Control(
                    control_id=row[0],
                    requirement=row[1],
                    level=row[2],
                    owner=row[3],
                    evidence=row[4],
                    frequency=row[5],
                    metric=row[6],
                    source=row[7],
                    line=lineno,
                )
            )

        self.controls = controls
        ids = [c.control_id for c in controls]
        known = set(ids)
        duplicates = [cid for cid, count in Counter(ids).items() if count > 1]
        for cid in duplicates:
            self.add("ERROR", "control.duplicate", f"Duplicate Control ID: {cid}", catalog_path)

        incomplete = []
        invalid_levels = []
        for control in controls:
            values = (
                control.requirement,
                control.level,
                control.owner,
                control.evidence,
                control.frequency,
                control.metric,
                control.source,
            )
            if any(not value or value in {"-", "TBD", "待确认"} for value in values):
                incomplete.append(control.control_id)
                self.add(
                    "WARNING",
                    "control.incomplete",
                    f"Control has empty or TBD fields: {control.control_id}",
                    catalog_path,
                    control.line,
                )
            if control.level not in {"MUST", "SHOULD", "MAY"}:
                invalid_levels.append(control.control_id)
                self.add(
                    "ERROR",
                    "control.level",
                    f"Invalid control level {control.level!r}: {control.control_id}",
                    catalog_path,
                    control.line,
                )

        reference_count: Counter[str] = Counter()
        unknown_refs: dict[str, set[str]] = defaultdict(set)
        for path in files:
            if path.resolve() == catalog_path.resolve() or self.is_archive(path):
                continue
            # Scan line-by-line so document metadata IDs such as SEC-POL-001
            # are not mistaken for Control IDs.
            for line in self.read(path).splitlines():
                if "Document ID" in line:
                    continue
                for cid in CONTROL_ID_RE.findall(line):
                    reference_count[cid] += 1
                    if cid not in known:
                        unknown_refs[cid].add(self.rel(path))

        for cid, paths in sorted(unknown_refs.items()):
            self.add(
                "WARNING",
                "control.unknown_reference",
                f"Referenced Control ID is absent from catalog: {cid}; "
                + ", ".join(sorted(paths)),
            )

        unreferenced = sorted(cid for cid in known if reference_count[cid] == 0)
        if unreferenced:
            self.add(
                "INFO",
                "control.unreferenced",
                f"{len(unreferenced)} catalog controls are not yet referenced by active documents. "
                "See JSON metrics.controls.unreferenced for the full list.",
            )

        self.metrics["controls"] = {
            "count": len(controls),
            "duplicate_ids": duplicates,
            "incomplete": incomplete,
            "invalid_levels": invalid_levels,
            "unknown_references": {k: sorted(v) for k, v in unknown_refs.items()},
            "unreferenced": unreferenced,
            "domains": dict(sorted(Counter(cid.split("-")[1] for cid in ids).items())),
        }

    def check_current_target_profile(self) -> None:
        path = self.root / "docs/governance/security-current-target-profile.md"
        if not path.exists():
            return

        rows = []
        for lineno, line in enumerate(self.read(path).splitlines(), 1):
            row = self.parse_pipe_row(line)
            if len(row) != 5:
                continue
            if row[0] in {"Domain", "---"}:
                continue
            if row[1] in {"待评估", "L0", "L1", "L2", "L3"}:
                rows.append((lineno, row))

        total = len(rows)
        pending = sum(1 for _, row in rows if row[1] == "待评估")
        assessed = total - pending
        invalid_targets = [
            row[0]
            for _, row in rows
            if not re.fullmatch(r"L[0-3](?:-L[0-3])?", row[2])
        ]

        if pending:
            self.add(
                "INFO",
                "profile.pending",
                f"{pending}/{total} Current Profile domains are still 待评估. "
                "This is implementation readiness, not a document syntax defect.",
                path,
            )

        for domain in invalid_targets:
            self.add(
                "WARNING",
                "profile.target",
                f"Unexpected target maturity format: {domain}",
                path,
            )

        self.metrics["current_target_profile"] = {
            "domains": total,
            "assessed": assessed,
            "pending": pending,
            "assessment_completion_percent": round(assessed / total * 100, 1)
            if total
            else 0.0,
            "invalid_targets": invalid_targets,
        }

    def check_parameters_register(self) -> None:
        path = self.root / "docs/governance/company-security-parameters-register.md"
        if not path.exists():
            return

        rows = []
        for lineno, line in enumerate(self.read(path).splitlines(), 1):
            row = self.parse_pipe_row(line)
            if len(row) != 5 or row[0] in {"Parameter", "---"}:
                continue
            if row[4] in {"Open", "Closed", "In Progress", "Accepted"}:
                rows.append((lineno, row))

        total = len(rows)
        statuses = Counter(row[4] for _, row in rows)
        pending_values = sum(1 for _, row in rows if row[1] == "待确认")
        resolved = sum(
            1
            for _, row in rows
            if row[1] != "待确认" and row[4] in {"Closed", "Accepted"}
        )

        if statuses["Open"]:
            self.add(
                "INFO",
                "parameters.open",
                f"{statuses['Open']}/{total} company security parameters are Open.",
                path,
            )

        self.metrics["company_parameters"] = {
            "total": total,
            "status": dict(statuses),
            "pending_values": pending_values,
            "resolved": resolved,
            "resolved_percent": round(resolved / total * 100, 1) if total else 0.0,
        }

    def check_stale_markers(self, files: Iterable[Path]) -> None:
        stale = []
        for path in files:
            if self.is_archive(path):
                continue
            text = self.read(path)
            for marker in STALE_ACTIVE_MARKERS:
                if marker in text:
                    stale.append((self.rel(path), marker))
                    self.add(
                        "WARNING",
                        "content.stale",
                        f"Active document contains stale version marker: {marker}",
                        path,
                    )
        self.metrics["stale_markers"] = stale

    def check_open_items(self, files: Iterable[Path]) -> None:
        total = 0
        by_file = []
        for path in files:
            if self.is_archive(path) or self.is_template(path):
                continue
            count = len(UNCHECKED_RE.findall(self.read(path)))
            if count:
                total += count
                by_file.append((self.rel(path), count))

        if total:
            self.add(
                "INFO",
                "content.open_checkboxes",
                f"{total} unchecked checklist items remain in active non-template docs.",
            )

        self.metrics["open_checkboxes"] = {
            "total": total,
            "by_file": sorted(by_file, key=lambda item: (-item[1], item[0])),
        }

    def check_orphans(self, files: Iterable[Path]) -> None:
        all_files = {path.resolve(): path for path in files}
        referenced: set[Path] = set()

        for path in files:
            text = self.read(path)
            for match in MD_LINK_RE.finditer(text):
                target = match.group(1).strip()
                if (
                    not target
                    or target.startswith("#")
                    or "://" in target
                    or target.startswith("mailto:")
                    or target.startswith("tel:")
                ):
                    continue
                local_target = target.split("#", 1)[0].split("?", 1)[0]
                if not local_target:
                    continue
                candidate = (path.parent / local_target).resolve()
                if candidate in all_files:
                    referenced.add(candidate)

            for match in WIKI_LINK_RE.finditer(text):
                resolved = self.resolve_wikilink(path, match.group(1))
                if resolved is not None and resolved in all_files:
                    referenced.add(resolved)

        orphans = []
        for resolved, path in all_files.items():
            if resolved == self.readme.resolve() or self.is_archive(path):
                continue
            if resolved not in referenced:
                orphans.append(self.rel(path))
                self.add(
                    "WARNING",
                    "navigation.orphan",
                    "Markdown file is not linked from any other Markdown file.",
                    path,
                    remediation="Link it from README or a parent index.",
                )

        self.metrics["orphan_active_docs"] = orphans

    def quality_summary(self) -> dict[str, object]:
        errors = {f.check for f in self.findings if f.severity == "ERROR"}
        warnings = {f.check for f in self.findings if f.severity == "WARNING"}

        categories = {
            "structure_and_links": (
                [
                    "markdown.h1",
                    "markdown.fence",
                    "link.broken",
                    "core.missing",
                    "core.duplicate",
                    "obsidian.wikilink_broken",
                ],
                ["markdown.heading_level"],
            ),
            "obsidian_graph": (
                [
                    "obsidian.frontmatter_missing",
                    "obsidian.property_missing",
                    "obsidian.parent",
                    "obsidian.relation_block",
                    "readme.knowledge_map",
                ],
                ["obsidian.security_tag", "knowledge_map.visual_depth", "knowledge_map.coverage"],
            ),
            "required_artifacts": (
                ["required.governance", "required.hierarchy", "required.templates", "split.subdocs"],
                ["split.index_size", "split.archive"],
            ),
            "control_governance": (
                ["control.duplicate", "control.level"],
                ["control.incomplete", "control.unknown_reference"],
            ),
            "maintainability": (
                [],
                ["maintainability.size", "navigation.orphan", "content.stale"],
            ),
        }

        result: dict[str, object] = {}
        for name, (blocking, caution) in categories.items():
            failed = [item for item in blocking if item in errors]
            warned = [item for item in caution if item in warnings]
            status = "FAIL" if failed else ("WARN" if warned else "PASS")
            result[name] = {
                "status": status,
                "blocking_checks": failed,
                "warning_checks": warned,
            }
        return result


def render_markdown(report: dict[str, object]) -> str:
    metrics = report["metrics"]
    findings = report["findings"]
    counts = Counter(item["severity"] for item in findings)
    profile = metrics.get("current_target_profile", {})
    params = metrics.get("company_parameters", {})
    controls = metrics.get("controls", {})
    obsidian = metrics.get("obsidian", {})
    wikilinks = metrics.get("wikilinks", {})

    lines = [
        "# Security Documentation Quality Report",
        "",
        f"- Generated: {report['generated_at']}",
        f"- Root: {report['project_root']}",
        f"- Markdown files: **{metrics.get('markdown_files', 0)}**",
        f"- Total lines: **{metrics.get('total_lines', 0)}**",
        f"- Findings: **{counts['ERROR']} ERROR / {counts['WARNING']} WARNING / {counts['INFO']} INFO**",
        "",
        "## 1. 结论",
        "",
    ]

    for name, item in metrics.get("documentation_quality", {}).items():
        lines.append(f"- **{name}**: {item['status']}")

    lines.extend(
        [
            "",
            "## 2. 文档体系完整性",
            "",
            f"- Core 00-30: **{metrics.get('core_docs_present', 0)}/{metrics.get('core_docs_expected', 0)}**",
        ]
    )

    for name, item in metrics.get("required_artifacts", {}).items():
        lines.append(f"- {name}: **{item['present']}/{item['expected']}**")

    lines.extend(
        [
            f"- Broken links: **{metrics.get('broken_links', 0)}**",
            f"- Oversized active docs: **{len(metrics.get('oversized_active_docs', []))}**",            f"- Obsidian Properties coverage: **{obsidian.get('frontmatter_files', 0)}/{obsidian.get('docs_files', 0)}**",
            f"- Core relation blocks: **{obsidian.get('core_relation_blocks', 0)}/{obsidian.get('core_relation_expected', 0)}**",
            f"- Obsidian WikiLinks: **{wikilinks.get('total', 0)}**, broken: **{wikilinks.get('broken', 0)}**",
            "",
            "## 3. Control Catalog",
            "",
            f"- Controls: **{controls.get('count', 0)}**",
            f"- Duplicate IDs: **{len(controls.get('duplicate_ids', []))}**",
            f"- Unknown exact references: **{len(controls.get('unknown_references', {}))}**",
            f"- Not yet referenced: **{len(controls.get('unreferenced', []))}**",
            "",
            "## 4. Current / Target Profile",
            "",
            f"- Domains: **{profile.get('domains', 0)}**",
            f"- Assessed: **{profile.get('assessed', 0)}**",
            f"- Pending: **{profile.get('pending', 0)}**",
            f"- Assessment completion: **{profile.get('assessment_completion_percent', 0)}%**",
            "",
            "## 5. 公司参数",
            "",
            f"- Parameters: **{params.get('total', 0)}**",
            f"- Pending values: **{params.get('pending_values', 0)}**",
            f"- Resolved: **{params.get('resolved', 0)}**",
            f"- Resolved percent: **{params.get('resolved_percent', 0)}%**",
            "",
            "## 6. Open Checklist",
            "",
        ]
    )

    open_items = metrics.get("open_checkboxes", {})
    lines.append(f"- Total unchecked items: **{open_items.get('total', 0)}**")
    for path, count in open_items.get("by_file", [])[:15]:
        lines.append(f"  - {path}: {count}")

    lines.extend(["", "## 7. Findings", ""])
    for severity in ("ERROR", "WARNING", "INFO"):
        current = [item for item in findings if item["severity"] == severity]
        lines.extend([f"### {severity} ({len(current)})", ""])
        if not current:
            lines.extend(["- None", ""])
            continue
        for item in current:
            location = item.get("path") or "-"
            if item.get("line"):
                location = f"{location}:{item['line']}"
            lines.append(f"- **{item['check']}** {location} — {item['message']}")
            if item.get("remediation"):
                lines.append(f"  - Fix: {item['remediation']}")
        lines.append("")

    lines.extend(
        [
            "## 8. CI 解释",
            "",
            "- 默认模式：仅 ERROR 导致非 0 退出码。",
            "- strict 模式：WARNING 也导致非 0 退出码。",
            "- Current Profile 待评估、公司参数 Open 和未勾选工作项属于实施进度 INFO，不默认阻断 CI。",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Quality-check the company Security Program Markdown repository."
    )
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--report-dir", type=Path, default=Path("reports"))
    parser.add_argument("--md-name", default="security-doc-quality-report.md")
    parser.add_argument("--json-name", default="security-doc-quality-report.json")
    parser.add_argument("--max-active-lines", type=int, default=1000)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()

    try:
        checker = QualityChecker(root=root, max_active_lines=args.max_active_lines)
        report = checker.run()

        md_path = None
        json_path = None
        if not args.no_write:
            report_dir = args.report_dir
            if not report_dir.is_absolute():
                report_dir = root / report_dir
            report_dir.mkdir(parents=True, exist_ok=True)
            md_path = report_dir / args.md_name
            json_path = report_dir / args.json_name
            md_path.write_text(render_markdown(report), encoding="utf-8")
            json_path.write_text(
                json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

        metrics = report["metrics"]
        errors = int(metrics.get("errors", 0))
        warnings = int(metrics.get("warnings", 0))
        infos = int(metrics.get("infos", 0))

        if args.quiet:
            print(f"security-doc-quality: errors={errors} warnings={warnings} infos={infos}")
        else:
            print("=" * 72)
            print("Security Documentation Quality Check")
            print("=" * 72)
            print(f"Root:       {root}")
            print(f"Markdown:   {metrics.get('markdown_files', 0)}")
            print(f"Lines:      {metrics.get('total_lines', 0)}")
            print(f"ERROR:      {errors}")
            print(f"WARNING:    {warnings}")
            print(f"INFO:       {infos}")
            profile = metrics.get("current_target_profile", {})
            params = metrics.get("company_parameters", {})
            print(
                f"Profile:    {profile.get('assessed', 0)}/{profile.get('domains', 0)} assessed"
            )
            print(
                f"Parameters: {params.get('resolved', 0)}/{params.get('total', 0)} resolved"
            )
            if md_path is not None:
                print(f"Markdown report: {md_path}")
                print(f"JSON report:     {json_path}")

        if errors:
            return 1
        if args.strict and warnings:
            return 2
        return 0

    except Exception as exc:
        print(f"security-doc-quality checker failed: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
