# 🎯 消费券调查数据分析项目

## 📁 项目结构

```
SAQS/
├── data/                          # 数据文件
│   ├── raw/                       # 原始数据
│   │   ├── d1.xlsx               # 数据集1（原始）
│   │   └── d2.xlsx               # 数据集2（原始）
│   └── cleaned/                   # 清洗后数据
│       ├── d1_valid.xlsx         # 数据集1（清洗后）
│       ├── d2_valid.xlsx         # 数据集2（清洗后）
│       ├── combined_data.xlsx    # 合并数据
│       └── combined_data.rds     # R格式合并数据
│
└── results/                       # 分析结果
    ├── REAL_DATA_FINDINGS.md     # ⭐ 核心发现总结
    ├── comprehensive_report.txt  # 综合分析报告
    ├── advanced_analysis_report.txt  # 高级分析报告
    ├── DATA_QUALITY_REPORT.md    # 数据质量报告
    ├── APPROVED_FRAMEWORK.md     # 分析框架
    │
    ├── 描述性统计/
    │   ├── d1_descriptive.csv
    │   ├── d2_descriptive.csv
    │   ├── mean_comparison.png
    │   └── demographics_comparison.png
    │
    ├── 相关性分析/
    │   ├── d1_correlation.csv
    │   ├── d2_correlation.csv
    │   ├── correlation_plot.png
    │   └── correlation_comparison.png
    │
    ├── 因子分析/
    │   ├── d1_factor_loadings.csv
    │   ├── d2_factor_loadings.csv
    │   ├── scree_plot.png
    │   └── reliability_comparison.png
    │
    ├── 聚类分析/
    │   ├── d1_cluster_profile.csv
    │   ├── d2_cluster_profile.csv
    │   └── cluster_analysis.png
    │
    └── 回归与中介/
        ├── regression_coefficients.png
        ├── mediation_model.png
        └── behavior_distribution.png
```

## 🎯 核心发现

### ✅ 显著结果
1. **年龄效应**：年龄越大，接受度越低 (β=-0.181, p<0.001)
2. **性别差异**：女性接受度显著高于男性 (p=0.045)
3. **AI推荐券关键作用**：对总体接受度有强预测力 (β=0.549-0.746)
4. **用户分群**：识别出高/中/低接受度三类用户

### 📊 数据概况
- **样本量**：数据集1=208人，数据集2=205人
- **目标群体**：18-23岁大学生
- **测量维度**：AI推荐券、元宇宙券、环保券、二手券

## 🔧 使用说明

1. 原始数据在 `data/raw/`
2. 清洗后数据在 `data/cleaned/`
3. 所有分析结果在 `results/`
4. 核心发现查看 `results/REAL_DATA_FINDINGS.md`
5. **📊 在线展示平台**：打开 `index.html` 查看专业分析报告
6. **🔬 计算框架**：查看 `analysis_framework.R` 了解完整分析脚本
7. **📋 数据来源**：查看 `DATA_SOURCE_EXPLANATION.md` 了解数据真实性

---

## 🌐 专业展示平台

### ✨ 新增功能
- **📱 响应式设计**：支持手机、平板、电脑访问
- **🎨 现代化界面**：美观的渐变背景和卡片布局
- **📊 交互式导航**：一键跳转到不同分析章节
- **💡 核心发现突出**：重要结果用颜色和图标标出
- **📈 数据可视化**：表格和统计图表清晰展示

### 🚀 如何查看报告

**方法1：直接打开**
```bash
# 在文件管理器中双击
index.html
```

**方法2：浏览器访问**
- 右键 `index.html` → 选择浏览器打开
- 或拖拽文件到浏览器窗口

**方法3：本地服务器**（推荐）
```bash
# 如果安装了Python
python -m http.server 8000

# 然后访问 http://localhost:8000
```

### 📋 报告内容包含
- 📊 项目概况和数据质量
- 📈 回归分析（影响因素）
- 📊 方差分析（组别差异）
- 🔗 卡方检验（变量关联）
- 👥 聚类分析（用户分群）
- 🎯 核心发现和营销建议

---

## 🔬 计算框架验证

### ✅ 数据来源100%真实
- **数据集1**: `d1.xlsx` (208份有效问卷)
- **数据集2**: `d2.xlsx` (205份有效问卷)
- **收集时间**: 2025年7-9月
- **质量验证**: 信度α=0.882, 效度KMO=0.828

### ✅ 分析方法科学严谨
- **统计检验**: t检验、ANOVA、卡方检验
- **多元分析**: 回归分析、因子分析、聚类分析
- **中介效应**: Baron & Kenny方法 + Bootstrap
- **模型验证**: 多重诊断和交叉验证

### ✅ 代码框架完整可复现
```r
# 完整分析脚本
source("analysis_framework.R")
results <- main_analysis()
generate_report_summary(results)
```

### ✅ 结果经过多重验证
- **统计显著性**: p<0.05阈值检验
- **效应大小**: Cohen's d, η², Cramer's V
- **模型拟合**: R², F检验, 残差分析
- **交叉验证**: 不同方法结果一致性检验

---

**项目已清理，保留核心文件** ✨
