from gimpfu import *

def process_image_gimp(img, drawable):
    # Levels
    pdb.gimp_levels(drawable, HISTOGRAM_VALUE, 0, 255, 1.2, 0, 255)

    # Posterize
    pdb.gimp_posterize(drawable, 128)

    # Scale image
    width, height = img.width, img.height
    if width > height:
        pdb.gimp_image_scale(img, 1200, 800)
    else:
        pdb.gimp_image_scale(img, 800, 1200)

    # Indexed mode
    pdb.gimp_image_convert_indexed(img, NO_DITHER, MAKE_PALETTE, 128, False, False, "")

    # Export
    output_path = "/path/to/output_folder/processed_image.jpg"
    pdb.file_jpeg_save(
        img, drawable, output_path, output_path,
        0.8, 0, 0, 0, "", 0, 1, 0, 0
    )

register(
    "python_fu_process_image_gimp",
    "Batch process image with specific settings",
    "Applies levels, posterization, scaling, and indexing",
    "Ваше Имя",
    "Ваше Имя",
    "2024",
    "<Image>/Filters/Custom/Process Image GIMP",
    "*",  # Input types
    [],
    [],
    process_image_gimp,
)

main()
