import urllib.request
import json
import re

url = "https://alfa-leetcode-api.onrender.com/smirao/solved"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

extracted = data["solvedProblem"]

with open('README.md', 'rt', encoding='utf-8') as filer: 
    text = filer.read()

replaced = f'<span class="to-change"><img src="https://img.shields.io/badge/LeetCodes%20Completed-{extracted}-yellow?style=for-the-badge" alt="LeetCodes Completed" /></span>'
result = re.sub(r'<span class="to-change">.*?</span>', replaced, text)

with open('README.md', 'w', encoding='utf-8') as filew:
    filew.write(result)