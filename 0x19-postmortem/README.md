# A Postmortem Project Example

For this school project, I created an imaginary situation that didn't happen to any of the projects that I've contributed in. But it's a good example to help other developers and the ones starting their career in the Software Engineering field avoid some similar disastrous situation and to valorize the significance of Postmortem.

## Introduction
We were working on developing a new social network and we've already had a beta version with a few hundred of test users. The application was built with Python, Django, MySQL and ReactJS. We were a small team of 4 software engineers working on different aspects of the application and  a new intern.

## Issue summary
On 05/04/2020 Starting from 8.35 AM GMT until 8.55 AM GMT, almost all the website application was down besides the home page, the login and the sign up pages. None of the 100% or our beta users could access to their data and the root cause was that the new intern have the privileges to manipulate the master MySQL database and he wrongly typed the command that deleted the whole database's data.

## Timeline
##### This following events took place on Monday, May the 4th, 2020.
* 8.40 AM GMT -  the impossibility to access the website as a logged in user issue was detected when the intern was asked to test some new features on the hosted version on the cloud.
* 8.41 AM GMT - The intern checked the internet connection by running a ping command to the Google and Facebook IP addresses.
* 8.43 AM GMT - The intern cleaned his browser's cache to.
* 8.44 AM GMT - The intern restarted Nginx on the web server.
* 8.45 AM GMT - The intern verified that the HTTP and the HTTPS ports were open on our servers and load balancer.
* 8.46 AM GMT - The intern informed the back-end developer of the issues and the steps he took to track the issue.
* 8.48 AM GMT - The back-end developer launched a GET request with the curl command to our homepage's URL and got an error.
* 8.49 AM GMT - The back-end developer logged into MySQL to check the database and ended up not finding any data.
* 8.50 AM GMT - The back-end developer checked the history of the typed commands on MySQL and found out the command typed by the intern.
* 8.52 AM GMT - The back-end developer generated a file from the slave MySQL database containing all the data that was on the master database. He then dumped the data from the file to the master database and restarted the server.
* 8.55 AM GMT - The The back-end developer verified that was everything went back to normal.

## Root cause and Resolution
This outage was caused by the deletion of the whole database by a new intern who's still learning how to code, because the development team gave him full privileges to manipulate everything in the code base, infrastructure and design mock-ups… Fortunately we already had back up for everything. So we just replicated the data from the slave database and copied it to the master one and the issue was resolved.

## Corrective and preventative measures
To prevent this kind of similar mistake, we must not give full access to everything in our platform to non-experienced developers and to work more on the accessibility to sensitive data and personalized algorithms and technical solutions.
The technical team also needs to better communicate with the new interns about their technical backgrounds, what technologies are they more comfortable with, are they interested in working on a specific thing in the application and to advise them to not be afraid or shy to inform or ask the engineering team about something one's not sure or knowledgeable about.

## Postmortem diagram
Below is a image illustrating the incident diagram framework set by atlassian.
[Postmortem Diagram](img.png)
