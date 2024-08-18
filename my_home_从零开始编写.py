'''进度条_挑战'''
import streamlit as st
import time

# 进度条st.progress()
roading = st.progress(0, '开始加载')
for i in range(1, 101, 1):
    time.sleep(0.02)
    roading.progress(i, '正在加载'+str(i)+'%')
roading.progress(100, '加载完毕！')

# 如何创建组件？ 用 变量名 = st。progress()方法
# 创建组件之后如何调用组件实现效果？ 对象.progress()
# 两个参数的作用分别是？长度(0~100), 提示信息

# 挑战：制作一个倒计时进度条，让进度条逐渐从100%变为0%
roading = st.progress(100, '开始倒计时')
for i in range(1, 101, 1):
    time.sleep(0.02)
    roading.progress(100 - i, '正在倒数'+str(i)+'%')
roading.progress(0, '计时结束！')