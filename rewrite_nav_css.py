import os

css_path = r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

old_css = """
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
  
  /* Ensure footer has padding at the bottom so content isn't hidden by nav */
  .footer {
    padding-bottom: 90px;
  }
}
"""

new_css = """
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
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
    padding: 12px 16px;
    justify-content: space-between;
    align-items: flex-end;
    z-index: 1000;
  }
  .mb-nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    text-decoration: none;
    color: #28385e;
    font-family: var(--font-body);
    font-size: 0.7rem;
    font-weight: 700;
    flex: 1;
    background: none;
    border: none;
    cursor: pointer;
  }
  .mb-icon {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    background: #f3f4fa;
  }
  .mb-icon svg {
    width: 20px;
    height: 20px;
    color: #28385e;
  }
  .mb-nav-item.active .mb-icon {
    background: #e6f0fd;
  }
  .mb-nav-item.active .mb-icon svg {
    color: #2b70e4;
  }
  .mb-nav-item.active .mb-label {
    color: #2b70e4;
  }
  
  .mb-call-btn {
    position: relative;
    z-index: 10;
  }
  .mb-call-btn .mb-icon-solid {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: #2b70e4;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: none;
    transform: translateY(-8px);
  }
  .mb-call-btn .mb-icon-solid svg {
    width: 24px;
    height: 24px;
    color: white;
    fill: white;
  }
  .mb-call-btn .mb-label {
    transform: translateY(0px);
    color: #2b70e4;
  }
  
  /* Ensure footer has padding at the bottom so content isn't hidden by nav */
  .footer {
    padding-bottom: 90px;
  }
}
"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced CSS successfully.")
else:
    print("Could not find the exact old CSS block to replace.")
