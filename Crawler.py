from bs4 import BeautifulSoup
from collections import Counter
import CrawlConstants
from CrawlExceptions import InvalidCrawlParameters, CrawlError
import requests
from typing import Dict, List, Set


def process_words(soupObj: BeautifulSoup, excludedWordList: List[str]):
    """
        This will process and filter words based on the text from a BeautifulSoup Object.
    """

    if soupObj != None:
        # get the list of words
        wordList = [word.strip().lower() for word in soupObj.getText().split()]

        # set a new list to capture the filtered words
        processedWords = []
        for word in wordList:
            # replace the symbols
            symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/.,"
            for i in range(len(symbols)):
                word = word.replace(symbols[i], '')

            # split the words if they are separated by a space
            words = word.split()

            # add the words to the processed list
            for processedAndSplitWord in words:
                if len(processedAndSplitWord) > 0 and processedAndSplitWord not in excludedWordList:
                    processedWords.append(word)

        return processedWords
    else:
        raise InvalidCrawlParameters(
            "Invalid BS4 Object passed as a parameter.")


def crawl(
        url: str,
        numberOfWordsToReturn: int,
        excludedWords: Set = None,
        localPath: str = None) -> Dict:
    """
        This function accepts the parameters: Url, Excluded Words, and the number of words to return in the result.
    """

   # region Validation
    if url != None and len(url) > 0:
        if not(url.startswith('https://')):
            raise InvalidCrawlParameters('Invalid URL.')
    elif localPath == None:
        raise InvalidCrawlParameters('Invalid URL.')

    if excludedWords != None:
        for word in excludedWords:
            if not isinstance(word, str):
                raise InvalidCrawlParameters('Invalid list of excluded words.')

    if numberOfWordsToReturn == None:
        numberOfWordsToReturn = CrawlConstants.getDefaultNumberOfWordsToReturn()

    if numberOfWordsToReturn < 0:
        raise InvalidCrawlParameters('Invalid number of words to return.')
    # endregion

    try:
        # get the source code of the url
        source = None
        if localPath != None:
            source = open(localPath, encoding="utf8")
        else:
            source = requests.get(url).text

        # create the b.s. object
        if localPath != None:
            soupObj = BeautifulSoup(source.read(), 'html.parser')
        else:
            soupObj = BeautifulSoup(source, 'html.parser')

        # filter information by getting rid of "invisible" text to the user
        [e.extract() for e in soupObj(
            ['style', 'script', 'head', 'title', 'meta', '[document]'])]

        # get all of the words
        words = process_words(soupObj, excludedWords)

        # count the occurence of the words
        counts = Counter(words)

        # return the top most common words
        return counts.most_common(numberOfWordsToReturn)

    except Exception as e:
        # notify system of unhandled error
        raise CrawlError(e)
