from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/address search')
def address_search():
    zipcode = request.args.get('zipcode')

    return f'address searchdayo'
    {zipcode =}

    @app.route('/shout/<string:name>')
    def shout(name: str):
        return f' {name}!!!'

    def main():
        app.run(debug=True)

    if __name__ == '__main__':
        main()
