This is the loose documentation for gosmish.

You have a DB and all the scripts necessary to make the campaign happen.

You'll need to get apache on your DO box. Run

apt install apache2 -y

Then, in the gophish directory, run

cp apache/\* /var/www/html 

The structure of the victims.csv file is that you need to have a unique ID, a first name, a last name, a phone number, and a role, then it'll add all those entries into gosmish.db. It won't let you add entries where there's a conflict in phone number or id.

You'll need to manually edit the send_smish.py file to make it what you want with the message, url to your domain/DO IP, and your own twillio account and API info. It would be most secure to make it what you want, use pyinstaller to make it an executable, and then store that on your local device since it contains your private API key.

Once you do, enter a new campaign number as a command line argument. Reusing an old campaign number can result in false positives.

Once the campaign is done, run "Make Report" with the campaign number (whatever number you chose when running send_smish.py) and it'll print the results to the screen of who took the bait.

Enjoy!

Your fren,

Cyber
