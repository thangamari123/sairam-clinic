import os
import re

files = ["about.html", "dr-nivetha.html", "dr-raghuraaman.html", "index.html", "treatments.html"]

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the scroll-top button block
    pattern = r"<!-- Scroll To Top -->\s*<button class=\"scroll-top\" id=\"scroll-top-btn\" aria-label=\"Scroll to top\">\s*<svg.*?>\s*<polyline.*?>\s*</svg>\s*</button>\s*"
    new_content = re.sub(pattern, "", content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)
        
print("Removed scroll-to-top button from all files!")
