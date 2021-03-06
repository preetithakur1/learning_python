{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup as bs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "comic_number=700"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "xkcd_url = \"https://xkcd.com/\"+str(comic_number)+\"/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://xkcd.com/700/'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xkcd_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "raw_data=requests.get(xkcd_url,\"lxml\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b'<!DOCTYPE html>\\n<html>\\n<head>\\n<link rel=\"stylesheet\" type=\"text/css\" href=\"/s/b0dcca.css\" title=\"Default\"/>\\n<title>xkcd: Complexion</title>\\n<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"/>\\n<link rel=\"shortcut icon\" href=\"/s/919f27.ico\" type=\"image/x-icon\"/>\\n<link rel=\"icon\" href=\"/s/919f27.ico\" type=\"image/x-icon\"/>\\n<link rel=\"alternate\" type=\"application/atom+xml\" title=\"Atom 1.0\" href=\"/atom.xml\"/>\\n<link rel=\"alternate\" type=\"application/rss+xml\" title=\"RSS 2.0\" href=\"/rss.xml\"/>\\n<script type=\"text/javascript\" src=\"/s/b66ed7.js\" async></script>\\n<script type=\"text/javascript\" src=\"/s/1b9456.js\" async></script>\\n\\n</head>\\n<body>\\n<div id=\"topContainer\">\\n<div id=\"topLeft\">\\n<ul>\\n<li><a href=\"/archive\">Archive</a></li>\\n<li><a href=\"http://what-if.xkcd.com\">What If?</a></li>\\n<li><a href=\"http://blag.xkcd.com\">Blag</a></li>\\n<li><a href=\"http://store.xkcd.com/\">Store</a></li>\\n<li><a rel=\"author\" href=\"/about\">About</a></li>\\n</ul>\\n</div>\\n<div id=\"topRight\">\\n<div id=\"masthead\">\\n<span><a href=\"/\"><img src=\"/s/0b7742.png\" alt=\"xkcd.com logo\" height=\"83\" width=\"185\"/></a></span>\\n<span id=\"slogan\">A webcomic of romance,<br/> sarcasm, math, and language.</span>\\n</div>\\n<div id=\"news\">\\n<div style=\"line-height:50%;\">\\n    &nbsp;\\n</div>\\nxkcd updates every Monday, Wednesday, and Friday\\n</div>\\n</div>\\n<div id=\"bgLeft\" class=\"bg box\"></div>\\n<div id=\"bgRight\" class=\"bg box\"></div>\\n</div>\\n<div id=\"middleContainer\" class=\"box\">\\n\\n<div id=\"ctitle\">Complexion</div>\\n<ul class=\"comicNav\">\\n<li><a href=\"/1/\">|&lt;</a></li>\\n<li><a rel=\"prev\" href=\"/699/\" accesskey=\"p\">&lt; Prev</a></li>\\n<li><a href=\"//c.xkcd.com/random/comic/\">Random</a></li>\\n<li><a rel=\"next\" href=\"/701/\" accesskey=\"n\">Next &gt;</a></li>\\n<li><a href=\"/\">&gt;|</a></li>\\n</ul>\\n<div id=\"comic\">\\n<img src=\"//imgs.xkcd.com/comics/complexion.png\" title=\"Why do all my attempts at science end with me being punched by Batman?  (P.S. benzoyl peroxide soap works great.)\" alt=\"Complexion\" />\\n</div>\\n<ul class=\"comicNav\">\\n<li><a href=\"/1/\">|&lt;</a></li>\\n<li><a rel=\"prev\" href=\"/699/\" accesskey=\"p\">&lt; Prev</a></li>\\n<li><a href=\"//c.xkcd.com/random/comic/\">Random</a></li>\\n<li><a rel=\"next\" href=\"/701/\" accesskey=\"n\">Next &gt;</a></li>\\n<li><a href=\"/\">&gt;|</a></li>\\n</ul>\\n<br />\\nPermanent link to this comic: https://xkcd.com/700/<br />\\nImage URL (for hotlinking/embedding): https://imgs.xkcd.com/comics/complexion.png\\n<div id=\"transcript\" style=\"display: none\">I get frustrated trying to judge whether acne creams are having any effect. In the spirit of a controlled trial, I used one on just half my face for a few weeks.\\n[[A graph shows pimples vs. time, with two lines--one remains one steady, and one is declining.]]\\n\\nIt was cool seeing the effects so clearly, so I got some friends to try different treatments in an impromptu study.\\n[[The narrator looks in a mirror, sees a half-pimpled face, and applies a treatment.]]\\n\\n[[The narrator is talking to a blonde and brunette friend, each with some pimples also.]]\\nNarrator: Okay, you try the saucylic acid first.\\nBlonde: Wait, we should randomize the trials. Got a coin?\\n\\nNarrator: Okay, call it. Heads, she gets the--\\n(Off-panel): YOU!\\n\\n[[Batman runs into frame and punches the narrator. The coin goes flying.]]\\n\\n{{Title text: Why do all my attempts at science end with me being punched by Batman?  (P.S. benzoyl peroxide soap works great.)}}</div>\\n</div>\\n<div id=\"bottom\" class=\"box\">\\n<img src=\"//imgs.xkcd.com/s/a899e84.jpg\" width=\"520\" height=\"100\" alt=\"Selected Comics\" usemap=\"#comicmap\"/>\\n<map id=\"comicmap\" name=\"comicmap\">\\n<area shape=\"rect\" coords=\"0,0,100,100\" href=\"/150/\" alt=\"Grownups\"/>\\n<area shape=\"rect\" coords=\"104,0,204,100\" href=\"/730/\" alt=\"Circuit Diagram\"/>\\n<area shape=\"rect\" coords=\"208,0,308,100\" href=\"/162/\" alt=\"Angular Momentum\"/>\\n<area shape=\"rect\" coords=\"312,0,412,100\" href=\"/688/\" alt=\"Self-Description\"/>\\n<area shape=\"rect\" coords=\"416,0,520,100\" href=\"/556/\" alt=\"Alternative Energy Revolution\"/>\\n</map>\\n<div>\\n<!--\\nSearch comic titles and transcripts:\\n<script type=\"text/javascript\" src=\"//www.google.com/jsapi\"></script>\\n<script type=\"text/javascript\">google.load(\\'search\\', \\'1\\');google.setOnLoadCallback(function() {google.search.CustomSearchControl.attachAutoCompletion(\\'012652707207066138651:zudjtuwe28q\\',document.getElementById(\\'q\\'),\\'cse-search-box\\');});</script>\\n<form action=\"//www.google.com/cse\" id=\"cse-search-box\">\\n<div>\\n<input type=\"hidden\" name=\"cx\" value=\"012652707207066138651:zudjtuwe28q\"/>\\n<input type=\"hidden\" name=\"ie\" value=\"UTF-8\"/>\\n<input type=\"text\" name=\"q\" id=\"q\" size=\"31\"/>\\n<input type=\"submit\" name=\"sa\" value=\"Search\"/>\\n</div>\\n</form>\\n<script type=\"text/javascript\" src=\"//www.google.com/cse/brand?form=cse-search-box&amp;lang=en\"></script>\\n-->\\n<a href=\"/rss.xml\">RSS Feed</a> - <a href=\"/atom.xml\">Atom Feed</a>\\n</div>\\n<br />\\n<div id=\"comicLinks\">\\nComics I enjoy:<br/>\\n        <a href=\"http://threewordphrase.com/\">Three Word Phrase</a>,\\n        <a href=\"http://www.smbc-comics.com/\">SMBC</a>,\\n        <a href=\"http://www.qwantz.com\">Dinosaur Comics</a>,\\n        <a href=\"http://oglaf.com/\">Oglaf</a> (nsfw),\\n        <a href=\"http://www.asofterworld.com\">A Softer World</a>,\\n        <a href=\"http://buttersafe.com/\">Buttersafe</a>,\\n        <a href=\"http://pbfcomics.com/\">Perry Bible Fellowship</a>,\\n        <a href=\"http://questionablecontent.net/\">Questionable Content</a>,\\n        <a href=\"http://www.buttercupfestival.com/\">Buttercup Festival</a>,\\n        <a href=\"http://www.mspaintadventures.com/?s=6&p=001901\">Homestuck</a>,\\n\\t<a href=\"http://www.jspowerhour.com/\">Junior Scientist Power Hour</a>,\\n</div>\\n<br />\\n<div id=\"comicLinks\">\\nOther things:<br/>\\n        <a href=\"http://womenalsoknowstuff.com/\">Women Also Know Stuff</a>,\\n        <a href=\"https://techsolidarity.org/\">Tech Solidarity</a>,\\n        <a href=\"https://medium.com/civic-tech-thoughts-from-joshdata/so-you-want-to-reform-democracy-7f3b1ef10597\">Tips on technology and government</a>\\n</div>\\n<br />\\n<center>\\n<div id=\"footnote\" style=\"width:70%\">xkcd.com is best viewed with Netscape Navigator 4.0 or below on a Pentium 3&plusmn;1 emulated in Javascript on an Apple IIGS<br />at a screen resolution of 1024x1. Please enable your ad blockers, disable high-heat drying, and remove your device<br />from Airplane Mode and set it to Boat Mode. For security reasons, please leave caps lock on while browsing.</div>\\n</center>\\n<div id=\"licenseText\">\\n<p>\\nThis work is licensed under a\\n<a href=\"http://creativecommons.org/licenses/by-nc/2.5/\">Creative Commons Attribution-NonCommercial 2.5 License</a>.\\n</p><p>\\nThis means you\\'re free to copy and share these comics (but not to sell them). <a rel=\"license\" href=\"/license.html\">More details</a>.</p>\\n</div>\\n</div>\\n</body>\\n<!-- Layout by Ian Clasbey, davean, and chromakode -->\\n</html>\\n\\n'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw_data.content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "soup=bs(raw_data.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "comic = soup.find(\"div\", {\"id\": \"comic\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div id=\"comic\">\n",
       "<img alt=\"Complexion\" src=\"//imgs.xkcd.com/comics/complexion.png\" title=\"Why do all my attempts at science end with me being punched by Batman?  (P.S. benzoyl peroxide soap works great.)\"/>\n",
       "</div>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "comic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "image_url = comic.img[\"src\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "image_url=\"https:\"+image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://imgs.xkcd.com/comics/complexion.png'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "extension_type=image_url.split(\".\")[len(image_url.split(\".\"))-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'png'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "extension_type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "image_data=requests.get(image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"comic_\"+str(comic_number)+\".\"+extension_type,\"wb\") as comic_file:\n",
    "    comic_file.write(image_data.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
