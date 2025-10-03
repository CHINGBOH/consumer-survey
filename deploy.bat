@echo off
echo 🚀 消费行为调查分析平台 - 部署脚本
echo ======================================

REM 检查 Hugo 是否安装
hugo version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Hugo 未安装，请先安装 Hugo：
    echo    choco install hugo
    echo    或者从 https://github.com/gohugoio/hugo/releases 下载
    pause
    exit /b 1
)

REM 检查 Quarto 是否安装
quarto --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Quarto 未安装，请从 https://quarto.org/docs/get-started/ 下载
    pause
    exit /b 1
)

echo ✅ 环境检查通过
echo.

echo 📦 正在生成网站...
echo.

REM 清理旧的构建文件
if exist "public" rmdir /s /q "public"
if exist "docs" rmdir /s /q "docs"

REM 使用 Quarto 渲染网站
echo 正在使用 Quarto 渲染...
quarto render

if %errorlevel% neq 0 (
    echo ❌ Quarto 渲染失败
    pause
    exit /b 1
)

echo ✅ 网站生成成功！
echo.

echo 🌐 本地预览：
echo    运行以下命令启动本地服务器：
echo    hugo server
echo.

echo 📤 部署选项：
echo    1. GitHub Pages: 将 docs/ 文件夹推送到 GitHub
echo    2. Netlify: 拖拽 docs/ 文件夹到 Netlify 控制台
echo    3. Vercel: 连接 GitHub 仓库自动部署
echo.

echo 🎉 部署脚本执行完成！
echo    生成的文件位于 docs/ 文件夹中

pause