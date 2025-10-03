# Netlify 自定义域名配置指南

## 📋 配置步骤

### 1. 登录Netlify
访问 https://netlify.com 登录你的账号

### 2. 选择网站项目
点击你的调研网站项目 (deft-moxie-85aa8a)

### 3. 添加自定义域名
1. 点击 **Site settings**
2. 点击 **Domain management**
3. 在 **Custom domains** 部分点击 **Add custom domain**
4. 输入域名：`chuning.cn`
5. 点击 **Verify**

### 4. 配置DNS
Netlify会显示需要配置的DNS记录：

**添加CNAME记录：**
- 主机记录：`www` (或 `@` 如果不需要www)
- 记录类型：`CNAME`
- 记录值：你的Netlify域名 (如 `deft-moxie-85aa8a.netlify.app`)

**或者添加A记录：**
- 主机记录：`@`
- 记录类型：`A`
- 记录值：Netlify提供的IP地址

### 5. 等待生效
DNS配置通常需要5-30分钟生效

## 🔧 DNS配置示例

在你的域名服务商处添加以下记录：

```
类型: CNAME
主机: @
值: deft-moxie-85aa8a.netlify.app
TTL: 3600
```

## ✅ 配置完成后

- 主域名：`https://chuning.cn`
- WWW域名：`https://www.chuning.cn` (如果配置了)

## 🚨 注意事项

1. 确保域名 `chuning.cn` 已购买且在有效期内
2. DNS配置前请备份现有DNS记录
3. 如果域名在阿里云，配置特别简单

## 🆘 遇到问题？

如果配置过程中遇到问题：
1. 检查域名是否到期
2. 确认DNS记录是否正确添加
3. 等待24小时让DNS完全生效
4. 联系Netlify支持

配置完成后，你的调研网站将有专业域名：`https://chuning.cn`