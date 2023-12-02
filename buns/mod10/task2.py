import requests
import re

data = requests.get('http://www.columbia.edu/~fdc/sample.html').text

data_pattern = r'<h3[^>]*>(.*?)</h3>'

result = re.findall(data_pattern, data)

print(result)