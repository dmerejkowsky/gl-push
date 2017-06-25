import requests
import netrc
import urllib

nrc = netrc.netrc()
_, _, token = nrc.authenticators("gitlab.com")

#response = requests.get("https://gitlab.com/api/v4/projects",
                        #headers={"PRIVATE-TOKEN": token},
                        #data={"owned": True})
#response.raise_for_status()
#print(response.json())

project_name = "dmerej/hello"
project_id = urllib.parse.quote(project_name, safe=[])


url = "https://gitlab.com/api/v4/projects/%s/merge_requests" % project_id
response = requests.post(url, headers={"PRIVATE-TOKEN": token},
                         data={
                               "id": project_id,
                               "source_branch": "test1",
                               "target_branch": "master",
                               "title": "test1",
                        })
response.raise_for_status()
print(response.json())
