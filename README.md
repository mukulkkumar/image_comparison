# Image Comparison

A small Python command-line tool that checks whether two images have identical
decoded pixel values. By default, it compares `images/image-1.jpg` with
`images/image-3.jpg`.

## Setup

Install the dependencies into your Python environment:

```powershell
python -m pip install -r requirements.txt
```

If you are using the included virtual environment on Windows:

```powershell
.\img_env\Scripts\python.exe -m pip install -r requirements.txt
```

## Usage

Compare the default images:

```powershell
.\img_env\Scripts\python.exe .\compare_images.py
```

Compare any two image files by passing their paths:

```powershell
.\img_env\Scripts\python.exe .\compare_images.py .\images\image-1.jpg .\images\image-10.jpg
```

The script prints `SAME` when the decoded image dimensions and pixel values
match, or `DIFFERENT` otherwise. It returns exit code `0` for a match, `1` for
different images, and `2` if an image cannot be read. Since this is an exact
pixel comparison, visually similar images with even small pixel differences
are reported as different.
