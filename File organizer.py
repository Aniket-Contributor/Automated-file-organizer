import os
from pathlib import Path

DIRECTORIES = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".csv", ".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", 
                  ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                  ".pptx", ".pptm", ".xml"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", 
              ".wma"],
    "Text Files": [".txt"],
    "PDF Files": [".pdf"],
    "Source Codes": [".py", ".c", ".cpp", ".java", ".css", ".js", ".jsx", ".html5", ".html", ".htm", ".xhtml", 
                    ".go", ".o", ".php", ".ejs", ".coffee", ".cmd", ".asp", ".aspx", ".atom", ".vscode"],
    "Font Files": [".abf", ".otf", ".ttf", ".woff"],
    "Programs": [".exe", ".msi"],
    "Command Shell": [".sh"],
    "MATLAB Source Files": [".m"],
    "PSpice Source Files": [".sch", ".dat", ".csd", ".out", ".cir", ".sim", ".slb"],
    "Temporary Files": [".tmp", ".temp"],
}

FILE_FORMATS = {ext: folder for folder, exts in DIRECTORIES.items() for ext in exts}

def organize_junk():
    print("Deleted Directories: ")
   
    for dir in os.scandir():
        if dir.is_dir():
            try:
                os.rmdir(dir)
                print(f"Deleted: {dir.name}")
            except OSError:
                pass  

    for entry in os.scandir():
        if entry.is_dir():
            continue

        file_name = Path(entry)
        file_extension = file_name.suffix.lower()

        if file_extension in FILE_FORMATS:
            folder_name = Path(FILE_FORMATS[file_extension])
            if not folder_name.exists():
                folder_name.mkdir()
            new_location = folder_name.joinpath(file_name.name)
            file_name.rename(new_location)
            print(f"Moved: {file_name} -> {new_location}")


organize_junk()

input("Press Enter to exit...")
