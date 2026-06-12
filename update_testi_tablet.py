import os
import re

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the 50% width in the 992px media query
content = re.sub(
    r'(\.testi-card\s*\{\s*min-width:\s*)calc\(50%\s*-\s*12px\);',
    r'\1 100%;',
    content
)

content = re.sub(
    r'(flex:\s*0\s*0\s*)calc\(50%\s*-\s*12px\);',
    r'\1 100%;',
    content
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated style.css for max-width: 992px testi-card.")
