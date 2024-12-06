# NodeMonkes Utils

这是一个非官方的 NodeMonkes 资源和工具库，包括原始 10000 个 NodeMonkes 的 PNG 图片，每个图片的像素数据，ExcelNodeMonkes等

## NodeMonkes资源

### 1. 原始图像 (10k PNG)
- 资源位于data/images/NodeMonkes_images.zip
- 图片名称 1.png, 2.png, 3.png, ...10000.png
- 每个图片28*28像素
- 是用fetch_nodemonkes.py从官网下载后打包的

### 2. 像素数据
- 资源位于data/pixels_data/NodeMonkes_pixels_data.zip
- 下载并解压缩后，有csv和txt两种格式
- 共10000行，每行是一张图片的像素值，28*28=784个像素
- 每个像素值是16进制表示的RGBA颜色值，RRGGBBAA
- 该像素数据是用extract_pixels.py从10k png图片中提取的

### 3. 属性图片
- 建设中

### 4. 属性表
- 建设中


## 使用方法

### 1. ExcelNodeMonkes：
- 打开 ExcelNodeMonkes.xlsm
- 确保启用宏功能
- 使用内置工具查看和切换显示不同的 NodeMonkes

### 2. 从官网下载图片（已下载并打包）：

```bash
python src/fetch_nodemonkes.py
```
- 将在 images 目录下下载所有 NodeMonkes 图片
- 下载过程中显示进度条
- 失败的下载会自动重试一次

### 3. 提取像素数据（已提取并打包）：

```bash
python src/extract_pixels.py
```
- 处理 images 目录下的所有图片
- 生成 image_data.csv 文件
- 显示处理进度和统计信息

### 4. 格式化数据（已格式化并打包）：

```bash
python src/format_pixels.py
```
- 读取 image_data.csv
- 生成 image_data.txt
- 显示处理结果统计



## 环境要求

### Python 依赖
- Python 3.6+
- requests
- numpy
- pandas
- Pillow
- tqdm

### 其他要求
- Microsoft Excel（需要支持 VBA）
- 足够的磁盘空间（约需要 2GB 用于存储图片）
- 稳定的网络连接

## 安装

1. 克隆仓库：

```bash
git clone https://github.com/yourusername/nodemonkes-utils.git
cd nodemonkes-utils
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

## 注意事项

- 请确保 Excel 启用了宏功能
- 打开NodeMonkes_pixels_data.csv时需要较大内存

## License

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

