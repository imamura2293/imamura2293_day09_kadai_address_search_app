import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/address_search')
def address_search():
    zipcode = request.args.get('zipcode')

    url = f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'

    response = requests.get(url)

    address1 = response.json()['results'][0]['address1']
    address2 = response.json()['results'][0]['address2']
    address3 = response.json()['results'][0]['address3']

    return f'{address1}{address2}{address3}'


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
