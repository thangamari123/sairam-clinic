import os

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Make slider arrows smaller
# Old dimensions: width: 48px; height: 48px;
# We'll replace width: 48px; with width: 36px;
# and height: 48px; with height: 36px;

# Let's locate the .slider-arrow block
import re
new_content = re.sub(r'\.slider-arrow\s*{[^}]*}', 
                     lambda m: m.group(0).replace('width: 48px;', 'width: 36px;').replace('height: 48px;', 'height: 36px;'),
                     content)

# We can also make SVG inside slider-arrow smaller
# Wait, it doesn't have a specific svg rule in style.css, it's defined in HTML (width="20" height="20"). That's fine.

# Let's also add a mobile specific rule to make them even smaller if needed, or 36px is small enough.
mobile_slider_arrow = """
  .slider-arrow {
    width: 32px;
    height: 32px;
  }
  .slider-arrow.prev {
    left: 12px;
  }
  .slider-arrow.next {
    right: 12px;
  }
"""

if "@media (max-width: 768px) {\n" in new_content:
    new_content = new_content.replace("@media (max-width: 768px) {\n", f"@media (max-width: 768px) {{\n{mobile_slider_arrow}\n")
else:
    new_content += f"\n@media (max-width: 768px) {{\n{mobile_slider_arrow}\n}}\n"

with open(css_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated slider arrows to be smaller.")
