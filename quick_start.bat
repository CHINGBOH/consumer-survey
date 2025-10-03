@echo off
echo ===========================================
echo   Consumer Behavior Survey Platform
echo ===========================================
echo.
echo [IMPORTANT] This is a CLEAN TEMPLATE with NO preset data!
echo - Website shows placeholder statistics (dashes and zeros)
echo - survey_data_template.csv is for LEARNING analysis methods
echo - Your real data goes in your_survey_data.csv
echo - Results will appear after you collect and analyze YOUR data
echo.
if exist "index.html" (
    echo [OK] Static website file exists
) else (
    echo [ERROR] Static website file missing
)

if exist "README.md" (
    echo [OK] Project documentation exists
) else (
    echo [ERROR] Project documentation missing
)

echo.
echo Environment check...

echo Detecting default browser...
where chrome >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Chrome browser available
    set BROWSER=chrome
    goto :browser_found
)

where firefox >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Firefox browser available
    set BROWSER=firefox
    goto :browser_found
)

where msedge >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Edge browser available
    set BROWSER=msedge
    goto :browser_found
)

echo [WARNING] No common browser detected
set BROWSER=start

:browser_found
echo.
echo ===========================================
echo   Recommended Workflow:
echo ===========================================
echo.
echo Phase 1: Survey Design
echo   - Use Wenjuanxing to design questionnaire
echo   - Collect data online (Excel/CSV)
echo   - Target sample size: 200-500 responses
echo.
echo Phase 2: Data Analysis
echo   - Use Google Colab for analysis
echo   - Or use Excel for basic statistics
echo   - Generate charts and reports
echo.
echo Phase 3: Results Presentation
echo   - Update index.html to show results
echo   - Deploy to GitHub Pages
echo   - Share research findings
echo.

echo ===========================================
echo   Quick Preview:
echo ===========================================
echo.

set /p choice="Open website preview now? (y/n): "
if /i "%choice%"=="y" (
    echo Starting browser...
    start "" "%BROWSER%" "file://%~dp0index.html"
) else (
    echo You can manually open index.html to preview the website
)

echo.
echo ===========================================
echo   Detailed Guides:
echo ===========================================
echo   - Open SETUP_GUIDE.md for complete setup process
echo   - Open README.md for project structure
echo.

echo ===========================================
echo   Next Steps:
echo ===========================================
echo   1. Design your consumer behavior survey questionnaire
echo   2. Start data collection
echo   3. Use online tools for data analysis
echo   4. Update website to showcase results
echo.

echo ===========================================
echo        Setup Complete! Good luck with research!
echo ===========================================

pause