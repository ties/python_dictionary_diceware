#
# Generate random word list from Linux Dictionary
#
# Based on script seen at CCC talk 4494 <http://ftp.ccc.de/events/camp2011/video/cccamp11-4494-laptop_and_electronics_searches_at_the_us_border-en.mp4> at 25:30
import argparse
import random
import math
import os

DICT_DIR = '/usr/share/dict/'

# get languages
def get_languages():
    return [f for f in os.listdir(DICT_DIR) if os.path.isfile(os.path.join(DICT_DIR, f))]

def count_lines(full_path):
    count = 0
    with open(full_path) as f:
        for _ in f:
            count += 1

    return count

parser = argparse.ArgumentParser(description='Diceware++ password generator')
parser.add_argument('--number', default=5, type=int,
                    help='Number of words')
parser.add_argument('--repeat', default=3, help='Number of passwords to generate')
parser.add_argument('--language', default=get_languages()[0], choices=get_languages())

args = parser.parse_args()

# Print the number of words per dictionary
for dict_file in get_languages():
    print("{: <35} {: >6} words".format("{}:".format(dict_file), count_lines(os.path.join(DICT_DIR, dict_file))))

print('#'*80)
print("Generating {} passwords".format(args.number))
print('#'*80)

with open(os.path.join(DICT_DIR, args.language), 'r') as f:
    words = f.readlines()
    for _ in range(args.repeat):
        print('_'.join(random.choice(words).rstrip() for i in range(args.number)))

    print('#'*80)
    entropy = args.number*math.log(len(words))/math.log(2)
    print("{} bits".format(entropy))
