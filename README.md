# NodeMonkes Utils

This is an unofficial NodeMonkes resource and tool library. It includes the original 10,000 NodeMonkes PNG images, pixel data for each image, ExcelNodeMonkes, and more.

## NodeMonkes Resources

### 1. Original Images (10k PNG)
- Resources located at: `data/images/NodeMonkes_images.zip`
- Image names: `1.png, 2.png, 3.png, ... 10000.png`
- Each image is 28×28 pixels
- Obtained using `fetch_nodemonkes.py` from the official website and then packaged

### 2. Pixel Data
- Resources located at: `data/pixels_data/NodeMonkes_pixels_data.zip`
- After downloading and extracting, you’ll have both CSV and TXT formats
- There are 10,000 rows total, each row corresponding to one image’s pixel values (28×28 = 784 pixels)
- Each pixel value is a hexadecimal RGBA color code in the format `RRGGBBAA`
- Pixel data extracted using `extract_pixels.py` from the 10k PNG images

### 3. Attribute Images
- Building...

### 4. Attribute Table
- Building...


## Usage

### 1. ExcelNodeMonkes:
- Open `ExcelNodeMonkes.xlsm`
- Ensure macros are enabled
- Use the built-in tools to view and switch between different NodeMonkes

### 2. Downloading Images from the Official Site (Already Downloaded and Packaged):

```bash
python src/fetch_nodemonkes.py
```

- Downloads all NodeMonkes images into the `images` directory
- Displays a progress bar during download
- Any failed downloads will automatically retry once

### 3. Extracting Pixel Data (Already Extracted and Packaged):

```bash
python src/extract_pixels.py
```

- Processes all images in the `images` directory
- Generates `image_data.csv`
- Displays progress and statistics

### 4. Formatting Data (Already Formatted and Packaged):

```bash
python src/format_pixels.py
```

- Reads `image_data.csv`
- Generates `image_data.txt`
- Shows processing results and statistics

## Requirements

### Python Dependencies
- Python 3.6+
- requests
- numpy
- pandas
- Pillow
- tqdm

### Other Requirements
- Microsoft Excel (with VBA support)
- Sufficient disk space (approximately 2GB needed for image storage)
- Stable internet connection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/nodemonkes-utils.git
cd nodemonkes-utils
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Notes

- Ensure macros are enabled in Excel
- Opening `NodeMonkes_pixels_data.csv` may require substantial memory

## License

MIT License

## Contributions

Issues and Pull Requests are welcome!