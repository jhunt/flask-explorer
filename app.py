#from flask import Flask, make_response, render_template, send_file
import os, subprocess, flask

def ls(dir):
  p = subprocess.Popen(['ls', '-la', f'/{dir}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
  s = ''
  while True:
    b = p.stdout.read(8192)
    if not b:
      p.wait()
      break
    s += b
  r = flask.make_response(s, 200)
  r.headers['Content-Type'] = 'text/plain'
  return r

app = flask.Flask('app')

@app.route("/")
def index_handler():
  return flask.render_template('index.html', env=os.environ.items())

@app.route("/file/<path:file>")
def file_handler(file):
  return flask.send_file(file, root_path='/')

@app.route("/ls")
def ls_handler_root():
  return ls('')

@app.route("/ls/<path:dir>")
def ls_handler(dir):
  return ls(dir)

if __name__ == '__main__':
  app.run(debug=True)
