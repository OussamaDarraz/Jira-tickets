from jira import JIRA

# Jira server URL and authentication credentials
options = {"server": "https://hagerdigitalfactory.atlassian.net/"}
username = "hageruser@gmail.com"
api_token = "ATATT3xFfGF0QNcBLN5jiJhivhLJVD2jdJv4CelQ5ybqo-JeOYeZn8iRrvlB1LtF-_qchWIvMk2VIyJF3XxYGpjX3ilXZmSfPHuLRv2x_imweIKUdPt4oxovRoPSR-QkPntsNcPt1K-ZY4EnCoMT8b8KCDph3YrS9tq2nzrqcl0tSxfEfKUDUeo=F88A88EC"

# Create a Jira client
jira = JIRA(options, basic_auth=(username, api_token))

# Prompt user to enter Jira ticket ID
ticket_id = raw_input("Enter Jira ticket ID (e.g., HDF-9887): ")

try:
    # Retrieve ticket information
    ticket = jira.issue(ticket_id)
    
    # Retrieve the status of the ticket
    status = ticket.fields.status.name
    
    # Display the status in the terminal
    print("The status of ticket {} is: {}".format(ticket_id, status))
except Exception as e:
    print("An error occurred:", str(e))
