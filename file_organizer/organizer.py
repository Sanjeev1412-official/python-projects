import os
import shutil
import argparse
from datetime import datetime


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".js", ".java", ".cpp", ".html", ".css"]
}

def get_category(directory):
    
    ext = os.path.splitext(directory)[1].lower()
    
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def get_month(directory):
    mod_time = os.path.getmtime(directory)
    return datetime.fromtimestamp(mod_time).strftime("%Y-%m")

def organize(folder_path, sort_by_date=False, dry_run=False):
    for filename in os.listdir(folder_path):
        
        filepath = os.path.join(folder_path, filename)
        
        if os.path.isdir(filepath):
            continue
        
        category = get_category(filename)
        
        dest_folder = os.path.join(folder_path, category)
        
        if sort_by_date:
            month_folder = get_month(filepath)
            dest_folder = os.path.join(dest_folder, month_folder)
        
        os.makedirs(dest_folder, exist_ok=True)
        
        dest_path = os.path.join(dest_folder, filename)
        
        if os.path.exists(dest_path):
            print(f"Skipping (already exists): {dest_path}")
            continue
        
        if dry_run:
            print(f"[DRY RUN] Would move: {filepath} -> {dest_path}")
        else:
            shutil.move(filepath, dest_path)
            print(f"Moved: {filepath} -> {dest_path}")
            
        
def main():
    parser = argparse.ArgumentParser(description="File Organizer Tool")

    parser.add_argument("folder", help="Folder to organize")
    parser.add_argument("--date", action="store_true",
                        help="Sort into subfolders by modified month")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without moving files")

    args = parser.parse_args()

    organize(
        folder_path=args.folder,
        sort_by_date=args.date,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()