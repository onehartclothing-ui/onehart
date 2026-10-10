import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(<script type="text/x-dc"[^>]*>)(.*?)(</script>)', content, re.DOTALL)
if match:
    with open('js_block.js', 'w', encoding='utf-8') as f:
        f.write(match.group(2))
    print("Extracted JS block to js_block.js")
else:
    print("Could not find JS block")
