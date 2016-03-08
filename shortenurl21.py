import sys
import click

#import from the 21 Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

#set up bitrequest client for BitTransfer requests
wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

@click.command()
@click.argument('long_url', required=False)

# Uncomment this line to use your own server
# @click.option('--server', default='localhost:5000', help='ip:port to connect to')

# Comment this line to not use my server
@click.option('--server', default='128.12.55.131:5000', help='ip:port to connect to')
def cli(server, long_url):

    """ Call the url-shortening api hosted on the micropayments server"""

    if not long_url:
        long_url = click.get_text_stream('stdin').read()

    # Send request to server with url to be shortened and user's wallet address for payment
    sel_url = 'http://' + server + '/shorten_url?long_url={0}&payout_address={1}'
    response = requests.get(url=sel_url.format(long_url, wallet.get_payout_address()))

    # Print the shortened url out to the terminal
    click.echo(response.text)
