import os

def rename_txt_to_md(directory):
    # List all files in the directory
    files = os.listdir(directory)

    for filename in files:
        # Check if the file has a .txt extension
        if filename.endswith(".txt"):
            # Generate the new filename with .md extension
            new_filename = os.path.splitext(filename)[0] + ".md"

            # Construct the full paths for the old and new filenames
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_filepath, new_filepath)

            print(f"Renamed: {filename} -> {new_filename}")

# Replace the directory_path with the actual path to your directory
directory_path = r'C:\Users\manis\OneDrive\Desktop\Coding\DSA\Strivers-A2Z-DSA-Sheet\Binary Search [1D, 2D Arrays, Search Space]\BS on Answers'

# Call the function to rename .txt files to .md
rename_txt_to_md(directory_path)
