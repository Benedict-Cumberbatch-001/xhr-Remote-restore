#!/bin/bash

# 进入到你的 Git 仓库目录
cd E:/xhr-Remote-restore

# 执行 Git 添加、提交和推送
git add .
git commit -m "Auto commit by git_push.sh"
git push origin master

# 输出一条消息表示操作完成
echo "Git push complete."

read -p "Press any key to continue..."