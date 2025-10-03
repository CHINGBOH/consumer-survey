import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [user, setUser] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [stats, setStats] = useState(null);

  // 获取统计数据
  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await fetch('http://localhost:3001/api/stats/overview');
      const data = await response.json();
      setStats(data);
    } catch (error) {
      console.error('获取统计数据失败:', error);
    }
  };

  const handleLogin = async (email, password) => {
    try {
      const response = await fetch('http://localhost:3001/api/users/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        setUser(data.user);
        setIsLoggedIn(true);
        localStorage.setItem('token', data.token);
      } else {
        alert(data.error);
      }
    } catch (error) {
      console.error('登录失败:', error);
    }
  };

  const handleLogout = () => {
    setUser(null);
    setIsLoggedIn(false);
    localStorage.removeItem('token');
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>💄 美研智库 - 动态版本</h1>
        <p>专业美容行业数据洞察平台</p>
      </header>

      <nav className="App-nav">
        {!isLoggedIn ? (
          <LoginForm onLogin={handleLogin} />
        ) : (
          <div className="user-info">
            <span>欢迎, {user.name}!</span>
            <button onClick={handleLogout}>退出登录</button>
          </div>
        )}
      </nav>

      <main className="App-main">
        <section className="stats-section">
          <h2>📊 平台数据统计</h2>
          {stats && (
            <div className="stats-grid">
              <div className="stat-card">
                <h3>注册用户</h3>
                <div className="stat-value">{stats.totalUsers}</div>
              </div>
              <div className="stat-card">
                <h3>测试次数</h3>
                <div className="stat-value">{stats.totalTests}</div>
              </div>
              <div className="stat-card">
                <h3>平均风险评分</h3>
                <div className="stat-value">{stats.averageRiskScore.toFixed(1)}</div>
              </div>
            </div>
          )}
        </section>

        {isLoggedIn && (
          <section className="user-section">
            <h2>👤 个人中心</h2>
            <UserDashboard userId={user.id} />
          </section>
        )}

        <section className="features-section">
          <h2>🚀 动态功能特色</h2>
          <div className="features-grid">
            <div className="feature-card">
              <h3>🔐 用户系统</h3>
              <p>注册登录，个性化体验</p>
            </div>
            <div className="feature-card">
              <h3>📈 实时分析</h3>
              <p>动态生成个性化报告</p>
            </div>
            <div className="feature-card">
              <h3>💾 数据存储</h3>
              <p>保存测试历史和偏好</p>
            </div>
            <div className="feature-card">
              <h3>📊 统计面板</h3>
              <p>实时查看平台数据</p>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

// 登录组件
function LoginForm({ onLogin }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onLogin(email, password);
  };

  return (
    <form onSubmit={handleSubmit} className="login-form">
      <input
        type="email"
        placeholder="邮箱"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="密码"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit">登录</button>
      <button type="button" onClick={() => alert('注册功能开发中...')}>
        注册
      </button>
    </form>
  );
}

// 用户仪表板组件
function UserDashboard({ userId }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetchUserResults();
  }, [userId]);

  const fetchUserResults = async () => {
    try {
      const response = await fetch(`http://localhost:3001/api/users/${userId}/results`);
      const data = await response.json();
      setResults(data.results);
    } catch (error) {
      console.error('获取用户结果失败:', error);
    }
  };

  return (
    <div className="user-dashboard">
      <h3>我的测试历史</h3>
      {results.length === 0 ? (
        <p>暂无测试记录，<a href="/survey">开始测试</a></p>
      ) : (
        <div className="results-list">
          {results.map(result => (
            <div key={result.id} className="result-card">
              <h4>用户类型: {result.userType}</h4>
              <p>风险评分: {result.riskScore}</p>
              <p>测试时间: {new Date(result.createdAt).toLocaleDateString()}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;