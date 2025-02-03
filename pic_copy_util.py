import os
import shutil

substring_file = 'file_containing_substrings'
source_dir = 'copy_fron_dir'
dest_dir = 'copy_to_dir'


def read_substrings(substring_file):
    """Read file substrings from a file."""
    with open(substring_file, 'r') as file:
        substrings = [line.strip() for line in file if line.strip()]
    return substrings

def copy_files_by_substring(source_dir, dest_dir, substrings):
    """Copy files matching the substrings from source_dir to dest_dir."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copied_files_count = 0

    for root, _, files in os.walk(source_dir):
        for file in files:
            if any(substring in file for substring in substrings):
                source_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                shutil.copy2(source_file, dest_file)
                copied_files_count += 1
                print(f"Copied: {source_file} -> {dest_file}")

    return copied_files_count

def main():
    substrings = read_substrings(substring_file)
    print(f"Substrings to match ({len(substrings)}): {substrings}")

    copied_files_count = copy_files_by_substring(source_dir, dest_dir, substrings)
    print(f"Total files copied: {copied_files_count}")

if __name__ == "__main__":
    main()
