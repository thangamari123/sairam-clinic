import os
import glob
import re

new_text = "⭐ 10+ Years Experience • 😊 4,000+ Happy Patients • 🏥 Advanced Dental Technology • 🦷 Expert Dental Care • 📞 +91 98945 49244 • 📱 +91 82484 36811 • 🛡️ Safe & Hygienic Environment • ✨ Beautiful Smiles Every Day"

# We create a single ab-item containing the text. 
# We duplicate it a few times inside the marquee-content so there's no gap during the loop if the screen is super wide.
# Wait, actually, the marquee animation needs enough content to span the width. 
# Since this text is very long, copying it twice per container is plenty.
span_html = f'<span style="padding: 0 20px; font-size: 0.9rem;">{new_text}</span>'

content_inner = f"""
      <div class="ab-item" style="display:inline-block; white-space:nowrap;">
        {span_html}
        {span_html}
      </div>"""

new_announcement_html = f"""  <div class="announcement-bar marquee-container">
    <div class="marquee-content" style="display:flex;">{content_inner}
    </div>
    <div class="marquee-content" aria-hidden="true" style="display:flex;">{content_inner}
    </div>
  </div>"""

directory = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic"
html_files = glob.glob(os.path.join(directory, "*.html"))

pattern = re.compile(r'<div class="announcement-bar[^>]*>.*?(?=<!-- ═══════════════ NAVBAR|<header)', re.DOTALL)

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Wait, the pattern above relies on exact comment characters which might have been mangled.
    # Let's use a simpler pattern: find announcement-bar and the next <header>
    pattern_backup = re.compile(r'<div class="announcement-bar[^>]*>.*?(?=<header)', re.DOTALL)
    
    new_content, count = pattern_backup.subn(new_announcement_html + '\n  ', content)
        
    if count > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}.")
    else:
        print(f"Could not find announcement bar in {os.path.basename(file_path)}.")
