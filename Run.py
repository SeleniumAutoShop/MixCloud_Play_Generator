import time 
from selenium import webdriver
import random

myProxy = "n" #Insert a Proxy here instead of "n" if you wish to run this with a Proxy.
fileName = 'MySongs' #Insert the name of the file instead of "MySongs" containing the song links you wish to run. Or just store the links in the "MySongs" txt file.
with open(str(fileName)+".txt") as f:
            urls = f.readlines()

#---------------------------------------------------------------------------------------------------------------------------
def setUp(): #Opens Chromedriver and goes to mixcloud.com and then the link to the first song in the list.
    global driver
    global proxy
    while True:
        try:
            driver.quit()
        except:
            pass
        try:
            if myProxy == 'n':
                print('no proxy')
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("window-size=1920,1080")
                chrome_options.add_argument('disable-infobars')
                chrome_options.add_argument("--mute-audio")
                chrome_options.add_argument('--disable-extensions')
                chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
                driver = webdriver.Chrome(chrome_options=chrome_options)
                driver.get('https://www.mixcloud.com/')
                time.sleep(10)
                driver.get(urls[0])
                print('page ready')
                time.sleep(3)
                break
            else:
                  print('starting with proxy')
                  proxy = myProxy
                  seleniumproxy = '--proxy-server={}'.format(proxy)
                  chrome_options = webdriver.ChromeOptions()
                  chrome_options.add_argument("window-size=1920,1080")
                  chrome_options.add_argument(seleniumproxy)
                  chrome_options.add_argument('disable-infobars')
                  chrome_options.add_argument("--mute-audio")
                  chrome_options.add_argument('--disable-extensions')
                  chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
                  driver = webdriver.Chrome(chrome_options=chrome_options)
                  driver.get('https://www.mixcloud.com/')
                  time.sleep(10)
                  driver.get(urls[0])
                  print('page ready')
                  time.sleep(3)
                  break
        except:
            print('ERROR')

#---------------------------------------------------------------------------------------------------------------------------
def rotateUrl(url, urls, index): #Formats throguh the links and rotates through 2 tabs on Chrome.
    print(url)
    driver.get(url)
    urls = [url.replace("\n", "") for url in urls]
    try:
        js = "window.open('{}');".format(urls[index+1])
        driver.execute_script(js)
        print('next song opened')
    except:
        js = "window.open('{}');".format(urls[0])
        print('starting at first song')
        driver.execute_script(js)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
        
#---------------------------------------------------------------------------------------------------------------------------
def click_play(): #Clicks on the play button. Update the Xpath if the play button cannot be found.
    playbutton = driver.find_element_by_xpath("//div[@class='content']/div/div")
    playbutton.click()
    print('play clicked')
    
#---------------------------------------------------------------------------------------------------------------------------
def play_check(): #Checks to see if the song is actually being played. Update the play_time Xpath if it cannot be found. (The slider bar at the bottom when a song is being played)
    for i in range(3):
        time.sleep(1)
        try:
            if driver.find_element_by_xpath('//span[@class="play-button play-button-cloudcast"]'):
                driver.refresh()
                time.sleep(5)
                click_play()
        except:
            play_time = driver.find_element_by_xpath("//div[@class='PlayerSliderComponent__StartTime-sc-z3gy2f-1 faCtHn']").text #Update here if needed.
            return str(play_time)
    
#---------------------------------------------------------------------------------------------------------------------------   
def play(): #Plays the song, will keep listening for n seconds.
    click_play()
    time.sleep(5)
    play_check()
    time.sleep(1)
    if play_check() != "0:00":
        print("play number +1")
        dice = random.randint(0, 20) #The chances of the dice here can be modified.
        if dice <=5:
            short = random.randint(4, 10) #The seconds here can be modified.
            print('listening to song for ' + str(short) + ' sec...')
            time.sleep(short)
        else:    
            listen = random.randint(5, 12) #The seconds here can be modified.
            print('listening to song for ' + str(listen) + ' sec...')
            time.sleep(listen)
            
#---------------------------------------------------------------------------------------------------------------------------
def popUp(): #Pop up handler.
    try:
        driver.find_element_by_xpath("//main[@class='content-wrapper content-wrapper-show cf']").click()
        print('popup clicked')
    except Exception as e:
        print(e)

#---------------------------------------------------------------------------------------------------------------------------
def start(): #Will try to run the whole script indefinitely. Quit the console entirely to stop running.
    while True:
        try:
            for index, url in enumerate(urls):
                setUp()
                rotateUrl(url, urls, index)
                popUp()
                try:
                    play()
                except:
                    pass
                    badUrl = driver.current_url
                    with open('badUrl.txt','w') as f: #Stores the current link in the "badUrl.txt" file if it cannot be played.
                        f.write(badUrl)
                time.sleep(1)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        except:
            print('Restarting')
            start()

start()
