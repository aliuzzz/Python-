import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread

#1、读取txt文本数据
text = open(r"学习群.txt", 'r', encoding='utf-8').read()

#2、分开词条
cut_text = jieba.cut(text)
result = ' '.join(cut_text)

#3、初始化自定义背景
image = imread('.\heart.jpg')

#4、生成词云图(mask 为一个遮罩，即词云形状)
wc = WordCloud(font_path=r'.\STXINWEI.TTF', background_color='white', max_font_size=200, mask = image)

wc.generate(result)
#从背景里面提取背景颜色
image_color = ImageColorGenerator(image)
#颜色放进去
wc.recolor(color_func=image_color)
wc.to_file(r'.\result.jpg')

#5、显示在项目中
plt.figure('study')
plt.imshow(wc)
plt.axis('off')
plt.show()



