import os

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

new_css = """
  /* Patient Reviews Compact Mobile */
  .testimonials-section {
    padding: 50px 0;
  }
  .testi-card {
    padding: 16px;
    gap: 12px;
    border-radius: 16px;
  }
  .testi-text {
    font-size: 0.85rem;
    line-height: 1.5;
  }
  .testi-avatar {
    width: 40px;
    height: 40px;
  }
  .testi-avatar svg {
    width: 40px;
    height: 40px;
  }
  .testi-author {
    gap: 12px;
  }
  .testi-stars {
    font-size: 1rem;
    letter-spacing: 1px;
  }
  .testi-slider-wrap {
    margin-top: 30px;
  }
"""

# Let's insert this into the existing @media (max-width: 768px) block.
# I know there is an @media (max-width: 768px) near the end for the mobile-bottom-nav
# But it's safer to just append a new @media (max-width: 768px) at the very end.

append_str = "\n@media (max-width: 768px) {\n" + new_css + "}\n"

with open(css_path, "a", encoding="utf-8") as f:
    f.write(append_str)

print("Appended compact review styles successfully.")
