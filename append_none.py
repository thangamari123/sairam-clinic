import os

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"
with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n.mobile-bottom-nav { display: none; }\n")

print("Appended successfully.")
