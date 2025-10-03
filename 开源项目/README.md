# 📊 问卷数据全流程分析框架 (Survey Data Analysis Framework)

[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/survey-analysis-framework.svg)](https://github.com/yourusername/survey-analysis-framework/stargazers)

> 一套完整的问卷数据清洗、分析、可视化解决方案，适用于学术研究、市场调研、用户研究等场景

## 🎯 项目特色

- ✅ **完整流程**：从原始数据到最终报告的全流程自动化
- ✅ **质量控制**：多维度数据清洗和质量检验
- ✅ **统计严谨**：涵盖描述统计、相关分析、因子分析、聚类、回归等
- ✅ **可视化美观**：出版级图表，支持中英文
- ✅ **可复用性强**：模块化设计，易于迁移到新项目
- ✅ **文档详细**：每个步骤都有详细注释和说明

## 📁 项目结构

```
survey-analysis-framework/
├── code/                      # 分析代码
│   ├── 01_data_cleaning.R    # 数据清洗
│   ├── 02_descriptive.R      # 描述性统计
│   ├── 03_correlation.R      # 相关分析
│   ├── 04_factor_analysis.R  # 因子分析
│   ├── 05_clustering.R       # 聚类分析
│   ├── 06_regression.R       # 回归分析
│   └── utils.R               # 工具函数
│
├── demo_data/                 # 示例数据
│   ├── raw_survey.xlsx       # 模拟原始问卷
│   └── data_dictionary.xlsx  # 数据字典
│
├── outputs/                   # 输出结果
│   ├── figures/              # 图表
│   ├── tables/               # 统计表
│   └── reports/              # 分析报告
│
├── docs/                      # 文档
│   ├── methodology.md        # 方法论说明
│   ├── tutorial.md           # 使用教程
│   └── best_practices.md     # 最佳实践
│
└── README.md                  # 项目说明
```

## 🚀 快速开始

### 1. 环境准备

```r
# 安装必需的R包
install.packages(c(
  "tidyverse",    # 数据处理
  "psych",        # 心理测量学分析
  "corrplot",     # 相关矩阵可视化
  "ggplot2",      # 高级绘图
  "cluster",      # 聚类分析
  "factoextra",   # 因子分析可视化
  "openxlsx",     # Excel读写
  "knitr",        # 报告生成
  "rmarkdown"     # 动态文档
))
```

### 2. 运行示例

```r
# 克隆项目
git clone https://github.com/yourusername/survey-analysis-framework.git
cd survey-analysis-framework

# 在R中运行
source("code/01_data_cleaning.R")
source("code/02_descriptive.R")
# ... 依次运行其他脚本
```

### 3. 适配你的数据

1. 将你的问卷数据放入 `demo_data/` 目录
2. 修改 `data_dictionary.xlsx` 定义变量
3. 调整代码中的变量名和参数
4. 运行分析脚本

## 📊 分析模块说明

### 模块1：数据清洗 (Data Cleaning)
- 缺失值处理
- 异常值检测
- 注意力检查题筛选
- 答题时长过滤
- 逻辑一致性检验

### 模块2：描述性统计 (Descriptive Statistics)
- 样本基本特征
- 各维度均值、标准差
- 频率分布
- 人口统计学分析

### 模块3：相关分析 (Correlation Analysis)
- Pearson相关系数
- 相关矩阵热图
- 显著性检验

### 模块4：因子分析 (Factor Analysis)
- 探索性因子分析(EFA)
- 信度分析(Cronbach's α)
- 碎石图
- 因子载荷矩阵

### 模块5：聚类分析 (Cluster Analysis)
- K-means聚类
- 最优聚类数确定
- 聚类轮廓分析
- 用户画像生成

### 模块6：回归分析 (Regression Analysis)
- 多元线性回归
- 影响因素识别
- 模型诊断
- 结果可视化

## 📈 输出示例

### 相关矩阵热图
![correlation](outputs/figures/correlation_heatmap.png)

### 聚类分析结果
![clustering](outputs/figures/cluster_profile.png)

### 回归系数图
![regression](outputs/figures/regression_coef.png)

## 🎓 适用场景

- **学术研究**：心理学、管理学、社会学问卷研究
- **市场调研**：用户满意度、品牌认知、消费行为
- **产品研究**：用户体验、需求分析、功能评估
- **政策评估**：公共服务满意度、政策效果评估
- **人力资源**：员工满意度、组织氛围调查

## 📚 方法论文档

详细的统计方法说明请查看：
- [分析方法论](docs/methodology.md)
- [数据质量控制](docs/quality_control.md)
- [可视化最佳实践](docs/visualization.md)

## 🛠️ 技术栈

- **语言**：R 4.0+
- **核心包**：tidyverse, psych, ggplot2
- **统计方法**：描述统计、相关分析、因子分析、聚类、回归
- **可视化**：ggplot2, corrplot, pheatmap

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📝 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 👨‍💻 作者

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- 知乎/CSDN/个人博客链接

## 🌟 如果这个项目对你有帮助，请给个Star！

## 📮 联系方式

- 技术咨询/商业合作：your.email@example.com
- 问卷数据分析服务：提供专业的数据分析咨询

---

**注**：本项目使用模拟数据进行演示，不涉及任何真实个人信息。
