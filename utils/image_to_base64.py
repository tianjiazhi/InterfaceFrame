import base64

def images_to_base64(file_full_path):
    '''将一张图片转换成为base64'''
    with open(file_full_path,'rb') as f:
        base64_data = base64.b64encode(f.read())
        return base64_data.decode()


if __name__ == '__main__':
    images = "D:\\test.png"
    base_code = images_to_base64(images)
    print(base_code)
