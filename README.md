## Facebook Timeline Cleaner
Because the world needs one more of those. Mostly because all I could find were broken and I needed one.

The script removes everything from your public timeline. It deletes what it can, the rest it tries to hide.
It does not unfriend people and it does not remove you from groups.

It is very naive, and takes a long time to run. But who cares. As it is written with selenium it is hopefully a little more robust for changes on facebook than the other scripts seem to be. Only time will tell.

If you find any bugs, you are welcome to create a pull request.

### Dependencies
You need python (I use 2.7) and the selenium webdriver api for python as well. Should be installable with
	
	sudo apt-get install python pip
	pip install selenium

or something like that.

### Usage
You need to put your username and password in as environment variables before running the script. Afterwards just run it with python
    
    export FBC_USER='<your facebook username>'
    export FBC_PASSWORD='<your facebook password>'
    python fbclean.py

It uses Firefox as it's default webdriver.

### License
Distribute, copy and do whatever you like with this code, just don't hold me liable. Otherwise I don't care.

Use this software at your own risk. I created it for my personal purpose, if it blows up in your face, you should have read the source.

If you like my work, buy me a beer or send me some bitcoins 1PuewXApS7Dk2VVjgVTWe432BomKnDnS4t
