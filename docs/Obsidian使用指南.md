---
aliases:
  - "Obsidian 使用指南"
type: "guide"
domain: "security-program"
phase:
  - "govern"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/guide"
  - "security/domain/security-program"
  - "security/priority/p1"
  - "security/phase/govern"
parent:
  - "[[docs/公司安全知识图谱]]"
related:
  - "[[docs/公司安全知识图谱]]"
  - "[[docs/governance/安全治理总览]]"
---
# Obsidian 使用指南

> 目标：把整个仓库直接作为 Obsidian Vault 打开后，既保留 Git 和标准 Markdown，又获得可用的 全局图谱、局部图谱、Properties、Tags 和 Backlinks。

## 1. 打开方式

在 Obsidian 选择 Open folder as vault，直接打开项目根目录：

~~~text
company-network-security-docs/
~~~

不要只打开 docs/，因为 README、脚本和 Vault 根路径都按项目根目录设计。

## 2. 第一入口

优先打开：

[[docs/公司安全知识图谱|公司安全知识图谱]]

不建议按 00～30 顺序逐篇阅读。

## 3. 属性

核心文档统一包含：

| Property | 用途 |
|---|---|
| aliases | 中文简称与搜索别名 |
| type | overview / standard / moc / policy / procedure / playbook / template |
| domain | 安全域 |
| phase | govern / identify / protect / detect / respond / recover |
| priority | P0 / P1 / P2 |
| status | active / archived |
| tags | 图谱分组和搜索 |
| parent | 上级知识节点 |
| related | 显式知识关系 |

Obsidian 会把 YAML Frontmatter 识别为 Properties。

## 4. 标签

本项目使用嵌套 Tags：

~~~text
security
security/type/standard
security/domain/devsecops
security/phase/protect
security/priority/p0
~~~

常用搜索：

~~~text
tag:#security/domain/devsecops
tag:#security/phase/detect
tag:#security/priority/p0
~~~

## 5. 全局图谱推荐

打开 Graph View 后，建议先隐藏不影响主知识结构的节点。

### 推荐文件搜索条件

~~~text
path:docs -path:docs/templates -path:docs/08-devsecops/V1历史完整参考 -path:docs/09-vulnerability/V1历史完整参考
~~~

### 推荐打开

- Existing files only
- Arrows
- Tags：按需要打开
- Orphans：排查知识孤岛时打开，平时可关闭

## 6. 图谱分组推荐

建议按以下搜索条件创建 Groups：

~~~text
tag:#security/domain/governance
tag:#security/domain/asset
tag:#security/domain/identity
tag:#security/domain/application-security
tag:#security/domain/devsecops
tag:#security/domain/vulnerability-management
tag:#security/domain/security-operations
tag:#security/domain/incident-response
tag:#security/domain/resilience
~~~

颜色属于个人阅读偏好，本仓库不提交固定颜色配置。

## 7. 局部图谱推荐

阅读单篇文档时，局部图谱 比 全局图谱 更实用：

- Depth = 1：看直接前置、下游、横向关系。
- Depth = 2：看完整业务链路。
- Depth > 2：只在体系分析时临时使用，否则容易过密。

例如打开：

[[docs/08-DevSecOps与软件供应链安全|08 DevSecOps 与供应链安全]]

局部图谱 可以直接看到 AppSec、威胁建模、Vulnerability、Security Platform、Crypto 等关联节点。

## 8. 关联知识区

00～30 核心文档末尾统一维护：

~~~text
Obsidian 关联知识
├── 上级导航
├── 前置知识
├── 下游知识
└── 横向关联
~~~

该区域由以下脚本自动生成和刷新：

~~~bash
python3 scripts/obsidian_optimize.py
~~~

不建议手工维护生成区。

## 9. 新增核心文档时

如果未来增加新的核心安全域：

1. 先判断是否真的需要新文档。
2. 在 scripts/obsidian_optimize.py 中加入元数据与关系。
3. 更新 [[docs/公司安全知识图谱|公司安全知识图谱]]。
4. 执行：

~~~bash
python3 scripts/obsidian_optimize.py
python3 scripts/security_docs_quality_check.py --strict
~~~

5. 确认没有孤儿节点和断链。

## 10. Git 与 Obsidian 本地状态

Obsidian 打开 Vault 后会产生本机 UI 和 Workspace 状态。

本项目不建议把个人 .obsidian/ 状态提交 Git，避免不同电脑窗口布局、本地插件和个人 Graph 设置造成无意义 Diff。

知识结构本身通过 Markdown、Properties、WikiLink 和 Tags 保存在仓库里。

## 11. 推荐工作方式

~~~text
Global Graph
  ↓ 找到知识域

Knowledge Map
  ↓ 找到业务场景

Local Graph
  ↓ 理解上下游

Standard
  ↓ 找到要求

SOP / Playbook / Template
  ↓ 执行

控制 / 证据
  ↓ 证明落实
~~~

Graph 的价值不是“看起来漂亮”，而是帮助快速定位安全工作的上下文。
