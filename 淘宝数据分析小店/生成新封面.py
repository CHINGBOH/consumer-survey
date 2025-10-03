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
    print("开始生成新风格封面...")
    
    generate_banner("封面1_真实风格.html", "封面1_真实风格.png")
    generate_banner("封面2_案例展示.html", "封面2_案例展示.png")
    generate_banner("封面3_服务流程.html", "封面3_服务流程.png")
    generate_banner("封面4_痛点共鸣.html", "封面4_痛点共鸣.png")
    generate_banner("封面5_价格对比.html", "封面5_价格对比.png")
    
    print("\n全部完成！5张新风格封面已生成")
    print("适合小红书/抖音/朋友圈")
