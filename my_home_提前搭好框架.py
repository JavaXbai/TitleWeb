'''我的主页'''
import random
import streamlit as st
import time
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', "我的网页跳转"])

def page_1():
    st.write("BGM：周杰伦-青花瓷 + 阳光宅男 (Live).mp3")
    with open(r"周杰伦-青花瓷 + 阳光宅男 (Live).mp3", "rb") as f:
        mymp3_1 = f.read()
    st.audio(mymp3_1, format="audio/mp3", start_time=0)

    st.write("BGM：周杰伦-说好不哭 (钢琴版).mp3")
    with open(r"周杰伦-说好不哭 (钢琴版).mp3", "rb") as f:
        mymp3_2 = f.read()
    st.audio(mymp3_2, format="audio/mp3", start_time=0)

    st.write("BGM：周杰伦-枫 (自制版伴奏).mp3")
    with open(r"周杰伦-枫 (自制版伴奏).mp3", "rb") as f:
        mymp3_3 = f.read()
    st.audio(mymp3_3, format="audio/mp3", start_time=0)
    
    tabMovie, tabBook, tabGame, tabPractive = st.tabs(["电影推荐", "书籍推荐", "游戏推荐", "习题推荐"])
    with tabMovie:
        st.write("JavaXbai推荐电影")

        col_movie1, col_movie2 = st.columns(2)
        with col_movie1:
            st.write("1：《阿甘正传》")
            st.image(r"阿甘正传.jpg")
            st.write(
                "《阿甘正传》是由罗伯特·泽米吉斯执导，瑞克·罗斯、温斯顿·格鲁姆编剧，汤姆·汉克斯、罗宾·怀特和莎莉·菲尔德等人主演的美国剧情电影。该片于1994年7月6日在美国上映。")
            st.write(
                "《阿甘正传》改编自美国作家温斯顿·格鲁姆于1986年出版的同名小说，讲述了智商只有75的阿甘如何凭借纯真善良和坚持不懈的精神，从童年的欺凌中跑出一条人生道路，成为大")
            st.write(
                "榄球明星、越战英雄，经历多次与挚爱珍妮的悲欢离合，无意中参与重大历史事件，最终成为成功的企业家和父亲，展现了一个普通人在非凡时代背景下的非凡人生旅程学橄，于19")
            st.write(
                "95年第67届奥斯卡金像奖中获得13项提名，最终斩获包括最佳影片、最佳导演等六个奖项。同年，获得第52届金球奖剧情类最佳影片，提名第48届英国电影和电视艺术学院奖最佳")
            st.write("影片。2022年5月，优酷以4K标准修复了《阿甘正传》等一批海外励志经典作品。")
            st.image(r"阿甘正传2.png")

        with col_movie2:
            st.write("2：《我是谁：没有绝对安全的系统》")
            st.image(r"我是谁：没有绝对安全的系统.jpg")
            st.write(
                "本杰明是一个这样的人：智商165，但是在现实世界中，他是一个失败者，并且常常为找不到存在感而忧伤。他没有女朋友，喜欢的女孩虽然是同学，但是由于他的性格怪癖所以常年")
            st.write(
                "坐在教室的后面，导致女孩不认识他。但是二十五岁的他却是一个电脑黑客，拥有对C/C++等多种编程语言以及在黑客死亡IP追踪上拥有不可思议的天赋，他可以追踪到任何一个人的")
            st.write(
                "任何信息。而影片中另一位主人公麦克斯是一个渴望“黑客世界”的潜在革命者，他注意到了本杰明在网络方面神一般的操控能力。《我是谁：没有绝对安全的系统》剧照(5张)他们组")
            st.write(
                "建了黑客组织CLAY（clown laghing at you意思是小丑的嘲笑），并且先后入侵了国际安全系统、国际金融系统、国际金融评估系统、德国安全局、德国情报局。而在这期间他认")
            st.write("识了他最开始喜欢的女孩，开始交往。")
            st.image(r"我是谁：没有绝对安全的系统2.jpg")
            st.image(r"我是谁：没有绝对安全的系统3.png")

    with tabBook:
        st.write("JavaXbai的书籍推荐")

        col_book1, col_book2 = st.columns(2)
        with col_book1:
            st.write("1：《钢铁是怎样练成的》")
            st.image(r"钢铁是怎样炼成的.png")
            st.write(
                "《钢铁是怎样炼成的》是前苏联作家尼古拉·奥斯特洛夫斯基所著的一部长篇小说，于1933年完成。1932年，《钢铁是怎样炼成的》第一部开始在《青年近卫军》杂志上分期连载")
            st.write(
                "，1934年，小说的第二部也在同一杂志上发表。该小说通过记叙保尔·柯察金的成长道路告诉人们，一个人只有在革命的艰难困苦中战胜敌人也战胜自己，只有在把自己的追求和")
            st.write(
                "祖国、人民的利益联系在一起的时候，才会创造出奇迹，才会成长为钢铁战士。20世纪末以群众投票的形式评选出“感动共和国的五十本书”，这本书位居榜首。此外，根据统计，")
            st.write(
                "在整个苏联历史上，《钢铁是怎样炼成的》是最受欢迎的一部长篇小说，在作家生前即已出版41次，截至1986年有650个版本问世，发行量达到3650万册，主人公保尔·柯察金成")
            st.write(
                "为苏联乃至全世界心怀共产主义理想的青年的偶像。2020年4月，列入《教育部基础教育课程教材发展中心 中小学生阅读指导目录（2020年版）》初中段")
            st.image(r"钢铁是怎样炼成的2.png")
        with col_book2:
            st.write("2：《平凡的世界》")
            st.image(r"平凡的世界.jpg")
            st.write(
                "《平凡的世界》是中国作家路遥创作的一部全景式地表现中国当代城乡社会生活的百万字长篇小说。全书共三部。1986年12月首次出版。该书以中国70年代中期到80年代中期十")
            st.write(
                "年间为背景，通过复杂的矛盾纠葛，以孙少安和孙少平两兄弟为中心，刻画了当时社会各阶层众多普通人的形象；劳动与爱情、挫折与追求、痛苦与欢乐、日常生活与巨大社会冲突")
            st.write("纷繁地交织在一起，深刻地展示了普通人在大时代历史进程中所走过的艰难曲折的道路")
            st.image(r"平凡的世界2.png")
    with tabGame:
        st.write("JavaXbai的推荐游戏")

        st.write("1：Minecraft")
        st.image(r"Minecraft.jpg")
        st.write(
            "《我的世界》（Minecraft）是一款沙盒类电子游戏，开创者为马库斯·阿列克谢·泊松（Notch）。游戏由Mojang Studios维护，现隶属于微软Xbox游戏工作室。游戏最初于")
        st.write(
            "2009年5月17日作为Classic版本发布，并于2011年11月18日发布Java正式版。我的世界的游戏平台囊括桌面设备、移动设备和游戏主机。中国版现由网易游戏代理，于2016年")
        st.write(
            "5月20日在中国大陆运营。自开创伊始到延斯·伯根斯坦（Jeb）加入并负责开发之前，我的世界几乎全部的开发工作由Notch完成。游戏音乐由丹尼尔·罗森菲尔德（C418）和莉娜")
        st.write(
            "·雷恩（Lena Raine）创作；克里斯托弗·泽特斯特兰绘制了游戏中的画。该游戏以玩家在一个充满着方块的三维空间中自由地创造和破坏不同种类的方块为主题。玩家在游戏中可")
        st.write(
            "以在单人或多人模式中通过摧毁或创造精妙绝伦的建筑物和艺术，或者收集物品探索地图以完成游戏的成就（进度）。玩家也可以尝试在创造模式下(打开作弊)红石电路和指令等玩")
        st.write("法。")
        st.image(r"Minecraft2.png")
    with tabPractive:
        st.write("JavaXbai的习题推荐")
        st.image(r"五三.jpg")
        st.write("5年中考3年模拟》是由教育科学出版社、首都师范大学出版社出版的图书，作者是曲一线")
        st.image(r"五三2.png")
        for i in range(100):
            st.write("\n")
        st.write("你怎么还在往下翻？？")
        for i in range(100):
            st.write("\n")
        st.write("八嘎呀路~阁下怎么能写作业呢！")
        st.write("手机电脑大大滴好玩")
        st.write("呦西~")
def page_2():
    '''我的图片处理工具'''
    st.write("sunglasses:图片处理小程序:sunglasses")
    uploaded_file = st.file_uploader("上传图片", type=["png", "jpeg", "jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab_Color, tab_Cropping, tab_Rotate, tab_setsize, tab_lightness = (
            st.tabs(["换色", "裁剪", "旋转", "缩放", "亮度"]))
        i = 0
        r, g, b = 0, 0, 0
        with tab_Color:
            ir = st.number_input("R:", 0, 2)
            ig = st.number_input("G:", 0, 2)
            ib = st.number_input("B:", 0, 2)
            st.write("原图：")
            st.image(img)
            st.write("现图：")
            roading = st.progress(0, '开始加载')
            for i in range(1, 101, 1):
                time.sleep(0.02)
                roading.progress(i, '正在加载' + str(i) + '%')
            roading.progress(100, '加载完毕！')
            st.image(img_change(img, ir, ig, ib))
        with tab_Cropping:
            ilx = st.number_input("左上角X坐标：", 0)
            ily = st.number_input("左上角Y坐标：", 0)
            irx = st.number_input("右上角X坐标：", 0, value = 1)
            iry = st.number_input("右下角Y坐标：", 0, value = 1)
            st.write("原图：")
            st.image(img)
            st.write("现图：")
            roading = st.progress(0, '开始加载')
            for i in range(1, 101, 1):
                time.sleep(0.02)
                roading.progress(i, '正在加载' + str(i) + '%')
            roading.progress(100, '加载完毕！')
            st.image(img_cropping(img, ilx, ily, irx, iry))
        with tab_Rotate:
            ang = st.number_input("旋转角度：", 0, 360)
            st.write("原图：")
            st.image(img)
            st.write("现图：")
            roading = st.progress(0, '开始加载')
            for i in range(1, 101, 1):
                time.sleep(0.02)
                roading.progress(i, '正在加载' + str(i) + '%')
            roading.progress(100, '加载完毕！')
            st.image(img_rotate(img, ang))
        with tab_setsize:
            w = st.number_input("宽度：", 1, value = 1)
            h = st.number_input("高度：", 1, value = 1)
            st.write("原图：")
            st.image(img)
            st.write("现图：")
            roading = st.progress(0, '开始加载')
            for i in range(1, 101, 1):
                time.sleep(0.02)
                roading.progress(i, '正在加载' + str(i) + '%')
            roading.progress(100, '加载完毕！')
            st.image(img_retsize(img, w, h))
        with tab_lightness:
            creat_lightness = st.number_input("亮度增加倍数：", 0.0)
            st.write("原图：")
            st.image(img)
            st.write("现图：")
            roading = st.progress(0, '开始加载')
            for i in range(1, 101, 1):
                time.sleep(0.02)
                roading.progress(i, '正在加载' + str(i) + '%')
            roading.progress(100, '加载完毕！')
            st.image(img_lightness(img, creat_lightness))

def img_change(img, rc, gc, bc) :
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    return img

def img_cropping(img, lx, ly, rx, ry):
    img2 = img.crop((lx, ly, rx, ry))
    return img2

def img_rotate(img, angle):
    img2 = img.rotate(angle)
    return img2

def img_retsize(img, width, height):
    img2 = img.resize((width, height))
    return img2

def img_lightness(img, lightness):
    img2 = img.point(lambda p: p * lightness)
    return img2

def img_vague(img):
    img2 = img.filter(ImageFilter.BLUR)
def page_3():
    '''我的智能词典'''
    st.write("智慧词典")
    with open(r"words_space.txt", "r", encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    word_dict = {}
    for i in words_list:
        word_dict[i[1]] = [int(i[0]), i[2]]
    with open(r"check_out_times.txt", "r", encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input("请输入要查询的单词 或 输入'全部'显示全部单词")
    if (word in word_dict):
        st.write(word_dict[word][1])
        n = word_dict[word][0]
        if (n in times_dict):
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("check_out_times.txt", "w", encoding="utf-8") as f:
            message = ""
            for k, v in times_dict.items():
                message += str(k) + "#" + str(v) + "\n"
            message = message[:-1]
            f.write(message)
        st.write("查询次数", times_dict[n])
    elif (word == "全部"):
        is_show = st.selectbox("这可能会造成网页卡顿，是否继续？", ["是", "否"])
        if (is_show == "是"):
            for j in word_dict:
                st.write(word_dict[j][0])
                st.write(word_dict[j][1])

def page_4():
    '''我的留言区'''
    st.write("我的留言区")
    with open(r"leave_messages.txt", "r", encoding="utf-8") as f:
        message_list = f.read().split("\n")
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split("#")
    for i in message_list:
        with st.chat_message(""):
            st.write(i[1], ":", i[2])
    name = st.text_input("留言者姓名")
    moods = ["开心😃",
             "生气😠",
             "难过😟",
             "无语😑",
             "红温😈",
             "黑化👾",
             "兴奋😆",
             "自责😰",
             "紧张😬",
             "惊讶😦",
             "自豪😎",
             "害怕😱"]
    jobs = ["国家机关、党群组织、企业、事业单位负责人",
            "专业技术人员",
            "办事人员和有关人员",
            "商业、服务业人员",
            "农、林、牧、渔、水利业生产人员",
            "生产、运输设备、操作人员、",
            "军人",
            "不便分类的其他从业人名",
            "学生"]
    job = st.selectbox("我是：", jobs)
    mood_temporary = st.selectbox("当前心情", moods)
    mood = mood_set(mood_temporary)
    new_message = st.text_input("想要说的话：")
    clear = st.selectbox("清楚所有留言", ["否", "是"])
    name += "[" + str(job) + "]"
    if (clear == "是"):
        with open(r"leave_messages.txt", "w", encoding="utf-8") as f:
            f.truncate()
        with open(r"leave_messages.txt", "w", encoding="utf-8") as f:
            f.write("1#系统#请友善留言！")
    if (st.button("留言")):
        message_list.append([str(int(message_list[-1][0]) + 1), "    " + mood + " " + name, new_message])
        with open(r"leave_messages.txt", "w", encoding="utf-8") as f:
            message = ""
            for i in message_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "\n"
            message = message[:-1]
            f.write(message)
def mood_set(choose_mood):
    mood_expression = ""
    if (choose_mood == "开心😃"): mood_expression = "😃"
    elif (choose_mood == "生气😠"): mood_expression = "😠"
    elif (choose_mood == "难过😟"): mood_expression = "😟"
    elif (choose_mood == "无语😑"): mood_expression = "😑"
    elif (choose_mood == "红温😈"): mood_expression = "😈"
    elif (choose_mood == "黑化👾"): mood_expression = "👾"
    elif (choose_mood == "兴奋😆"): mood_expression = "😆"
    elif (choose_mood == "自责😰"): mood_expression = "😰"
    elif (choose_mood == "紧张😬"): mood_expression = "😬"
    elif (choose_mood == "惊讶😦"): mood_expression = "😦"
    elif (choose_mood == "自豪😎"): mood_expression = "😎"
    elif (choose_mood == "害怕😱"): mood_expression = "😱"
    return mood_expression

def page_5():
    st.write("我的跳转网页")

    col_socialize, col_play, col_study, col_work, col_other, col_buy, col_music = st.columns(7)

    with col_socialize:
        st.write("社交网站：")
        st.link_button('百度', 'https://www.baidu.com/')
        st.link_button("微博", "https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F")
        st.link_button("快手", "https://www.kuaishou.com/?isHome=1")
    with col_play:
        st.write("娱乐网站：")
        st.link_button("抖音", "https://www.douyin.com/")
        st.link_button("YouTube", "https://www.youtube.com/")
        st.link_button("小红书", "https://www.xiaohongshu.com/explore")
    with col_study:
        st.write("学习网站：")
        st.link_button("GitHub", "https://github.com/")
        st.link_button("CSDN", "https://www.csdn.net/")
        st.link_button("知乎", "https://www.zhihu.com/signin?next=%2F")
        st.link_button("B站", "https://www.bilibili.com/")
        st.link_button("博客", "https://www.cnblogs.com/")
    with col_work:
        st.write("办公网站：")
        st.link_button("Ps", "https://www.adobe.com/products/photoshop.html?promoid=RBS7NL7F&mv=other")
        st.link_button("美图秀秀", "https://pc.meitu.com/")
        st.link_button("WPS", "https://www.wps.cn/")
    with col_buy:
        st.write("网购网站：")
        st.link_button("京东", "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_42ff5c6d09574c7993001f3832192bf6")
        st.link_button("淘宝", "https://www.taobao.com/")
        st.link_button("拼夕夕", "https://www.pinduoduo.com/")
    with col_music:
        st.write("音乐网站：")
        st.link_button("QQ音乐", "https://y.qq.com/")
        st.link_button("酷狗音乐", "https://www.kugou.com/")
        st.link_button("网易云音乐", "https://music.163.com/")
    with col_other:
        st.write("其他网站：")
        st.link_button("ChatGPT-4", "https://openai.com/index/chatgpt/")
        st.link_button("文心一言", "https://yiyan.baidu.com/")

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == "我的网页跳转":
    page_5()
