import os

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"

with open(css_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Let's find where the weird text starts and cut it off completely.
bad_text_marker = ". m o b i l e"
if bad_text_marker in content:
    content = content.split(bad_text_marker)[0]

# Also cut off any previous /* MOBILE BOTTOM NAV */
if "/* ─────────── MOBILE BOTTOM NAV ─────────── */" in content:
    content = content.split("/* ─────────── MOBILE BOTTOM NAV ─────────── */")[0]

# Now let's append the PERFECT CSS block
perfect_css = """
/* ─────────── MOBILE BOTTOM NAV ─────────── */
.mobile-bottom-nav {
  display: none;
}

@media (max-width: 768px) {
  .mobile-bottom-nav {
    display: flex;
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: calc(100% - 32px);
    max-width: 500px;
    background: white;
    border-radius: 40px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    padding: 10px 16px;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
  }
  .mb-nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    text-decoration: none;
    color: #2b3d56;
    font-family: var(--font-body);
    font-size: 0.75rem;
    font-weight: 700;
    flex: 1;
    background: none;
    border: none;
    cursor: pointer;
  }
  .mb-icon {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    background: #f4f7fc;
  }
  .mb-icon svg {
    width: 22px;
    height: 22px;
    color: #2b3d56;
  }
  .mb-nav-item.active .mb-icon {
    background: #e3effd;
  }
  .mb-nav-item.active .mb-icon svg {
    color: #246ce0;
  }
  .mb-nav-item.active .mb-label {
    color: #246ce0;
  }
  
  .mb-call-btn {
    position: relative;
    z-index: 10;
  }
  .mb-call-btn .mb-icon-solid {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #246ce0;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 12px 30px rgba(36, 108, 224, 0.4);
    transform: translateY(-16px);
  }
  .mb-call-btn .mb-icon-solid svg {
    width: 26px;
    height: 26px;
    color: white;
  }
  .mb-call-btn .mb-label {
    transform: translateY(-10px);
    color: #246ce0;
  }
  
  /* Ensure body has padding at the bottom so content isn't hidden */
  body {
    padding-bottom: 90px;
  }
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content + perfect_css)

print("Fixed CSS successfully!")
