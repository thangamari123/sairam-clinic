import os
import glob
import re

directory = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the mobile bottom nav
    if "mobile-bottom-nav" in content:
        # Re-inject the correct SVG for Treatments with xmlns
        old_svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c-3 0-5-3-5-6v-2a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v2c0 3-2 6-5 6z"></path><path d="M9 10V8a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v2"></path><path d="M12 21v-4"></path></svg>'
        new_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c-3 0-5-3-5-6v-2a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v2c0 3-2 6-5 6z"></path><path d="M9 10V8a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v2"></path><path d="M12 21v-4"></path></svg>'
        
        # Also just in case, replace any <svg viewBox="0 0 24 24" that lacks xmlns inside mobile-bottom-nav
        # Actually a simple string replace of the exact SVG is safest.
        
        updated_content = content.replace(old_svg, new_svg)
        
        # Also let's update the Call icon to exactly match the white outline in the screenshot
        # The screenshot phone is a rounded phone with no filled parts.
        
        if updated_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated {file_path}")
        else:
            print(f"No changes for {file_path}")
