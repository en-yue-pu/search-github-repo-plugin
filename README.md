# github自带的搜索仓库api
使用chatgpt设定3个参数
query关键词
language编程语言
max最大个数(option) 默认是1

返回给chatgpt的是json
所以GPT应该知道很多细节

# 参考
Get
https://api.github.com/search/repositories?q=react+language:javascript&sort=stars&order=desc
关键词react 语言javascript 顺序stars 并且降序

GET https://api.github.com/search/repositories?q=flutter+language:swift&sort=stars&order=desc&per_page=5 只显示前5

GET https://api.github.com/search/repositories?q=flutter+language:swift&sort=stars&order=desc&page=2 显示第二页

https://api.github.com/search/repositories?q=en-japan+language:python&sort==best%20match&order=desc&per_page=2 不按照star数  按照best match 顺序 降序


https://api.github.com/search/repositories
URLQueryItem(name: "q", value: "\(q)"),
URLQueryItem(name: "sort", value: "desc"),
URLQueryItem(name: "order", value: "best match"),
URLQueryItem(name: "page", value: "1"),
URLQueryItem(name: "per_page", value: "30"),



# pip install -r requirements.txt
# python main.py
# ngrok http 5003
