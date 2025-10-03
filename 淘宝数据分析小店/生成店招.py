from playwright.sync_api import sync_playwright
import os

def generate_banner(template_path, output_filename):
    """从HTML模板生成高清图片"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = f"file://{os.path.join(current_dir, template_path)}"
        
        page.goto(html_file_path)
        page.wait_for_timeout(500)
        
        canvas_element = page.locator("#canvas")
        canvas_element.screenshot(path=output_filename)
        
        print(f"[OK] {output_filename}")
        
        browser.close()

if __name__ == "__main__":
    print("生成店招横幅...")
    generate_banner("店招_主横幅.html", "店招_主横幅.png")
    print("完成！")
