"""
00 fork this replit to your replit 

01a do your code
01b your final goal is to hit Run and have all tests PASS IN GREEN

02a git commit push to github repo - view guide https://drive.google.com/file/d/1PZZ2xIlamM0pPtLlbpDodseCKcIVhTzW/view?usp=sharing
02b get url to your git repo in 02a above - we call it :gitrepourl

03 paste :gitrepourl into this google form and submit it
   https://forms.gle/cuxhb8cbYaJLHRYz5
   ma_debai = toya03bainopmauflaskapiapp
"""

import os
from types import resolve_bases

import requests
from flask import Flask, jsonify

app = Flask(__name__)
port = os.environ.get("PORT")
port = os.getenv("PORT", 5000) if port is None else int(port)


@app.route('/')
def index():
  return {}
    
@app.route('/release')
def release():
  response = requests.get("https://api.github.com/repos/pyenv/pyenv/releases")
  
  if response.status_code == 404:
    return jsonify({
        "error": "Không thể lấy dữ liệu từ GitHub"
    })
  else:
    data = response.json()
    releases = []
    for release in data:
        releases.append({
            "created_at": release["created_at"],
            "tag_name": release["tag_name"],
            "body": release["body"]
        })
    return releases

@app.route('/most_3_recent/release')
def most_3_recent():
  releases = release()
  most_3_recent = releases[:3]
  return most_3_recent


if __name__=='__main__':
  app.run(debug=True, port = os.environ.get("PORT",5000))