# 美研智库 - 动态网站演示

这是一个将静态美研智库网站升级为动态版本的概念演示。

## 🚀 功能特色

### 动态功能
- ✅ 用户注册和登录系统
- ✅ 个性化测试结果存储
- ✅ 实时数据统计面板
- ✅ 用户历史记录管理
- ✅ API驱动的数据处理

### 技术栈
- **后端**: Node.js + Express
- **前端**: React (演示)
- **数据库**: 内存存储 (演示用)
- **API**: RESTful 接口

## 🛠️ 安装和运行

### 1. 安装依赖
```bash
cd dynamic_demo
npm install
```

### 2. 启动API服务器
```bash
npm start
# 或开发模式
npm run dev
```

服务器将在 `http://localhost:3001` 启动

### 3. 测试API接口

#### 用户注册
```bash
curl -X POST http://localhost:3001/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"123456","name":"测试用户"}'
```

#### 用户登录
```bash
curl -X POST http://localhost:3001/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"123456"}'
```

#### 提交测试结果
```bash
curl -X POST http://localhost:3001/api/survey/submit \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 1,
    "answers": [{"question":1,"answer":"A","riskLevel":"low"}],
    "userType": "理性型"
  }'
```

#### 获取统计数据
```bash
curl http://localhost:3001/api/stats/overview
```

## 📊 API接口文档

### 用户管理
- `POST /api/users/register` - 用户注册
- `POST /api/users/login` - 用户登录
- `GET /api/users/:userId/results` - 获取用户测试历史

### 测试功能
- `POST /api/survey/submit` - 提交测试结果

### 数据统计
- `GET /api/stats/overview` - 获取平台统计数据

## 🔄 与静态版本的对比

| 功能 | 静态版本 | 动态版本 |
|------|----------|----------|
| 用户系统 | ❌ 无 | ✅ 注册登录 |
| 数据存储 | ❌ 本地存储 | ✅ 数据库存储 |
| 个性化 | ❌ 通用报告 | ✅ 个性化分析 |
| 实时更新 | ❌ 静态内容 | ✅ 动态数据 |
| 管理后台 | ❌ 无 | ✅ 内容管理 |
| API接口 | ❌ 无 | ✅ RESTful API |

## 📈 扩展方向

### Phase 1: 基础功能
- [ ] 用户认证系统 (JWT)
- [ ] 数据库集成 (PostgreSQL)
- [ ] 测试结果持久化

### Phase 2: 高级功能
- [ ] 实时数据可视化
- [ ] 个性化推荐算法
- [ ] 邮件通知系统

### Phase 3: 商业化
- [ ] 付费服务集成
- [ ] 企业级定制
- [ ] 多租户架构

## 💰 成本考虑

### 开发成本
- 基础动态网站: ¥50,000-100,000
- 高级功能版本: ¥150,000-300,000
- 企业级定制: ¥300,000+

### 运营成本 (每月)
- 服务器: ¥500-2,000
- 数据库: ¥200-1,000
- CDN: ¥100-500
- 域名: ¥100

## 🎯 适用场景

### 适合动态化的业务场景
- 需要用户注册登录
- 个性化内容推荐
- 实时数据分析
- 商业付费服务
- 大量用户交互

### 仍适合静态的场景
- 纯展示型网站
- 小型企业官网
- 个人博客
- 文档网站

---

*这是一个概念演示，实际部署需要考虑安全、性能、可扩展性等因素。*