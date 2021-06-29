#####
#
# Please feel free to take and reuse this simple upload script.
# You'll want to customize the columns based on your data & Trello lists.
# For reference, please see https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
#
# - Kojo DH, 6/28/21
#
#####

import csv, json, requests


url = "https://api.trello.com/1/cards"


# Read-in credentials
with open('..\..\Misc\AKL\ATK.txt', 'r', encoding='ANSI') as kf:
  dkey = kf.read()

with open('..\..\Misc\AKL\ATT.txt', 'r', encoding='ANSI') as tf:
  dtoken = tf.read()


# Read-in Aha export file
with open('unstarted_aha_list_features_210614223659.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0                                          # Tracks progress in the file
    
    for row in csv_reader:
        if line_count > 0:            
            dname = row[2]                                  # Feature name
            ddesc = row[11]                                 # Feature description

            # Lists on the 'AllyNet Features' board
            if '| Unspecified' in str(row[1]):
                dlist = '60da4c5fd0a50936b5d76b5c'          # Parking Lot | Unspecified
            elif 'Questions /' in str(row[1]):
                dlist = '60da4c926fc50b203a927fcc'          # Parking Lot | Q's & Suggestions
            elif '| Fixes' in str(row[1]):
                dlist = '60da4cac599c858d99ae06eb'          # Parking Lot | Fixes
            else:
                dlist = '60b923b512b51670f856c8ce'          # Backlog
            


            # Prepare request
            query = {
                'key': dkey,
                'token': dtoken,
                'name': dname,
                'desc': ddesc,
                'pos': 'bottom',                            # Other options include "top" or a (positive) number
                'idList': dlist
            }

            # Send request
            response = requests.request(
               "POST",
               url,
               params=query
            )

            # Results output
            res = response.json()                           # Convert API response into a Dictionary
            if res["id"] is not None:                       # Validates that Trello successfully assigned the row an ID
                if line_count % 10 == 0:
                    print(">",line_count," - Success")
            else:
                print(">",line_count," - Error")
                print(">",response.text)
        line_count += 1
