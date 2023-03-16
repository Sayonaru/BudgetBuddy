# Team Project - Budget Buddy

## What is Budget Buddy


## Downloading the database
- Begin by downloading WAMP from the following link https://www.wampserver.com/en/download-wampserver-64bits/, this grants access to the database services required
- After it has downloaded, run it and there should be a little icon in the taskbar below
![Opening WAMP](/ReadMeImages/ReadMeImg3.png "Opening WAMP")
- When you click the icon, a menu will appear. Navigate to "phpmyadmin" and click the button 
![Opening phpmyadmin](/ReadMeImages/ReadMeImg4.png "Opening phpmyadmin")
- A log in page should appear with username being root and the password empty. Select "MySQL" for server choice, leave the username and password the same and press the log in button
- With the dashboard present, navigate to the import button and choose the "user-table" SQL file
![Importing Database](/ReadMeImages/ReadMeImg5.png "Importing Database")
- Scroll to the bottom of the page and press the import button
- You can then navigate to the table by selecting the "user-table" on the sidebar and clicking the "user" file
## How to run
- Open your terminal of choice (i.e. GitBash)
- Navigate into the project folder using the commands "cd {folder name here}" to move into a folder and "ls" to display all the current available files
![Folder Navigation](/ReadMeImages/ReadMeImg1.png "Folder Navigation")
- Once navigated into the "Full Project" folder, if flask is not installed, type "pip install flask"
- You will also need to run "npm install chart.js" which install packages for certain features we are utilising
- To begin running the server, type "python app.py" and some text should appear giving information of the server
![Running Flask](/ReadMeImages/ReadMeImg2.png "Running Flask")
- You can then go to your prefered browser and type "http://localhost:5000" and the program will be working
- To exit the program, return to the terminal and hold control while pressing "C" (the same as copying something) and the server should quit. You will be able to tell by a blank line in the terminal

## What the tables are in the database
In phpmyadmin, the database is visualised. For example, in the "user" file in "user-table", the data gathered from the sign up page is stored and then used for validation in the log in