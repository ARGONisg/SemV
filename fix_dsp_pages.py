#!/usr/bin/env python3
import os
import glob
import sys

def fix_dsp_book_folder(target_dir):
    if not os.path.isdir(target_dir):
        print(f"Error: Directory not found: {target_dir}")
        sys.exit(1)

    files = sorted(glob.glob(os.path.join(target_dir, "*.jpg")))
    print(f"Found {len(files)} total files in '{target_dir}'.")

    # 1. Identify 0-byte corrupted files
    zero_bytes = [f for f in files if os.path.getsize(f) == 0]
    print(f"\n[1/4] Deleting {len(zero_bytes)} 0-byte corrupted files...")
    for f in zero_bytes:
        os.remove(f)
        print(f"  Deleted empty file: {os.path.basename(f)}")

    # Refresh file list
    files = sorted(glob.glob(os.path.join(target_dir, "*.jpg")))

    # 2. Identify and delete duplicate copies of pg 321 (files 0323 to 0372)
    duplicates = []
    valid_files = []
    for f in files:
        name = os.path.basename(f)
        # Extract file number
        num_part = "".join(filter(str.isdigit, name))
        if not num_part:
            continue
        num = int(num_part)
        if 323 <= num <= 372:
            duplicates.append(f)
        else:
            valid_files.append((f, num))

    print(f"\n[2/4] Deleting {len(duplicates)} duplicate copies of pg 321 (files 0323 to 0372)...")
    for f in duplicates:
        os.remove(f)
        print(f"  Deleted duplicate: {os.path.basename(f)}")

    # 3. Two-phase rename to prevent file collision
    print(f"\n[3/4] Renaming {len(valid_files)} files to match actual printed book page numbers...")
    # Map to actual book pages:
    # Files 0236..0322 -> actual page = file_number - 1
    # Files 0373..0523 -> actual page = file_number - 51
    temp_rename_list = []
    final_rename_list = []

    for fpath, num in valid_files:
        if num <= 322:
            actual_page = num - 1
        else:
            actual_page = num - 51
        
        dir_name = os.path.dirname(fpath)
        temp_name = os.path.join(dir_name, f"__temp_page_{actual_page:04d}.jpg")
        final_name = os.path.join(dir_name, f"DSP_Salivahanan_page_{actual_page:04d}.jpg")
        
        temp_rename_list.append((fpath, temp_name))
        final_rename_list.append((temp_name, final_name))

    # Phase A: rename to temp names
    for src, dst in temp_rename_list:
        os.rename(src, dst)

    # Phase B: rename temp names to final names
    for src, dst in final_rename_list:
        os.rename(src, dst)

    # 4. Summary & Verification
    final_files = sorted(glob.glob(os.path.join(target_dir, "*.jpg")))
    actual_pages = [int("".join(filter(str.isdigit, os.path.basename(f)))) for f in final_files]
    
    print("\n[4/4] Verification Summary:")
    print(f"  Total valid files remaining: {len(final_files)}")
    print(f"  Actual book page range: {min(actual_pages)} to {max(actual_pages)}")
    
    full_range = set(range(min(actual_pages), max(actual_pages) + 1))
    missing = sorted(list(full_range - set(actual_pages)))
    print(f"  Missing actual pages in this range ({len(missing)}): {missing}")
    print("\nDone! Files have been cleanly renamed to their actual book page numbers.")

if __name__ == "__main__":
    target = "/Users/parth/Downloads/DSP book/Attemp 2"
    if len(sys.argv) > 1:
        target = sys.argv[1]
    fix_dsp_book_folder(target)
