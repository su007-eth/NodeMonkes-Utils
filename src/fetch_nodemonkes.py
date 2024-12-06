import requests
import os
from tqdm import tqdm
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_image(number):
    url = f"https://nodemonkes.com/tokens/{number}.png"
    filename = f"{number}.png"
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"下载 {number}.png 时出错: {str(e)}")
        return False

def main():
    if not os.path.exists("images"):
        os.makedirs("images")
    
    os.chdir("images")
    
    # 创建一个进度条
    pbar = tqdm(total=10000, desc="下载进度")
    
    # 使用线程池进行并发下载，max_workers 可以根据你的网络情况调整
    with ThreadPoolExecutor(max_workers=20) as executor:
        # 创建所有下载任务
        future_to_number = {executor.submit(download_image, number): number 
                          for number in range(1, 10001)}
        
        # 处理完成的任务
        for future in as_completed(future_to_number):
            number = future_to_number[future]
            try:
                success = future.result()
                if not success:
                    # 如果下载失败，重试一次
                    time.sleep(1)
                    download_image(number)
            except Exception as e:
                print(f"处理 {number}.png 时出错: {str(e)}")
            finally:
                pbar.update(1)
    
    pbar.close()

if __name__ == "__main__":
    main()
