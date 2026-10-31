import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from pathlib import Path

# Get the project folder
BASE_DIR = Path(__file__).resolve().parent

# Load the input image
image_path = BASE_DIR / "input.jpg"

print("Loading image...")

# Open and preprocess the image
image = Image.open(image_path).convert("L")
image = image.resize((256, 256))

original = np.asarray(image, dtype=float) / 255.0

height, width = original.shape

print("Image dimensions:", original.shape)

# Select principal components
k = 50

# Apply PCA
pca = PCA(n_components=k)
compressed = pca.fit_transform(original)

# Reconstruct the image
reconstructed = pca.inverse_transform(compressed)
reconstructed = np.clip(reconstructed, 0, 1)

# Calculate MSE
mse = np.mean((original - reconstructed) ** 2)

# Calculate PSNR
if mse == 0:
    psnr = float("inf")
else:
    psnr = 10 * np.log10(1.0 / mse)

# Calculate estimated compression ratio
original_values = height * width
compressed_values = height * k + k * width + width

compression_ratio = original_values / compressed_values

# Calculate explained variance
explained_variance = np.sum(
    pca.explained_variance_ratio_
) * 100

# Display results
print("\n===== PCA IMAGE COMPRESSION RESULTS =====")
print("Image dimensions:", original.shape)
print("Components:", k)
print(f"MSE: {mse:.6f}")
print(f"PSNR: {psnr:.2f} dB")
print(f"Estimated compression ratio: {compression_ratio:.2f}:1")
print(f"Explained variance: {explained_variance:.2f}%")

# Save reconstructed image
output_path = BASE_DIR / "reconstructed.png"

output_image = Image.fromarray(
    (reconstructed * 255).round().astype(np.uint8)
)

output_image.save(output_path)

print("\nReconstructed image saved successfully!")
print("Output file:", output_path)

# Display original and reconstructed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original, cmap="gray", vmin=0, vmax=1)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(reconstructed, cmap="gray", vmin=0, vmax=1)
plt.title(f"Reconstructed Image (k={k})")
plt.axis("off")

plt.tight_layout()
plt.show()