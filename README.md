lircremotesdownloader
=====================

Disclaimer:
I do not own the remote control files hosted by the LIRC comminity at http://lirc.sourceforge.net/remotes/
In the case it is disallowed or illegal to download, please send email me at nitish.k.reddy@gmail.com so that I can take down the repository

Improvements:
If you find at any time the program needs improvements or changes, drop everything you are doing at the moment and send in a pull request. I'd like to learn and I'd like there to be good code provided.

Aim:
To be able to download all the available LIRC Remote Control model files from the LIRC library at http://lirc.sourceforge.net/remotes/ - this is assuming they are available for download.

The LIRC package anyway comes with a remotes list but the list is limited to most commonly used ones. In case you are looking for the most commonly used files it is preferable to down the LIRC package from http://www.lirc.org/ and take it from there since downloading it using the python file is quite slow.

Why?
It could be a good enough reason to start programming in python because it is loads of fun!

To download all remote control files in the case you are an LIRC user, maybe there is a much better way to do this but I'm not aware of it.

To research and find patterns in consumer IR so that you can build your own universal remote. Thats what I'm doing :)


Instructions:
1) Download & install Python v 2.7 from http://www.python.org/download/ (porting to python 3 is not at all difficult especially on such a small code)

2) Download & install Setuptool Library from https://pypi.python.org/pypi/setuptools . Make sure to download and install this before other libraries in the case they require setuptools to be installed.

3) Download & install BeautifulSoup Library from http://www.crummy.com/software/BeautifulSoup/

4) Download & install Lxml Html Parser Library from http://lxml.de/index.html#download

5) Run the python file
