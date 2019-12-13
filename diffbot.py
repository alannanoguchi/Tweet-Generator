import os
import requests
from dotenv import load_dotenv
load_dotenv()

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = os.getenv('DIFFBOT_ACCESS_TOKEN_SECRET')

def get_article(article_url):
    # article_url = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=greys-anatomy&episode=s01e01"
    
    # set request params for API request
    params = { 'token': DIFFBOT_DEV_TOKEN,
               'url': article_url,
               'discussion': 'false' }

    res = requests.get(DIFFBOT_API_URL, params) # hit the Diffbot API
    print(params)
    print(res.json())
    res_obj = res.json()['objects'][0]          # parse the response object

    return res_obj['text']                      # pull out the text

if __name__ == '__main__':
    import sys
    urls_file = open(sys.argv[1])
    output_file = open('corpus.txt', 'w')

    corpus = ''

    for line in urls_file:
        url = line.strip() # remove leading/trailing whitespace
        article = get_article(url)
        corpus += article

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))