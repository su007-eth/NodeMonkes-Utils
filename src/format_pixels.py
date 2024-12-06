import pandas as pd

def main():
    # 读取CSV文件
    print("正在读取CSV文件...")
    df = pd.read_csv('image_data.csv')
    
    # 删除file_id列
    df = df.drop('file_id', axis=1)
    
    # 将每一行合并成一个字符串（无空格）
    print("正在处理数据...")
    text_lines = df.apply(lambda row: ''.join(row.values.astype(str)), axis=1)
    
    # 保存到文本文件
    print("正在保存文件...")
    with open('image_data.txt', 'w') as f:
        f.write('\n'.join(text_lines))
    
    print(f"处理完成！共生成 {len(text_lines)} 行数据")
    print("数据已保存到 image_data.txt")

if __name__ == "__main__":
    main()
