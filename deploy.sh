#!/bin/bash
cd /root/redis-demo
# 拉取最新代码
git pull origin main
# 安装依赖
pip3 install -r requirements.txt
# 重启服务（先杀掉旧进程，再启动新进程）
pkill -f "python3 app.py"
nohup python3 app.py > app.log 2>&1 &
echo "✅ Deploy success"
