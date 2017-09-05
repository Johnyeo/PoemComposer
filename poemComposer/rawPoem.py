# coding:utf-8

frequecyList = [('人', 769), ('不', 752), ('风', 751), ('花', 728), ('春', 639), ('一', 584), ('山', 553), ('无', 544),
                ('月', 507), ('水', 468), ('日', 463), ('雨', 437), ('秋', 430), ('愁', 420), ('年', 418), ('天', 396),
                ('来', 394), ('云', 387), ('夜', 355), ('上', 352), ('江', 348), ('相', 341), ('有', 334), ('雪', 328),
                ('思', 319), ('寒', 314), ('时', 310), ('里', 309), ('明', 300), ('落', 295), ('归', 293), ('酒', 287),
                ('长', 277), ('何', 277), ('中', 274), ('叶', 273), ('处', 270), ('飞', 264), ('柳', 263), ('去', 263),
                ('如', 262), ('黄', 262), ('白', 243), ('千', 242), ('是', 241), ('泪', 237), ('红', 232), ('青', 229),
                ('尽', 228), ('万', 223), ('君', 220), ('清', 220), ('西', 220), ('心', 218), ('马', 218), ('东', 215),
                ('见', 208), ('家', 207), ('声', 206), ('草', 204), ('今', 201), ('知', 197), ('香', 197), ('生', 197),
                ('情', 197), ('楼', 192), ('流', 191), ('南', 190), ('满', 189), ('下', 188), ('空', 187), ('行', 186),
                ('烟', 181), ('自', 180), ('未', 175), ('子', 173), ('深', 173), ('故', 172), ('别', 172), ('在', 171),
                ('独', 171), ('梦', 170), ('雁', 169), ('阳', 167), ('头', 164), ('色', 164), ('玉', 163), ('绿', 158),
                ('为', 156), ('小', 155), ('重', 154), ('树', 154), ('断', 154), ('城', 154), ('金', 153), ('多', 151),
                ('新', 150), ('谁', 149), ('过', 148), ('似', 148), ('桥', 147), ('前', 147), ('离', 146), ('三', 146),
                ('高', 146), ('路', 146), ('得', 144), ('远', 144), ('此', 144), ('梅', 143), ('孤', 143), ('开', 142),
                ('？', 141), ('欲', 141), ('已', 139), ('竹', 137), ('门', 137), ('几', 136), ('事', 136), ('望', 135),
                ('更', 134), ('客', 132), ('枝', 132), ('看', 131), ('河', 131), ('十', 129), ('入', 128), ('边', 128),
                ('吹', 128), ('暮', 125), ('恨', 124), ('与', 123), ('桃', 123), ('乡', 123), ('我', 122), ('还', 121),
                ('成', 120), ('鸟', 120), ('到', 118), ('残', 117), ('燕', 116), ('老', 115), ('出', 113), ('斜', 112),
                ('回', 112), ('霜', 111), ('光', 111), ('轻', 111), ('影', 110), ('送', 109), ('女', 109), ('杨', 109),
                ('衣', 108), ('芳', 108), ('海', 108), ('朝', 108), ('伤', 107), ('醉', 106), ('旧', 103), ('两', 103),
                ('外', 103), ('当', 103), ('萧', 102), ('歌', 101), ('书', 101), ('可', 101), ('北', 101), ('初', 100),
                ('起', 100), ('后', 99), ('闲', 99), ('半', 99), ('国', 98), ('难', 97), ('又', 97), ('向', 97), ('华', 97),
                ('间', 97), ('道', 96), ('阴', 95), ('莫', 94), ('照', 94), ('兮', 93), ('犹', 93), ('游', 93), ('地', 93),
                ('好', 91), ('发', 91), ('晚', 91), ('平', 90), ('凉', 90), ('少', 90), ('古', 89), ('将', 89), ('尘', 89),
                ('野', 88), ('儿', 88), ('村', 88), ('碧', 88), ('语', 87), ('正', 87), ('垂', 87), ('关', 86), ('丝', 86),
                ('窗', 84), ('应', 84), ('暗', 83), ('林', 83), ('细', 82), ('画', 82), ('意', 82), ('露', 82), ('倚', 82),
                ('啼', 82), ('只', 81), ('问', 81), ('作', 80), ('百', 80), ('晓', 79), ('点', 79), ('湖', 79), ('沙', 79),
                ('灯', 76), ('依', 76), ('四', 76), ('舟', 76), ('也', 75), ('闻', 75), ('之', 75), ('溪', 75), ('双', 75),
                ('大', 75), ('星', 75), ('却', 74), ('笑', 74), ('庭', 74), ('乱', 74), ('带', 74), ('台', 74), ('同', 72),
                ('冷', 72), ('惊', 72), ('夕', 72), ('共', 72), ('荷', 72), ('岁', 71), ('昏', 71), ('木', 71), ('波', 71),
                ('帘', 71), ('身', 71), ('悲', 70), ('五', 70), ('能', 70), ('苦', 69), ('逢', 69), ('翠', 69), ('鸣', 69),
                ('数', 69), ('度', 68), ('节', 68), ('阑', 67), ('对', 67), ('悠', 67), ('忆', 66), ('晴', 66), ('气', 65),
                ('淡', 64), ('园', 64), ('疏', 64), ('菊', 64), ('动', 64), ('然', 64), ('微', 63), ('怜', 63), ('亭', 63),
                ('分', 63), ('横', 62), ('散', 62), ('眼', 62), ('复', 62), ('曾', 61), ('听', 61), ('先', 61), ('杯', 60),
                ('佳', 60), ('寂', 59), ('田', 59), ('肠', 59), ('随', 59), ('池', 59), ('手', 59), ('涯', 58), ('魂', 58),
                ('汉', 57), ('纷', 57), ('留', 57), ('片', 56), ('近', 56), ('曲', 55), ('凄', 55), ('解', 55), ('坐', 55),
                ('船', 54), ('飘', 54), ('火', 54), ('舞', 54), ('莺', 54), ('若', 54), ('塞', 53), ('宫', 53), ('寄', 53),
                ('觉', 53), ('堪', 53), ('胡', 53), ('隔', 53), ('冰', 53), ('岸', 52), ('从', 51), ('！', 51), ('遥', 51),
                ('安', 51), ('松', 50), ('美', 50), ('梨', 50), ('二', 50), ('言', 49), ('早', 49), ('消', 49), ('干', 49),
                ('幽', 49), ('绝', 48), ('罗', 48), ('绕', 48), ('征', 47), ('兰', 47), ('临', 47), ('寻', 47), ('九', 47),
                ('枕', 47), ('记', 46), ('须', 46), ('连', 46), ('教', 46), ('念', 45), ('卷', 45), ('登', 45), ('静', 45),
                ('低', 45), ('角', 45), ('眉', 45), ('了', 45), ('都', 45), ('条', 45), ('面', 44), ('卧', 44), ('和', 44),
                ('军', 44), ('终', 44), ('州', 43), ('待', 43), ('宵', 43), ('其', 43), ('浮', 43), ('把', 43), ('漫', 43),
                ('薄', 43), ('常', 43), ('想', 42), ('眠', 42), ('昨', 42), ('渐', 42), ('龙', 42), ('世', 42), ('桐', 42),
                ('住', 42), ('而', 41), ('直', 41), ('立', 41), ('亦', 41), ('怀', 41), ('童', 41), ('且', 41), ('死', 41),
                ('凭', 41), ('休', 41), ('塘', 41), ('渡', 41), ('宿', 40), ('湘', 40), ('珠', 40), ('茫', 40), ('转', 40),
                ('莲', 40), ('诗', 40), ('信', 40), ('湿', 40), ('昔', 40), ('石', 39), ('楚', 39), ('妆', 39), ('映', 39),
                ('王', 39), ('鱼', 39), ('沉', 39), ('最', 39), ('食', 39), ('桑', 38), ('吴', 38), ('陵', 38), ('短', 38),
                ('惟', 38), ('秦', 38), ('易', 38), ('苍', 37), ('忽', 37), ('梧', 37), ('胜', 37), ('报', 37), ('收', 37),
                ('于', 37), ('；', 37), ('识', 36), ('锦', 36), ('吟', 36), ('迢', 36), ('车', 36), ('鸦', 36), ('笛', 36),
                ('鸿', 36), ('至', 36), ('怨', 36), ('鸡', 36), ('爱', 36), ('非', 36), ('凝', 36), ('经', 35), ('浪', 35),
                ('仙', 35), ('许', 35), ('谢', 35), ('名', 35), ('催', 35), ('妾', 35), ('往', 35), ('峰', 35), ('紫', 35),
                ('方', 35), ('才', 35), ('荒', 35), ('期', 35), ('稀', 35), ('但', 35), ('镜', 35), ('容', 35), ('乐', 35),
                ('丹', 34), ('堂', 34), ('欢', 34), ('辞', 34), ('牛', 34), ('折', 34), ('那', 34), ('斗', 34), ('目', 34),
                ('原', 34), ('颜', 34), ('凤', 34), ('墙', 34), ('夫', 34), ('饮', 34), ('他', 34), ('掩', 34), ('鬓', 33),
                ('醒', 33), ('久', 33), ('战', 33), ('惜', 33), ('首', 33), ('被', 33), ('迟', 33), ('神', 33), ('漠', 33),
                ('叹', 33), ('瘦', 33), ('说', 33), ('物', 33), ('摇', 32), ('景', 32), ('畔', 32), ('盈', 32), ('浓', 32),
                ('取', 32), ('帆', 32), ('杏', 32), ('旗', 32), ('痕', 32), ('李', 31), ('六', 31), ('川', 31), ('会', 31),
                ('余', 31), ('阁', 31), ('素', 31), ('泉', 31), ('遍', 31), ('量', 31), ('院', 31), ('娇', 31), ('拂', 30),
                ('合', 30), ('采', 30), ('絮', 30), ('逐', 30), ('破', 30), ('限', 30), ('结', 30), ('暖', 29), ('群', 29),
                ('底', 29), ('银', 29), ('零', 29), ('傍', 29), ('径', 29), ('滴', 29), ('争', 29), ('销', 29), ('兴', 29),
                ('试', 29), ('种', 28), ('芙', 28), ('翻', 28), ('洲', 28), ('伴', 28), ('穷', 28), ('潇', 28), ('接', 28),
                ('弦', 28), ('袖', 28), ('洛', 28), ('音', 28), ('放', 28), ('岂', 27), ('穿', 27), ('梁', 27), ('因', 27),
                ('粉', 27), ('怅', 27), ('彩', 27), ('泥', 27), ('愿', 27), ('鼓', 27), ('骨', 27), ('屏', 27), ('息', 27),
                ('元', 27), ('朱', 27), ('英', 27), ('疑', 27), ('圆', 27), ('锁', 27), ('尊', 27), ('桂', 27), ('含', 26),
                ('系', 26), ('蝶', 26), ('晨', 26), ('端', 26), ('载', 26), ('剑', 26), ('妇', 26), ('午', 26), ('寞', 26),
                ('没', 26), ('尚', 26), ('霏', 26), ('蓉', 26), ('哀', 26), ('臣', 26), ('弄', 26), ('隐', 26), ('艳', 26),
                ('娥', 25), ('岭', 25), ('挂', 25), ('尺', 25), ('洗', 25), ('传', 25), ('户', 25), ('以', 25), ('罢', 25),
                ('管', 25), ('吾', 25), ('柔', 25), ('偏', 25), ('虚', 25), ('夏', 25), ('篱', 25), ('定', 25), ('钱', 25),
                ('寸', 25), ('著', 24), ('病', 24), ('冻', 24), ('蓬', 24), ('笼', 24), ('霞', 24), ('举', 24), ('阶', 24),
                ('急', 24), ('繁', 24), ('沾', 24), ('兵', 24), ('际', 24), ('轩', 24), ('衰', 24), ('栖', 24), ('芦', 23),
                ('使', 23), ('足', 23), ('积', 23), ('鹂', 23), ('土', 23), ('蝉', 23), ('忘', 23), ('雷', 23), ('读', 23),
                ('遗', 23), ('茶', 23), ('睡', 23), ('秀', 23), ('羞', 23), ('钟', 23), ('扬', 22), ('浅', 22), ('丛', 22),
                ('抱', 22), ('参', 22), ('麦', 22), ('学', 22), ('便', 22), ('母', 22), ('字', 22), ('郎', 22), ('织', 22),
                ('唱', 22), ('枫', 22), ('携', 22), ('力', 22), ('堤', 22), ('唯', 22), ('袅', 22), ('七', 22), ('渔', 22),
                ('虽', 22), ('忧', 22), ('嘶', 21), ('踏', 21), ('压', 21), ('闺', 21), ('劝', 21), ('总', 21), ('本', 21),
                ('良', 21), ('枯', 21), ('栏', 21), ('洒', 21), ('缕', 21), ('匆', 21), ('京', 21), ('走', 21), ('呼', 21),
                ('乍', 21), ('盘', 21), ('主', 21), ('洞', 20), ('交', 20), ('指', 20), ('杜', 20), ('衫', 20), ('父', 20),
                ('碎', 20), ('轮', 20), ('缘', 20), ('昼', 20), ('谷', 20), ('萋', 20), ('冉', 20), ('师', 20), ('差', 20),
                ('鹊', 20), ('浦', 20), ('悴', 20), ('壮', 20), ('况', 19), ('宝', 19), ('肯', 19), ('武', 19), ('忍', 19),
                ('禁', 19), ('倾', 19), ('渺', 19), ('团', 19), ('修', 19), ('扇', 19), ('钓', 19), ('鞍', 19), ('陌', 19),
                ('琴', 19), ('透', 19), ('雾', 19), ('帝', 19), ('歇', 19), ('杀', 19), ('蹄', 19), ('濛', 19), ('憔', 19),
                ('齐', 19), ('孙', 19), ('耕', 19), ('始', 19), ('危', 19), ('翁', 19), ('纱', 19), ('味', 19), ('喜', 19),
                ('潮', 19), ('借', 19), ('雄', 19), ('绣', 18), ('各', 18), ('骑', 18), ('士', 18), ('血', 18), ('猿', 18),
                ('裳', 18), ('唤', 18), ('居', 18), ('守', 18), ('床', 18), ('炉', 18), ('旌', 18), ('绵', 18), ('纤', 18),
                ('冥', 18), ('乌', 18), ('迷', 18), ('坠', 18), ('移', 18), ('层', 18), ('怕', 18), ('皆', 18), ('旅', 18),
                ('黛', 18), ('钩', 18), ('烛', 18), ('刀', 18), ('幕', 18), ('染', 17), ('鸳', 17), ('遮', 17), ('及', 17),
                ('鹭', 17), ('所', 17), ('觅', 17), ('八', 17), ('暂', 17), ('换', 17), ('俱', 17), ('虎', 17), ('邻', 17),
                ('盖', 17), ('亡', 17), ('个', 17), ('负', 17), ('衔', 17), ('亲', 17), ('岩', 17), ('宜', 17), ('闭', 17),
                ('冠', 17), ('令', 17), ('官', 17), ('恐', 17), ('功', 17), ('者', 17), ('雕', 17), ('再', 17), ('琼', 17),
                ('拥', 17), ('苏', 17), ('苑', 17), ('芜', 17), ('壶', 17), ('苔', 17), ('感', 17), ('尔', 17), ('戍', 17),
                ('倒', 16), ('市', 16), ('馆', 16), ('营', 16), ('漏', 16), ('真', 16), ('荡', 16), ('勤', 16), ('约', 16),
                ('井', 16), ('屋', 16), ('舍', 16), ('料', 16), ('佩', 16), ('绪', 16), ('极', 16), ('戎', 16), ('巴', 16),
                ('射', 16), ('越', 16), ('皎', 16), ('失', 16), ('壁', 16), ('郭', 16), ('狂', 16), ('永', 16), ('牵', 16),
                ('扫', 16), ('用', 16), ('灭', 16), ('迎', 16), ('添', 16), ('汀', 16), ('鸾', 16), ('凌', 15), ('阙', 15),
                ('弓', 15), ('赠', 15), ('倦', 15), ('烽', 15), ('茅', 15), ('商', 15), ('殿', 15), ('泣', 15), ('否', 15),
                ('场', 15), ('蕊', 15), ('戈', 15), ('蒲', 15), ('劳', 15), ('弹', 15), ('通', 15), ('席', 15), ('聚', 15),
                ('寺', 15), ('浩', 15), ('渚', 15), ('沧', 15), ('番', 15), ('顾', 15), ('肥', 15), ('柴', 15), ('比', 15),
                ('恰', 15), ('鞭', 15), ('扶', 15), ('由', 15), ('懒', 15), ('襟', 15), ('铁', 14), ('瑟', 14), ('毛', 14),
                ('檐', 14), ('根', 14), ('响', 14), ('题', 14), ('滋', 14), ('驱', 14), ('异', 14), ('论', 14), ('频', 14),
                ('冬', 14), ('公', 14), ('徒', 14), ('写', 14), ('哭', 14), ('脱', 14), ('泛', 14), ('阔', 14), ('姑', 14),
                ('太', 14), ('口', 14), ('蚕', 14), ('皇', 14), ('巾', 14), ('变', 14), ('蒙', 14), ('丰', 14), ('裙', 14),
                ('羽', 14), ('强', 14), ('奈', 14), ('引', 14), ('损', 14), ('潭', 14), ('黑', 14), ('豆', 14), ('梢', 14),
                ('虹', 14), ('蛾', 13), ('怒', 13), ('沈', 13), ('寥', 13), ('密', 13), ('缺', 13), ('忙', 13), ('乃', 13),
                ('彻', 13), ('惆', 13), ('榆', 13), ('插', 13), ('全', 13), ('扉', 13), ('庐', 13), ('贫', 13), ('藏', 13),
                ('汗', 13), ('索', 13), ('背', 13), ('娟', 13), ('线', 13), ('则', 13), ('着', 13), ('厌', 13), ('命', 13),
                ('榴', 13), ('志', 13), ('荆', 13), ('叠', 13), ('竿', 13), ('陇', 13), ('熟', 13), ('黯', 13), ('梳', 13),
                ('诉', 13), ('牧', 13), ('帐', 13), ('脉', 13), ('泊', 13), ('侵', 13), ('就', 13), ('民', 13), ('步', 13),
                ('笙', 13), ('必', 13), ('迹', 12), ('算', 12), ('亩', 12), ('披', 12), ('棹', 12), ('琶', 12), ('萦', 12),
                ('雀', 12), ('幸', 12), ('竟', 12), ('章', 12), ('规', 12), ('甚', 12), ('晖', 12), ('侧', 12), ('软', 12),
                ('敢', 12), ('帷', 12), ('历', 12), ('覆', 12), ('单', 12), ('阵', 12), ('酌', 12), ('遇', 12), ('鬼', 12),
                ('凋', 12), ('淮', 12), ('棠', 12), ('误', 12), ('鸥', 12), ('烧', 12), ('巷', 12), ('买', 12), ('弱', 12),
                ('堕', 12), ('巢', 12), ('簟', 12), ('羁', 12), ('旋', 12), ('惨', 12), ('机', 12), ('净', 12), ('悄', 12),
                ('淇', 11), ('蜀', 11), ('图', 11), ('辰', 11), ('丈', 11), ('赏', 11), ('触', 11), ('槛', 11), ('荣', 11),
                ('津', 11), ('渭', 11), ('砌', 11), ('霁', 11), ('续', 11), ('涛', 11), ('惹', 11), ('敲', 11), ('觞', 11),
                ('萝', 11), ('郁', 11), ('聊', 11), ('顷', 11), ('贱', 11), ('布', 11), ('偷', 11), ('纸', 11), ('并', 11),
                ('追', 11), ('蕉', 11), ('任', 11), ('计', 11), ('烂', 11), ('挥', 11), ('恩', 11), ('萸', 11), ('切', 11),
                ('堆', 11), ('赤', 11), ('啸', 11), ('纵', 11), ('乔', 11), ('阿', 11), ('鸯', 11), ('瑶', 11), ('藕', 11),
                ('芭', 10), ('腰', 10), ('筝', 10), ('程', 10), ('馀', 10), ('益', 10), ('脸', 10), ('喧', 10), ('街', 10),
                ('叫', 10), ('甲', 10), ('肌', 10), ('占', 10), ('停', 10), ('每', 10), ('理', 10), ('减', 10), ('猎', 10),
                ('吐', 10), ('灵', 10), ('朔', 10), ('伫', 10), ('话', 10), ('击', 10), ('菲', 10), ('持', 10), ('羌', 10),
                ('句', 10), ('招', 10), ('仍', 10), ('脂', 10), ('虏', 10), ('卖', 10), ('鹤', 10), ('咸', 10), ('琵', 10),
                ('驿', 10), ('赋', 10), ('皋', 10), ('做', 10), ('锄', 10), ('嗟', 10), ('趁', 10), ('第', 10), ('改', 10),
                ('凰', 10), ('代', 10), ('柏', 10), ('稻', 10), ('樽', 10), ('畏', 10), ('萼', 10), ('悬', 10), ('房', 10),
                ('辛', 10), ('恼', 10), ('男', 10), ('涨', 10), ('活', 10), ('宴', 10), ('绮', 10), ('展', 10), ('腊', 10),
                ('拟', 10), ('倩', 10), ('滚', 10), ('*', 10), ('箫', 10), ('悔', 10), ('飒', 10), ('啭', 9), ('霭', 9),
                ('裁', 9), ('豪', 9), ('表', 9), ('郊', 9), ('淅', 9), ('乘', 9), ('候', 9), ('廊', 9), ('疾', 9), ('列', 9),
                ('逝', 9), ('蓝', 9), ('浸', 9), ('澄', 9), ('鹃', 9), ('打', 9), ('夹', 9), ('欺', 9), ('态', 9), ('融', 9),
                ('投', 9), ('求', 9), ('威', 9), ('妃', 9), ('箭', 9), ('奇', 9), ('室', 9), ('返', 9), ('调', 9), ('铜', 9),
                ('杳', 9), ('羊', 9), ('窥', 9), ('认', 9), ('陶', 9), ('驾', 9), ('盏', 9), ('困', 9), ('巧', 9), ('内', 9),
                ('灞', 9), ('骚', 9), ('恋', 9), ('既', 9), ('崖', 9), ('冢', 9), ('盛', 9), ('笔', 9), ('菜', 9), ('张', 9),
                ('殷', 9), ('围', 9), ('翩', 9), ('瓜', 9), ('实', 8), ('侣', 8), ('仰', 8), ('利', 8), ('宽', 8), ('惯', 8),
                ('洁', 8), ('笳', 8), ('跃', 8), ('衾', 8), ('髻', 8), ('遣', 8), ('御', 8), ('摘', 8), ('徊', 8), ('砧', 8),
                ('伊', 8), ('文', 8), ('灰', 8), ('视', 8), ('等', 8), ('怪', 8), ('扑', 8), ('浴', 8), ('蜡', 8), ('嶂', 8),
                ('垣', 8), ('耿', 8), ('符', 8), ('抽', 8), ('广', 8), ('帏', 8), ('嫩', 8), ('笺', 8), ('岳', 8), ('观', 8),
                ('众', 8), ('鬟', 8), ('兼', 8), ('供', 8), ('渌', 8), ('萤', 8), ('榭', 8), ('匹', 8), ('递', 8), ('隅', 8),
                ('忠', 8), ('府', 8), ('澹', 8), ('慨', 8), ('付', 8), ('体', 8), ('戏', 8), ('裘', 8), ('除', 8), ('愧', 8),
                ('娘', 8), ('剪', 8), ('菱', 8), ('槐', 8), ('侯', 8), ('省', 8), ('暝', 8), ('敛', 8), ('舒', 8), ('环', 8),
                ('练', 8), ('禽', 8), ('泽', 8), ('摧', 8), ('姿', 8), ('加', 8), ('嫁', 8), ('要', 8), ('工', 8), ('杂', 8),
                ('败', 8), ('蓑', 8), ('妻', 7), ('快', 7), ('延', 7), ('裂', 7), ('酸', 7), ('承', 7), ('霰', 7), ('邀', 7),
                ('姬', 7), ('攀', 7), ('霄', 7), ('胧', 7), ('铺', 7), ('酣', 7), ('蔽', 7), ('稚', 7), ('涧', 7), ('拍', 7),
                ('钿', 7), ('称', 7), ('荔', 7), ('暑', 7), ('护', 7), ('避', 7), ('策', 7), ('坛', 7), ('藤', 7), ('牙', 7),
                ('俯', 7), ('饥', 7), ('峭', 7), ('冲', 7), ('吞', 7), ('饭', 7), ('龟', 7), ('萍', 7), ('浊', 7), ('扁', 7),
                ('化', 7), ('缀', 7), ('缠', 7), ('值', 7), ('蛩', 7), ('店', 7), ('宁', 7), ('怎', 7), ('屈', 7), ('斋', 7),
                ('蜂', 7), ('集', 7), ('峡', 7), ('巫', 7), ('宇', 7), ('薇', 7), ('严', 7), ('胭', 7), ('汪', 7), ('莽', 7),
                ('峨', 7), ('耳', 7), ('毫', 7), ('药', 7), ('针', 7), ('芰', 7), ('封', 7), ('源', 7), ('涌', 7), ('噪', 7),
                ('樵', 7), ('丁', 7), ('丘', 7), ('矣', 7), ('精', 7), ('夭', 7), ('挑', 7), ('号', 7), ('茱', 7), ('涕', 6),
                ('沽', 6), ('耐', 6), ('俗', 6), ('鲈', 6), ('慰', 6), ('蘋', 6), ('座', 6), ('辕', 6), ('祠', 6), ('弟', 6),
                ('颠', 6), ('藉', 6), ('尖', 6), ('次', 6), ('滨', 6), ('筵', 6), ('诏', 6), ('薰', 6), ('徘', 6), ('艾', 6),
                ('谓', 6), ('的', 6), ('泗', 6), ('麻', 6), ('寐', 6), ('肉', 6), ('览', 6), ('誓', 6), ('甘', 6), ('驻', 6),
                ('农', 6), ('妨', 6), ('形', 6), ('颗', 6), ('赖', 6), ('恶', 6), ('违', 6), ('殊', 6), ('勒', 6), ('钗', 6),
                ('请', 6), ('属', 6), ('欹', 6), ('簇', 6), ('袍', 6), ('谋', 6), ('咽', 6), ('敌', 6), ('温', 6), ('溶', 6),
                ('洋', 6), ('辽', 6), ('鹅', 6), ('浑', 6), ('委', 6), ('雰', 6), ('僧', 6), ('羡', 6), ('黍', 6), ('樯', 6),
                ('慵', 6), ('垒', 6), ('拨', 6), ('网', 6), ('吊', 6), ('缓', 6), ('杖', 6), ('鼠', 6), ('猫', 6), ('周', 6),
                ('即', 6), ('促', 6), ('郡', 6), ('弃', 6), ('乾', 6), ('健', 6), ('苹', 6), ('谈', 6), ('吠', 6), ('富', 6),
                ('笋', 6), ('痴', 6), ('怯', 6), ('社', 6), ('眺', 6), ('贾', 6), ('蔷', 6), ('虫', 6), ('苗', 6), ('圣', 6),
                ('激', 6), ('踪', 6), ('萏', 6), ('菡', 6), ('样', 6), ('绡', 6), ('灼', 6), ('曙', 6), ('磨', 6), ('支', 6),
                ('润', 6), ('抛', 6), ('妒', 6), ('尝', 6), ('晶', 6), ('兽', 6), ('受', 5), ('嫦', 5), ('赊', 5), ('礼', 5),
                ('鸠', 5), ('滟', 5), ('匀', 5), ('熏', 5), ('置', 5), ('词', 5), ('整', 5), ('袂', 5), ('冈', 5), ('鹿', 5),
                ('旷', 5), ('喷', 5), ('补', 5), ('答', 5), ('碗', 5), ('丽', 5), ('茂', 5), ('存', 5), ('渊', 5), ('媒', 5),
                ('鲜', 5), ('赴', 5), ('魄', 5), ('翼', 5), ('托', 5), ('适', 5), ('泰', 5), ('骄', 5), ('闹', 5), ('夸', 5),
                ('柯', 5), ('啾', 5), ('器', 5), ('苎', 5), ('朵', 5), ('填', 5), ('翦', 5), ('剩', 5), ('鹉', 5), ('靡', 5),
                ('鹦', 5), ('卿', 5), ('荻', 5), ('奴', 5), ('荠', 5), ('提', 5), ('蓼', 5), ('己', 5), ('宅', 5), ('兔', 5),
                ('途', 5), ('婵', 5), ('决', 5), ('义', 5), ('竞', 5), ('升', 5), ('犬', 5), ('貂', 5), ('笠', 5), ('顿', 5),
                ('米', 5), ('寿', 5), ('劲', 5), ('界', 5), ('输', 5), ('禾', 5), ('迁', 5), ('侬', 5), ('瀚', 5), ('饱', 5),
                ('材', 5), ('冶', 5), ('兹', 5), ('坟', 5), ('宣', 5), ('嫌', 5), ('趋', 5), ('或', 5), ('眸', 5), ('斑', 5),
                ('泻', 5), ('诸', 5), ('汾', 5), ('隋', 5), ('捣', 5), ('跨', 5), ('谩', 5), ('烦', 5), ('乞', 5), ('蛙', 5),
                ('玄', 5), ('浣', 5), ('蒿', 5), ('蝴', 5), ('坚', 5), ('漾', 5), ('圃', 5), ('废', 5), ('啄', 5), ('埋', 5),
                ('栊', 5), ('炬', 5), ('陂', 5), ('仲', 5), ('蕖', 5), ('柘', 5), ('障', 5), ('橘', 5), ('葵', 5), ('狼', 5),
                ('访', 5), ('瀑', 5), ('祝', 5), ('枉', 5), ('执', 5), ('截', 5), ('杵', 5), ('撑', 5), ('霎', 5), ('烈', 5),
                ('排', 5), ('板', 5), ('这', 4), ('舌', 4), ('惬', 4), ('藻', 4), ('旆', 4), ('娃', 4), ('讶', 4), ('珍', 4),
                ('衡', 4), ('助', 4), ('蛮', 4), ('紧', 4), ('盆', 4), ('偎', 4), ('馨', 4), ('牡', 4), ('抵', 4), ('豚', 4),
                ('焉', 4), ('汴', 4), ('浙', 4), ('抹', 4), ('韩', 4), ('岚', 4), ('联', 4), ('掣', 4), ('恁', 4), ('挟', 4),
                ('篷', 4), ('缆', 4), ('泼', 4), ('恻', 4), ('酿', 4), ('斯', 4), ('悦', 4), ('撩', 4), ('岫', 4), ('砚', 4),
                ('潜', 4), ('骊', 4), ('攒', 4), ('戴', 4), ('降', 4), ('鉴', 4), ('胆', 4), ('艇', 4), ('彼', 4), ('晦', 4),
                ('酬', 4), ('沼', 4), ('跳', 4), ('恒', 4), ('循', 4), ('免', 4), ('毵', 4), ('瑞', 4), ('婿', 4), ('吏', 4),
                ('艰', 4), ('祭', 4), ('枣', 4), ('蓟', 4), ('儒', 4), ('嵩', 4), ('犊', 4), ('毡', 4), ('飕', 4), ('哗', 4),
                ('派', 4), ('皱', 4), ('割', 4), ('湾', 4), ('宠', 4), ('齿', 4), ('骎', 4), ('费', 4), ('栽', 4), ('飐', 4),
                ('贵', 4), ('墨', 4), ('热', 4), ('迥', 4), ('闷', 4), ('阻', 4), ('鸪', 4), ('鹧', 4), ('颦', 4), ('仗', 4),
                ('嘉', 4), ('爽', 4), ('肤', 4), ('奔', 4), ('襄', 4), ('胥', 4), ('埃', 4), ('耶', 4), ('耀', 4), ('束', 4),
                ('尾', 4), ('瓯', 4), ('耻', 4), ('湛', 4), ('段', 4), ('增', 4), ('韶', 4), ('戚', 4), ('左', 4), ('酥', 4),
                ('摵', 4), ('业', 4), ('碛', 4), ('诚', 4), ('蛱', 4), ('缝', 4), ('末', 4), ('屠', 4), ('窕', 4), ('窈', 4),
                ('凛', 4), ('蟾', 4), ('矶', 4), ('伏', 4), ('旁', 4), ('赢', 4), ('陈', 4), ('垆', 4), ('遨', 4), ('株', 4),
                ('特', 4), ('媚', 4), ('养', 4), ('雏', 4), ('私', 4), ('友', 4), ('泠', 4), ('略', 4), ('鲁', 4), ('慷', 4),
                ('探', 4), ('冤', 4), ('韵', 4), ('搔', 4), ('昆', 4), ('性', 4), ('鲛', 4), ('：', 4), ('蔌', 4), ('荐', 4),
                ('贪', 4), ('虑', 4), ('拜', 4), ('逾', 4), ('檀', 4), ('槿', 4), ('驰', 4), ('陪', 4), ('蒂', 4), ('鹰', 4),
                ('局', 4), ('瓦', 4), ('毂', 4), ('滩', 4), ('扰', 4), ('壑', 4), ('棋', 4), ('梯', 4), ('螺', 4), ('果', 4),
                ('些', 4), ('予', 4), ('掷', 4), ('氏', 4), ('杭', 4), ('翔', 4), ('弥', 4), ('乎', 4), ('遭', 4), ('玲', 4),
                ('荇', 4), ('涵', 4), ('胸', 4), ('溢', 4), ('辨', 4), ('窟', 4), ('裛', 4), ('央', 4), ('煮', 4), ('弯', 4),
                ('缨', 4), ('溅', 4), ('淘', 4), ('璃', 4), ('琉', 4), ('朽', 4), ('骤', 4), ('刘', 4), ('舂', 3), ('犁', 3),
                ('告', 3), ('侍', 3), ('蔻', 3), ('飖', 3), ('琅', 3), ('浥', 3), ('漪', 3), ('颍', 3), ('震', 3), ('鼎', 3),
                ('混', 3), ('沃', 3), ('伐', 3), ('翅', 3), ('块', 3), ('陲', 3), ('妙', 3), ('闾', 3), ('惭', 3), ('仓', 3),
                ('籍', 3), ('装', 3), ('昭', 3), ('瘴', 3), ('卓', 3), ('象', 3), ('隰', 3), ('韭', 3), ('淹', 3), ('蕙', 3),
                ('岑', 3), ('旦', 3), ('徐', 3), ('磬', 3), ('盟', 3), ('猛', 3), ('炎', 3), ('般', 3), ('刚', 3), ('骖', 3),
                ('貌', 3), ('瓶', 3), ('墟', 3), ('庆', 3), ('餐', 3), ('逼', 3), ('狐', 3), ('榔', 3), ('暇', 3), ('替', 3),
                ('偶', 3), ('顽', 3), ('纹', 3), ('皓', 3), ('刷', 3), ('藜', 3), ('庾', 3), ('赐', 3), ('秉', 3), ('逞', 3),
                ('禄', 3), ('包', 3), ('印', 3), ('庙', 3), ('宾', 3), ('济', 3), ('博', 3), ('泫', 3), ('晕', 3), ('簪', 3),
                ('渠', 3), ('厚', 3), ('匣', 3), ('椰', 3), ('舸', 3), ('朦', 3), ('匝', 3), ('犯', 3), ('施', 3), ('溟', 3),
                ('樱', 3), ('敬', 3), ('嬉', 3), ('筹', 3), ('醺', 3), ('险', 3), ('捧', 3), ('奉', 3), ('戛', 3), ('粲', 3),
                ('飙', 3), ('卉', 3), ('仞', 3), ('眇', 3), ('拆', 3), ('害', 3), ('伯', 3), ('椎', 3), ('拼', 3), ('闰', 3),
                ('酹', 3), ('毕', 3), ('逗', 3), ('阖', 3), ('彭', 3), ('握', 3), ('霓', 3), ('踌', 3), ('浇', 3), ('翰', 3),
                ('辉', 3), ('腮', 3), ('醪', 3), ('膏', 3), ('铅', 3), ('颇', 3), ('靥', 3), ('奢', 3), ('塔', 3), ('坤', 3),
                ('荚', 3), ('缲', 3), ('蟠', 3), ('拔', 3), ('贯', 3), ('荞', 3), ('葱', 3), ('粒', 3), ('砂', 3), ('谙', 3),
                ('兄', 3), ('稠', 3), ('固', 3), ('臆', 3), ('鳞', 3), ('怆', 3), ('渴', 3), ('粱', 3), ('挽', 3), ('朗', 3),
                ('帽', 3), ('霸', 3), ('晌', 3), ('建', 3), ('突', 3), ('徙', 3), ('喃', 3), ('嘹', 3), ('致', 3), ('酴', 3),
                ('葩', 3), ('唳', 3), ('穗', 3), ('序', 3), ('茎', 3), ('裴', 3), ('灶', 3), ('畴', 3), ('裹', 3), ('煎', 3),
                ('篇', 3), ('褪', 3), ('贤', 3), ('杪', 3), ('涓', 3), ('献', 3), ('葭', 3), ('涉', 3), ('饶', 3), ('蒹', 3),
                ('鼻', 3), ('注', 3), ('邪', 3), ('瞰', 3), ('卫', 3), ('酷', 3), ('厨', 3), ('宛', 3), ('皑', 3), ('慕', 3),
                ('辜', 3), ('品', 3), ('茧', 3), ('幅', 3), ('络', 3), ('患', 3), ('邑', 3), ('柚', 3), ('漳', 3), ('卢', 3),
                ('沦', 3), ('班', 3), ('峦', 3), ('秣', 3), ('绛', 3), ('蘸', 3), ('纶', 3), ('达', 3), ('寝', 3), ('架', 3),
                ('坊', 3), ('熊', 3), ('鲤', 3), ('腻', 3), ('亏', 3), ('你', 3), ('腹', 3), ('坞', 3), ('污', 3), ('珊', 3),
                ('溜', 3), ('躯', 3), ('祁', 3), ('召', 3), ('卮', 3), ('缸', 3), ('筠', 3), ('确', 3), ('荦', 3), ('奏', 3),
                ('疲', 3), ('伦', 3), ('芽', 3), ('稍', 3), ('慈', 3), ('滞', 3), ('推', 3), ('妹', 3), ('沟', 3), ('壕', 3),
                ('假', 3), ('呵', 3), ('拚', 3), ('倍', 3), ('蜓', 3), ('蜻', 3), ('篙', 2), ('屑', 2), ('滂', 2), ('止', 2),
                ('徭', 2), ('法', 2), ('储', 2), ('典', 2), ('晋', 2), ('宰', 2), ('嵬', 2), ('铃', 2), ('拈', 2), ('壤', 2),
                ('铎', 2), ('滑', 2), ('拳', 2), ('惠', 2), ('瞻', 2), ('慊', 2), ('桨', 2), ('娆', 2), ('蕤', 2), ('它', 2),
                ('刻', 2), ('区', 2), ('葳', 2), ('涂', 2), ('项', 2), ('嗷', 2), ('贞', 2), ('件', 2), ('赌', 2), ('妩', 2),
                ('简', 2), ('觑', 2), ('蓿', 2), ('苜', 2), ('粟', 2), ('效', 2), ('煞', 2), ('按', 2), ('普', 2), ('退', 2),
                ('胫', 2), ('麟', 2), ('巳', 2), ('控', 2), ('霖', 2), ('蹑', 2), ('掀', 2), ('莹', 2), ('菖', 2), ('沓', 2),
                ('妍', 2), ('播', 2), ('殒', 2), ('粽', 2), ('巨', 2), ('慢', 2), ('衢', 2), ('锡', 2), ('荫', 2), ('浆', 2),
                ('骢', 2), ('淋', 2), ('慳', 2), ('箔', 2), ('楫', 2), ('拾', 2), ('鸶', 2), ('设', 2), ('拭', 2), ('俦', 2),
                ('骋', 2), ('贼', 2), ('乏', 2), ('夷', 2), ('於', 2), ('扈', 2), ('谹', 2), ('顺', 2), ('焰', 2), ('陨', 2),
                ('薪', 2), ('贴', 2), ('苞', 2), ('菟', 2), ('棘', 2), ('霾', 2), ('恢', 2), ('唐', 2), ('镇', 2), ('史', 2),
                ('牖', 2), ('敝', 2), ('糁', 2), ('么', 2), ('阊', 2), ('纨', 2), ('蚁', 2), ('徕', 2), ('枥', 2), ('捉', 2),
                ('乳', 2), ('蓄', 2), ('搴', 2), ('洮', 2), ('樾', 2), ('凡', 2), ('湑', 2), ('孩', 2), ('揭', 2), ('沛', 2),
                ('菇', 2), ('鼙', 2), ('膻', 2), ('茨', 2), ('舜', 2), ('掠', 2), ('愚', 2), ('淑', 2), ('篥', 2), ('觱', 2),
                ('酲', 2), ('翡', 2), ('栋', 2), ('飏', 2), ('潸', 2), ('麋', 2), ('炙', 2), ('栈', 2), ('遐', 2), ('进', 2),
                ('右', 2), ('薜', 2), ('籁', 2), ('揖', 2), ('苇', 2), ('搂', 2), ('瞿', 2), ('邮', 2), ('康', 2), ('雉', 2),
                ('纳', 2), ('亚', 2), ('贺', 2), ('茸', 2), ('蛇', 2), ('粮', 2), ('蕃', 2), ('辅', 2), ('坂', 2), ('副', 2),
                ('膳', 2), ('庸', 2), ('萱', 2), ('焚', 2), ('黏', 2), ('服', 2), ('较', 2), ('鸢', 2), ('债', 2), ('叩', 2),
                ('完', 2), ('蹀', 2), ('箧', 2), ('箨', 2), ('凫', 2), ('赵', 2), ('龄', 2), ('翮', 2), ('崇', 2), ('具', 2),
                ('俭', 2), ('帖', 2), ('速', 2), ('藓', 2), ('缟', 2), ('亮', 2), ('偕', 2), ('屯', 2), ('仪', 2), ('捻', 2),
                ('醅', 2), ('罩', 2), ('县', 2), ('舫', 2), ('充', 2), ('熠', 2), ('驴', 2), ('烹', 2), ('辄', 2), ('脑', 2),
                ('後', 2), ('苒', 2), ('蛛', 2), ('婆', 2), ('冒', 2), ('荏', 2), ('翳', 2), ('纡', 2), ('善', 2), ('袭', 2),
                ('踞', 2), ('桄', 2), ('瓢', 2), ('腕', 2), ('厉', 2), ('勾', 2), ('牂', 2), ('毁', 2), ('痛', 2), ('擢', 2),
                ('漻', 2), ('狎', 2), ('粪', 2), ('运', 2), ('娱', 2), ('炊', 2), ('鬖', 2), ('肃', 2), ('玩', 2), ('厩', 2),
                ('莱', 2), ('靖', 2), ('宸', 2), ('骓', 2), ('姥', 2), ('洪', 2), ('嵯', 2), ('履', 2), ('刺', 2), ('朋', 2),
                ('格', 2), ('函', 2), ('贮', 2), ('怡', 2), ('碍', 2), ('逆', 2), ('漂', 2), ('枻', 2), ('剥', 2), ('势', 2),
                ('禹', 2), ('炼', 2), ('槊', 2), ('错', 2), ('辇', 2), ('辔', 2), ('湄', 2), ('胶', 2), ('髓', 2), ('顶', 2),
                ('葬', 2), ('堑', 2), ('辈', 2), ('窦', 2), ('柱', 2), ('殢', 2), ('揉', 2), ('眄', 2), ('捷', 2), ('港', 2),
                ('刃', 2), ('箱', 2), ('澳', 2), ('像', 2), ('愔', 2), ('陆', 2), ('蹴', 2), ('荧', 2), ('轧', 2), ('涩', 2),
                ('葆', 2), ('郴', 2), ('颓', 2), ('纠', 2), ('腾', 2), ('妖', 2), ('潦', 2), ('务', 2), ('绾', 2), ('稳', 2),
                ('鹄', 2), ('躇', 2), ('叟', 2), ('领', 2), ('菩', 2), ('姮', 2), ('莎', 2), ('臂', 2), ('瑁', 2), ('咏', 2),
                ('麝', 2), ('玳', 2), ('莼', 2), ('祗', 2), ('篆', 2), ('坼', 2), ('碾', 2), ('凿', 2), ('昌', 2), ('翘', 2),
                ('茕', 2), ('闪', 2), ('奁', 2), ('珑', 2), ('婚', 2), ('沅', 2), ('椒', 2), ('位', 2), ('喻', 2), ('肝', 2),
                ('雍', 2), ('棉', 2), ('榻', 2), ('毅', 2), ('铸', 2), ('敷', 2), ('亿', 2), ('芬', 2), ('俸', 2), ('幼', 2),
                ('澌', 2), ('炯', 2), ('辙', 2), ('炭', 2), ('蜜', 2), ('隘', 2), ('鹜', 2), ('蹊', 2), ('缈', 2), ('缥', 2),
                ('惶', 2), ('佛', 2), ('傲', 2), ('辟', 2), ('槎', 2), ('乖', 2), ('澜', 2), ('斛', 2), ('超', 2), ('反', 2),
                ('寨', 2), ('坡', 2), ('伶', 2), ('摩', 2), ('燃', 2), ('跎', 2), ('蹉', 2), ('恣', 2), ('鸭', 2), ('菀', 2),
                ('仑', 2), ('烘', 2), ('拦', 2), ('掌', 2), ('振', 2), ('郸', 2), ('邯', 2), ('幔', 2), ('柄', 2), ('谯', 2),
                ('穴', 2), ('陷', 2), ('簸', 2), ('划', 2), ('簌', 2), ('欣', 2), ('栀', 2), ('韬', 2), ('据', 2), ('汶', 2),
                ('芊', 2), ('造', 2), ('滔', 2), ('稽', 2), ('蓁', 2), ('瘁', 2), ('躬', 2), ('鞠', 2), ('趵', 2), ('畦', 2),
                ('浔', 2), ('姓', 2), ('唇', 2), ('珀', 2), ('琥', 2), ('宗', 2), ('窅', 2), ('濯', 2), ('庄', 2), ('甜', 2),
                ('竭', 2), ('匈', 2), ('咤', 2), ('潼', 2), ('呜', 2), ('尸', 2), ('侠', 2), ('款', 2), ('曹', 2), ('戟', 2),
                ('曈', 2), ('夺', 2), ('欸', 2), ('季', 2), ('镀', 2), ('潺', 2), ('犀', 2), ('粼', 2), ('擒', 2), ('构', 1),
                ('衍', 1), ('甍', 1), ('曝', 1), ('跸', 1), ('保', 1), ('璜', 1), ('璇', 1), ('槟', 1), ('漆', 1), ('狱', 1),
                ('刈', 1), ('舰', 1), ('艟', 1), ('艨', 1), ('跼', 1), ('踡', 1), ('脆', 1), ('怼', 1), ('枹', 1), ('援', 1),
                ('絷', 1), ('仔', 1), ('祖', 1), ('稷', 1), ('皂', 1), ('茹', 1), ('囚', 1), ('缧', 1), ('薶', 1), ('牲', 1),
                ('牺', 1), ('泮', 1), ('饤', 1), ('册', 1), ('踵', 1), ('编', 1), ('柝', 1), ('眷', 1), ('钦', 1), ('圯', 1),
                ('哦', 1), ('司', 1), ('孀', 1), ('迳', 1), ('拖', 1), ('螀', 1), ('蔼', 1), ('幌', 1), ('湍', 1), ('苣', 1),
                ('靸', 1), ('矗', 1), ('闱', 1), ('瘢', 1), ('缭', 1), ('刳', 1), ('办', 1), ('骇', 1), ('镈', 1), ('霂', 1),
                ('蝟', 1), ('缩', 1), ('觇', 1), ('斧', 1), ('霡', 1), ('羲', 1), ('植', 1), ('卜', 1), ('税', 1), ('嵋', 1),
                ('蔬', 1), ('阏', 1), ('敞', 1), ('饼', 1), ('惮', 1), ('帛', 1), ('颅', 1), ('鸷', 1), ('轴', 1), ('绢', 1),
                ('婴', 1), ('培', 1), ('砾', 1), ('获', 1), ('粜', 1), ('狗', 1), ('偿', 1), ('樊', 1), ('呢', 1), ('旍', 1),
                ('鄂', 1), ('攸', 1), ('倏', 1), ('埏', 1), ('喉', 1), ('黠', 1), ('灾', 1), ('徂', 1), ('谿', 1), ('队', 1),
                ('弋', 1), ('阡', 1), ('蝼', 1), ('憀', 1), ('辩', 1), ('頩', 1), ('鹳', 1), ('谤', 1), ('窖', 1), ('锐', 1),
                ('伸', 1), ('涘', 1), ('缣', 1), ('泳', 1), ('鶒', 1), ('鸂', 1), ('鬒', 1), ('墦', 1), ('泾', 1), ('毯', 1),
                ('质', 1), ('飚', 1), ('汐', 1), ('雊', 1), ('暧', 1), ('窣', 1), ('掾', 1), ('资', 1), ('酾', 1), ('勋', 1),
                ('欠', 1), ('俟', 1), ('姊', 1), ('吃', 1), ('跋', 1), ('捕', 1), ('淖', 1), ('蹡', 1), ('踉', 1), ('膊', 1),
                ('厢', 1), ('哑', 1), ('呕', 1), ('甑', 1), ('诲', 1), ('颖', 1), ('姨', 1), ('飧', 1), ('缁', 1), ('穆', 1),
                ('寓', 1), ('蹇', 1), ('纥', 1), ('魏', 1), ('羔', 1), ('洌', 1), ('擅', 1), ('郑', 1), ('孺', 1), ('轳', 1),
                ('焦', 1), ('芋', 1), ('讼', 1), ('橦', 1), ('辘', 1), ('藿', 1), ('骝', 1), ('庶', 1), ('邃', 1), ('瓠', 1),
                ('罟', 1), ('蜃', 1), ('浃', 1), ('枚', 1), ('刹', 1), ('罹', 1), ('豺', 1), ('噤', 1), ('统', 1), ('苕', 1),
                ('彤', 1), ('垠', 1), ('腥', 1), ('曜', 1), ('辍', 1), ('茗', 1), ('猷', 1), ('绀', 1), ('雱', 1), ('叇', 1),
                ('叆', 1), ('嗥', 1), ('冽', 1), ('蠡', 1), ('镝', 1), ('惩', 1), ('滕', 1), ('榼', 1), ('稊', 1), ('呖', 1),
                ('擘', 1), ('呗', 1), ('脊', 1), ('琪', 1), ('域', 1), ('搓', 1), ('宦', 1), ('娑', 1), ('抚', 1), ('孟', 1),
                ('慑', 1), ('饵', 1), ('蜍', 1), ('跗', 1), ('议', 1), ('梵', 1), ('橹', 1), ('幂', 1), ('宏', 1), ('诮', 1),
                ('桁', 1), ('践', 1), ('嫣', 1), ('筇', 1), ('哥', 1), ('潘', 1), ('骏', 1), ('玑', 1), ('靓', 1), ('纻', 1),
                ('诺', 1), ('寡', 1), ('蔡', 1), ('唁', 1), ('邺', 1), ('氛', 1), ('斓', 1), ('韘', 1), ('芄', 1), ('驼', 1),
                ('垄', 1), ('俎', 1), ('俊', 1), ('灿', 1), ('累', 1), ('晻', 1), ('雌', 1), ('橡', 1), ('耦', 1), ('铮', 1),
                ('袨', 1), ('醿', 1), ('罅', 1), ('镊', 1), ('柮', 1), ('婷', 1), ('娉', 1), ('榾', 1), ('猜', 1), ('赛', 1),
                ('鄣', 1), ('杷', 1), ('枇', 1), ('职', 1), ('轲', 1), ('担', 1), ('淼', 1), ('畎', 1), ('附', 1), ('嘱', 1),
                ('葓', 1), ('傅', 1), ('屐', 1), ('斤', 1), ('削', 1), ('堵', 1), ('帔', 1), ('镫', 1), ('葺', 1), ('榈', 1),
                ('衙', 1), ('茵', 1), ('幄', 1), ('涡', 1), ('軝', 1), ('磐', 1), ('琚', 1), ('饷', 1), ('筑', 1), ('矢', 1),
                ('萨', 1), ('菰', 1), ('铓', 1), ('琳', 1), ('酱', 1), ('蒟', 1), ('馐', 1), ('爪', 1), ('耒', 1), ('檄', 1),
                ('蒸', 1), ('歜', 1), ('邱', 1), ('沂', 1), ('掬', 1), ('庑', 1), ('佃', 1), ('鞋', 1), ('衲', 1), ('庵', 1),
                ('讨', 1), ('勇', 1), ('霍', 1), ('銮', 1), ('皲', 1), ('嵲', 1), ('贷', 1), ('嵽', 1), ('旱', 1), ('黦', 1),
                ('袜', 1), ('靿', 1), ('奠', 1), ('痒', 1), ('甸', 1), ('讽', 1), ('描', 1), ('徇', 1), ('谪', 1), ('叛', 1),
                ('殪', 1), ('躐', 1), ('筋', 1), ('颊', 1), ('沁', 1), ('蔓', 1), ('崔', 1), ('刬', 1), ('傥', 1), ('筐', 1),
                ('悢', 1), ('豗', 1), ('役', 1), ('旻', 1), ('歧', 1), ('选', 1), ('刑', 1), ('禀', 1), ('姜', 1), ('劈', 1),
                ('峙', 1), ('竦', 1), ('岛', 1), ('炀', 1), ('盂', 1), ('茜', 1), ('溰', 1), ('囊', 1), ('漼', 1), ('堍', 1),
                ('瞅', 1), ('圈', 1), ('抬', 1), ('虿', 1), ('蕨', 1), ('电', 1), ('饯', 1), ('瞥', 1), ('狸', 1), ('让', 1),
                ('豫', 1), ('蛰', 1), ('科', 1), ('斟', 1), ('肩', 1), ('髇', 1), ('婺', 1), ('蛄', 1), ('蟪', 1), ('晏', 1),
                ('呀', 1), ('扪', 1), ('绳', 1), ('靴', 1), ('惚', 1), ('豳', 1), ('誉', 1), ('姞', 1), ('罴', 1), ('恍', 1),
                ('帜', 1), ('检', 1), ('拘', 1), ('乙', 1), ('诵', 1), ('悟', 1), ('敏', 1), ('峻', 1), ('髭', 1), ('狖', 1),
                ('搀', 1), ('崩', 1), ('覃', 1), ('汝', 1), ('隙', 1), ('憩', 1), ('鹴', 1), ('鹔', 1), ('启', 1), ('肆', 1),
                ('暄', 1), ('秾', 1), ('柂', 1), ('捩', 1), ('咒', 1), ('涪', 1), ('垓', 1), ('侈', 1), ('孔', 1), ('枳', 1),
                ('槲', 1), ('顗', 1), ('隳', 1), ('逅', 1), ('邂', 1), ('邈', 1), ('警', 1), ('咫', 1), ('.', 1), ('僻', 1),
                ('订', 1), ('冀', 1), ('騑', 1), ('姝', 1), ('颃', 1), ('颉', 1), ('泄', 1), ('鹯', 1), ('殇', 1), ('墉', 1),
                ('剖', 1), ('袛', 1), ('剧', 1), ('艖', 1), ('汨', 1), ('醴', 1), ('掇', 1), ('绫', 1), ('睛', 1), ('稗', 1),
                ('蔚', 1), ('迭', 1), ('罍', 1), ('嵘', 1), ('峥', 1), ('羸', 1), ('医', 1), ('劚', 1), ('遽', 1), ('箩', 1),
                ('旎', 1), ('旖', 1), ('碣', 1), ('蜘', 1), ('哉', 1), ('斵', 1), ('疮', 1), ('腐', 1), ('葑', 1), ('佁', 1),
                ('澈', 1), ('撼', 1), ('祈', 1), ('辗', 1), ('溯', 1), ('毳', 1), ('拏', 1), ('蹙', 1), ('概', 1), ('习', 1),
                ('漱', 1), ('媛', 1), ('遂', 1), ('弭', 1), ('焜', 1), ('牢', 1), ('棕', 1), ('搅', 1), ('鬣', 1), ('骛', 1),
                ('擎', 1), ('醮', 1), ('琐', 1), ('醾', 1), ('桔', 1), ('夔', 1), ('庚', 1), ('捶', 1), ('娄', 1), ('黔', 1),
                ('糅', 1), ('禅', 1), ('迸', 1), ('窄', 1), ('备', 1), ('监', 1), ('圬', 1), ('峋', 1), ('兆', 1), ('仿', 1),
                ('篌', 1), ('俜', 1), ('箜', 1), ('鍪', 1), ('兜', 1), ('逍', 1), ('隄', 1), ('欬', 1), ('謦', 1), ('缃', 1),
                ('橙', 1), ('暴', 1), ('搧', 1), ('赶', 1), ('鹖', 1), ('哮', 1), ('咆', 1), ('沥', 1), ('彰', 1), ('嶙', 1),
                ('撒', 1), ('互', 1), ('弗', 1), ('嘘', 1), ('琨', 1), ('籴', 1), ('麒', 1), ('斡', 1), ('缪', 1), ('绸', 1),
                ('纲', 1), ('纪', 1), ('醇', 1), ('镛', 1), ('徨', 1), ('揾', 1), ('膝', 1), ('鲵', 1), ('聆', 1), ('财', 1),
                ('仆', 1), ('婢', 1), ('萌', 1), ('迤', 1), ('逶', 1), ('霪', 1), ('摆', 1), ('盗', 1), ('寇', 1), ('廷', 1),
                ('鲸', 1), ('酝', 1), ('躞', 1), ('悭', 1), ('嚬', 1), ('砀', 1), ('芒', 1), ('瓮', 1), ('酊', 1), ('酩', 1),
                ('矮', 1), ('亘', 1), ('什', 1), ('缫', 1), ('拣', 1), ('斫', 1), ('劫', 1), ('唾', 1), ('扙', 1), ('虢', 1),
                ('掖', 1), ('铭', 1), ('瘗', 1), ('球', 1), ('札', 1), ('缄', 1), ('珰', 1), ('宪', 1), ('拄', 1), ('骸', 1),
                ('凶', 1), ('裟', 1), ('袈', 1), ('箸', 1), ('漉', 1), ('衬', 1), ('准', 1), ('森', 1), ('曳', 1), ('圞', 1),
                ('脩', 1), ('涸', 1), ('丑', 1), ('核', 1), ('阕', 1), ('搭', 1), ('颤', 1), ('咨', 1), ('蚤', 1), ('研', 1),
                ('訧', 1), ('俾', 1), ('治', 1), ('梓', 1), ('蒌', 1), ('佐', 1), ('桓', 1), ('谐', 1), ('莞', 1), ('趣', 1),
                ('标', 1), ('荄', 1), ('忒', 1), ('慧', 1), ('娲', 1), ('畅', 1), ('讯', 1), ('桡', 1), ('韦', 1), ('呆', 1),
                ('勿', 1), ('秽', 1), ('铢', 1), ('篠', 1), ('蝇', 1), ('课', 1), ('奖', 1), ('掺', 1), ('谴', 1), ('晼', 1),
                ('萎', 1), ('璧', 1), ('熔', 1), ('庞', 1), ('僵', 1), ('粤', 1), ('阮', 1), ('渝', 1), ('鄜', 1), ('饿', 1),
                ('拙', 1), ('旬', 1), ('雳', 1), ('霹', 1), ('槽', 1), ('旄', 1), ('蘼', 1), ('巡', 1), ('氲', 1), ('氤', 1),
                ('譀', 1), ('岱', 1), ('睹', 1), ('嗤', 1), ('笄', 1), ('娩', 1), ('婉', 1), ('祓', 1), ('袷', 1), ('葛', 1),
                ('境', 1), ('摸', 1), ('俄', 1), ('狭', 1), ('朴', 1), ('雹', 1), ('幡', 1), ('闼', 1), ('柑', 1), ('弊', 1),
                ('疆', 1), ('谒', 1), ('评', 1), ('搁', 1), ('吼', 1), ('嘴', 1), ('律', 1), ('纬', 1), ('楝', 1), ('杆', 1),
                ('救', 1), ('揽', 1), ('嫂', 1), ('德', 1), ('罔', 1), ('绩', 1), ('耘', 1), ('析', 1), ('贰', 1), ('霆', 1),
                ('孰', 1), ('坑', 1), ('鲍', 1), ('媪', 1), ('湟', 1), ('甫', 1), ('齧', 1), ('镳', 1), ('愈', 1), ('饕', 1),
                ('虐', 1), ('忌', 1), ('例', 1), ('帅', 1), ('绊', 1), ('箬', 1), ('佯', 1), ('艋', 1), ('舴', 1), ('类', 1),
                ('墓', 1), ('刖', 1), ('蛟', 1), ('验', 1), ('舷', 1), ('扣', 1), ('挺', 1), ('孝', 1), ('脍', 1), ('伪', 1),
                ('腔', 1), ('熳', 1), ('砺', 1), ('瞬', 1), ('捐', 1), ('縠', 1), ('髡', 1), ('榕', 1), ('蹰', 1), ('鼐', 1),
                ('操', 1), ('脚', 1), ('究', 1), ('喑', 1), ('恃', 1), ('耽', 1), ('募', 1), ('芝', 1), ('雅', 1), ('宋', 1),
                ('择', 1), ('逃', 1), ('遁', 1), ('晞', 1), ('篁', 1), ('莓', 1), ('曛', 1), ('哪', 1), ('穹', 1), ('敕', 1),
                ('革', 1), ('剃', 1), ('钵', 1), ('努', 1), ('涴', 1), ('绦', 1), ('制', 1), ('瑾', 1), ('沸', 1), ('汤', 1),
                ('励', 1), ('勉', 1), ('范', 1), ('磁', 1), ('杰', 1), ('毋', 1), ('娶', 1), ('芍', 1), ('襦', 1), ('撷', 1),
                ('栅', 1), ('锤', 1), ('啖', 1), ('棺', 1), ('卑', 1), ('遒', 1), ('斥', 1), ('爆', 1), ('萄', 1), ('葡', 1),
                ('价', 1), ('鳜', 1), ('潋', 1), ('聒', 1), ('噎', 1), ('咬', 1), ('逑', 1), ('福', 1), ('祸', 1), ('苟', 1),
                ('逊', 1), ('厦', 1), ('刎', 1), ('縢', 1), ('惘', 1), ('骰', 1)]

# 声调
tone = [
    'a',"ā", "á", "ǎ", "à", 'o',"ō", "ó", "ǒ", "ò",'e', "ē", "é", "ě", "è",'i', "ī", "í", "ǐ", "ì",'u', "ū",
    "ú", "ǔ", "ù", 'v',"ǖ", "ǘ", "ǚ","ǜ",
]

vowel = [
    "a", "o", "e", "ai", "ei", "ao", "ou", "an", "en", "ang", "eng", "ong", "i", "ia", "ie", "iao", "iou", "ian", "in",
    "iang", "iong", "u", "ua", "uai", "uan", "uen", "uang", "ueng", "v", "ve", "van", "vn",
]

initials = [
    "b","p","d","t","g","k","z","c","zh","ch","j","q","f","h","s","sh","r","x","m","n","l","y"
]


