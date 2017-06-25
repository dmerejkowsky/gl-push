import requests
import netrc

nrc = netrc.netrc()
_, _, token = nrc.authenticators("gitlab.com")

response = requests.get("https://gitlab.com/api/v4/projects",
                        headers={"PRIVATE-TOKEN": token},
                        data={"owned": True})
print(response.json())
