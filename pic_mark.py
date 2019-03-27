#RGB 红蓝绿组成的各种颜色
#灰度 不同饱和度表示图像
#把不同像素点对应不同灰度，对应不同字符


from PIL import Image

chars = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~!lI`'

#chars = '@8#*/\|()1?-_+~<>i!lI,^`'
img = Image.open('aaa.jpg')
#print(img.format) #图像格式或来源
#print(img.mode) #色彩模式
#print(img.size) #图片尺寸
width, height = img.size #取得图片尺寸
#处理大小
if width > 100:
    n = width//100
else:
    n = 1
width = width//(n)
height = height//(n) #对图像进行缩减
img = img.resize((width, height))
txt = ''
#遍历每一个像素
for i in range(height):  #y轴
    for j in range(width):  #x轴
        r, g, b = img.getpixel((j, i))  #获取每一个像素
#变成灰度,利用公式
        gray = int(0.2126*r+0.7152*g+0.0722*b)
        unit = 256/len(chars) #灰度值除以不同等级，得到字符对应的位置
        char = chars[int(gray/unit)] #获取相应字符
#用字符组成画
        txt += char
    txt += '\n' #换行
#将字符写到文件中
with open('aaa.txt', 'w') as f:
    f.write(txt)
