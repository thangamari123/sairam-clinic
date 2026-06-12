import os
import glob

announcement_html = """
  <!-- ═══════════════ ANNOUNCEMENT BAR ═══════════════ -->
  <div class="announcement-bar">
    <div class="ab-item">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
      </svg>
      <span>Call us: +91 94436 49405</span>
    </div>
    <div class="ab-item">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"></circle>
        <polyline points="12 6 12 12 16 14"></polyline>
      </svg>
      <span>Mon - Sat: 9:30 AM - 8:30 PM</span>
    </div>
  </div>
"""

directory = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "class=\"announcement-bar\"" in content:
        print(f"Skipping {os.path.basename(file_path)}: already has announcement bar.")
        continue

    # Insert right before the navbar
    if "<header class=\"navbar\"" in content:
        new_content = content.replace("<header class=\"navbar\"", announcement_html + "\n  <header class=\"navbar\"")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}.")
    else:
        print(f"Could not find navbar in {os.path.basename(file_path)}.")
