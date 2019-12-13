import requests


def get_transcripts(transcripts_urls):

    #loop through all transcript urls
    episode_count = 0
    for transcript in transcripts_urls:
        episode_count += 1
        r = requests.get(f'https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=greys-anatomy{transcript}')

        #write webpage to html file
        with open(f"Episode-{episode_count}.html", 'w+') as f:
            f.write(r.text)


if __name__ == "__main__":
