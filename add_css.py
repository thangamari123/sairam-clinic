import os

css = """
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
    gap: 4px;
    text-decoration: none;
    color: var(--navy);
    font-family: var(--font-body);
    font-size: 0.7rem;
    font-weight: 600;
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
    background: rgba(14, 165, 233, 0.05);
  }
  .mb-icon svg {
    width: 20px;
    height: 20px;
    color: var(--navy);
  }
  .mb-nav-item.active .mb-icon {
    background: rgba(14, 165, 233, 0.15);
  }
  .mb-nav-item.active .mb-icon svg {
    color: var(--blue);
  }
  .mb-nav-item.active .mb-label {
    color: var(--blue);
  }
  
  .mb-call-btn .mb-icon-solid {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: var(--blue);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 24px rgba(14, 165, 233, 0.3);
    transform: translateY(-8px);
  }
  .mb-call-btn .mb-icon-solid svg {
    width: 24px;
    height: 24px;
    color: white;
  }
  .mb-call-btn .mb-label {
    transform: translateY(-4px);
    color: var(--blue);
  }
  
  /* Ensure body has padding at the bottom so content isn't hidden */
  body {
    padding-bottom: 90px;
  }
}
"""

with open(r"c:\Users\thang\OneDrive\Desktop\sairam-clinic\style.css", "a", encoding="utf-8") as f:
    f.write(css)
