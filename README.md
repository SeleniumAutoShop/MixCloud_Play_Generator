# MixCloud_Play_Generator
Generate unlimited amount of plays for any shows on Mixcloud.com

*FULLY AUTOMATED PLAY GENERATOR FOR MUSIC ON MIXCLOUD.COM*

## Features  
-Unlimited amount of plays indefinitely  
-Fully automated, can be run 24/7  
-Length of listening time can be modified to your needs  
-This script can be modified to run at scale from multiple CommandPrompts  

## Getting Started  
-This will work with or without a Proxy  
***Using a Proxy is strongly recommended for without one your IP can be blocked by MixCloud after a while***  
-VPNs will also do the trick. Just make sure the Proxy option is turned off inside the script if you have a VPN turned on (Proxy option is off by default)  
-A rotating Proxy works better, you can also manually change the VPN location from time to time  

## Prerequisites  
-Have the up-to-date 'chromedriver' inside the same folder as the script  
-You need python 3 installed on your System  
-pip install Selenium  
-Create a txt file named 'BadUrl' and have it inside the same folder as the script  
-Create a txt file named 'MySongs' and have it inside the same folder as the script  
-Have the URLs of the desired songs saved inside the 'MySongs' txt file  
-If you want to put more than 1 URL inside 'MySongs.txt' make sure to have no extra spaces/empty lines at all  
(Copy and paste 1 URL, hit the enter key, paste the next URL and so on)  

## Running  
-You can run this script by uploading it to your console(I used Spyder), and simply hitting the Run button from your console  
-You can run this script from Commandprompt by going to your project directory, then enter 'python SimplePlayGenerator_LastUpdated2022.py'  

## Known Bugs  
-This version is using Xpath to operate  
-The Xapth in *line 88* needs to be updated from time to time  

## Author & Support
**SeleniumAutoShop**  
GitHub(https://github.com/SeleniumAutoShop)  


For any questions or issues with this script, please feel free to shoot me an email at chrish1826@gmail.com
