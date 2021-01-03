<h1>Login to ELMS using Selenium</h1>

    Description: Basic python script to login to ELMS as a UMD student using Selenium. Opens class based on user input to zoom page of class, and clicker (if necessary). Used it to open my classes before online classes started each day during the 2020 pandemic. Added comments throughout to make it easier to customize for your own classes. 

**Requirements:**
- [Python](https://www.python.org/downloads/)

- [Selenium](https://selenium-python.readthedocs.io/installation.html)

- [ChromeDriver](https://chromedriver.chromium.org)

**Instructions before running:**
- Update the **login_info.py** with your directory id and password. (Or even better update the code and use [env variables](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5))

- Update **elms_login.py** with your class info. I added TODOs in parts that you should update

**To Run:**
- $ python3 elms_login.py

**Resources:**
- Interested in learning about Selenium? Watch the Selenium tutorials by [Tech With Tim](https://www.youtube.com/watch?v=Xjv1sY630Uc). It's how I learned. 

- [Selenium Docs](https://selenium-python.readthedocs.io) 