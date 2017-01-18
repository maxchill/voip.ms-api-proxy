import requests
import json

url = 'https://voip.ms/api/v1/rest.php'

# Initialize the Flask application
app = Flask(__name__)

@app.route('/send/', methods=['POST'])
def sendSMS():
    message = request.values.get('message')
    dst = request.values.get('dst')

    secret = request.values.get('secret')

    realIP = request.headers.get('X-Real-IP')

    if secret != 'secretapiproxykey':
       return 'not authorized', 401

    payload = {'api_username' : 'username',
                'api_password' : 'apipassword',
                'method' : 'sendSMS',
                'did' : '5555551234',
                'dst' : dst,
                'message' : message
              }

    r = requests.get(url, params=payload)

    print(dst)
    print(message)
    print(realIP)
    print(r.text)

    if r.status_code == 200:
        return 'success', 200
    else:
        return 'error', int(r.status_code)


# Run the app
if __name__ == '__main__':
  app.run(
        host="127.0.0.1",
        port=int("8050"),
        debug= True
  )
