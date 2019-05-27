#! python3
# quickSubreddit takes you to a subreddit of your choice
# without the clicks in the middle

import webbrowser, sys
if len(sys.argv) > 1:
    # Get subreddit from the command line
    subreddit = ' '.join(sys.argv[1:])
else:
    # Get subreddit after being prompted
    print('Enter a subreddit to be directed to: ')
    subreddit = input()

webbrowser.open('https://www.reddit.com/r/' + subreddit)
