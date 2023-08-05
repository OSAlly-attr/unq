from PIL import Image
from io import BytesIO 
import numpy as np
import csv

list1 = []

with open('list1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        list1.append(row)

sz = len(list1)

for i in range(sz):
    filename = './pkimag/'+ list1[i][0] +'.png'
    # 画像ファイルパスから読み込み
    img = Image.open(filename)
    # numpy配列の取得
    img_array = np.asarray(img)
    height = len(img_array)
    width = len(img_array[0])
    arr = np.broadcast_to(img_array, (height, width, 4)).copy()
    for k in range(height):
        for j in range(width):
            if arr[k][j][3] != 0:
                arr[k][j][0] = 0
                arr[k][j][1] = 0
                arr[k][j][2] = 0
                arr[k][j][3] = 255
    pil_img = Image.fromarray(arr)
    filename = './pkimag_b/'+ list1[i][0] +'b.png'
    print(filename)
    pil_img.save(filename)
