import qrcode

data = 'https://www.baidu.com/'
img_file = r'code.png'
# 实例化QRCode生成qr对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
# 传入数据
qr.add_data(data)
qr.make(fit=True)
# 生成二维码
img = qr.make_image()
# 保存二维码
img.save(img_file)
# 展示二维码
img.show()
