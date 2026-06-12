import glob

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    content = content.replace('href="#appointment"', 'href="appointment.html"')
    content = content.replace('href="index.html#appointment"', 'href="appointment.html"')
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
