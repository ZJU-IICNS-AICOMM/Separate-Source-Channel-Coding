import cv2
import numpy as np
import os
def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2.0)
    if mse == 0:
        return 100.
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

# Replace 'input_image.png' and 'compressed_image.bpg' with your file paths
aver_len = 0
for i in range(100):
    index = np.random.randint(1, 5000)
    input_image_path = str(10000 + index) + '.png'
    compressed_bpg_path = str(10000 + index) + '_compressed' +'.png'

    # Encode the input image to BPG QP 0~50
    encode_command = f'E:/bpg_lib/bpgenc -e x265 -q 43 -f 444 -o encoded_bitstream.txt {input_image_path}'
    os.system(encode_command)

    # Decode the BPG image back to PNG
    decoded_image_path = compressed_bpg_path
    decode_command = f'E:/bpg_lib/bpgdec -o {decoded_image_path} encoded_bitstream.txt'
    os.system(decode_command)



    # 打开一个文件（如果文件不存在，将创建一个新文件）
    file_path = 'encoded_bitstream.txt'
    file = open(file_path, "rb")  # 使用 "r" 模式表示只读模式
    # # 读取文件的内容
    file_contents = file.read()
    print(len(file_contents))
    aver_len = aver_len + len(file_contents)

    # 关闭文件
    file.close()

print('Average length:{}'.format(aver_len/100))

aver_psnr = 0
for i in range(100):
    # Encode the input image to BPG
    index = np.random.randint(1, 5000)
    input_image_path = str(10000 + index) + '.png'
    compressed_bpg_path = str(10000 + index) + '_compressed' + '.png'

    # Encode the input image to BPG QP 0~50
    encode_command = f'E:/bpg_lib/bpgenc -e x265 -q 43 -f 444 -o encoded_bitstream.txt {input_image_path}'
    os.system(encode_command)

    # Decode the BPG image back to PNG
    decoded_image_path = compressed_bpg_path
    decode_command = f'E:/bpg_lib/bpgdec -o {decoded_image_path} encoded_bitstream.txt'
    os.system(decode_command)
    img1 = cv2.imread(input_image_path)
    img2 = cv2.imread(decoded_image_path)
    print(psnr(img1 + 0., img2 + 0.))
    aver_psnr = aver_psnr + psnr(img1 + 0., img2 + 0.)

print('Average PSNR:{}'.format(aver_psnr/100))