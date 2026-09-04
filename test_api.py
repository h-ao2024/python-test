import requests
url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)
print("状态码：",response.status_code)
if response.status_code==200:
    data=response.json()
    print("总条数：",len(data))
    for post in data[:5]:
        print(f"标题：{post['title']}")
        print(f"内容：{post['body'][:50]}...")
        print("-"*30)
    else:
        print("请求失败")

