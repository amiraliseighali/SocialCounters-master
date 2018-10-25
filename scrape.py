import bs4
import re

from bs4 import BeautifulSoup
import requests
import time




try:
    while True:
                
                res = requests.get('https://twitter.com/monashts')
                soup = BeautifulSoup(res.text,'lxml')

                url = 'https://www.instagram.com/monashtechschool'
                r = requests.get(url)
    
                fburl = 'https://www.facebook.com/monashtechschool/'
                fbr = requests.get(fburl)
		f = open('file','w')
		finsta = open('fileinsta','w')
		fface = open('filefacebook','w')
   		
   		follow_box = soup.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
                followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
                f.write( followers.get('data-count'))
		f.close()

                Instasoup = BeautifulSoup(r.content)
                Instafollowers = Instasoup.find('meta', {'name': 'description'})['content']
                follower_count = Instafollowers.split('Followers')[0]

                finsta.write( follower_count)
		finsta.close()
    
                fbsoup = BeautifulSoup(fbr.content)
                for node in fbsoup.find("div").find("div", {"class": "_3-95"}).find("div", {"class": "_4bl9"}):
                    like = (node.findAll(text=True))
                #gets an array of likes so you need the first element
        
    
    
                newlikes = re.findall('\d+',like[0])
                fface.write( newlikes[0])
		fface.close()
    
                print(newlikes[0])#print the first element of new like
    
                print("Number of Twitter followers are : " + followers.get('data-count'))
                print("Number of Instagram followers are : " + follower_count)
                time.sleep(1)
	#end while

    
 
except KeyboardInterrupt:
    print('Cannot find the handle right now')


