from playwright.sync_api import sync_playwright
import os
import shutil

def generate_banner(template_path, output_filename):
    """
    从指定的HTML模板生成高清横幅图片。
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2) # 使用2倍缩放以获得高清图
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = f"file://{os.path.join(current_dir, template_path)}"
        
        page.goto(html_file_path)
        
        canvas_element = page.locator("#canvas")
        canvas_element.screenshot(path=output_filename)
        
        print(f"🎉 成功生成图片：{output_filename}")
        
        browser.close()

def generate_html(template_path, output_filename):
    """
    从指定的HTML模板生成HTML文件。
    """
    shutil.copy(template_path, output_filename)
    print(f"🎉 成功生成HTML：{output_filename}")

# --- 开始调用！---
if __name__ == "__main__":
    # 生成第一张图：品牌主形象
    generate_html(
        template_path="template_banner_1.html",
        output_filename="banner_1_brand.html"
    )
    
    # 生成第二张图：服务起点
    generate_html(
        template_path="template_banner_2.html",
        output_filename="banner_2_service_start.html"
    )
    
    # 生成第三张图：核心产品
    generate_html(
        template_path="template_banner_3.html",
        output_filename="banner_3_core_products.html"
    )
    
    # 生成第四张图：增值选项
    generate_html(
        template_path="template_banner_4.html",
        output_filename="banner_4_value_added.html"
    )
    
    # 生成第五张图：服务保障与引导
    generate_html(
        template_path="template_banner_5.html",
        output_filename="banner_5_service_guarantee.html"
    )

