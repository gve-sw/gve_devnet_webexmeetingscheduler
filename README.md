# Webex Meeting Scheduler

An application to schedule a Webex Meetings from CSV file via Webex Integration. 

## Contacts
* Eda Akturk (eakturk@cisco.com)

## Solution Components
* Cisco Webex
* Python 3.8 


## Prerequisites
- **Webex Meetings**: A Webex Meetings account is required
   
- **Webex Integration**: Register a Webex OAuth 2 Integration following the steps outlined [here](https://developer.webex.com/docs/integrations)
    - *Redirect URI* must be set to: http://localhost:5000/webexoauth
    - *Scope*, must have the following permissions:
        - spark:all
        - meeting:schedules_write

## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

#### Install the libraries :

```$ pip install -r requirements.txt```


## Setup: 

1. Add the webex integration credential to env_var.py
```
webex_integration_client_id = " "
webex_integration_client_secret= " "
webex_integration_redirect_uri = "http://localhost:5000/webexoauth"
webex_integration_scope = "spark:all meeting:schedules_write"
```

## Usage
Run the web application by:
```
    python main.py
```

# Screenshots
![/IMAGES/login.PNG](/IMAGES/login.PNG)

![/IMAGES/file_selector.PNG](/IMAGES/file_selector.PNG)

![/IMAGES/meetings.PNG](/IMAGES/meetings.PNG)


#### License
Provided under Cisco Sample Code License, for details see [LICENSE](./LICENSE.md).


#### Code of Conduct
Our code of conduct is available [here](./CODE_OF_CONDUCT.md).


#### Contributing
See our contributing guidelines [here](./CONTRIBUTING.md).


#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
