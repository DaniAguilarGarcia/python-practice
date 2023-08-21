import requests
import os
from PIL import Image
from IPyton.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

r.status_code
print(r.request.headers)

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
#An image is a response object that contains the image as a bytes-like object. As a result,
# we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'example.txt')
r=requests.get(url)
#We save the file, in order to access the body of the response we use the attribute
# <code>content</code> then save it using the <code>open</code> function and write <code>method</code>:
with open(path,'wb') as f:
    f.write(r.content)