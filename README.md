# MajorProject
This project is made to automate the tasks performed in a data center. Created a browser application that automates various operational tasks in data-centers such as spinning up EC2 instances, Containerized Web-Servers, setting up Hadoop Clusters all over voice-based instructions. 


#Description:-
  In this project I have used anisble playbooks which automate the tasks. These ansible playbooks are accessed by python cgi as a backend.
  The task user choose to do from the frontend is proccessed by python-cgi which contains python scripts to interact with the os.
  That cgi will access the playbooks and provide the required variables to the playbooks and create the required rescources.
  
#Requirments:-
  Ansible, Python Script, HTML.

# How to use:-

This project contains two folders- html and cgi-bin.
    cgi-bin:- This folder contians two types of files- The .py file are used to perform backend tasks. THese are written in python. 
              These files access the .yaml files to perform the required tasks.
                  PLAYBOOKS:- This folder contains Ansible playbooks which automate the tasks like EC2 create, S3 bucket creation, 
                  user creation.       
    html:- THis folder contains the main html files which can be used by the user to interact. It has the frontend websites.          
