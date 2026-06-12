import os
import glob

directory = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic"
html_files = glob.glob(os.path.join(directory, "*.html"))

old_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c-3 0-5-3-5-6v-2a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v2c0 3-2 6-5 6z"></path><path d="M9 10V8a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v2"></path><path d="M12 21v-4"></path></svg>'

# A beautiful simple tooth outline SVG matching the image
new_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3c-1.2 0-2.4.6-3 1.5-.6-.9-1.8-1.5-3-1.5-2.5 0-4 1.5-4 4 0 4.5 1.5 6.5 1.5 8s-.5 4-.5 4.5c0 1 .5 1.5 1.5 1.5 1.2 0 2.2-.8 3.5-2.5 1.3 1.7 2.3 2.5 3.5 2.5 1 0 1.5-.5 1.5-1.5 0-.5-.5-3-.5-4.5 0-1.5 1.5-3.5 1.5-8 0-2.5-1.5-4-4-4z" /></svg>'


for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if old_svg in content:
        content = content.replace(old_svg, new_svg)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
