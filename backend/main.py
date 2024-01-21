from flask import Flask, render_template
from playground.search_and_replace import search_and_replace_func

from flask_cors import CORS

app = Flask(__name__)
# CORS(app, resources={r"/": {"origins": "118.89.145.103"}})
CORS(app)


from rembg import remove
from rembg.session_factory import new_session

model_name = "u2netp"
session = new_session(model_name)

from PIL import Image
import time


@app.route('/')
def index():
  return render_template('dist/index.html')
  # return 'Hello from Flask!'


@app.route('/search_and_replace')
def search_and_replace():
  # search_and_replace_func('abc', '123')
  return 'success！！！'


@app.route('/remove_image_bg')
def remove_image_bg():
  # search_and_replace_func('abc', '123')
  print('start remove_image_bg')
  start_time = time.time()

  input_path = 'generated_horse.png'
  output_path = 'output.png'

  input = Image.open(input_path)
  output = remove(input, session=session)
  output.save(output_path)

  # Your function call goes here

  end_time = time.time()
  execution_time = end_time - start_time
  print(f"Execution time: {execution_time} seconds")
  return 'success！！！'


app.run(host='0.0.0.0', port=9000, debug=True, ssl_context='adhoc')
