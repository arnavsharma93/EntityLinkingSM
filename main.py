#!/usr/include/python
import sys
import os
import wikipedia

def GetTweet():
    return open(sys.argv[1]).read()

def RunTagger(TweetSet):
    os.system('./tweet-pos/runTagger.sh --output-format conll --no-confidence ' + sys.argv[1] + ' > .temp_output 2> /tmp/null' )

def GetNE():
    word_tag_list = open('.temp_output').readlines()
    word_tag = []
    for item in word_tag_list:
        try:
            word, tag = item.split('\t')
        except:
            continue
        tag = tag[:len(tag) - 1]
        if tag in ('N', 'V'):
            word_tag.append((word, tag))

    return word_tag

def GetWikiLinks(word_tag):
    word_links = []
    for item in word_tag:
        word = item[0]
        links = wikipedia.search(word)
        word_links.append((word, links))
    return word_links

def ShowOutput(tweet, word_links):
    print tweet
    for item in word_links:
        entity = item[0]
        links = item[1]
        print entity
        for link in links:
            print '\t' + link

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "It takes the filename containing tweets as the argument"
        sys.exit()

    RunTagger(sys.argv[1])
    word_tag = GetNE()
    word_links = GetWikiLinks(word_tag)
    tweet = GetTweet()
    ShowOutput(tweet, word_links)
