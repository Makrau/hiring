#!/usr/bin/python3
from block_io import BlockIo, BlockIoAPIError
secretPIN = '35kTalBneckAe'
def inicializarAPI():
	#inicializando a API
	
	version = 2 # API version
	
	bitcointTestnetApiKey = 'dac5-24ba-d04c-19f9'
	block_io = BlockIo(bitcointTestnetApiKey, secretPIN, version)
	return block_io

def main():
	block_io = inicializarAPI()

	exampleWallet = '2N2MPfFRUmipSSdFaio23YiYw8eq6SV49qt'
	testWallet = '2MtSQLgfWpREsDjpax9k71MjiN6GRECuv2P'
	hiringWallet = 'mnYoahiweETgdXsfY92GCWA6HoRj9knQUw'

	try:
		#envia 1 btc
		withdraw = block_io.withdraw_from_addresses(amounts='1.0', 
			from_addresses=exampleWallet, to_addresses=hiringWallet, pin=secretPIN)

		print("Status da operacao: ", withdraw['status'])
		print("Enviado: ", withdraw['data']['amount_sent'])
	except BlockIoAPIError as error:
		print(error)

	return

if __name__ == '__main__':
	main()
