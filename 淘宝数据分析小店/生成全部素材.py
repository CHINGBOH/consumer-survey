from playwright.sync_api import sync_playwright
import os
from pathlib import Path

def generate_image(template_path, output_filename):
    """从HTML模板生成高清图片"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        
        current_dir = Path(__file__).parent
        full_path = current_dir / template_path
        html_file_path = full_path.as_uri()
        
        page.goto(html_file_path)
        page.wait_for_timeout(800)
        
        canvas_element = page.locator("#canvas")
        canvas_element.screenshot(path=output_filename)
        
        print(f"[OK] {output_filename}")
        
        browser.close()

def split_9_grid(input_image, output_folder):
    """将9宫格大图切分成9张小图"""
    from PIL import Image
    import os
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    img = Image.open(input_image)
    width, height = img.size
    
    grid_width = width // 3
    grid_height = height // 3
    
    for i in range(3):
        for j in range(3):
            left = j * grid_width
            top = i * grid_height
            right = left + grid_width
            bottom = top + grid_height
            
            cropped = img.crop((left, top, right, bottom))
            cropped.save(f"{output_folder}/grid_{i*3+j+1}.png")
    
    print(f"[OK] 9宫格已切分到 {output_folder}")

if __name__ == "__main__":
    print("开始生成全部营销素材...")
    print()
    
    print("1. 生成朋友圈9宫格...")
    generate_image("朋友圈9宫格.html", "朋友圈9宫格_完整.png")
    
    print("2. 切分9宫格...")
    try:
        split_9_grid("朋友圈9宫格_完整.png", "朋友圈9宫格")
    except:
        print("   需要安装Pillow: pip install Pillow")
    
    print()
    print("3. 生成详情页长图...")
    generate_image("详情页_完整流程.html", "详情页_完整流程.png")
    
    print()
    print("4. 生成价格对比表...")
    generate_image("价格对比表.html", "价格对比表.png")
    
    print()
    print("5. 生成案例展示图...")
    generate_image("案例展示图.html", "案例展示图.png")
    
    print()
    print("=" * 50)
    print("全部完成！")
    print("=" * 50)
    print()
    print("已生成文件：")
    print("- 朋友圈9宫格_完整.png (2400x2400)")
    print("- 朋友圈9宫格/ (9张小图)")
    print("- 详情页_完整流程.png (800x3200)")
    print("- 价格对比表.png (1200x800)")
    print("- 案例展示图.png (800x1200)")
