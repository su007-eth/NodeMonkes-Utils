import numpy as np
from PIL import Image
import pandas as pd
import os

def process_image(image_path):
    img = Image.open(image_path)
    img = img.convert('RGBA')
    img_array = np.array(img)
    
    # 将RGBA值转换为单个16进制数字
    hex_values = (img_array[:, :, 0].astype(np.uint32) << 24 | 
                 img_array[:, :, 1].astype(np.uint32) << 16 | 
                 img_array[:, :, 2].astype(np.uint32) << 8  | 
                 img_array[:, :, 3].astype(np.uint32))
    
    return hex_values.flatten()

def main():
    # 设置图片目录
    image_dir = 'images'
    if not os.path.exists(image_dir):
        print(f"错误：找不到 {image_dir} 目录！")
        return
        
    # 处理10000张图片
    all_data = []
    file_ids = []  # 存储文件编号
    found_files = 0
    
    print("开始处理图片...")
    
    # 假设图片命名为1.png, 2.png, ..., 10000.png
    for i in range(1, 10001):
        image_path = os.path.join(image_dir, f'{i}.png')
        if os.path.exists(image_path):
            found_files += 1
            try:
                hex_values = process_image(image_path)
                all_data.append(hex_values)
                file_ids.append(i)
                if found_files % 100 == 0:
                    print(f"已处理 {found_files} 个文件...")
            except Exception as e:
                print(f"处理图片 {image_path} 时出错: {e}")
    
    if found_files == 0:
        print("错误：在 images 目录下没有找到任何PNG文件！")
        print("请确保文件名格式为：1.png, 2.png, 3.png 等")
        return
    
    print(f"找到并处理了 {found_files} 个文件")
    
    # 创建DataFrame，包含文件编号
    df = pd.DataFrame(all_data)
    
    # 将数值转换为16进制字符串
    df = df.applymap(lambda x: f'{x:08X}')
    
    # 在最前面插入文件编号列
    df.insert(0, 'file_id', file_ids)
    
    # 保存为CSV文件
    df.to_csv('image_data.csv', index=False)
    print(f"处理完成！数据形状: {df.shape}")
    print(f"数据已保存到 image_data.csv")

if __name__ == "__main__":
    main()
