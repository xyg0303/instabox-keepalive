🛡️ InstaBox Keepalive | 保活挂机脚本
 
English / 中文 双语文档
 
This project is based on GitHub Actions, designed exclusively for the InstaBox free sandbox environment. It provides a fully automatic, multi-layer keepalive mechanism to bypass the official limits.
 
本项目基于 GitHub Actions，专为 InstaBox 免费沙盒环境打造，提供全自动多层保活机制，彻底突破平台限制。
 
Refactored from the open-source logic by @caichengle666. Optimized for Chinese users with no overseas credit cards, no AI platforms, and even no PC. Only a GitHub account is required for permanent free 24h online.
 
基于开源作者重构优化，适配国内纯白嫖用户，无需海外账号、无需外币卡、无需电脑，仅 GitHub 即可实现 24 小时永久在线。
 
✨ Core Features | 核心功能
 
1. Anti-idle Sleep | 防闲置休眠
 
Automatically trigger active heartbeat every 10 minutes to avoid the official 30-minute idle shutdown rule.
每 10 分钟自动心跳巡检，杜绝官方 30 分钟闲置休眠。
 
2. Anti-8h Force Suspend | 防 8 小时强制停机
 
Automatically execute  suspend → resume  seamless rotation at 7 hours 50 minutes of runtime. Reset the official 8-hour timer with only ~10s downtime.
运行至 7 小时 50 分自动执行暂停/恢复轮换，重置 8 小时计时，停机仅约 10 秒，近乎无缝。
 
3. Anti-60-day Workflow Disable | 防 60 天任务封印
 
Built-in monthly auto-commit timestamp script to prevent GitHub Actions from disabling scheduled workflows due to long-term inactivity.
内置月度自动提交脚本，破除 GitHub 60 天无提交停用定时任务的限制，永久保活。
 
⚙️ Working Principle | 工作原理
 
-  keepalive.yml 
Core scheduled task, runs every 10 minutes to execute keepalive detection.
核心定时任务，每 10 分钟执行一次保活巡检。
-  instabox_tick.py 
Core judgment logic, detects machine status and executes sleep/reset strategy.
核心决策脚本，读取机器状态、判断运行时长、执行轮换保活。
-  auto-commit.yml 
Auto-generate commit monthly to keep GitHub workflow active permanently.
月度自动提交，维持仓库活跃度，防止定时任务被封禁。
 
📂 Project Structure | 项目结构
 
 
 
🚀 Deployment Guide | 部署教程（手机3分钟完成）
 
1. Get InstaBox API Key | 获取密钥
 
Log in to InstaBox →  Profile  →  API keys 
Create a key with  machines:write  permission (starts with  ibk_ ).
登录 InstaBox 后台，个人设置 → API密钥，创建拥有机器读写权限的密钥（ibk_开头）。
 
2. Configure GitHub Secrets | 配置环境变量
 
Repo  Settings  →  Secrets and variables  →  Actions 
Add new secret:
 
- Name:  INSTABOX_API_KEY 
- Value: Your InstaBox API Key
 
仓库设置 → Actions 密钥，新建变量填入你的 API 密钥。
 
3. Test Run | 启动测试
 
Open  Actions  → Select  InstaBox Keepalive  →  Run workflow 
Green tick = Deployment succeed.
 
进入 Actions 手动运行一次，出现绿色对勾即部署成功。
 
⚠️ Disclaimer | 免责声明
 
- This project is for personal learning and research purposes only.
本项目仅用于个人学习测试，请遵守对应平台用户协议。
- Thanks to the original algorithm author: @caichengle666
轮换算法逻辑感谢原作者开源贡献。
