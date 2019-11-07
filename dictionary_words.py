import sys, random


def random_word(params):
    random_words = []
    num_words = int(params)
    with open ('/usr/share/dict/words', 'r') as f:
        words = f.readlines()
        for _ in range(num_words):
            random_words.append((random.choice(words).strip()))

    random_sentence = (" ".join(random_words))
    print(random_sentence)



if __name__ == "__main__":
    params = sys.argv[1]
    random_word(params)