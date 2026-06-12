import os
import re

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove border-right from .footer-brand
content = re.sub(
    r'(\.footer-brand\s*\{[^}]*)border-right:\s*1px\s*solid\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.2\s*\);',
    r'\1',
    content
)

# 2. Update .testi-card width to 100%
content = re.sub(
    r'(\.testi-card\s*\{[^}]*)min-width:\s*calc\(33\.333%\s*-\s*16px\);',
    r'\1min-width: 100%;',
    content
)

content = re.sub(
    r'(\.testi-card\s*\{[^}]*)flex:\s*0\s*0\s*calc\(33\.333%\s*-\s*16px\);',
    r'\1flex: 0 0 100%;',
    content
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated style.css for footer border and single card testimonial display.")
