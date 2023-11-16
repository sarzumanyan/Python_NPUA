import requests

get_request=requests.get("https://jsonplaceholder.typicode.com/posts")
post_request=requests.post("https://jsonplaceholder.typicode.com/posts/11")
put_request=requests.put("https://jsonplaceholder.typicode.com/posts/2")
delete_request=requests.delete("https://jsonplaceholder.typicode.com/posts/3")

if get_request.status_code==200:
    print(f"GET request successful, status code {get_request.status_code}")
    get_title=[]
    for item in get_request.json():
        if len(item["title"])>6:
            get_title.append(item["title"])
    get_body=[]
    for item in get_request.json():
         if len(item["body"].split('\n')) > 3:
            get_body.append(item["body"])
else:
    print(f"Failed to make GET request, status code {get_request.status_code}")