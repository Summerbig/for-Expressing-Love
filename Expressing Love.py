#Expressing Love
import time
from playsound import playsound  # 需要安装 playsound 库，用于播放音乐

print("我喜欢你，你愿不愿意做我的女朋友？")
time.sleep(2)

response = input("请输入你的答案（yes/no）：")

if response == "yes":
    print("太好了，你愿意做我的女朋友！")
    playsound("love_song.mp3")  # 播放音乐
else:
    print("好的，我会继续努力的。")
