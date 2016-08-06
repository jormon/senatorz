import json, urllib

SENATOR_URL = "https://www.govtrack.us/api/v2/role?current=true&limit=1000"

data = urllib.urlopen(SENATOR_URL).read()
senator_data = json.loads(data)

for senator in senator_data["objects"]:
    if senator["role_type_label"] == "Representative":
        continue
    person = senator["person"]
    first_name = person["firstname"]
    last_name = person["lastname"]
    affiliation = "R"
    print u"{0} {1} ({2})".format(first_name, last_name, affiliation)
