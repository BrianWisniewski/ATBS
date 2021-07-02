#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import pyperclip
import sys

if len(sys.argv) < 2: #sys.argv returns a list of the arguments given starting with the name of the file
        print('Usage: python MultiClipboard.py [keyphrase] - copy phrase text')
        sys.exit

keyphrase = sys.argv[1] #stores the cmd line argument as the var 'keyphrase'

if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print(f'Text for {keyphrase} copied to clipboard.')
else:
        print(f"'{keyphrase}' is not a valid argument")
