# 🖼️ PCA-Based Image Compression Using Python

## 📌 Project Overview

This project demonstrates image compression and reconstruction using Principal Component Analysis (PCA) in Python. It reduces image dimensionality while attempting to preserve important visual information.

The project reconstructs the image using 50 principal components and evaluates the reconstruction quality using MSE, PSNR, explained variance, and an estimated compression ratio.

## ✨ Features

* Image preprocessing and grayscale conversion
* Image resizing to 256 × 256 pixels
* PCA-based dimensionality reduction
* Image reconstruction using 50 principal components
* Mean Squared Error (MSE) calculation
* Peak Signal-to-Noise Ratio (PSNR) calculation
* Explained variance calculation
* Estimated compression ratio
* Visualization of original and reconstructed images
* Saving the reconstructed image as a PNG file

## 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib
* Pillow
* Scikit-learn

## 📂 Project Structure

```text
PCA-Image-Compression/
├── main.py
├── input.jpg
├── requirements.txt
├── README.md
└── reconstructed.png
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd PCA-Image-Compression
```

### 3. Install the required libraries

```bash
python -m pip install -r requirements.txt
```

### 4. Run the project

Place an image named `input.jpg` in the project folder, then execute:

```bash
python main.py
```

## 📊 Evaluation Metrics

**MSE (Mean Squared Error):** Measures the average squared difference between the original and reconstructed images. Lower values generally indicate less reconstruction error.

**PSNR (Peak Signal-to-Noise Ratio):** Measures reconstruction quality in decibels. Higher values generally indicate better image quality.

**Explained Variance:** Indicates how much of the image data's variance is represented by the selected principal components.

**Estimated Compression Ratio:** Estimates the reduction in the number of numerical values required by the PCA representation. It is not a measurement of actual image-file size reduction.

## 🚀 Future Enhancements

* Compare different numbers of principal components.
* Generate graphs of reconstruction quality.
* Compare actual storage requirements.
* Extend the method to color images.
* Develop a graphical user interface.

## 👨‍💻 Author

**Vishnu Vardhan Maddipati**

B.Tech Student
