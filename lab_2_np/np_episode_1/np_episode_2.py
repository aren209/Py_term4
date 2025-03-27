import numpy as np
from PIL import Image

for j in range(3):
    img = Image.open(f'lunar_images/lunar0{j+1}_raw.jpg')
    data = np.array(img)

    a = float(data.min())
    b = float(data.max())
    
    k = 255 / (b - a)
    p = (255 - k * (a + b)) / 2
    
    rows = data.shape[0]
    columns = data.shape[1]
    
    updated_data = np.empty_like(data, dtype = np.uint8)
    
    # print(rows)
    # print(columns)
    for u in range(rows):
        for i in range(columns):
            x = data[u][i]
            updated_data[u][i] = k * x + p    

    res_img = Image.fromarray(updated_data)
    res_img.save(f'result_images/updated_lunar{j+1}.jpg')