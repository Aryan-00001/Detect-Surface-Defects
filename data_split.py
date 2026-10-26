import os
import shutil

# 1. The folder where all 1800 files currently reside.
SOURCE_DIR = "Z:\\New folder\\OTML\\NEU-DET\\train\\IMAGES"

# 2. The folder where the selected files (271 to 300) will be moved.
DESTINATION_DIR = "Z:\\New folder\\OTML\\NEU-DET\\test\\IMAGES"

# 3. Start index (inclusive)
START_INDEX = 271

# 4. End index (inclusive)
END_INDEX = 300
def move_files_by_range(source_dir, destination_dir, start_index, end_index):
    """
    Moves files in the format 'class_N.ext' where N is in the specified range,
    for all 6 defect classes, along with their corresponding .xml/.jpg pair.
    """
    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # The 6 defect classes (prefix in the filename)
    classes = ["crazing", "inclusion", "patches", "pitted_surface", "rolled-in_scale", "scratches"]
    # NOTE: NEU-DET filenames use 'Cr', 'In', etc., not 'crazing', 'inclusion'.

    moved_count = 0

    print(f"Starting to move files from index {start_index} to {end_index}...")

    for defect_prefix in classes:
        print(f"\nProcessing defect type: {defect_prefix}...")

        for i in range(start_index, end_index + 1):
            # Construct the base filename (e.g., 'Cr_271')
            base_filename = f"{defect_prefix}_{i}"
            # Full file paths in the source directory
            # xml_src = os.path.join(source_dir, base_filename + ".xml")
            jpg_src = os.path.join(source_dir, base_filename + ".jpg")
            # Full file paths in the destination directory
            # xml_dst = os.path.join(destination_dir, base_filename + ".xml")
            jpg_dst = os.path.join(destination_dir, base_filename + ".jpg")
            # Check if the files exist before attempting to move
            if os.path.exists(jpg_src) :
                # os.path.exists(xml_src)
                # and os.path.exists(jpg_src)
                try:
                    # Move the XML annotation file
                    # shutil.move(xml_src, xml_dst)
                    # Move the corresponding image file
                    shutil.move(jpg_src, jpg_dst)
                    moved_count += 1
                    # print(f"  Moved: {base_filename}.*") # Uncomment for detailed output
                except Exception as e:
                    print(f"ERROR moving {base_filename}: {e}")
            else:
                # This handles cases where a file in the range might be missing (optional print)
                pass
                # print(f"  Skipped: {base_filename}.* (Not found in source)")

    print("\n========================================")
    print(f" File movement complete!")
    print(f"Total files moved (XML + JPG): {moved_count}")
    print(f"Moved files now reside in: {DESTINATION_DIR}")
    print("========================================")


if __name__ == "__main__":
    move_files_by_range(SOURCE_DIR, DESTINATION_DIR, START_INDEX, END_INDEX)
