import os

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's remove the previous append
old_append = """
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
if old_append in content:
    content = content.replace(old_append, "")

# Now add an ultra compact block
ultra_compact = """
  /* Ultra Compact Patient Reviews for Mobile */
  .testimonials-section {
    padding: 40px 0;
  }
  .testi-card {
    padding: 14px;
    gap: 8px;
    border-radius: 12px;
  }
  .testi-stars {
    font-size: 0.85rem;
    letter-spacing: 0px;
    margin-bottom: 2px;
  }
  .testi-text {
    font-size: 0.75rem;
    line-height: 1.4;
  }
  .testi-avatar {
    width: 32px;
    height: 32px;
  }
  .testi-avatar svg {
    width: 32px;
    height: 32px;
  }
  .testi-author {
    gap: 8px;
  }
  .testi-author strong {
    font-size: 0.75rem;
  }
  .testi-author span {
    font-size: 0.6rem;
  }
  .testi-slider-wrap {
    margin-top: 20px;
  }
"""
# Find the @media (max-width: 768px) we created for this.
if "@media (max-width: 768px) {\n}\n" in content:
    content = content.replace("@media (max-width: 768px) {\n}\n", f"@media (max-width: 768px) {{\n{ultra_compact}\n}}\n")
else:
    # Just append it
    content += f"\n@media (max-width: 768px) {{\n{ultra_compact}\n}}\n"

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied ultra compact review styling.")
