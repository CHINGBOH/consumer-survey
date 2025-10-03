# 📊 消费行为调查数据分析脚本
# ======================================

# 加载必要的包
library(tidyverse)
library(ggplot2)
library(psych)
library(corrplot)
library(cluster)
library(factoextra)

# 设置工作目录（根据实际情况修改）
# setwd("C:/Users/l/Documents/GitHub/SurveyAnalysis")

# ======================================
# 1. 数据导入和预处理
# ======================================

# 读取数据
raw_data <- read_csv("data/sample_survey_data.csv")

# 数据概览
cat("数据基本信息：\n")
cat("样本量：", nrow(raw_data), "\n")
cat("变量数：", ncol(raw_data), "\n")
glimpse(raw_data)

# 数据预处理
processed_data <- raw_data %>%
  mutate(
    # 年龄分组
    age_group = cut(age,
                   breaks = c(0, 20, 25, 30, 100),
                   labels = c("18-20", "21-25", "26-30", "30+")),

    # 收入水平转换为数值
    income_numeric = case_when(
      monthly_income == "3000-5000" ~ 4000,
      monthly_income == "5000-8000" ~ 6500,
      monthly_income == "8000以上" ~ 10000,
      TRUE ~ 4000
    ),

    # 购物频率转换为数值
    shopping_freq_numeric = case_when(
      shopping_frequency == "经常" ~ 5,
      shopping_frequency == "偶尔" ~ 3,
      TRUE ~ 1
    )
  )

# ======================================
# 2. 描述性统计分析
# ======================================

# 基本统计量
summary_stats <- processed_data %>%
  summarise(
    n = n(),
    mean_age = mean(age, na.rm = TRUE),
    sd_age = sd(age, na.rm = TRUE),
    female_prop = mean(gender == "女"),
    high_edu_prop = mean(education %in% c("本科学历", "研究生"))
  )

print("描述性统计结果：")
print(summary_stats)

# 分类变量频数统计
gender_dist <- processed_data %>% count(gender)
education_dist <- processed_data %>% count(education)
income_dist <- processed_data %>% count(monthly_income)

# ======================================
# 3. 数据可视化
# ======================================

# 年龄分布直方图
age_plot <- ggplot(processed_data, aes(x = age)) +
  geom_histogram(binwidth = 2, fill = "#4CAF50", color = "white", alpha = 0.8) +
  theme_minimal() +
  labs(title = "受访者年龄分布",
       x = "年龄", y = "频数")

# 性别比例饼图
gender_pie <- processed_data %>%
  count(gender) %>%
  mutate(prop = n / sum(n) * 100) %>%
  ggplot(aes(x = "", y = prop, fill = gender)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  theme_void() +
  geom_text(aes(label = paste0(round(prop, 1), "%")),
            position = position_stack(vjust = 0.5)) +
  labs(title = "性别比例分布") +
  scale_fill_manual(values = c("#2196F3", "#E91E63"))

# 消费决策因素雷达图数据准备
decision_factors <- processed_data %>%
  summarise(
    价格敏感度 = mean(price_sensitivity),
    品牌重要性 = mean(brand_importance),
    服务重要性 = mean(service_importance)
  ) %>%
  pivot_longer(everything(), names_to = "factor", values_to = "score")

# ======================================
# 4. 相关性分析
# ======================================

# 选择数值变量进行相关性分析
numeric_vars <- processed_data %>%
  select(age, income_numeric, shopping_freq_numeric,
         price_sensitivity, brand_importance, service_importance)

# 计算相关系数矩阵
cor_matrix <- cor(numeric_vars, use = "complete.obs")

# 输出相关系数
print("相关性矩阵：")
print(round(cor_matrix, 3))

# 可视化相关性矩阵
corrplot(cor_matrix,
         method = "color",
         type = "upper",
         addCoef.col = "black",
         tl.col = "black",
         title = "消费行为相关性分析")

# ======================================
# 5. 假设检验
# ======================================

# t检验：性别与消费金额差异
t_test_age <- t.test(age ~ gender, data = processed_data)
print("性别与年龄差异t检验：")
print(t_test_age)

# t检验：性别与价格敏感度差异
t_test_price <- t.test(price_sensitivity ~ gender, data = processed_data)
print("性别与价格敏感度差异t检验：")
print(t_test_price)

# 方差分析：年龄组与消费频率差异
anova_result <- aov(shopping_freq_numeric ~ age_group, data = processed_data)
print("年龄组与消费频率方差分析：")
summary(anova_result)

# ======================================
# 6. 聚类分析
# ======================================

# 准备聚类数据
cluster_data <- processed_data %>%
  select(price_sensitivity, brand_importance, service_importance) %>%
  scale()

# 确定最佳聚类数
fviz_nbclust(cluster_data, kmeans, method = "wss") +
  labs(title = "肘部法确定聚类数")

# K-means聚类（假设3个聚类）
set.seed(123)
kmeans_result <- kmeans(cluster_data, centers = 3, nstart = 25)

# 添加聚类标签
clustered_data <- processed_data %>%
  mutate(cluster = as.factor(kmeans_result$cluster))

# 聚类可视化
fviz_cluster(kmeans_result, data = cluster_data,
             geom = "point",
             ellipse.type = "convex",
             ggtheme = theme_minimal()) +
  labs(title = "消费行为聚类分析")

# 聚类特征分析
cluster_profile <- clustered_data %>%
  group_by(cluster) %>%
  summarise(
    n = n(),
    mean_age = mean(age),
    female_prop = mean(gender == "女"),
    mean_price_sens = mean(price_sensitivity),
    mean_brand_imp = mean(brand_importance),
    mean_service_imp = mean(service_importance)
  )

print("聚类特征分析：")
print(cluster_profile)

# ======================================
# 7. 因子分析
# ======================================

# 因子分析
fa_result <- fa(processed_data[, c("price_sensitivity", "brand_importance", "service_importance")],
                nfactors = 2, rotate = "varimax")

print("因子分析结果：")
print(fa_result)

# 因子载荷图
fa.diagram(fa_result, main = "消费决策因素因子分析")

# ======================================
# 8. 回归分析
# ======================================

# 多元线性回归：预测价格敏感度
regression_model <- lm(price_sensitivity ~ age + gender + education + income_numeric,
                       data = processed_data)

print("多元回归分析结果：")
summary(regression_model)

# 模型诊断图
par(mfrow = c(2, 2))
plot(regression_model)

# ======================================
# 9. 保存分析结果
# ======================================

# 保存处理后的数据
write_csv(processed_data, "data/processed_survey_data.csv")

# 保存统计结果
write_csv(cluster_profile, "results/cluster_analysis_results.csv")

# 保存相关性矩阵
write.csv(cor_matrix, "results/correlation_matrix.csv")

# ======================================
# 10. 生成分析报告
# ======================================

# 使用 RMarkdown 生成报告（如果需要）
# rmarkdown::render("analysis_report.Rmd",
#                   output_file = "消费行为分析报告.html")

cat("\n🎉 数据分析完成！\n")
cat("结果文件已保存到 results/ 目录\n")
cat("可视化图表请查看 RStudio 的 Plots 面板\n")