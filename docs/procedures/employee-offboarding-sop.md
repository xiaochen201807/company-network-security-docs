# 员工离职与转岗权限回收 SOP

| Metadata | Value |
|---|---|
| Document ID | SEC-SOP-IAM-001 |
| Type | Procedure |
| Owner | IAM/IT |
| Related Control | SEC-IAM-002 |

## 1. Trigger

HR 提交离职/转岗生效信息。

## 2. Offboarding

在生效时间执行：

- 禁用统一身份账号。
- 撤销 VPN/ZTNA。
- Git/Jenkins/Cloud 管理权限回收。
- 数据库/生产权限回收。
- 撤销 Token/SSH Key/证书。
- 注销高风险 Session。
- 回收公司设备。
- 转移 System/Data Owner。
- 处理个人创建的自动化和服务账号。

## 3. Transfer

转岗：

1. 回收旧岗位无关权限。
2. 新岗位权限重新审批。
3. 检查生产、数据、管理员、VPN 和第三方系统。

## 4. Verification

IAM/IT 输出回收清单并由系统 Owner 抽查高权限系统。

## 5. Evidence

HR Trigger、Account Disable、Access Review、Device Return、Owner Transfer。
