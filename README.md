# Turncoat
Tool For Enumerating Telegram Bot Secret Messages 

# Requirements
1. Telegram App Installed
2. Bot API Key (eg. botXXXXXXXXXX:XXXXXXXXXXXXXXXX-XXXXXXX_XXXXXXX)
3. Bot chat_id number that contains secrets
4. Python3

# Summary
Malware campaigns suchs as AgentTesla (as part of C2) and phishing kits will sometimes utilize Telegram Bot API calls to to do the following:
* Send notifications on interaction (Phishing)
* Send phished credentials (Phishing)
* Send keylogger data (Malware)
* Send victim desktop screenshots (Malware) 
* Send victim machine cookies/passwords (Malware)

Often these campaigns expose the botid along with their API key. In order for Turncoat to work, we must be able to have access to the 'chat_id' that they are sending their secrets to.

Thanks to the implementation of the 'copyMessage' feature, we can conduct an attack with the following methodology using access to the bot api key:
1. Retrieve the bot 'first_name' and 'username' Telegram fields using the 'getMe' request.
2. Search for the bot username on Telegram. (Manual Step)
3. Send a simple message to the bot in the private chat on Telegram. (Manual Step)
4. Retrieve our user accounts 'id' that will be utilized as 'chat_id' for the private converation utilizing the 'getUpdates' request.
5. Finally, we will tell the bot to copy whatever quantity of messages from their malware/phishing campaign using 'from_chat_id' to our private 'chat_id' using the 'copyMessage' request.

# Quick Walkthrough
For this example I will be using a botkey and chat_id from a phishing campaing located on urlscan.io
This was chosen to highlight the script features while not exposing sensitive information as this particular campaign is only using the bot for alerting on click through and logging on the phishing page.

![alt text](https://github.com/DODC/turncoat/blob/main/images/example_campaign.png "example")

* The area highlighted in green will be used as our '--botkey' value in the turncoat.py script.
* The chat_id number in red will be used as our '--dropid' value later in the example when we actually copy the secret messages.
  
  
1. Open Telegram and login with the account of your choosing that you want to receive the messages from the bot.
  
2. python3 turncoat.py --botkey {Bot API Key} --getname
![alt text](https://github.com/DODC/turncoat/blob/main/images/get_name.png "getname")
  
3. In Telegram App, search for @username retrieved. Ensure that the first_name matches as well.

![alt text](https://github.com/DODC/turncoat/blob/main/images/search_bot.png "search bot username")
  
  
4. Start a private chat with the bot

![alt text](https://github.com/DODC/turncoat/blob/main/images/bot_start.png "bot start")
  
  
5. python3 turncoat.py --botkey {Bot API Key} --getchat

![alt text](https://github.com/DODC/turncoat/blob/main/images/get_chat.png "getchat")
  
  
6. 'Message From' should display your Telegram username. Copy the 'chat_id', this is your Telegram account id that can be used by bots to send you messages.
  
  
7. python3 turncoat.py --botkey {Bot API Key} -turncoat --chatid {Your chat_id from --getchat} --dropid {malware/phishing campaign chat_id with secrets}

![alt text](https://github.com/DODC/turncoat/blob/main/images/full_turncoat.png "turncoat")
  
  
8. Check Telegram for messages

![alt text](https://github.com/DODC/turncoat/blob/main/images/turncoat_first10.png "first 10 messages")
  
  
  
Additionally, you can specify the offset and count of messages you would like to retrieve. 
![alt text](https://github.com/DODC/turncoat/blob/main/images/turncoat_offset_count.png "offset")
  
The default offset is 1 and the default count is 10 messages. There is no simple way to determine the number of messages the bot has in the private chat, but I may look to add this feature in the future.
