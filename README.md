# Coded by Kevin Ngo on 10/9/2021

Timeboxed to 3H

Assumptions:
- Although not stated, it was assumed that this program would also accept an argument for the URL (if not passed then it defaulted to the Microsoft Wikipedia page)
- This also assumed that the excluded words from the search would be passed via command line arguments
- This also assumed that the results should be printed to the console

Notes:
- There can be further testing done to the web parser to better extract the number of words in a given page.
- There can be further research done into how to target parsing specific sections of a given page.
- There is currently a lack of unit testing on this, although given more time this would be accounted for within the /testing portion of the sln.