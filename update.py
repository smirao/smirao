import urllib.request
import json, re

url = "https://alfa-leetcode-api.onrender.com/smirao/solved"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

extracted = data["solvedProblem"]

with open('README.md', 'rt', encoding='utf-8') as filer: 
    text = filer.read()

replaced = f'<span class="to-change">{extracted}</span>'
result = re.sub(r'<span class="to-change">.*?</span>', replaced, text)
print(result)

with open('README.md', 'w', encoding='utf-8') as filew:
    filew.write(result)