#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply idempotent Obsidian metadata and relationship blocks."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CORE = {
    0:  {"alias": "公司安全体系总览", "domain": "governance", "phase": ["govern"], "priority": "P0", "up": [], "down": [1,2,4,6,9,10,11,12,13], "cross": []},
    1:  {"alias": "安全治理与制度", "domain": "governance", "phase": ["govern"], "priority": "P0", "up": [0], "down": [13,27,30], "cross": []},
    2:  {"alias": "资产与网络架构", "domain": "asset", "phase": ["identify"], "priority": "P0", "up": [0,1], "down": [3,4,7,9,10,16,17], "cross": []},
    3:  {"alias": "网络与边界安全", "domain": "network", "phase": ["protect"], "priority": "P0", "up": [2,4], "down": [5,14,15,16], "cross": [10]},
    4:  {"alias": "身份与访问控制", "domain": "identity", "phase": ["protect"], "priority": "P0", "up": [1,2], "down": [3,5,6,15,21,25,27], "cross": []},
    5:  {"alias": "终端与服务器安全", "domain": "endpoint", "phase": ["protect"], "priority": "P0", "up": [2,3,4], "down": [10,14,15,29], "cross": [16]},
    6:  {"alias": "应用与 API 安全", "domain": "application-security", "phase": ["protect"], "priority": "P0", "up": [4,17], "down": [8,9,18,22,23,24], "cross": [7,21]},
    7:  {"alias": "数据安全", "domain": "data-security", "phase": ["protect"], "priority": "P0", "up": [2,4], "down": [21,26,27], "cross": [6,25]},
    8:  {"alias": "DevSecOps 与供应链安全", "domain": "devsecops", "phase": ["protect"], "priority": "P0", "up": [6,17], "down": [9,18,22], "cross": [21]},
    9:  {"alias": "漏洞管理与授权渗透测试", "domain": "vulnerability-management", "phase": ["detect"], "priority": "P0", "up": [2,6,8,14], "down": [10,11,19,20], "cross": []},
    10: {"alias": "日志监控与安全运营", "domain": "security-operations", "phase": ["detect"], "priority": "P1", "up": [2,3,4,5,9], "down": [11,19], "cross": [25]},
    11: {"alias": "安全事件与应急响应", "domain": "incident-response", "phase": ["respond"], "priority": "P1", "up": [9,10], "down": [12,28], "cross": [19,20,25]},
    12: {"alias": "备份容灾与稳定性协同", "domain": "resilience", "phase": ["recover"], "priority": "P0", "up": [11,28], "down": [], "cross": [14,16,27,29]},
    13: {"alias": "合规与审计", "domain": "audit", "phase": ["govern"], "priority": "P1", "up": [0,1], "down": [], "cross": [14]},
    14: {"alias": "安全基线与检查清单", "domain": "security-baseline", "phase": ["protect"], "priority": "P0", "up": [3,5,8], "down": [9], "cross": [12,16]},
    15: {"alias": "零信任与设备可信", "domain": "zero-trust", "phase": ["protect"], "priority": "P1", "up": [2,4,5], "down": [], "cross": [3,16,21]},
    16: {"alias": "云与工作负载安全", "domain": "cloud-security", "phase": ["protect"], "priority": "P1", "up": [2,3,4,5], "down": [], "cross": [8,12,14,15,21,22]},
    17: {"alias": "安全架构评审与威胁建模", "domain": "security-architecture", "phase": ["identify","protect"], "priority": "P1", "up": [2], "down": [6,8,18,22,23,24], "cross": []},
    18: {"alias": "产品安全与默认安全", "domain": "product-security", "phase": ["protect"], "priority": "P1", "up": [6,8,17], "down": [20], "cross": [22,23,24]},
    19: {"alias": "威胁情报、红队与紫队", "domain": "threat-informed-defense", "phase": ["detect"], "priority": "P1", "up": [9,10], "down": [11], "cross": [14]},
    20: {"alias": "PSIRT 与漏洞披露", "domain": "psirt", "phase": ["respond"], "priority": "P2", "up": [9,18], "down": [11], "cross": [27]},
    21: {"alias": "密码学、PKI、KMS 与凭据治理", "domain": "cryptography", "phase": ["protect"], "priority": "P1", "up": [4,7], "down": [6,8,16,22], "cross": [15]},
    22: {"alias": "安全工程平台", "domain": "security-platform", "phase": ["protect"], "priority": "P1", "up": [6,8,17,21], "down": [18], "cross": [14]},
    23: {"alias": "AI、大模型与智能体安全", "domain": "ai-security", "phase": ["protect"], "priority": "P2", "up": [6,7,17,18,21,22], "down": [26], "cross": []},
    24: {"alias": "移动应用安全", "domain": "mobile-security", "phase": ["protect"], "priority": "P2", "up": [6,17,18,21,22], "down": [], "cross": []},
    25: {"alias": "邮件与协作平台安全", "domain": "email-security", "phase": ["protect","detect"], "priority": "P0", "up": [4,7,30], "down": [10,11], "cross": [26]},
    26: {"alias": "隐私与个人信息保护", "domain": "privacy", "phase": ["govern","protect"], "priority": "P1", "up": [7,25], "down": [], "cross": [18,23,27]},
    27: {"alias": "第三方风险管理", "domain": "third-party-risk", "phase": ["govern"], "priority": "P1", "up": [1], "down": [7,26,28], "cross": [4,12]},
    28: {"alias": "BIA 与业务连续性", "domain": "business-continuity", "phase": ["recover"], "priority": "P1", "up": [11,27], "down": [12], "cross": [29]},
    29: {"alias": "物理、环境与介质安全", "domain": "physical-security", "phase": ["protect"], "priority": "P2", "up": [5,28], "down": [], "cross": [12,30]},
    30: {"alias": "安全意识、安全倡导者与安全人才体系", "domain": "security-awareness", "phase": ["govern","protect"], "priority": "P1", "up": [1], "down": [6,8,10,11,25], "cross": [29]},
}

EXTRA_NOTES = {
    "docs/公司安全知识图谱.md": {
        "alias": "公司安全知识图谱", "type": "moc", "domain": "security-program",
        "phase": ["govern","identify","protect","detect","respond","recover"], "priority": "P0",
        "parent": [], "related": ["docs/00-公司安全体系总览", "docs/governance/安全治理总览", "docs/Obsidian使用指南"],
    },
    "docs/governance/安全治理总览.md": {
        "alias": "安全治理 V2.0", "type": "moc", "domain": "governance",
        "phase": ["govern"], "priority": "P0", "parent": ["docs/公司安全知识图谱"],
        "related": [
            "docs/governance/安全控制目录",
            "docs/governance/安全现状与目标画像",
            "docs/governance/安全职责RACI",
            "docs/governance/公司安全参数登记表",
            "docs/governance/文档层级与维护规则",
        ],
    },
    "docs/governance/安全控制目录.md": {
        "alias": "安全控制目录", "type": "catalog", "domain": "governance",
        "phase": ["govern"], "priority": "P0", "parent": ["docs/governance/安全治理总览"],
        "related": ["docs/governance/安全现状与目标画像", "docs/governance/安全职责RACI", "docs/13-合规与审计"],
    },
    "docs/governance/安全现状与目标画像.md": {
        "alias": "安全现状与目标画像", "type": "profile", "domain": "governance",
        "phase": ["govern"], "priority": "P0", "parent": ["docs/governance/安全治理总览"],
        "related": ["docs/governance/安全控制目录", "docs/governance/公司安全参数登记表", "docs/13-合规与审计"],
    },
    "docs/governance/安全职责RACI.md": {
        "alias": "安全职责矩阵（RACI）", "type": "matrix", "domain": "governance",
        "phase": ["govern"], "priority": "P0", "parent": ["docs/governance/安全治理总览"],
        "related": ["docs/governance/安全控制目录", "docs/01-安全治理与制度"],
    },
    "docs/governance/公司安全参数登记表.md": {
        "alias": "公司安全参数登记表", "type": "register", "domain": "governance",
        "phase": ["govern"], "priority": "P0", "parent": ["docs/governance/安全治理总览"],
        "related": ["docs/governance/安全现状与目标画像", "docs/00-公司安全体系总览"],
    },
    "docs/governance/文档层级与维护规则.md": {
        "alias": "安全文档层级与维护规则", "type": "standard", "domain": "governance",
        "phase": ["govern"], "priority": "P1", "parent": ["docs/governance/安全治理总览"],
        "related": ["docs/公司安全知识图谱", "docs/01-安全治理与制度"],
    },
    "docs/Obsidian使用指南.md": {
        "alias": "Obsidian 使用指南", "type": "guide", "domain": "security-program",
        "phase": ["govern"], "priority": "P1", "parent": ["docs/公司安全知识图谱"],
        "related": ["docs/公司安全知识图谱", "docs/governance/安全治理总览"],
    },
    "docs/playbooks/处置手册索引.md": {
        "alias": "安全处置手册索引", "type": "moc", "domain": "operations",
        "phase": ["respond"], "priority": "P0", "parent": ["docs/公司安全知识图谱"],
        "related": ["docs/11-安全事件与应急响应", "docs/10-日志监控与安全运营"],
    },
    "docs/templates/模板索引.md": {
        "alias": "安全模板索引", "type": "moc", "domain": "template",
        "phase": ["govern"], "priority": "P1", "parent": ["docs/公司安全知识图谱"],
        "related": [],
    },
}

TYPE_BY_DIR = {
    "policies": "policy",
    "procedures": "procedure",
    "playbooks": "playbook",
    "templates": "template",
}

SUPPORTING_INDEX_FILES = {
    "处置手册索引.md",
    "模板索引.md",
}

REL_START = "<!-- obsidian-relations:start -->"
REL_END = "<!-- obsidian-relations:end -->"


def core_path(num: int) -> Path:
    matches = sorted(DOCS.glob(f"{num:02d}-*.md"))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one core document for {num:02d}, got {matches}")
    return matches[0]


def vault_stem(path: Path) -> str:
    return str(path.relative_to(ROOT).with_suffix("")).replace("\\", "/")


def wiki(path: Path, alias: str | None = None) -> str:
    target = vault_stem(path)
    return f"[[{target}|{alias}]]" if alias else f"[[{target}]]"


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def make_frontmatter(*, alias: str, note_type: str, domain: str, phase: list[str],
                     priority: str, parent: list[str], related: list[str],
                     status: str = "active") -> str:
    tags = [
        "security",
        f"security/type/{note_type}",
        f"security/domain/{domain}",
        f"security/priority/{priority.lower()}",
    ] + [f"security/phase/{item}" for item in phase]

    lines = [
        "---",
        "aliases:",
        f"  - {yaml_quote(alias)}",
        f"type: {yaml_quote(note_type)}",
        f"domain: {yaml_quote(domain)}",
        "phase:",
    ]
    lines.extend(f"  - {yaml_quote(item)}" for item in phase)
    lines.extend([
        f"priority: {yaml_quote(priority)}",
        f"status: {yaml_quote(status)}",
        "tags:",
    ])
    lines.extend(f"  - {yaml_quote(item)}" for item in tags)
    if parent:
        lines.append("parent:")
        lines.extend(f"  - {yaml_quote(f'[[{item}]]')}" for item in parent)
    if related:
        lines.append("related:")
        lines.extend(f"  - {yaml_quote(f'[[{item}]]')}" for item in related)
    lines.extend(["---", ""])
    return "\n".join(lines)


def replace_frontmatter(text: str, frontmatter: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return frontmatter + text[end + 5:].lstrip("\n")
    return frontmatter + text.lstrip("\n")


def relation_block(num: int, meta: dict) -> str:
    def links(nums: list[int]) -> str:
        if not nums:
            return "无"
        return " · ".join(
            wiki(core_path(n), f"{n:02d} {CORE[n]['alias']}") for n in nums
        )

    return "\n".join([
        REL_START,
        "## Obsidian 关联知识",
        "",
        "> [!tip] 图谱导航",
        "> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian 全局图谱 / 局部图谱。业务正文请维护在上方章节。",
        "",
        "- **上级导航**：[[docs/公司安全知识图谱|公司安全知识图谱]]",
        f"- **前置知识**：{links(meta['up'])}",
        f"- **下游知识**：{links(meta['down'])}",
        f"- **横向关联**：{links(meta['cross'])}",
        "",
        REL_END,
    ])


def replace_relation_block(text: str, block: str) -> str:
    pattern = re.compile(re.escape(REL_START) + r".*?" + re.escape(REL_END), re.S)
    if pattern.search(text):
        return pattern.sub(block, text).rstrip() + "\n"
    return text.rstrip() + "\n\n" + block + "\n"


def apply_core() -> int:
    changed = 0
    for num, meta in CORE.items():
        path = core_path(num)
        text = path.read_text(encoding="utf-8")
        related_nums = list(dict.fromkeys(meta["up"] + meta["down"] + meta["cross"]))
        frontmatter = make_frontmatter(
            alias=meta["alias"],
            note_type="overview" if num == 0 else "standard",
            domain=meta["domain"],
            phase=meta["phase"],
            priority=meta["priority"],
            parent=["docs/公司安全知识图谱"],
            related=[vault_stem(core_path(n)) for n in related_nums],
        )
        new = replace_frontmatter(text, frontmatter)
        new = replace_relation_block(new, relation_block(num, meta))
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def apply_extra() -> int:
    changed = 0
    for rel, meta in EXTRA_NOTES.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        frontmatter = make_frontmatter(
            alias=meta["alias"], note_type=meta["type"], domain=meta["domain"],
            phase=meta["phase"], priority=meta["priority"],
            parent=meta["parent"], related=meta["related"],
        )
        new = replace_frontmatter(text, frontmatter)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def apply_supporting() -> int:
    changed = 0
    split_specs = [
        (DOCS / "08-devsecops", "devsecops", "protect", "docs/08-DevSecOps与软件供应链安全"),
        (DOCS / "09-vulnerability", "vulnerability-management", "detect", "docs/09-漏洞管理与授权渗透测试"),
    ]
    for directory, domain, phase, parent in split_specs:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            archived = path.name == "V1历史完整参考.md"
            title = re.search(r"^#\s+(.+)$", text, re.M)
            alias = title.group(1).strip() if title else path.stem
            frontmatter = make_frontmatter(
                alias=alias,
                note_type="archive" if archived else "standard",
                domain=domain,
                phase=[phase],
                priority="P0",
                parent=[parent],
                related=[],
                status="archived" if archived else "active",
            )
            new = replace_frontmatter(text, frontmatter)
            if new != text:
                path.write_text(new, encoding="utf-8")
                changed += 1

    for folder, note_type in TYPE_BY_DIR.items():
        directory = DOCS / folder
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name in SUPPORTING_INDEX_FILES:
                continue
            text = path.read_text(encoding="utf-8")
            title = re.search(r"^#\s+(.+)$", text, re.M)
            alias = title.group(1).strip() if title else path.stem
            domain = "governance" if folder == "policies" else (
                "operations" if folder in {"procedures", "playbooks"} else "template"
            )
            phase = ["govern"] if folder in {"policies", "templates"} else ["respond"]
            frontmatter = make_frontmatter(
                alias=alias, note_type=note_type, domain=domain, phase=phase,
                priority="P1", parent=["docs/公司安全知识图谱"], related=[],
            )
            new = replace_frontmatter(text, frontmatter)
            if new != text:
                path.write_text(new, encoding="utf-8")
                changed += 1
    return changed


def main() -> int:
    changed = apply_core() + apply_extra() + apply_supporting()
    print(f"obsidian optimization updated_files={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
