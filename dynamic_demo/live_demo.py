#!/usr/bin/env python3
"""
美研智库动态功能演示
模拟动态网站的核心功能
"""

import json
import time
from datetime import datetime

# 模拟数据库
users_db = []
test_results_db = []

def simulate_api_call(endpoint, method="GET", data=None):
    """模拟API调用"""
    print(f"\n🌐 {method} {endpoint}")
    print("-" * 60)
    time.sleep(0.5)  # 模拟网络延迟

    if data:
        print(f"📤 请求数据: {json.dumps(data, ensure_ascii=False, indent=2)}")

def demo_user_registration():
    """演示用户注册功能"""
    simulate_api_call("/api/users/register", "POST", {
        "email": "xiaoming@example.com",
        "password": "123456",
        "name": "小明"
    })

    # 模拟服务器响应
    user = {
        "id": 1,
        "email": "xiaoming@example.com",
        "name": "小明",
        "created_at": datetime.now().isoformat()
    }
    users_db.append(user)

    print("✅ 服务器响应 (201 Created):")
    print(json.dumps({
        "message": "注册成功",
        "user": {
            "id": user["id"],
            "email": user["email"],
            "name": user["name"]
        }
    }, ensure_ascii=False, indent=2))

    return user["id"]

def demo_user_login():
    """演示用户登录功能"""
    simulate_api_call("/api/users/login", "POST", {
        "email": "xiaoming@example.com",
        "password": "123456"
    })

    # 模拟服务器验证
    user = next((u for u in users_db if u["email"] == "xiaoming@example.com"), None)

    if user:
        token = f"token_{user['id']}_{int(datetime.now().timestamp())}"
        print("✅ 服务器响应 (200 OK):")
        print(json.dumps({
            "message": "登录成功",
            "token": token,
            "user": {
                "id": user["id"],
                "email": user["email"],
                "name": user["name"]
            }
        }, ensure_ascii=False, indent=2))
        return user["id"]
    else:
        print("❌ 服务器响应 (401 Unauthorized):")
        print(json.dumps({"error": "邮箱或密码错误"}, ensure_ascii=False, indent=2))
        return None

def demo_submit_survey(user_id):
    """演示提交测试结果"""
    survey_data = {
        "userId": user_id,
        "userType": "理性型",
        "answers": [
            {"question": 1, "answer": "A", "riskLevel": "low"},
            {"question": 2, "answer": "B", "riskLevel": "medium"},
            {"question": 3, "answer": "C", "riskLevel": "high"},
            {"question": 4, "answer": "A", "riskLevel": "low"},
            {"question": 5, "answer": "B", "riskLevel": "medium"}
        ]
    }

    simulate_api_call("/api/survey/submit", "POST", survey_data)

    # 模拟风险评分计算
    risk_score = 0
    for answer in survey_data["answers"]:
        if answer["riskLevel"] == "high":
            risk_score += 25
        elif answer["riskLevel"] == "medium":
            risk_score += 15
        else:
            risk_score += 5
    risk_score = min(100, max(0, risk_score))

    # 模拟个性化推荐
    recommendations = {
        "理性型": [
            "继续保持理性的消费习惯",
            "可以适当尝试新品，但要有数据支持",
            "关注性价比和实际效果"
        ]
    }.get(survey_data["userType"], ["建议咨询专业美容师"])

    # 保存到数据库
    result = {
        "id": len(test_results_db) + 1,
        "userId": user_id,
        "userType": survey_data["userType"],
        "riskScore": risk_score,
        "recommendations": recommendations,
        "created_at": datetime.now().isoformat()
    }
    test_results_db.append(result)

    print("✅ 服务器响应 (201 Created):")
    print(json.dumps({
        "message": "测试结果已保存",
        "result": {
            "id": result["id"],
            "userType": result["userType"],
            "riskScore": result["riskScore"],
            "recommendations": result["recommendations"]
        }
    }, ensure_ascii=False, indent=2))

def demo_get_user_history(user_id):
    """演示获取用户历史记录"""
    simulate_api_call(f"/api/users/{user_id}/results", "GET")

    user_results = [r for r in test_results_db if r["userId"] == user_id]

    print("✅ 服务器响应 (200 OK):")
    print(json.dumps({
        "results": user_results
    }, ensure_ascii=False, indent=2))

def demo_get_platform_stats():
    """演示获取平台统计数据"""
    simulate_api_call("/api/stats/overview", "GET")

    total_users = len(users_db)
    total_tests = len(test_results_db)

    # 用户类型分布
    user_type_stats = {}
    for result in test_results_db:
        user_type = result["userType"]
        user_type_stats[user_type] = user_type_stats.get(user_type, 0) + 1

    # 平均风险评分
    avg_risk_score = sum(r["riskScore"] for r in test_results_db) / len(test_results_db) if test_results_db else 0

    print("✅ 服务器响应 (200 OK):")
    print(json.dumps({
        "totalUsers": total_users,
        "totalTests": total_tests,
        "userTypeDistribution": user_type_stats,
        "averageRiskScore": round(avg_risk_score, 1)
    }, ensure_ascii=False, indent=2))

def demo_multiple_users():
    """演示多用户场景"""
    print("\n👥 演示: 多用户同时使用")
    print("=" * 60)

    # 添加更多用户
    users = [
        {"email": "xiaohong@example.com", "name": "小红", "type": "冲动型"},
        {"email": "xiaoli@example.com", "name": "小李", "type": "科学型"},
        {"email": "xiaowang@example.com", "name": "小王", "type": "结果导向型"}
    ]

    for user_data in users:
        user = {
            "id": len(users_db) + 1,
            "email": user_data["email"],
            "name": user_data["name"],
            "created_at": datetime.now().isoformat()
        }
        users_db.append(user)

        # 模拟提交测试
        result = {
            "id": len(test_results_db) + 1,
            "userId": user["id"],
            "userType": user_data["type"],
            "riskScore": 45 + len(test_results_db) * 10,  # 模拟不同分数
            "recommendations": [f"为{user_data['type']}用户定制的建议"],
            "created_at": datetime.now().isoformat()
        }
        test_results_db.append(result)

        print(f"✅ {user['name']} 完成测试 - 类型: {user_data['type']}")

    # 显示实时统计
    demo_get_platform_stats()

def main():
    """主演示函数"""
    print("🎭 美研智库动态功能演示")
    print("=" * 80)
    print("展示动态网站相比静态网站的核心优势")
    print()

    # 演示1: 用户注册
    user_id = demo_user_registration()

    # 演示2: 用户登录
    if user_id:
        login_user_id = demo_user_login()

        # 演示3: 提交测试结果
        if login_user_id:
            demo_submit_survey(login_user_id)

            # 演示4: 获取用户历史
            demo_get_user_history(login_user_id)

    # 演示5: 平台统计
    demo_get_platform_stats()

    # 演示6: 多用户场景
    demo_multiple_users()

    print("\n🎉 演示完成!")
    print("\n🚀 动态网站的核心优势:")
    print("• 🔐 用户账户系统 - 注册、登录、个性化")
    print("• 💾 数据持久化 - 测试结果永久保存")
    print("• 📊 实时统计 - 动态更新平台数据")
    print("• 🎯 个性化服务 - 基于用户历史的智能推荐")
    print("• 👥 多用户支持 - 并发访问和数据隔离")
    print("• 📱 状态管理 - 记住用户操作和偏好")
    print("• 🔄 实时更新 - 数据变化立即反映")
    print("• 📈 商业分析 - 用户行为和趋势洞察")

    print("\n💡 这些功能让美研智库从展示型网站")
    print("   升级为智能化数据服务平台!")

if __name__ == "__main__":
    main()