from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return 'This is home'

@app.route('/get-test', methods=["GET"])
def gettest():
     dictToReturn = {'text': "this is an endpoint for get requests" }
     return jsonify(dictToReturn)

@app.route('/post-test', methods=["POST"])
def posttest():
     dictToReturn = {'text': "this is an endpoint for post requests" }
     return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run()