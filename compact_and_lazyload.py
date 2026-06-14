import os
import re

# 1. Update style.css for compactness
css_file = "style.css"
with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

# Make padding smaller
css_content = re.sub(r'padding:\s*60px\s+0;', 'padding: 40px 0;', css_content)
css_content = re.sub(r'padding:\s*80px\s+0;', 'padding: 50px 0;', css_content)
css_content = re.sub(r'padding:\s*72px\s+0\s+80px;', 'padding: 48px 0 50px;', css_content)

# Reduce padding globally
css_content = re.sub(r'padding:\s*48px\s+32px;', 'padding: 32px 24px;', css_content)
css_content = re.sub(r'padding:\s*32px;', 'padding: 24px;', css_content)

# Reduce root vars for navbar height
css_content = re.sub(r'--nav-h:\s*76px;', '--nav-h: 60px;', css_content)

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css_content)
print("Updated style.css for compactness.")

# 2. Add loading="lazy" to all img tags in HTML files
html_files = [f for f in os.listdir(".") if f.endswith(".html")]
for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Find all <img> tags
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading=' in img_tag:
            return img_tag
        if 'logo-image' in img_tag or 'logo.png' in img_tag.lower():
            return img_tag
        return img_tag.replace('<img ', '<img loading="lazy" ')

    new_html = re.sub(r'<img[^>]+>', add_lazy, html_content)
    
    if new_html != html_content:
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Added lazy loading to {html_file}")

print("Done.")
