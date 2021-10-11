import argparse
import CrawlConstants


class CommandLine:
    def __init__(self):
        self.Parser = argparse.ArgumentParser(
            description='This is a web crawler which will visit a URL and return the top number of words (by frequency).')
        self.Parser.add_argument('-mf', metavar='--most-frequent-number-of-words', type=int, default=CrawlConstants.getDefaultNumberOfWordsToReturn,
                                 help='the most frequent number of words to be returned.')
        self.Parser.add_argument(
            '-ew', '--excluded-words', nargs='+', default=[], help="the words to be excluded within the count.")
        self.Parser.add_argument(
            '-url', '--url', type=str, default=CrawlConstants.getDefaultUrl(), help="the url to the page to be crawled.")
        self.Args = self.Parser.parse_args()
