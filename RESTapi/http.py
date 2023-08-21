import requests
import os
from PIL import Image
from IPyton.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

r.status_code
print(r.request.headers)

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)