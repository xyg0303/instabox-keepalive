# 🛡️ InstaBox Keepalive

本项目基于 GitHub Actions，专为 InstaBox 免费沙盒环境设计，提供**全自动、双层防护**的保活机制。彻底解决平台“30分钟闲置休眠”和“连续运行8小时强制暂停”的限制。

结合本地看门狗脚本（需在服务器内配置），可实现近乎 100% 的在线率。

## ✨ 核心功能 (Features)

1. **防闲置休眠**：每 10 分钟自动发送一次轻量命令，在 30 分钟闲置线前刷新机器活跃状态。
2. **防 8 小时强制关机**：在机器运行满 7 小时 50 分（470分钟）时，自动执行一次 `suspend` -> `resume` 无缝轮换，重置平台的 8 小时计时器，将停机时间压缩至约 10 秒。
3. **防 60 天休眠封印**：GitHub Actions 的“霸王条款”规定，仓库连续 60 天无代码提交会停用定时任务。本项目内置了每月自动提交（Auto-Commit）脚本，确保定时任务永不断供。

## ⚙️ 工作原理 (How it works)

*   `keepalive.yml`：定时器，每 10 分钟唤醒一次 Python 脚本执行巡检。
*   `instabox_tick.py`：核心逻辑（源自 `caichengle666` 的开源方案适配），读取机器状态、判断是否到期、执行防睡或轮换指令。
*   `auto-commit.yml`：每月 1 号自动向仓库写入时间戳文件，破除 60 天无活动限制。

## 🚀 快速部署 (Setup)

### 1. 准备 InstaBox API Key
登录 [InstaBox](https://instabox.sh) 控制台，进入 `Profile -> API keys`，创建一个带有 `machines:write` 权限的 Key（以 `ibk_` 开头），复制备用。

### 2. 配置 GitHub Secrets
进入本仓库的 `Settings -> Secrets and variables -> Actions`，点击 `New repository secret`，添加：
*   **Name**: `INSTABOX_API_KEY`
*   **Secret**: 填入你刚才复制的 `ibk_...` 密钥。

### 3. 运行测试
进入仓库的 `Actions` 标签页，选择 `InstaBox Keepalive`，点击 `Run workflow` 手动触发一次，确认日志显示 `Success` 即可。

## 📂 项目结构 (Structure)

```text
├── .github/workflows/
│   ├── auto-commit.yml      # 防 60 天停用自动打卡脚本
│   └── keepalive.yml        # 核心定时巡检任务
├── scripts/
│   ├── ib_api.py            # API 请求封装
│   └── instabox_tick.py     # 核心保活决策逻辑
└── timestamp.txt            # 自动打卡生成的时间戳文件
