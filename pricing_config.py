# 淘宝数据分析小店价格配置
# 修改此文件中的价格，所有模板会自动更新

PRICING = {
    # 咨询服务
    "consultation": 50,

    # 基础套餐
    "basic_package": 100,
    "standard_package": 200,
    "premium_package": 300,
    "sas_enterprise_package": 500,

    # 增值服务
    "chart_beautification": 30,
    "report_polish": 50,
    "code_delivery": 20,
    "vip_service": 80,
    "urgent_service": 50,
}

# 套餐名称映射
PACKAGE_NAMES = {
    "basic_package": "基础版",
    "standard_package": "标准版",
    "premium_package": "高级版",
    "sas_enterprise_package": "SAS企业版",
}

# 增值服务名称映射
ADDON_NAMES = {
    "chart_beautification": "可视化增强",
    "report_polish": "报告润色",
    "code_delivery": "代码交付",
    "vip_service": "VIP服务包",
    "urgent_service": "加急服务",
}