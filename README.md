# Trello_CSV_Import
Quick &amp; dirty import script to [generate Trello cards](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post) from CSV records

1. Follow [these steps](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) to get your Trello API key and token.
2. Store your credentials locally and update the filenames in the script. (or copy/paste them directly into the script if security isn't a concern)
3. Update the following per your data and target Trello board(s):
   - File Name
   - Column(s) for import
   - Target List(s)
7. If you want more or less output, adjust which fields display (and when) from the response object.
