# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

# 要转换为图片的文字
text = "你好，世界"
# 创建一个新的图像，设置宽度和高度
width, height = 800, 600
image = Image.new('RGB', (width, height), color=(255, 255, 255))  # 白色背景
# 创建一个可以在图像上绘图的Draw对象
draw = ImageDraw.Draw(image)
# 选择一个支持中文的字体文件(.ttf格式)，并设置字体大小
# 请确保你有这个字体文件，并且它支持中文
font_path = 'D:\字体\WenQuanZhengHei\WenQuanZhengHei-1.ttf'  # 替换为你的字体文件路径
font_size = 20  # 字体大小
font = ImageFont.truetype(font_path, font_size)
# 计算文本的位置以使其居中
text_width, text_height = draw.textsize(text, font=font)
margin = 10  # 文本边缘的间距
x = (width - text_width) / 2
y = (height - text_height) / 2
# 将文字绘制到图像上，设置文本颜色为黑色
draw.text((x, y), text, font=font, fill=(0, 0, 0))
# 保存图像到文件
image.save('text_image.png')
# 显示图像（如果需要）
image.show()
