import argparse
import requests
import json


url = "https://api.telegram.org/"
def getname(botkey):
	try:
		res = requests.post(url+botkey+'/getme')
		data = json.loads(res.text)
		fname = data["result"]["first_name"]
		uname = data["result"]["username"]
		print('[+] Bot First Name : '+fname)
		print('[+] Bot User Name : '+uname)
		print('[+] Send private chat message to bot in Telegram, then re run script with --getchat')
	except:
		print('[+] Error Retrieving Bot Info')


def getchat(botkey):
	try:
		res = requests.post(url+botkey+'/getupdates')
		data = json.loads(res.text)
		for item in data["result"]:
			base = item["message"]["from"]
			chatid = str(base["id"])
			fname = base["first_name"]
			print('[+] Message from '+fname)
			print('[+] Chat ID : '+chatid)
		print('[+] Choose the correct chat ID and re run script with -t or --turncoat')
	except:
		print('[+] Error Retrieving Chat ID')
		print('[+] Check that you have private messaged the correct bot on Telegram first')

def turncoat(botkey,chatid,dropid,start,count):
	complete=0
	print('[+] Attempting to transfer '+str(count)+' messages ranged '+str(start)+' through '+str(start+count-1))
	for i in range(start,start+count):
		try:
			req_data = {"from_chat_id": str(dropid), "chat_id": str(chatid), "message_id": str(i)}
			res = requests.post(url+botkey+'/copymessage',data=req_data)
			data = json.loads(res.text)
			if data["ok"] == True:
				complete+=1
		except:
			print('[+] Error transferring chat data for message ID : '+str(i))
	print('[+] Total messages transferred : '+str(complete))
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-b", "--botkey", help="BOT API KEY")
	parser.add_argument("-gn", "--getname", action="store_true")
	parser.add_argument("-gc", "--getchat", action="store_true")
	parser.add_argument("-t", "--turncoat", action="store_true")
	parser.add_argument("-k", "--kill", action="store_true", help="Not yet implemeneted")
	parser.add_argument("-cid", "--chatid", help="Your chat ID")
	parser.add_argument("-did", "--dropid", help="Chat ID from Scam")
	parser.add_argument("-os", "--offset", help="(Turncoat only) Starting Message Number - Default 1")
	parser.add_argument("-mc", "--count", help="(Turncoat only) Total Message Count - Default 10 messages")
	args = parser.parse_args()
	print('''

__ __| |   |  _ \   \  |  ___|  _ \    \ __ __| 
   |   |   | |   |   \ | |     |   |  _ \   |   
   |   |   | __ <  |\  | |     |   | ___ \  |   
  _|  \___/ _| \_\_| \_|\____|\___/_/    _\_|   
                           by DODC                    
''')
	if args.botkey:
		if args.getname:
			print('[+] Retrieving Bot Info')
			getname(args.botkey)
		elif args.getchat:
			print('[+] Retrieving Chat Info')
			getchat(args.botkey)
		elif args.turncoat:
			if args.chatid and args.dropid:
				print('[+] Turn Coat Initiated')
				print('[+] Attempting Chat Transfer')
				if args.offset:
					start = args.offset
				else:
					start = 1
				if args.count:
					count = args.count
				else:
					count = 10
				turncoat(args.botkey,args.chatid,args.dropid,int(start),int(count))
			elif args.chatid:
				print('[+] Drop Chat ID Required as -did or --dropid')
			elif args.dropid:
				print('[+] Your Telegram chat ID is required as -cid or --chatid')
				print('[+] Run script with -gc or --getchat to retrieve')
		else:
			print('[+] No Options Selected')
			parser.print_help()
	else:
		print('[+] BOT KEY REQUIRED using -b or --botkey')


 
if __name__ == "__main__":
	main()
