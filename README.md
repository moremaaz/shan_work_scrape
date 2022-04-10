# How I 'scrapped' the website:

I included some links here in the readme file that will teach you how to webscrape in python. The problem with this webpage is that the table you want to scrape is actually a google doc that is embedded with javascript, so it's difficult to get the information with traditional scrapping methods. Luckily, I found a much easier way to do this by:

1. Finding the link of the google sheet within the HTML file of the website: https://docs.google.com/spreadsheets/d/e/2PACX-1vSE0bsn0p8so7jAYi2whjJLt2MyZ_MljJPVgIcK3GutuRHxohzDwmFR4xx_iEPrRyOL0MigxTdfKsuP/pubhtml?
2. Reading the google sheet directly into a dataframe: https://stackoverflow.com/questions/60194993/scrape-embedded-google-sheet-from-html-in-python 

# Ideas:
I think what would make the most sense would be to setup an automatic script that will send you an email of the .csv file of the states + description that made a change during that day of the month. It can be something that runs automatically and will send you an alert (email) that this state made some opioid update on xyz day (assuming that whenever an update is made, they write something about the date they made the edit on). We can add that functionality later, if you would find it useful.  

# Location of the files:
The main python file is called template.py under the starter_files folder. I left the playground.ipynb just in case you wanted to see how some of the output of the function looked like. 

# Other helpful links that teach you how to scrape:
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://www.youtube.com/watch?v=ng2o98k983k
- https://medium.com/analytics-vidhya/a-beginners-guide-to-web-scrapping-using-beautiful-soup-9f91a400c324
