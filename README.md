# 🎨 Image Processor Toolkit

A small but powerful set of tools for batch processing images, tailored for personal needs. This project provides **two options** for automating image manipulation tasks:

1. **GIMP Plugin**: A script for advanced editing directly in [GIMP](https://www.gimp.org/).  
2. **Standalone System Tool**: A Python script utilizing the lightweight and efficient [Pillow](https://pillow.readthedocs.io/) library.

Both tools can batch process images, applying adjustments such as **levels, posterization, scaling**, and **format conversion**, making your workflow faster and more efficient! 🚀

## ✨ Features

- **Adjust Levels**: Fine-tune brightness and contrast.
- **Posterization**: Limit the number of colors to create artistic effects.
- **Smart Scaling**: Automatically adjust image dimensions while preserving aspect ratio.
- **Indexed Color Mode**: Optimize images with a color palette for lightweight storage.
- **Metadata Cleanup**: Strip unnecessary EXIF/XMP data to reduce file size.
- **Custom Export Options**: Save images in high-quality, compressed formats.

## 🛠️ Requirements

### For the GIMP Plugin:
- GIMP (2.x or newer)
- Python (pre-installed with GIMP in most setups)

### For the System Tool:
- Python 3.6 or newer
- Pillow library:
  ```bash
  pip install pillow
  ```


## 📋 How to Use

### 1. **GIMP Plugin**

1. Copy the plugin script to GIMP's plugin directory:
   - **Linux**: `~/.gimp-2.x/plug-ins/`
   - **Windows**: `C:\Users\<your_username>\AppData\Roaming\GIMP\2.x\plug-ins\`
   - **macOS**: `~/Library/Application Support/GIMP/2.x/plug-ins/`
2. Make the script executable:
   ```bash
   chmod +x process_image.py
   ```
3. Restart GIMP.
4. Open an image and navigate to **Filters → Custom → Process Image GIMP**.
5. Enjoy automated adjustments! ✨

### 2. **System Tool (Pillow)**

1. Place all images to be processed in a folder (e.g., `input_images`).
2. Run the script:
   ```bash
   python process_images.py
   ```
3. Processed images will be saved in an `output_images` folder with new settings applied.

## ⚡ Example Command Line Workflow (System Tool)

```bash
# Step 1: Install dependencies
pip install pillow

# Step 2: Run the script
python system-convertor.py
```

Expected output:
- Input: `input_images/example.jpg`
- Output: `output_images/processed_example.jpg` with:
  - Adjusted levels
  - Posterization to 128 colors
  - Resized to 800x1200 or 1200x800
  - Indexed color palette
  - Metadata stripped


## 🤔 Why Use This?

This project combines **powerful image editing options** with **convenient automation** for batch processing, whether you're a designer, artist, or just need a quick optimization tool. Use the GIMP plugin for precise control or the standalone Python script for fast, headless workflows.


## 📝 Contribution

This is a small project built for personal needs, but if you'd like to contribute or improve it, feel free to fork the repo and submit a PR. Contributions aren't necessary, but if you're inspired — why not? 😊


## 📜 License

This project is released under the MIT License.


## 🚀 Get Started Now!

Clone the repository, set up your environment, and start processing images in no time!

**Happy Editing!** 🎉
