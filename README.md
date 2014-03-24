EntityLinkingSM
===============

Entity Linking in Social Media -  For a given tweet, find the entities and then using contextual information about these entities, try to link it with the corresponding information resources.

Dependencies 
1. TweetNLP POS tagger by CMU http://www.ark.cs.cmu.edu/TweetNLP/
2. Wikipedia python library https://pypi.python.org/pypi/wikipedia

Pre-requesites 
1. Java 6
2. Python
3. Pip

Installation
sudo pip install wikipedia

How to use:
1. Make EntityLinkingSM your pwd.
2. python main.py <name of the file containing a tweet>
    eg: 
    ```bash
    python main.py data/one_tweet
    ```


