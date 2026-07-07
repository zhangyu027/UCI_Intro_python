# Google Colab / Google Drive Path Note

This course package supports two ways to run notebooks.

## Option A: Google Colab
Run this first in Colab:

```python
from google.colab import drive
drive.mount('/content/drive')

BASE_DIR = '/content/drive/MyDrive/Colab Notebooks/UCI/UCI_427.62_Python_for_Data_Analysis'
DATA_DIR = f'{BASE_DIR}/05_Datasets'
ASSIGNMENTS_DIR = f'{BASE_DIR}/04_Assignments'
OUTPUTS_DIR = f'{BASE_DIR}/04_Assignments/Outputs'
```

Use Colab paths such as:

```python
filepath = f'{DATA_DIR}/Most_Popular_Baby_Boy_Names__Illinois_1980-2013.csv'
```

## Option B: Local Jupyter / Anaconda
Do not use `/content/drive` on your computer. Use relative paths such as:

```python
filepath = '../05_Datasets/Most_Popular_Baby_Boy_Names__Illinois_1980-2013.csv'
```

## Important
The Mac path below is only your local Google Drive sync path and should not be used inside Colab:

`/Users/yuzhang/Library/CloudStorage/GoogleDrive-zhangyu027@gmail.com/My Drive/...`
