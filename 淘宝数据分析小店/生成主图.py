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
        page.wait_for_timeout(500)  # 等待字体加载
        
        canvas_element = page.locator("#canvas")
        canvas_element.screenshot(path=output_filename)
        
        print(f"[OK] {output_filename}")
        
        browser.close()

if __name__ == "__main__":
    print("开始生成淘宝主图...")
    
    # 生成5张主图
    generate_banner("主图1_封面.html", "淘宝主图1_封面.png")
    generate_banner("主图2_价格.html", "淘宝主图2_价格.png")
    generate_banner("主图3_交付物.html", "淘宝主图3_交付物.png")
    generate_banner("主图4_保障.html", "淘宝主图4_保障.png")
    generate_banner("主图5_场景.html", "淘宝主图5_场景.png")
    
    print("\n全部完成！5张主图已生成")
    print("文件位置：当前目录")
