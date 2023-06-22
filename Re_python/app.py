from flask import Flask, render_template, request
from jira import JIRA

app = Flask(__name__)


options = {"server": "https://hagerdigitalfactory.atlassian.net/"}
username = "hageruser@gmail.com"
api_token = ""


jira = JIRA(options, basic_auth=(username, api_token))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ticket_id = request.form['ticketId']
        try:
            ticket = jira.issue(ticket_id)
            status = ticket.fields.status.name
            description = ticket.fields.description
            customer = ticket.fields.reporter.displayName
            return render_template('index.html', status=status, description=description, customer=customer)
        except Exception as e:
            error_message = str(e)
            return render_template('index.html', error=error_message)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
