import requests

response = requests.get("https://codeforces.com/api/problemset.problems")
problemset = response.json()["result"]["problems"]
print(len(problemset))
