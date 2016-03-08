import os
import json
from flask import Flask, request
from apiclient.discovery import build

#import from the 21 Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

# set up server side wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# create a developer account on Google and obtain a API key for the url shortening app
service = build('urlshortener', 'v1', developerKey=os.environ.get('GOOGLE_URL_SHORTEN_API_KEY'))

# create a 402 end-point that accepts a url as input and shortens and returns it
@app.route('/shorten_url')
@payment.required(50)
def shorten():
    """Shorten the given URL"""
    
    # Get user's input text
    print(request.get_data)

    # Send a request to Google's URL Shortener API using API credentials defined above
    url = service.url()
    body = {'longUrl': request.args.get('long_url') }
    resp = url.insert(body=body).execute()
    print(resp)


    # Return short url to user
    return resp['id']

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)