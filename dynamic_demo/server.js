const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3001;

// 中间件
app.use(cors());
app.use(bodyParser.json());

// 模拟用户数据库
let users = [];
let testResults = [];

// API路由

// 1. 用户注册
app.post('/api/users/register', (req, res) => {
  const { email, password, name } = req.body;

  // 检查用户是否已存在
  const existingUser = users.find(user => user.email === email);
  if (existingUser) {
    return res.status(400).json({ error: '用户已存在' });
  }

  const newUser = {
    id: users.length + 1,
    email,
    password, // 实际应用中需要加密
    name,
    createdAt: new Date()
  };

  users.push(newUser);
  res.status(201).json({
    message: '注册成功',
    user: { id: newUser.id, email: newUser.email, name: newUser.name }
  });
});

// 2. 用户登录
app.post('/api/users/login', (req, res) => {
  const { email, password } = req.body;

  const user = users.find(user => user.email === email && user.password === password);
  if (!user) {
    return res.status(401).json({ error: '邮箱或密码错误' });
  }

  // 生成简单的token (实际应用中使用JWT)
  const token = `token_${user.id}_${Date.now()}`;

  res.json({
    message: '登录成功',
    token,
    user: { id: user.id, email: user.email, name: user.name }
  });
});

// 3. 提交测试结果
app.post('/api/survey/submit', (req, res) => {
  const { userId, answers, userType } = req.body;

  const result = {
    id: testResults.length + 1,
    userId,
    answers,
    userType,
    riskScore: calculateRiskScore(answers),
    recommendations: generateRecommendations(userType),
    createdAt: new Date()
  };

  testResults.push(result);

  res.status(201).json({
    message: '测试结果已保存',
    result: {
      id: result.id,
      userType: result.userType,
      riskScore: result.riskScore,
      recommendations: result.recommendations
    }
  });
});

// 4. 获取用户历史记录
app.get('/api/users/:userId/results', (req, res) => {
  const { userId } = req.params;

  const userResults = testResults.filter(result => result.userId == userId);
  res.json({ results: userResults });
});

// 5. 获取统计数据
app.get('/api/stats/overview', (req, res) => {
  const totalUsers = users.length;
  const totalTests = testResults.length;

  // 用户类型分布
  const userTypeStats = {};
  testResults.forEach(result => {
    userTypeStats[result.userType] = (userTypeStats[result.userType] || 0) + 1;
  });

  res.json({
    totalUsers,
    totalTests,
    userTypeDistribution: userTypeStats,
    averageRiskScore: testResults.reduce((sum, r) => sum + r.riskScore, 0) / testResults.length || 0
  });
});

// 辅助函数
function calculateRiskScore(answers) {
  // 简单的风险评分算法 (0-100)
  let score = 0;
  answers.forEach(answer => {
    if (answer.riskLevel === 'high') score += 25;
    else if (answer.riskLevel === 'medium') score += 15;
    else score += 5;
  });
  return Math.min(100, Math.max(0, score));
}

function generateRecommendations(userType) {
  const recommendations = {
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
  };

  return recommendations[userType] || ['建议咨询专业美容师'];
}

// 启动服务器
app.listen(PORT, () => {
  console.log(`美研智库API服务器运行在端口 ${PORT}`);
});

module.exports = app;