import json
profile = '{"name":"Montri Taion","age":"3x","github":"https://github.com/onionsh"}'

result = json.loads(profile)

print(result["github"])