import os
import glob

bottom_nav_html = """  <!-- ═══════════════ MOBILE BOTTOM NAV ═══════════════ -->
  <nav class="mobile-bottom-nav">
    <a href="index.html" class="mb-nav-item">
      <div class="mb-icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
      </div>
      <span class="mb-label">Home</span>
    </a>
    <a href="treatments.html" class="mb-nav-item">
      <div class="mb-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c-3 0-5-3-5-6v-2a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v2c0 3-2 6-5 6z"></path><path d="M9 10V8a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v2"></path><path d="M12 21v-4"></path></svg>
      </div>
      <span class="mb-label">Treatments</span>
    </a>
    <a href="tel:+919894549244" class="mb-nav-item mb-call-btn">
      <div class="mb-icon-solid">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
      </div>
      <span class="mb-label">Call Us</span>
    </a>
    <a href="index.html#testimonials" class="mb-nav-item">
      <div class="mb-icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
      </div>
      <span class="mb-label">Reviews</span>
    </a>
    <button class="mb-nav-item" id="mb-more-btn" aria-label="More Menu">
      <div class="mb-icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </div>
      <span class="mb-label">More</span>
    </button>
  </nav>

</body>"""

directory = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "mobile-bottom-nav" in content:
        print(f"Skipping {os.path.basename(file_path)}: already has bottom nav.")
        continue

    # Insert right before </body>
    if "</body>" in content:
        new_content = content.replace("</body>", bottom_nav_html)
        
        if os.path.basename(file_path) == "index.html":
            new_content = new_content.replace('<a href="index.html" class="mb-nav-item">', '<a href="index.html" class="mb-nav-item active">')
        elif os.path.basename(file_path) == "treatments.html":
            new_content = new_content.replace('<a href="treatments.html" class="mb-nav-item">', '<a href="treatments.html" class="mb-nav-item active">')
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}.")
    else:
        print(f"Could not find </body> in {os.path.basename(file_path)}.")
