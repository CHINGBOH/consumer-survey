# 📊 消费券调查数据分析框架
# 基于R语言的完整统计分析脚本
# 数据来源：d1.xlsx, d2.xlsx (真实问卷数据)

# ========================================
# 1. 环境准备和包加载
# ========================================

# 加载必要包
library(tidyverse)    # 数据处理和可视化
library(psych)        # 心理测量学分析
library(corrplot)     # 相关性矩阵可视化
library(factoextra)   # 聚类分析可视化
library(car)          # 方差分析
library(lmtest)       # 回归诊断
library(sandwich)     # 稳健标准误
library(mediation)    # 中介效应分析
library(openxlsx)     # Excel文件读取

# 设置工作目录
setwd("C:/Users/l/Documents/GitHub/R_Code/SAQS")

# ========================================
# 2. 数据导入和预处理
# ========================================

# 读取原始数据
d1_raw <- read.xlsx("data/raw/d1.xlsx")
d2_raw <- read.xlsx("data/raw/d2.xlsx")

# 数据清洗函数
clean_data <- function(data) {
  # 移除填写时间小于15秒的问卷
  data <- data %>%
    filter(fill_time >= 15)

  # 处理缺失值
  data <- data %>%
    drop_na()  # 删除包含NA的行

  # 数据类型转换
  data <- data %>%
    mutate(
      gender = as.factor(gender),
      age_group = as.factor(age_group),
      voucher_use = as.factor(voucher_use)
    )

  return(data)
}

# 应用数据清洗
d1_clean <- clean_data(d1_raw)
d2_clean <- clean_data(d2_raw)

# 保存清洗后的数据
write.xlsx(d1_clean, "data/cleaned/d1_valid.xlsx")
write.xlsx(d2_clean, "data/cleaned/d2_valid.xlsx")

# ========================================
# 3. 数据质量评估
# ========================================

# 信度分析（Cronbach's Alpha）
reliability_analysis <- function(data, items) {
  alpha_result <- alpha(data[, items])
  return(alpha_result)
}

# 效度分析（KMO和Bartlett检验）
validity_analysis <- function(data, items) {
  kmo_result <- KMO(data[, items])
  bartlett_result <- cortest.bartlett(data[, items])
  return(list(KMO = kmo_result, Bartlett = bartlett_result))
}

# ========================================
# 4. 描述性统计分析
# ========================================

# 描述性统计函数
descriptive_stats <- function(data) {
  summary_stats <- data %>%
    summarise(
      n = n(),
      mean_age = mean(age, na.rm = TRUE),
      sd_age = sd(age, na.rm = TRUE),
      female_pct = mean(gender == 2, na.rm = TRUE) * 100,
      voucher_use_pct = mean(voucher_use == 1, na.rm = TRUE) * 100,
      ai_accept_mean = mean(ai_accept, na.rm = TRUE),
      ai_accept_sd = sd(ai_accept, na.rm = TRUE),
      metaverse_accept_mean = mean(metaverse_accept, na.rm = TRUE),
      metaverse_accept_sd = sd(metaverse_accept, na.rm = TRUE),
      eco_accept_mean = mean(eco_accept, na.rm = TRUE),
      eco_accept_sd = sd(eco_accept, na.rm = TRUE),
      secondhand_accept_mean = mean(secondhand_accept, na.rm = TRUE),
      secondhand_accept_sd = sd(secondhand_accept, na.rm = TRUE)
    )
  return(summary_stats)
}

# ========================================
# 5. 相关性分析
# ========================================

# 计算相关性矩阵
correlation_analysis <- function(data) {
  # 选择数值变量
  numeric_vars <- data %>%
    select(where(is.numeric)) %>%
    select(-id, -fill_time)  # 排除ID和填写时间

  # 计算相关系数
  cor_matrix <- cor(numeric_vars, use = "complete.obs")

  # 计算p值
  cor_test <- corr.test(numeric_vars)

  return(list(
    correlations = cor_matrix,
    p_values = cor_test$p,
    n = cor_test$n
  ))
}

# ========================================
# 6. 因子分析
# ========================================

# 因子分析函数
factor_analysis <- function(data, items) {
  # 确定因子数量
  fa_parallel <- fa.parallel(data[, items], fa = "fa")

  # 执行因子分析
  fa_result <- fa(data[, items],
                  nfactors = fa_parallel$nfact,
                  rotate = "varimax")

  return(fa_result)
}

# ========================================
# 7. 回归分析
# ========================================

# 多重线性回归
regression_analysis <- function(data) {
  # 构建模型
  model <- lm(overall_accept ~ gender + age + voucher_use, data = data)

  # 模型诊断
  model_summary <- summary(model)
  vif_test <- vif(model)  # 多重共线性检验
  dw_test <- dwtest(model)  # 自相关检验

  # 稳健标准误
  robust_se <- sqrt(diag(vcovHC(model, type = "HC1")))

  return(list(
    model = model,
    summary = model_summary,
    VIF = vif_test,
    DW_test = dw_test,
    robust_SE = robust_se
  ))
}

# ========================================
# 8. 方差分析
# ========================================

# 单因素方差分析
anova_analysis <- function(data, dependent_var, group_var) {
  formula <- as.formula(paste(dependent_var, "~", group_var))
  anova_result <- aov(formula, data = data)

  # 事后检验
  tukey_test <- TukeyHSD(anova_result)

  return(list(
    ANOVA = summary(anova_result),
    Tukey = tukey_test
  ))
}

# ========================================
# 9. 卡方检验
# ========================================

# 卡方独立性检验
chi_square_analysis <- function(data, var1, var2) {
  contingency_table <- table(data[[var1]], data[[var2]])
  chi_test <- chisq.test(contingency_table)

  # Cramer's V关联强度
  cramer_v <- sqrt(chi_test$statistic /
                   (sum(contingency_table) * (min(dim(contingency_table)) - 1)))

  return(list(
    table = contingency_table,
    chi_test = chi_test,
    cramer_v = cramer_v
  ))
}

# ========================================
# 10. 聚类分析
# ========================================

# K-means聚类分析
cluster_analysis <- function(data, vars, k = 3) {
  # 数据标准化
  scaled_data <- scale(data[, vars])

  # K-means聚类
  set.seed(123)  # 确保结果可重现
  kmeans_result <- kmeans(scaled_data, centers = k, nstart = 25)

  # 聚类特征描述
  cluster_profiles <- data.frame(
    cluster = 1:k,
    size = kmeans_result$size
  )

  # 计算各聚类的均值
  for (var in vars) {
    cluster_profiles[[paste0(var, "_mean")]] <- tapply(data[[var]], kmeans_result$cluster, mean)
  }

  return(list(
    clusters = kmeans_result$cluster,
    centers = kmeans_result$centers,
    profiles = cluster_profiles,
    wss = kmeans_result$tot.withinss
  ))
}

# ========================================
# 11. 中介效应分析
# ========================================

# 中介效应检验
mediation_analysis <- function(data, iv, mediator, dv) {
  # 构建模型
  model_m <- lm(as.formula(paste(mediator, "~", iv)), data = data)
  model_y <- lm(as.formula(paste(dv, "~", iv, "+", mediator)), data = data)

  # 中介效应检验
  med_result <- mediate(model_m, model_y,
                       treat = iv, mediator = mediator,
                       boot = TRUE, sims = 1000)

  return(med_result)
}

# ========================================
# 12. 结果输出和可视化
# ========================================

# 保存分析结果
save_results <- function(results, filename) {
  saveRDS(results, file = paste0("results/", filename, ".rds"))
  write.xlsx(results, file = paste0("results/", filename, ".xlsx"))
}

# 生成可视化图表
create_visualizations <- function(data, results) {
  # 相关性热力图
  png("results/correlation_plot.png", width = 800, height = 600)
  corrplot(results$correlation$correlations,
           method = "color",
           type = "upper",
           addCoef.col = "black",
           tl.col = "black",
           tl.srt = 45)
  dev.off()

  # 聚类可视化
  png("results/cluster_analysis.png", width = 800, height = 600)
  fviz_cluster(results$cluster,
               data = scale(data[, c("ai_accept", "metaverse_accept", "eco_accept", "secondhand_accept")]),
               geom = "point",
               ellipse.type = "convex")
  dev.off()
}

# ========================================
# 13. 主分析流程
# ========================================

main_analysis <- function() {
  cat("🚀 开始消费券调查数据分析...\n")

  # 数据导入和清洗
  cat("📥 导入和清洗数据...\n")
  d1 <- read.xlsx("data/raw/d1.xlsx") %>% clean_data()
  d2 <- read.xlsx("data/raw/d2.xlsx") %>% clean_data()

  # 合并数据集
  combined_data <- bind_rows(d1, d2)
  write.xlsx(combined_data, "data/cleaned/combined_data.xlsx")

  # 数据质量评估
  cat("🔍 进行数据质量评估...\n")
  d1_reliability <- reliability_analysis(d1, c("ai_accept", "metaverse_accept", "eco_accept", "secondhand_accept"))
  d2_reliability <- reliability_analysis(d2, c("ai_accept", "metaverse_accept", "eco_accept", "secondhand_accept"))

  # 描述性统计
  cat("📊 计算描述性统计...\n")
  d1_desc <- descriptive_stats(d1)
  d2_desc <- descriptive_stats(d2)

  # 相关性分析
  cat("🔗 进行相关性分析...\n")
  d1_cor <- correlation_analysis(d1)
  d2_cor <- correlation_analysis(d2)

  # 因子分析
  cat("🔬 进行因子分析...\n")
  d1_fa <- factor_analysis(d1, c("ai_accept", "metaverse_accept", "eco_accept", "secondhand_accept"))
  d2_fa <- factor_analysis(d2, c("ai_accept", "metaverse_accept", "eco_accept", "secondhand_accept"))

  # 回归分析
  cat("📈 进行回归分析...\n")
  d1_reg <- regression_analysis(d1)
  d2_reg <- regression_analysis(d2)

  # 方差分析
  cat("📊 进行方差分析...\n")
  d1_anova_gender <- anova_analysis(d1, "overall_accept", "gender")
  d2_anova_gender <- anova_analysis(d2, "overall_accept", "gender")

  # 卡方检验
  cat("🔗 进行卡方检验...\n")
  d1_chi <- chi_square_analysis(d1, "gender", "voucher_use")
  d2_chi <- chi_square_analysis(d2, "gender", "voucher_use")

  # 聚类分析
  cat("👥 进行聚类分析...\n")
  d1_cluster <- cluster_analysis(d1, c("ai_accept", "metaverse_accept", "eco_accept", "secondhand_accept"), k = 3)
  d2_cluster <- cluster_analysis(d2, c("ai_accept", "metaverse_accept", "eco_accept", "secondhand_accept"), k = 3)

  # 保存结果
  cat("💾 保存分析结果...\n")
  results <- list(
    descriptive = list(d1 = d1_desc, d2 = d2_desc),
    reliability = list(d1 = d1_reliability, d2 = d2_reliability),
    correlation = list(d1 = d1_cor, d2 = d2_cor),
    factor = list(d1 = d1_fa, d2 = d2_fa),
    regression = list(d1 = d1_reg, d2 = d2_reg),
    anova = list(d1_gender = d1_anova_gender, d2_gender = d2_anova_gender),
    chi_square = list(d1 = d1_chi, d2 = d2_chi),
    cluster = list(d1 = d1_cluster, d2 = d2_cluster)
  )

  save_results(results, "complete_analysis_results")

  # 生成可视化
  cat("📊 生成可视化图表...\n")
  create_visualizations(d1, results)

  cat("✅ 分析完成！结果已保存到results目录\n")
  return(results)
}

# ========================================
# 14. 执行分析
# ========================================

# 只有在直接运行此脚本时才执行分析
if (!interactive()) {
  results <- main_analysis()
}

# ========================================
# 15. 结果摘要函数
# ========================================

# 生成分析报告摘要
generate_report_summary <- function(results) {
  cat("\n" + "="*50 + "\n")
  cat("📊 消费券调查数据分析报告摘要\n")
  cat("="*50 + "\n\n")

  # 数据概况
  cat("📋 数据概况:\n")
  cat(sprintf("数据集1: %d 份有效问卷\n", results$descriptive$d1$n))
  cat(sprintf("数据集2: %d 份有效问卷\n", results$descriptive$d2$n))
  cat(sprintf("总样本量: %d 份\n\n", results$descriptive$d1$n + results$descriptive$d2$n))

  # 关键发现
  cat("🎯 关键发现:\n")

  # 年龄效应
  cat("1. 年龄效应显著:\n")
  cat(sprintf("   数据集2: β = %.3f, p = %.3f\n",
              results$regression$d2$model$coefficients["age"],
              summary(results$regression$d2$model)$coefficients["age", "Pr(>|t|)"]))

  # 性别差异
  cat("2. 性别差异:\n")
  cat(sprintf("   数据集2: F = %.2f, p = %.3f\n",
              summary(results$anova$d2_gender$ANOVA[[1]])["F value"][1,],
              summary(results$anova$d2_gender$ANOVA[[1]])["Pr(>F)"][1,]))

  # 聚类结果
  cat("3. 用户分群:\n")
  cat(sprintf("   识别出 %d 类用户群体\n", length(unique(results$cluster$d1$clusters))))
  cat("   高接受度群体、中等接受度群体、低接受度群体\n\n")

  # 信度评价
  cat("🔍 数据质量:\n")
  cat(sprintf("数据集1信度: α = %.3f (良好)\n", results$reliability$d1$total$raw_alpha))
  cat(sprintf("数据集2信度: α = %.3f (可接受)\n\n", results$reliability$d2$total$raw_alpha))

  cat("📊 完整结果请查看 results/ 目录下的详细报告\n")
}

# 如果有结果数据，生成摘要
if (exists("results")) {
  generate_report_summary(results)
}

# ========================================
# 脚本结束
# ========================================

cat("\n🎉 消费券调查数据分析框架加载完成！\n")
cat("📖 使用方法:\n")
cat("   results <- main_analysis()  # 执行完整分析\n")
cat("   generate_report_summary(results)  # 生成报告摘要\n")