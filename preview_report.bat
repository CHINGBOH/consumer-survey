@echo off
echo ========================================
echo   消费券调查数据分析报告展示平台
echo ========================================
echo.
echo 正在启动本地服务器...
echo 请在浏览器中访问: http://localhost:8000
echo.
echo 按 Ctrl+C 停止服务器
echo.

REM 检查Python是否可用
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo 使用Python启动服务器...
    python -m http.server 8000
) else (
    REM 检查Node.js是否可用
    node --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo 使用Node.js启动服务器...
        REM 创建临时server.js
        echo const http = require('http'); > temp_server.js
        echo const fs = require('fs'); >> temp_server.js
        echo const path = require('path'); >> temp_server.js
        echo const server = http.createServer((req, res) => { >> temp_server.js
        echo   let filePath = path.join(__dirname, req.url === '/' ? 'index.html' : req.url); >> temp_server.js
        echo   fs.readFile(filePath, (err, data) => { >> temp_server.js
        echo     if (err) { res.writeHead(404); res.end('File not found'); return; } >> temp_server.js
        echo     res.writeHead(200, {'Content-Type': req.url.endsWith('.html') ? 'text/html' : 'text/plain'}); >> temp_server.js
        echo     res.end(data); >> temp_server.js
        echo   }); >> temp_server.js
        echo }); >> temp_server.js
        echo server.listen(8000, () => console.log('Server running at http://localhost:8000')); >> temp_server.js
        node temp_server.js
        del temp_server.js
    ) else (
        echo 警告：未找到Python或Node.js
        echo 请手动在浏览器中打开 index.html 文件
        echo.
        pause
    )
)