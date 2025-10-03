# 消费者调研数据分析脚本
# 使用R语言进行数据处理和可视化

# 加载必要的包
library(dplyr)
library(ggplot2)

# 设置工作目录（根据实际情况调整）
setwd("C:/Users/l/Documents/GitHub/SurveyAnalysis")

# 1. 数据读取和预处理
# 假设调研数据存储在CSV文件中
survey_data <- read.csv("survey_responses.csv", stringsAsFactors = FALSE)

# 数据结构检查
str(survey_data)
summary(survey_data)

# 2. 数据清洗
clean_data <- survey_data %>%
  filter(!is.na(age) & !is.na(gender)) %>%  # 过滤缺失值
  mutate(
    age_group = cut(age, breaks = c(0, 25, 35, 45, 100),
                   labels = c("18-25", "26-35", "36-45", "46+")),
    satisfaction_level = factor(satisfaction,
                               levels = 1:5,
                               labels = c("很不满意", "不满意", "一般", "满意", "很满意"))
  )

# 3. 描述性统计
# 年龄分布
age_stats <- clean_data %>%
  group_by(age_group) %>%
  summarise(count = n(), percentage = n()/nrow(clean_data)*100)

print("年龄分布统计：")
print(age_stats)

# 性别分布
gender_stats <- clean_data %>%
  group_by(gender) %>%
  summarise(count = n(), percentage = n()/nrow(clean_data)*100)

print("性别分布统计：")
print(gender_stats)

# 4. 可视化分析

# 年龄段满意度分布
ggplot(clean_data, aes(x = age_group, fill = satisfaction_level)) +
  geom_bar(position = "fill") +
  scale_fill_brewer(palette = "RdYlGn") +
  labs(title = "不同年龄段用户满意度分布",
       x = "年龄段", y = "比例",
       fill = "满意度") +
  theme_minimal()

# 保存图表
ggsave("age_satisfaction_distribution.png", width = 8, height = 6)

# 性别满意度对比
ggplot(clean_data, aes(x = gender, fill = satisfaction_level)) +
  geom_bar(position = "dodge") +
  scale_fill_brewer(palette = "RdYlGn") +
  labs(title = "性别与满意度关系",
       x = "性别", y = "人数",
       fill = "满意度") +
  theme_minimal()

ggsave("gender_satisfaction_comparison.png", width = 8, height = 6)

# 5. 文本分析（评论数据）- 暂时跳过，需要安装额外包
# 假设有评论数据
# if(file.exists("comments.txt")) {
#   comments <- readLines("comments.txt", encoding = "UTF-8")
#   
#   # 创建语料库
#   corpus <- Corpus(VectorSource(comments))
#   
#   # 文本预处理
#   corpus <- corpus %>%
#     tm_map(content_transformer(tolower)) %>%
#     tm_map(removePunctuation) %>%
#     tm_map(removeNumbers) %>%
#     tm_map(removeWords, stopwords("chinese")) %>%  # 中文停用词
#     tm_map(stripWhitespace)
#   
#   # 创建词频矩阵
#   dtm <- DocumentTermMatrix(corpus)
#   freq <- colSums(as.matrix(dtm))
#   
#   # 生成词云
#   wordcloud2(data.frame(word = names(freq), freq = freq),
#              size = 0.5, color = "random-light", backgroundColor = "white")
# }# 6. 相关性分析
# 假设有数值变量
numeric_vars <- clean_data %>%
  select_if(is.numeric) %>%
  select(-age)  # 排除年龄，如果有其他数值变量

if(ncol(numeric_vars) > 1) {
  correlation_matrix <- cor(numeric_vars, use = "complete.obs")
  print("相关性矩阵：")
  print(correlation_matrix)
}

# 7. 输出结果
# 保存处理后的数据
write.csv(clean_data, "processed_survey_data.csv", row.names = FALSE)

# 生成总结报告
summary_report <- paste0(
  "调研数据分析报告\n\n",
  "总样本量：", nrow(clean_data), "\n",
  "男性比例：", round(gender_stats$percentage[gender_stats$gender == "男"], 1), "%\n",
  "女性比例：", round(gender_stats$percentage[gender_stats$gender == "女"], 1), "%\n",
  "平均年龄：", round(mean(clean_data$age, na.rm = TRUE), 1), "岁\n",
  "满意度均值：", round(mean(as.numeric(clean_data$satisfaction), na.rm = TRUE), 2), "\n\n",
  "详细分析结果请查看生成的图表文件。"
)

writeLines(summary_report, "survey_analysis_report.txt")

print("数据分析完成！请查看生成的图表和报告文件。")