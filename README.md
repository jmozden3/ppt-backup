# ppt-backup
python script to automate saving and downloading online ppts

<b>Summary</b> <br>
As a consultant, I work on documents (mostly powerpoint decks) all the time. Additionally, most of these are live documents that I (and my coworkers) edit in real-time. These documents save in real time as well.
Thus, it's common practice to save a local copy of that live document every few days. That way you always have an older version backed up in case you ever need to revert back to a previous version. 
  
<b>Script Details</b> <br>
The script goes to the url of the live document <br>
Downloads the live document<br>
Moves the document to a folder designated by the user<br>
And adds timestamp to the name of the downloaded document

<b>How to enable automated backup on Windows</b>
1. Download the code and put in necessary inputs (your url, path, etc)
2. Turn your .py file into a .exe file. I use py-to-exe lib. https://pypi.org/project/auto-py-to-exe/
3. Use Task Scheduler to run the .exe file whenever you want. 

<b>Additional Note</b> <br>
This is my first git project, and at the time of creation, I still wasn't fully familiar with .venv's. There is a possibility some of the requirements aren't necessary. 
