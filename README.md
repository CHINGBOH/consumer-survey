# 📊 消费行为调查分析平台

基于 **Hugo + Quarto** 构建的现代化消费行为研究平台，助您**从零开始**设计问卷、收集数据、进行分析并展示成果。

## 🚨 重要提醒

**这个项目是空白模板，没有预设数据或结论！**

- ❌ 网站中显示的统计数字都是占位符 (`--` 或 `0%`)
- ❌ `survey_data_template.csv` 仅供学习分析方法
- ✅ 您的真实数据请记录在 `your_survey_data.csv`
- ✅ 分析结果将在您收集数据后动态生成

## 🚀 项目特色

- **🔬 科学方法**：基于统计学的严谨分析框架
- **📱 现代化界面**：响应式设计，支持移动端访问
- **⚡ 高效开发**：Hugo 快速生成 + Quarto 代码执行
- **📊 交互可视化**：丰富的图表和数据探索功能
- **🔄 可复现研究**：开放数据和可执行代码

## 📁 项目结构

```
SurveyAnalysis/
├── _quarto.yml          # Quarto 网站配置
├── index.qmd           # 网站首页
├── survey/             # 问卷设计模块
│   └── index.qmd      # 问卷设计指南
├── analysis/           # 数据分析模块
│   └── index.qmd      # 分析框架与方法
├── results/            # 研究成果展示
│   └── index.qmd      # 分析结果报告
├── data/               # 数据存储目录
│   └── sample_survey_data.csv  # 示例数据集
└── styles.css          # 自定义样式文件
```

## 🛠️ 技术栈

- **静态网站生成**：Hugo
- **文档发布系统**：Quarto
- **数据分析语言**：R
- **可视化库**：ggplot2, plotly
- **部署平台**：GitHub Pages / Netlify

## 📋 使用指南

### 1. 环境准备

```bash
# 安装 Hugo (Windows)
choco install hugo

# 安装 Quarto
# 从 https://quarto.org/docs/get-started/ 下载

# 安装 R 和必要包
install.packages(c("tidyverse", "ggplot2", "rmarkdown", "psych", "corrplot"))
```

### 2. 本地预览

```bash
# 进入项目目录
cd SurveyAnalysis

# 启动 Hugo 服务器
hugo server

# 或者使用 Quarto 预览
quarto preview
```

### 3. 构建网站

```bash
# 生成静态网站
hugo

# 或者使用 Quarto 渲染
quarto render
```

## 📊 数据分析流程

### 第一阶段：问卷设计
1. 明确研究目标和问题
2. 设计问卷结构和题型
3. 内部测试和优化

### 第二阶段：数据收集
1. 选择合适的问卷工具
2. 制定分发策略
3. 监控数据质量

### 第三阶段：数据分析
1. 数据清洗和预处理
2. 描述性统计分析
3. 探索性数据分析
4. 假设检验和回归分析

### 第四阶段：成果展示
1. 生成分析报告
2. 创建交互式可视化
3. 部署网站展示

## 🎯 核心功能模块

### 问卷设计模块
- 科学的问卷设计方法
- 多种题型选择指南
- 质量控制检查表

### 数据分析模块
- 完整的统计分析流程
- R 代码示例和模板
- 可视化图表生成

### 成果展示模块
- 专业的报告模板
- 交互式数据探索
- 响应式网站设计

## 📈 示例分析结果

基于示例数据集的分析结果显示：

- **样本特征**：以21-25岁年轻人为主
- **消费偏好**：线上电商平台占比最高
- **决策因素**：服务重要性评分最高
- **关键洞察**：价格敏感度与品牌重要性呈负相关

## 🔧 自定义配置

### 网站主题配置

编辑 `_quarto.yml` 文件：

```yaml
format:
  html:
    theme: cosmo  # 可选: default, cerulean, journal, flatly, darkly, readable, spacelab, united, cosmo
    css: styles.css
```

### 添加新分析页面

1. 在相应目录创建 `.qmd` 文件
2. 在 `_quarto.yml` 中添加导航链接
3. 编写 R 代码进行数据分析

## 📚 学习资源

- [Hugo 官方文档](https://gohugo.io/documentation/)
- [Quarto 指南](https://quarto.org/docs/guide/)
- [R for Data Science](https://r4ds.had.co.nz/)
- [ggplot2 文档](https://ggplot2.tidyverse.org/)

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

**💡 提示**: 这是一个完整的消费行为研究平台模板，您可以根据具体研究需求进行定制和扩展。</content>
<parameter name="filePath">C:\Users\l\Documents\GitHub\SurveyAnalysis\README.md