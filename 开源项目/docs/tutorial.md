# 🎓 使用教程：从零开始的问卷数据分析

## 第一步：准备你的数据

### 1.1 数据格式要求

你的Excel文件应该是这样的结构：

| ID | Q1_性别 | Q2_年龄 | Q3_满意度1 | Q3_满意度2 | Q3_满意度3 | ... |
|----|---------|---------|-----------|-----------|-----------|-----|
| 1  | 1       | 22      | 4         | 5         | 4         | ... |
| 2  | 2       | 21      | 3         | 3         | 4         | ... |

**关键要求：**
- ✅ 第一行是变量名
- ✅ 每一列是一个问题
- ✅ 每一行是一个受访者
- ✅ 数值编码清晰（如：1=男，2=女）

### 1.2 创建数据字典

创建 `data_dictionary.xlsx`，包含以下列：

| 变量名 | 题目内容 | 类型 | 编码说明 |
|--------|---------|------|---------|
| Q1 | 您的性别 | 分类 | 1=男,2=女 |
| Q2 | 您的年龄 | 连续 | 实际年龄 |
| Q3_1 | 我对产品很满意 | Likert | 1-5分 |

## 第二步：数据清洗

### 2.1 运行清洗脚本

```r
# 加载必要的包
library(tidyverse)
library(openxlsx)

# 读取数据
raw_data <- read.xlsx("demo_data/raw_survey.xlsx")

# 查看数据结构
str(raw_data)
head(raw_data)

# 运行清洗脚本
source("code/01_data_cleaning.R")
```

### 2.2 清洗步骤说明

```r
# 步骤1：删除测试数据
data_clean <- raw_data %>%
  filter(!grepl("测试|test", 姓名, ignore.case = TRUE))

# 步骤2：答题时长过滤
data_clean <- data_clean %>%
  filter(答题时长 >= 120 & 答题时长 <= 1800)  # 2-30分钟

# 步骤3：注意力检查题
# 假设Q10是"请选择'非常同意'"
data_clean <- data_clean %>%
  filter(Q10 == 5)

# 步骤4：直线作答检测
likert_cols <- paste0("Q", 3:15)  # Likert题项
data_clean <- data_clean %>%
  mutate(sd_likert = apply(select(., all_of(likert_cols)), 1, sd, na.rm=TRUE)) %>%
  filter(sd_likert > 0.5)

# 步骤5：缺失值处理
data_clean <- data_clean %>%
  filter(rowSums(is.na(.)) / ncol(.) < 0.3)  # 删除缺失>30%的样本

# 保存清洗后数据
write.xlsx(data_clean, "outputs/cleaned_data.xlsx")
```

### 2.3 生成数据质量报告

```r
# 样本量变化
cat("原始样本:", nrow(raw_data), "\n")
cat("清洗后样本:", nrow(data_clean), "\n")
cat("保留率:", round(nrow(data_clean)/nrow(raw_data)*100, 1), "%\n")

# 缺失值统计
missing_summary <- data_clean %>%
  summarise(across(everything(), ~sum(is.na(.))/n()*100))
```

## 第三步：描述性统计

### 3.1 样本基本特征

```r
source("code/02_descriptive.R")

# 性别分布
table(data_clean$性别)
prop.table(table(data_clean$性别)) * 100

# 年龄描述
summary(data_clean$年龄)
sd(data_clean$年龄, na.rm=TRUE)

# 可视化
library(ggplot2)

# 年龄分布直方图
ggplot(data_clean, aes(x=年龄)) +
  geom_histogram(binwidth=1, fill="steelblue", color="white") +
  theme_minimal() +
  labs(title="年龄分布", x="年龄", y="频数")
```

### 3.2 各维度描述统计

```r
library(psych)

# 选择Likert量表题项
likert_items <- data_clean %>% select(Q3_1:Q3_10)

# 描述统计
desc_stats <- describe(likert_items)
print(desc_stats)

# 保存结果
write.csv(desc_stats, "outputs/tables/descriptive_stats.csv")
```

## 第四步：相关分析

### 4.1 计算相关矩阵

```r
source("code/03_correlation.R")

# 计算Pearson相关
cor_matrix <- cor(likert_items, use="pairwise.complete.obs")

# 显著性检验
cor_test <- corr.test(likert_items)
print(cor_test, short=FALSE)
```

### 4.2 可视化相关矩阵

```r
library(corrplot)

# 方法1：圆圈图
corrplot(cor_matrix, method="circle", type="upper",
         tl.col="black", tl.srt=45,
         addCoef.col="black", number.cex=0.7)

# 方法2：热图
library(pheatmap)
pheatmap(cor_matrix, 
         display_numbers = TRUE,
         number_format = "%.2f",
         fontsize_number = 8,
         cluster_rows = FALSE,
         cluster_cols = FALSE)
```

## 第五步：因子分析

### 5.1 适用性检验

```r
source("code/04_factor_analysis.R")

# KMO检验
KMO(likert_items)

# Bartlett球形检验
cortest.bartlett(cor(likert_items), n=nrow(likert_items))
```

### 5.2 确定因子数

```r
# 方法1：特征值>1
eigen_values <- eigen(cor(likert_items))$values
sum(eigen_values > 1)

# 方法2：碎石图
scree(likert_items, factors=FALSE)

# 方法3：平行分析
fa.parallel(likert_items, fa="fa")
```

### 5.3 提取因子

```r
# 提取3个因子，使用Varimax旋转
fa_result <- fa(likert_items, nfactors=3, rotate="varimax", fm="ml")

# 查看因子载荷
print(fa_result$loadings, cutoff=0.3)

# 可视化
fa.diagram(fa_result)
```

### 5.4 信度分析

```r
# 假设因子1包含Q3_1到Q3_4
factor1_items <- data_clean %>% select(Q3_1:Q3_4)
alpha_result <- alpha(factor1_items)
print(alpha_result)
```

## 第六步：聚类分析

### 6.1 确定聚类数

```r
source("code/05_clustering.R")

library(factoextra)

# 肘部法则
fviz_nbclust(likert_items, kmeans, method="wss") +
  labs(title="肘部法则")

# 轮廓系数法
fviz_nbclust(likert_items, kmeans, method="silhouette") +
  labs(title="轮廓系数法")
```

### 6.2 执行K-means聚类

```r
# 假设选择3个类别
set.seed(123)
kmeans_result <- kmeans(scale(likert_items), centers=3, nstart=25)

# 添加聚类标签到数据
data_clean$cluster <- kmeans_result$cluster

# 聚类大小
table(kmeans_result$cluster)
```

### 6.3 聚类特征分析

```r
# 各类别在各维度的均值
cluster_profile <- data_clean %>%
  group_by(cluster) %>%
  summarise(across(Q3_1:Q3_10, mean, na.rm=TRUE))

# 可视化
fviz_cluster(kmeans_result, data=likert_items,
             palette="jco", 
             ellipse.type="convex",
             ggtheme=theme_minimal())
```

## 第七步：回归分析

### 7.1 构建回归模型

```r
source("code/06_regression.R")

# 假设预测总体满意度
model <- lm(总体满意度 ~ 性别 + 年龄 + Q3_1 + Q3_2 + Q3_3, 
            data=data_clean)

# 查看结果
summary(model)
```

### 7.2 模型诊断

```r
# 残差图
par(mfrow=c(2,2))
plot(model)

# VIF检验
library(car)
vif(model)

# Durbin-Watson检验
durbinWatsonTest(model)
```

### 7.3 结果可视化

```r
# 系数图
library(coefplot)
coefplot(model, intercept=FALSE, 
         title="回归系数及95%置信区间")

# 或使用ggplot2
library(broom)
tidy_model <- tidy(model, conf.int=TRUE) %>%
  filter(term != "(Intercept)")

ggplot(tidy_model, aes(x=estimate, y=term)) +
  geom_point() +
  geom_errorbarh(aes(xmin=conf.low, xmax=conf.high), height=0.2) +
  geom_vline(xintercept=0, linetype="dashed", color="red") +
  theme_minimal() +
  labs(title="回归系数图", x="系数估计值", y="")
```

## 第八步：生成报告

### 8.1 使用R Markdown

创建 `analysis_report.Rmd`：

````markdown
---
title: "问卷数据分析报告"
author: "Your Name"
date: "`r Sys.Date()`"
output: 
  html_document:
    toc: true
    toc_float: true
    theme: cosmo
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo=FALSE, message=FALSE, warning=FALSE)
library(tidyverse)
library(knitr)
```

# 1. 研究背景

# 2. 样本特征

```{r}
# 插入描述统计表
```

# 3. 主要发现

## 3.1 相关分析

```{r}
# 插入相关矩阵图
```

## 3.2 因子分析

## 3.3 聚类分析

## 3.4 回归分析

# 4. 结论与建议
````

### 8.2 渲染报告

```r
rmarkdown::render("analysis_report.Rmd")
```

## 常见问题 FAQ

### Q1: 数据量太小怎么办？
A: 因子分析至少需要100个样本，回归分析建议样本量>10*变量数

### Q2: 数据不符合正态分布？
A: 可以使用非参数方法（Spearman相关、Mann-Whitney检验等）

### Q3: 如何处理多重共线性？
A: 删除VIF>10的变量，或使用主成分回归、岭回归

### Q4: 聚类数如何确定？
A: 综合考虑肘部法则、轮廓系数和实际业务意义

### Q5: 如何报告统计结果？
A: 参考APA格式，包含统计量、自由度、p值、效应量

## 下一步学习

- 📚 [方法论详解](methodology.md)
- 🎨 [可视化最佳实践](visualization.md)
- 💡 [高级分析技巧](advanced_techniques.md)

---

**有问题？** 提交Issue或发邮件到 your.email@example.com
