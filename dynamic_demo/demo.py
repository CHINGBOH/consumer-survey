import requests
import json

# API基础URL
BASE_URL = "http://localhost:5000/api"

def demo_user_registration():
    """演示用户注册"""
    print("🔐 演示1: 用户注册")
    print("-" * 50)

    user_data = {
        "email": "xiaoming@example.com",
        "password": "123456",
        "name": "小明"
    }

    try:
        response = requests.post(f"{BASE_URL}/users/register",
                               json=user_data,
                               headers={"Content-Type": "application/json"})

        print(f"请求: POST {BASE_URL}/users/register")
        print(f"数据: {json.dumps(user_data, ensure_ascii=False, indent=2)}")
        print(f"状态码: {response.status_code}")

        if response.status_code == 201:
            result = response.json()
            print("✅ 注册成功!")
            print(f"用户ID: {result['user']['id']}")
            print(f"用户名: {result['user']['name']}")
            return result['user']['id']
        else:
            print(f"❌ 注册失败: {response.json()}")
            return None

    except Exception as e:
        print(f"❌ 网络错误: {e}")
        return None

def demo_user_login():
    """演示用户登录"""
    print("\n🔑 演示2: 用户登录")
    print("-" * 50)

    login_data = {
        "email": "xiaoming@example.com",
        "password": "123456"
    }

    try:
        response = requests.post(f"{BASE_URL}/users/login",
                               json=login_data,
                               headers={"Content-Type": "application/json"})

        print(f"请求: POST {BASE_URL}/users/login")
        print(f"数据: {json.dumps(login_data, ensure_ascii=False, indent=2)}")
        print(f"状态码: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("✅ 登录成功!")
            print(f"Token: {result['token'][:20]}...")
            print(f"用户: {result['user']['name']}")
            return result['user']['id']
        else:
            print(f"❌ 登录失败: {response.json()}")
            return None

    except Exception as e:
        print(f"❌ 网络错误: {e}")
        return None

def demo_submit_survey(user_id):
    """演示提交测试结果"""
    print(f"\n📝 演示3: 提交测试结果 (用户ID: {user_id})")
    print("-" * 50)

    survey_data = {
        "userId": user_id,
        "userType": "理性型",
        "answers": [
            {"question": 1, "answer": "A", "riskLevel": "low"},
            {"question": 2, "answer": "B", "riskLevel": "medium"},
            {"question": 3, "answer": "C", "riskLevel": "high"}
        ]
    }

    try:
        response = requests.post(f"{BASE_URL}/survey/submit",
                               json=survey_data,
                               headers={"Content-Type": "application/json"})

        print(f"请求: POST {BASE_URL}/survey/submit")
        print(f"数据: {json.dumps(survey_data, ensure_ascii=False, indent=2)}")
        print(f"状态码: {response.status_code}")

        if response.status_code == 201:
            result = response.json()
            print("✅ 测试结果提交成功!")
            print(f"用户类型: {result['result']['userType']}")
            print(f"风险评分: {result['result']['riskScore']}")
            print("推荐建议:")
            for i, rec in enumerate(result['result']['recommendations'], 1):
                print(f"  {i}. {rec}")
        else:
            print(f"❌ 提交失败: {response.json()}")

    except Exception as e:
        print(f"❌ 网络错误: {e}")

def demo_get_user_history(user_id):
    """演示获取用户历史记录"""
    print(f"\n📚 演示4: 获取用户历史 (用户ID: {user_id})")
    print("-" * 50)

    try:
        response = requests.get(f"{BASE_URL}/users/{user_id}/results")

        print(f"请求: GET {BASE_URL}/users/{user_id}/results")
        print(f"状态码: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print(f"✅ 获取成功! 共找到 {len(result['results'])} 条记录")

            for i, record in enumerate(result['results'], 1):
                print(f"\n记录 {i}:")
                print(f"  用户类型: {record['userType']}")
                print(f"  风险评分: {record['riskScore']}")
                print(f"  测试时间: {record['created_at'][:19]}")
        else:
            print(f"❌ 获取失败: {response.json()}")

    except Exception as e:
        print(f"❌ 网络错误: {e}")

def demo_get_platform_stats():
    """演示获取平台统计数据"""
    print("\n📊 演示5: 平台统计数据")
    print("-" * 50)

    try:
        response = requests.get(f"{BASE_URL}/stats/overview")

        print(f"请求: GET {BASE_URL}/stats/overview")
        print(f"状态码: {response.status_code}")

        if response.status_code == 200:
            stats = response.json()
            print("✅ 统计数据获取成功!")
            print(f"注册用户数: {stats['totalUsers']}")
            print(f"测试总次数: {stats['totalTests']}")
            print(f"平均风险评分: {stats['averageRiskScore']}")

            print("\n用户类型分布:")
            for user_type, count in stats['userTypeDistribution'].items():
                print(f"  {user_type}: {count} 人")
        else:
            print(f"❌ 获取失败: {response.json()}")

    except Exception as e:
        print(f"❌ 网络错误: {e}")

def main():
    """主演示函数"""
    print("🎭 美研智库动态API功能演示")
    print("=" * 60)
    print("服务器地址: http://localhost:5000")
    print("请确保Flask服务器正在运行...")
    print()

    # 演示用户注册
    user_id = demo_user_registration()

    if user_id:
        # 演示用户登录
        login_user_id = demo_user_login()

        if login_user_id:
            # 演示提交测试
            demo_submit_survey(login_user_id)

            # 演示获取历史记录
            demo_get_user_history(login_user_id)

    # 演示平台统计
    demo_get_platform_stats()

    print("\n🎉 演示完成!")
    print("这些功能展示了动态网站相比静态网站的核心优势:")
    print("• 用户账户系统")
    print("• 数据持久化存储")
    print("• 实时统计分析")
    print("• 个性化服务")

if __name__ == "__main__":
    main()