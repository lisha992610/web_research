# web_research
Automatising the multiple search on google with Command: <site:website "keywords">. 

This command enables the keyword search on specific Homepage or sub-domain. This Python Programm is used to automatize multiple search processes of a list of keywords in a specific homepage. It extracts the number of search result from the HTML file. 
Possible utiliuzation for google advaced search commands: https://blog.hubspot.com/blog/tabid/6307/bid/1264/12-quick-tips-to-search-google-like-an-expert.aspx

Limitation: In this program, no google custom search API is used. After around 150 searches (some depends on the results), Google will recognize it as Robot and block it for min. 1 day (harmless). According google custom API website, with custom search API-key it allows up to 100 automatised search per day. For more is possible with a paid API-Key. 
Example Files: The parsingWebsite.py will read the list of keywords from Keyword.csv and custom search in given "website", then write the reuslt into recording.csv
