from flask import Flask, render_template, request, Response, send_file
from playground.search_and_replace import search_and_replace_func
import io, os
from rembg import remove
from rembg.session_factory import new_session
from PIL import Image
import time

os.environ['U2NET_HOME'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/models')

app = Flask(__name__)

model_name = "u2netp"
session = new_session(model_name)


@app.route("/")
def index():
    return render_template("dist/index.html")
    # return 'Hello from Flask!'


@app.route("/search_and_replace")
def search_and_replace():
    # search_and_replace_func('abc', '123')
    return "success！！！"


@app.route("/api/remove_image_bg", methods=["POST"])
def remove_image_bg():
    """
    files["image"]: 待处理图片
    """
    if request.method != "POST":
        return
    print("start remove_image_bg")
    start_time = time.time()

    im_file = request.files["image"]
    im_bytes = im_file.read()
    im = Image.open(io.BytesIO(im_bytes))

    output_path = "output.png"
    output = remove(im, session=session)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    # output.save(output_path)

    img_io = io.BytesIO()
    output.save(img_io, "PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")


app.run(host="0.0.0.0", port=9000, debug=False, ssl_context="adhoc")
