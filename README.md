# mypkg
# リポジトリの概要
2021年度ロボットシステム学の課題２の提出用リポジトリです。
今年の運勢を占えます。ぜひお試しを
# 動作環境
- ubuntu 20.04.1 LTS
# 使用したもの
- Raspberry pi 4
-  Micro SD Card
# デモ動画
[![おみくじ](https://www.youtube.com/watch?v=qE2sXgm62OQ&feature=youtu.be)

# インストール方法
ROSを予めインストールしておいてください。
```
cd ~/catkin_ws/src
git clone https://github.com/sakurai-ruka/mypkg.git 
cd ..
catkin_make
```
# 実行方法
以下のコマンドで実行できます
- ターミナル1
```
roscore
```
- ターミナル2
```
cd ~/catkin_ws/src/mypkg/scripts
rosrun mypkg omi.py
```
- ターミナル3
```
cd ~/catkin_ws/src/mypkg/scripts
rosrun mypkg henkan.py
```
# ライセンス
BCD 3-Clause License
