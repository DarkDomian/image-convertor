from PIL import Image, ImageOps
import os
import shutil


def process_image(input_path, output_path, target_size=(800, 1200)):
    # Open an image
    img = Image.open(input_path)

    # change the levels
    img = ImageOps.autocontrast(img, cutoff=1)

    # Posterize it
    img = img.convert("RGB")
    img = ImageOps.posterize(img, bits=7)

    # Scale image
    img.thumbnail(target_size, Image.LANCZOS)

    # Indexed mode use with format `PNG`
    # img = img.convert("P", palette=Image.ADAPTIVE, colors=128)

    # Exporting
    img.save(
        output_path,
        format="JPEG",
        quality=80,
        optimize=True,
        progressive=True,
        # for easy use pass `web_low` / `web_medium` / `web_maximum`
        qtables="web_medium",
    )


def batch_process(input_folder, output_folder, target_size=(800, 1200)):
    # Create folder for saving data
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, f"processed_{file_name}")

            try:
                process_image(input_path, output_path, target_size)
                print(f"Finished: {file_name}")
            except Exception as e:
                print(f"Error in procces {file_name}: {e}")


# Declare the folders here
input_folder = "input_images"
output_folder = "output_images"

# Run
batch_process(input_folder, output_folder)
