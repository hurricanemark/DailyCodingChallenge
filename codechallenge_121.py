#! python3
'''
Date: 06/28/2022

Challenge description:
======================

Automate webbrowser to search for my online interests.

1. Launch a map in the browser using an address from the command line or clipboard.

2. Download every single XKCD comic images

'''
import webbrowser, sys
import pyperclip
import requests, os, bs4  # bs4 is a beautiful soup library

# ----------
# Function: Launch google map in the browser to display the address.
#
# 1. Highlight an address text in any open application will copy it to the clipboard.
# 2. Luanch this program like this `python .\codechallenge_121.py`
#
# Warning: This function will open a new browser window to the last 
# address you search using your browser(even you clear the browsed data).  
# You could open some one else'search history which is not cool snooping.
def browse_map_address():
    if len(sys.argv) > 1:
        # get the address from the command line
        # The sys.argv contains ['999', 'Commercial', 'St, ', 'Palo', 'Alto, ', 'CA', '94303']
        # A foreign address: ['Thành', 'phố', 'Cà', 'Mau', 'Ca', 'Mau', 'Vietnam']
        # A GPS coordinate: [8.691333, 104.905278]
        address = ' '.join(sys.argv[1:])
    else:
        # get the address from the clipboard
        address = pyperclip.paste()

    # open the browser if address has something in it
    if address:
        webbrowser.open('https://www.google.com/maps/place/' + address)    
        


        
        
def web_download_img(url):
    # Downloads every single XKCD comic.
    while not url.endswith('#'):
        # Download the page.
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
            break
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            # download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            try:
                res.raise_for_status()
            except Exception as exc:
                print('There was a problem: %s' % (exc))
            

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

            # Get the Prev button's url.
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')

    print('Done.')        
    

    
if __name__ == '__main__':
    browse_map_address()
    
    url = 'https://xkcd.com'               # starting url
    os.makedirs('xkcd', exist_ok=True)     # store comics in ./xkcd
    web_download_img(url)                  # download all the comic images 