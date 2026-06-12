import os
import re

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Make the wrapper max-width small to constrain the cards to a compact size
# This ensures it's "one by one" but "small and compact"
content = re.sub(
    r'(\.testi-slider-wrap\s*\{[^}]*max-width:\s*)1200px;',
    r'\1 450px;',
    content
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated style.css to constrain testi-slider-wrap to max-width: 450px.")
