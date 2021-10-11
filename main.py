from CommandLine import CommandLine
from Crawler import crawl
import CrawlConstants

try:
    cmdLine = CommandLine()

    numberOfWordsToReturn = cmdLine.Args.mf if cmdLine.Args.mf > 0 else CrawlConstants.getDefaultNumberOfWordsToReturn()
    excludedWords = cmdLine.Args.excluded_words
    url = cmdLine.Args.url

    result = crawl(
        url=url,
        numberOfWordsToReturn=numberOfWordsToReturn,
        excludedWords=excludedWords
    )

    print(result)

except Exception as e:
    raise e
