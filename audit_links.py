import re

with open(r'C:\Users\jackg\jarvis-ops\index.html', encoding='utf-8') as f:
    content = f.read()

hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
onclicks = re.findall(r'onclick=["\']([^"\']+)["\']', content)
titles = re.findall(r'class="card-title"[^>]*>([^<]+)<', content)

print('=== HREFS ===')
for h in hrefs: print(' ', h)
print()
print('=== ONCLICKS ===')
for o in onclicks: print(' ', o)
print()
print('=== CARD TITLES ===')
for t in titles: print(' ', t)
