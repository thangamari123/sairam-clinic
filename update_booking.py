import os
import glob

directory = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic"
html_files = glob.glob(os.path.join(directory, "*.html"))

old_reviews_html = """    <a href="index.html#testimonials" class="mb-nav-item">
      <div class="mb-icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
      </div>
      <span class="mb-label">Reviews</span>
    </a>"""

new_booking_html = """    <a href="appointment.html" class="mb-nav-item">
      <div class="mb-icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
      </div>
      <span class="mb-label">Booking</span>
    </a>"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Sometimes formatting might be slightly different.
    # Let's use string replace but be careful.
    if old_reviews_html in content:
        content = content.replace(old_reviews_html, new_booking_html)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
    else:
        # fallback regex if formatting differs
        import re
        pattern = re.compile(r'<a href="index\.html#testimonials" class="mb-nav-item">[\s\S]*?<span class="mb-label">Reviews</span>\s*</a>')
        new_content, count = pattern.subn(new_booking_html, content)
        if count > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(file_path)} using regex")
