#!/usr/bin/python3

from block_io import BlockIo
import hiring

def test_hiring():
	secretPIN = '35kTalBneckAe'
	block_io = hiring.inicializarAPI(secretPIN)
	amount = '0.00002000'
	exampleWallet = '2N2MPfFRUmipSSdFaio23YiYw8eq6SV49qt'
	testWallet = '2MtSQLgfWpREsDjpax9k71MjiN6GRECuv2P'
	hiringWallet = 'mnYoahiweETgdXsfY92GCWA6HoRj9knQUw'
	withdraw = hiring.send_btc(block_io, amount, exampleWallet, testWallet,
		secretPIN)

	assert withdraw['status']=='success'
	assert withdraw['data']['amount_sent']==amount

