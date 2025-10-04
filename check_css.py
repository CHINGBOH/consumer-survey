import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS from style tag
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if css_match:
    css = css_match.group(1)

    # Check for basic CSS syntax issues
    issues = []

    # Check for unclosed braces
    open_braces = css.count('{')
    close_braces = css.count('}')
    if open_braces != close_braces:
        issues.append(f'Brace mismatch: {open_braces} opening vs {close_braces} closing')

    # Check for @media rules
    media_rules = re.findall(r'@media[^{]*\{', css)
    for media in media_rules:
        media_start = css.find(media)
        media_content = css[media_start:]
        # Find the matching closing brace for this @media rule
        brace_count = 0
        found_closing = False
        for i, char in enumerate(media_content):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    found_closing = True
                    break
        if not found_closing:
            issues.append(f'Unclosed @media rule: {media.strip()}')

    # Check for selectors without closing braces
    selectors = re.findall(r'[^}]*\{', css)
    for selector in selectors:
        selector = selector.strip()
        if selector and not selector.startswith('@'):
            # Find the position of this selector
            pos = css.find(selector + '{')
            if pos != -1:
                # Count braces from this position
                brace_count = 0
                found_closing = False
                for i in range(pos, len(css)):
                    if css[i] == '{':
                        brace_count += 1
                    elif css[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            found_closing = True
                            break
                if not found_closing:
                    issues.append(f'Unclosed selector: {selector}')

    if issues:
        print('CSS Syntax Issues Found:')
        for issue in issues:
            print(f'- {issue}')
    else:
        print('No obvious CSS syntax issues found.')

    print(f'\nTotal CSS length: {len(css)} characters')
    print(f'Opening braces: {open_braces}')
    print(f'Closing braces: {close_braces}')