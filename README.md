# search-github-repo-plugin

github自带的搜索仓库api
Get
https://api.github.com/search/repositories?q=react+language:javascript&sort=stars&order=desc

https://api.github.com/search/repositories
URLQueryItem(name: "q", value: "\(q)"),
URLQueryItem(name: "sort", value: "desc"),
URLQueryItem(name: "order", value: "best match"),
URLQueryItem(name: "page", value: "1"),
URLQueryItem(name: "per_page", value: "30"),



pip install -r requirements.txt
python main.py

