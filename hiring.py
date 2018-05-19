#!/usr/bin/python3
from block_io import BlockIo, BlockIoAPIError


def inicializarAPI(_secretPIN):
	#inicializando a API
	
	version = 2 # API version
	
	bitcointTestnetApiKey = 'dac5-24ba-d04c-19f9'
	block_io = BlockIo(bitcointTestnetApiKey, _secretPIN, version)
	return block_io

def send_btc(_block_io, _secretPIN):
	exampleWallet = '2N2MPfFRUmipSSdFaio23YiYw8eq6SV49qt'
	testWallet = '2MtSQLgfWpREsDjpax9k71MjiN6GRECuv2P'
	hiringWallet = 'mnYoahiweETgdXsfY92GCWA6HoRj9knQUw'

	try:
		#envia 1 btc
		amount = '1.0'
		withdraw = _block_io.withdraw_from_addresses(amounts=amount, 
			from_addresses=exampleWallet, to_addresses=hiringWallet, pin=_secretPIN)

		print("Status da operacao: ", withdraw['status'])
		print("Enviado: ", withdraw['data']['amount_sent'])
	except BlockIoAPIError as error:
		print(error)

	return

def main():
	secretPIN = '35kTalBneckAe'
	block_io = inicializarAPI(secretPIN)
	send_btc(block_io, secretPIN)

	return


if __name__ == '__main__':
	main()
