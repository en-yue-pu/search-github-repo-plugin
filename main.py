import json
import requests
import quart
import quart_cors
from quart import jsonify, request

app = quart.Quart(__name__)
quart_cors.cors(app, allow_origin="https://chat.openai.com") # 只允许chatgpt官方domin的访问
    
@app.route("/repos/<string:query>/<string:language>/<number>", methods=['GET'])
async def get_repos(query, language, number=1):
    url = f"https://api.github.com/search/repositories?q={query}+language:{language}&sort=stars&order=desc&per_page={number}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return quart.Response(response=json.dumps(data), status=200)
    else:
        return quart.Response(response=json.dumps({"error": f"请求失败，状态码：{response.status_code}"}), status=400)
    
@app.get("/logo.jpg")#响应读取logo的请求
async def plugin_logo():
    filename = 'logo.jpg'
    try:
        return await quart.send_file(filename, mimetype='image/jpg')
    except FileNotFoundError:
        return jsonify({"error": f"文件'{filename}'不存在"}), 404

@app.get("/.well-known/ai-plugin.json")#响应读取manifest文件的请求
async def plugin_manifest():
    host = request.headers['Host']
    filename = "./.well-known/ai-plugin.json"
    try:
        with open(filename) as f:
            text = f.read()
            return quart.Response(text, mimetype="text/json")
    except FileNotFoundError:
        return jsonify({"error": f"文件'{filename}'不存在"}), 404

@app.get("/openapi.yaml")#响应读取openAPI规范文件(仕様書)的请求
async def openapi_spec():
    host = request.headers['Host']
    filename = "openapi.yaml"
    try:
        with open(filename) as f:
            text = f.read()
            return quart.Response(text, mimetype="text/yaml")
    except FileNotFoundError:
        return jsonify({"error": f"文件'{filename}'不存在"}), 404

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)#启动服务

if __name__ == "__main__":
    main()