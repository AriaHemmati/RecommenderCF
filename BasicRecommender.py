import requests

def getID(problem):
    if(problem.get("contestId") == None):
        return None
    return f"{problem['contestId']}{problem['index']}"

def count_ac(problemset, users):
    userlist = open(users, "r")
    count = dict()

    accepted_problems = []
    for user in userlist.readlines():
        handle = user.strip()
        # print(handle)
        response = requests.get(f"https://codeforces.com/api/user.status?handle={handle}")
        submitions = response.json()["result"]
        ac_problems = []
        for s in submitions:
            if(s["verdict"] == "OK"):
                ac_problems.append(s["problem"])
        accepted_problems.append(ac_problems)

    for problem in problemset:
        flag = 0
        for oth in problemset:
            if(problem["name"] == oth["name"]):
                flag += 1
        cnt = 0
        id = getID(problem)
        for ac_problems in accepted_problems:
            for ac_submition in ac_problems:
                if(ac_submition["name"] == problem["name"] and (flag == 1 or getID(ac_submition) == id)):
                    cnt += 1
                    break
        count[id] = cnt
    return count


response = requests.get("https://codeforces.com/api/problemset.problems")
problemset = response.json()["result"]["problems"]
response = requests.get("https://codeforces.com/api/contest.list")
constests = response.json()["result"]

students = count_ac(problemset, "hoi36.txt")
legends = count_ac(problemset, "legends.txt")

isDiv2 = dict()
for contest in constests:
    if(("Div. 2" in contest["name"]) and ("Div. 1" not in contest["name"])):
        isDiv2[contest["id"]] = True
    else:
        isDiv2[contest["id"]] = False

tags = [""]
rate = [2500 , 2800]
for problem in problemset:
    if("tags" not in problem or "rating" not in problem):
        continue
    # if(problem["rating"] < rate[0] or rate[1] < problem["rating"]):
    #     continue
    # validTags = False
    # for tag in problem["tags"]:
    #     if(tag in tags):
    #         validTags = True
    # if(validTags == False):
    #     continue
    # if(not isDiv2[problem["contestId"]]):
    #     continue
    id = getID(problem)
    # url = "https://codeforces.com/problemset/problem/{0}/{1}".format(problem["contestId"], problem["index"])
    # print('{0}\t=HYPERLINK("{1}", "{2}")\t{3}\t{4}\t{5}'.format(
        # id, url, problem["name"], problem["rating"], legends[id], students[id]))
    print("{0}\t{1}\t{2}".format(id, legends[id], students[id]))