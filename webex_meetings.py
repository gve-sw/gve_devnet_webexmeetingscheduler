# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Eda Akturk <eakturk@cisco.com>"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import csv
import requests


def createMeeting(meeting_name, host, start_time, end_time, attendee, token):
    """
    This function will create the webex meeting based on the parameters and send a Webex Bot message once the meeting
    has been created
    :param: webex meeting information
    :return: create meeting api response
    """
    url = "https://webexapis.com/v1/meetings"

    attendeeList = []
    for a in attendee:
        entry = {'email': a}
        attendeeList.append(entry)

    payload = {
        "title": meeting_name,
        "password": "BgJep@43",
        "start": start_time,
        "end": end_time,
        "enabledAutoRecordMeeting": False,
        "allowAnyUserToBeCoHost": False,
        "enabledJoinBeforeHost": False,
        "enableConnectAudioBeforeHost": False,
        "allowFirstUserToBeCoHost": False,
        "allowAuthenticatedDevices": False,
        "invitees": attendeeList,
        "sendEmail": True,
        "hostEmail": host,
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    return response.status_code

def csv_scheduler(token, filename):
    """
    This function open and read the CSV file that contains the information to schedule Webex Meetings then send the
    information to Webex meeting scheduler function in webex.py to schedule
    :return: list of scheduled meetings
    """
    scheduled_meetings = []
    print('*** now going to read csv file ***')

    # try to read csv file, if not, read an excel file and convert it to csv
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row_number, row in enumerate(csv_reader):
            if row_number == 0:
                print("*** do not record this row - Headers ***")
                continue
            else:
                meeting_name = row[0]
                host = row[1]
                start_time = row[2]
                end_time = row[3]

                attendees = row[4]
                attendees = attendees.replace(' ','')
                attendees = attendees.split(';')

                try:
                    response = createMeeting(meeting_name, host, start_time, end_time, attendees, token)
                    if response == 200:
                        meeting = {'name': meeting_name, 'start': start_time, 'end': end_time}
                        scheduled_meetings.append(meeting)
                        print("*** scheduled meetings ***")
                except:
                    print("*** unable to schedule meeting from CSV file, please check CSV ***")

    return scheduled_meetings
