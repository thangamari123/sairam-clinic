import os
import glob

directory = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Change stroke-width="2" to stroke-width="1.8" for a sleeker look
    if "mobile-bottom-nav" in content:
        # Just replace all stroke-width="2" with stroke-width="1.5" inside the mobile nav
        # We'll isolate the mobile bottom nav
        parts = content.split('<!-- ═══════════════ MOBILE BOTTOM NAV ═══════════════ -->')
        if len(parts) == 2:
            nav_part = parts[1].replace('stroke-width="2"', 'stroke-width="1.8"')
            new_content = parts[0] + '<!-- ═══════════════ MOBILE BOTTOM NAV ═══════════════ -->' + nav_part
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated stroke width in {file_path}")
