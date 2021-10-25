# Binance-NFT-Alert
Alert through a Discord Webhook when an artist on Binance drops Fresh NFTs.

## Specs
- Built in Python 3.9
- Built for Windows & Linux

## How to setup
### How to find Binance NFT Artist ID
- Go to the artists Binance profile page
- In the url there will be a `uid=` and you'll need the numbers after that till the `&` character

### Windows
- Install [Python 3 or over](https://www.python.org/)
- Remember to have it added to Environment Variables (you'll get asked during the setup)
- Clone this repository to your local machine or download it as a zip file and extract it
- Open a command prompt and find your way over to the cloned folder
- Use `py -m pip install -r requirements.txt` or `pip install -r requirements.txt` to get the used python libraries
- Edit `config.json` to use your own Discord Webhook and follow your own Binance NFT Artist
- Write `py alert.py` to start the Alerter

### Linux
- Install Python 3 using `apt-get install python3`
- Clone this repository to your local machine or download it as a zip file and extract it
- Change directory till you're in the folder where you have `alert.py`
- Use `python3 -m pip install -r requirements.txt` or `pip3 install -r requirements.txt` to get the used python libraries
- Edit `config.json` to use your own Discord Webhook and follow your own Binance NFT Artist
- Use `python3 alert.py` to start the Alerter

### How to have it run 24/7 on a VPS
- Same steps as Linux, but before you run the program you have to do the following
- Use `apt-get install tmux` to get the Linux Package called [tmux](https://en.wikipedia.org/wiki/Tmux)
- Use `tmux` to get a new virtual instance
- Change directory if you're not already in the same directory as the `alert.py` file
- Use `python3 alert.py` to start the Alerter
- Hold down CTRL and click B and then D to get out of the virtual instance
  -  To get into the virtual instance again (if you don't already have used tmux before)
  -  Use `tmux a -t 0` to get into the first indexed virtual instance
