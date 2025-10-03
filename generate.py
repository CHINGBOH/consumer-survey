from playwright.sync_api import sync_playwright
import os
import shutil
import re
from pricing_config import PRICING, PACKAGE_NAMES, ADDON_NAMES

def generate_banner(template_path, output_filename):
    """
    从指定的HTML模板生成高清横幅图片（自动应用价格配置）。
    """
    # 创建临时文件应用价格配置
    temp_template = f"temp_{template_path}"
    apply_pricing_to_template(template_path, temp_template)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2) # 使用2倍缩放以获得高清图

        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = f"file://{os.path.join(current_dir, temp_template)}"

        page.goto(html_file_path)

        canvas_element = page.locator("#canvas")
        canvas_element.screenshot(path=output_filename)

        print(f"🎉 成功生成图片：{output_filename}")

        browser.close()

    # 清理临时文件
    if os.path.exists(temp_template):
        os.remove(temp_template)

def generate_long_image(template_path, output_filename):
    """
    从指定的HTML模板生成高清长图（自动应用价格配置）。
    """
    # 创建临时文件应用价格配置
    temp_template = f"temp_{template_path}"
    apply_pricing_to_template(template_path, temp_template)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2) # 使用2倍缩放以获得高清图

        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = f"file://{os.path.join(current_dir, temp_template)}"

        page.goto(html_file_path)

        # 等待页面完全加载
        page.wait_for_load_state('networkidle')

        # 设置视口大小以适应长图
        page.set_viewport_size({"width": 1200, "height": 2200})

        # 截取整个页面
        page.screenshot(path=output_filename, full_page=True)

        print(f"🎉 成功生成长图：{output_filename}")

        browser.close()

    # 清理临时文件
    if os.path.exists(temp_template):
        os.remove(temp_template)

def apply_pricing_to_template(template_path, output_path):
    """
    将价格配置应用到HTML模板中。
    """
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换价格占位符
    for key, price in PRICING.items():
        # 替换形如 {{consultation}} 的占位符为实际价格
        placeholder = f"{{{{{key}}}}}"
        content = content.replace(placeholder, str(price))

        # 替换形如 ¥{{consultation}} 的占位符
        yen_placeholder = f"¥{{{{{key}}}}}"
        content = content.replace(yen_placeholder, f"¥{price}")

        # 替换形如 +¥{{consultation}} 的占位符
        plus_placeholder = f"+¥{{{{{key}}}}}"
        content = content.replace(plus_placeholder, f"+¥{price}")

    # 替换套餐名称占位符
    for key, name in PACKAGE_NAMES.items():
        placeholder = f"{{{{package_{key}}}}}"
        content = content.replace(placeholder, name)

    # 替换增值服务名称占位符
    for key, name in ADDON_NAMES.items():
        placeholder = f"{{{{addon_{key}}}}}"
        content = content.replace(placeholder, name)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"🎉 价格配置已应用到：{output_path}")

def generate_html(template_path, output_filename):
    """
    从指定的HTML模板生成HTML文件（自动应用价格配置）。
    """
    # 创建临时文件应用价格配置
    temp_template = f"temp_{template_path}"
    apply_pricing_to_template(template_path, temp_template)

    # 复制处理后的模板
    shutil.copy(temp_template, output_filename)

    # 清理临时文件
    if os.path.exists(temp_template):
        os.remove(temp_template)

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

    # 生成长图：完整服务流程说明
    generate_html(
        template_path="template_process_guide.html",
        output_filename="process_guide.html"
    )

    # 生成长图PNG版本
    generate_long_image(
        template_path="template_process_guide.html",
        output_filename="process_guide.png"
    )