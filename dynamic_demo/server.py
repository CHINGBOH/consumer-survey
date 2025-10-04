from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 模拟数据库
users = []
test_results = []

@app.route('/api/users/register', methods=['POST'])
def register_user():
    """用户注册"""
    data = request.get_json()

    # 检查必填字段
    if not all(k in data for k in ('email', 'password', 'name')):
        return jsonify({'error': '缺少必要字段'}), 400

    # 检查用户是否已存在
    if any(user['email'] == data['email'] for user in users):
        return jsonify({'error': '用户已存在'}), 400

    # 创建新用户
    new_user = {
        'id': len(users) + 1,
        'email': data['email'],
        'password': data['password'],  # 实际应用中需要加密
        'name': data['name'],
        'created_at': datetime.now().isoformat()
    }

    users.append(new_user)

    return jsonify({
        'message': '注册成功',
        'user': {
            'id': new_user['id'],
            'email': new_user['email'],
            'name': new_user['name']
        }
    }), 201

@app.route('/api/users/login', methods=['POST'])
def login_user():
    """用户登录"""
    data = request.get_json()

    if not all(k in data for k in ('email', 'password')):
        return jsonify({'error': '缺少邮箱或密码'}), 400

    # 查找用户
    user = next((u for u in users if u['email'] == data['email'] and u['password'] == data['password']), None)

    if not user:
        return jsonify({'error': '邮箱或密码错误'}), 401

    # 生成简单token
    token = f"token_{user['id']}_{int(datetime.now().timestamp())}"

    return jsonify({
        'message': '登录成功',
        'token': token,
        'user': {
            'id': user['id'],
            'email': user['email'],
            'name': user['name']
        }
    })

@app.route('/api/survey/submit', methods=['POST'])
def submit_survey():
    """提交测试结果"""
    data = request.get_json()

    if not all(k in data for k in ('userId', 'answers', 'userType')):
        return jsonify({'error': '缺少必要字段'}), 400

    # 计算风险评分
    risk_score = calculate_risk_score(data['answers'])

    # 生成推荐
    recommendations = generate_recommendations(data['userType'])

    result = {
        'id': len(test_results) + 1,
        'userId': data['userId'],
        'answers': data['answers'],
        'userType': data['userType'],
        'riskScore': risk_score,
        'recommendations': recommendations,
        'created_at': datetime.now().isoformat()
    }

    test_results.append(result)

    return jsonify({
        'message': '测试结果已保存',
        'result': {
            'id': result['id'],
            'userType': result['userType'],
            'riskScore': result['riskScore'],
            'recommendations': result['recommendations']
        }
    }), 201

@app.route('/api/users/<int:user_id>/results', methods=['GET'])
def get_user_results(user_id):
    """获取用户测试历史"""
    user_results = [r for r in test_results if r['userId'] == user_id]

    return jsonify({
        'results': user_results
    })

@app.route('/api/stats/overview', methods=['GET'])
def get_stats():
    """获取平台统计数据"""
    total_users = len(users)
    total_tests = len(test_results)

    # 用户类型分布
    user_type_stats = {}
    for result in test_results:
        user_type = result['userType']
        user_type_stats[user_type] = user_type_stats.get(user_type, 0) + 1

    # 平均风险评分
    avg_risk_score = sum(r['riskScore'] for r in test_results) / len(test_results) if test_results else 0

    return jsonify({
        'totalUsers': total_users,
        'totalTests': total_tests,
        'userTypeDistribution': user_type_stats,
        'averageRiskScore': round(avg_risk_score, 1)
    })

def calculate_risk_score(answers):
    """计算风险评分"""
    score = 0
    for answer in answers:
        risk_level = answer.get('riskLevel', 'low')
        if risk_level == 'high':
            score += 25
        elif risk_level == 'medium':
            score += 15
        else:
            score += 5
    return min(100, max(0, score))

def generate_recommendations(user_type):
    """生成个性化推荐"""
    recommendations = {
        '冲动型': [
            '建议选择基础护肤品，避免过度消费',
            '多学习护肤知识，建立理性消费观',
            '定期评估护肤效果，不要频繁更换产品'
        ],
        '理性型': [
            '继续保持理性的消费习惯',
            '可以适当尝试新品，但要有数据支持',
            '关注性价比和实际效果'
        ],
        '科学型': [
            '深入研究护肤成分和机制',
            '可以考虑专业级的护肤方案',
            '关注学术研究和临床数据'
        ],
        '结果导向型': [
            '选择有明确效果保证的产品',
            '重视产品评价和用户反馈',
            '关注实际使用效果'
        ],
        '新手型': [
            '从基础护肤开始学习',
            '多咨询专业人士意见',
            '循序渐进，避免一次性购买过多产品'
        ]
    }

    return recommendations.get(user_type, ['建议咨询专业美容师'])

if __name__ == '__main__':
    print("🚀 美研智库动态API服务器启动中...")
    print("📡 API地址: http://localhost:5000")
    print("📊 可用接口:")
    print("   POST /api/users/register - 用户注册")
    print("   POST /api/users/login - 用户登录")
    print("   POST /api/survey/submit - 提交测试")
    print("   GET  /api/users/<id>/results - 用户历史")
    print("   GET  /api/stats/overview - 平台统计")
    app.run(debug=True, port=5000)