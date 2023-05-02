# Economic News Webscraper

## Table of Contents
- [Overview](#overview)
- [Files](#files)
- [Usage](#usage)
- [Contribution](#contribution)

## Overview
This Economic News Webscraper is an open-source project designed to improve the efficiency of delivering high-impact macroeconomic news from the US, UK, and EU regions. Developed by myslef, a quantitative analyst at EDEN Fund (school endowment fund), this project automatically scrapes news events every 30 minutes, filters relevant information, and sends notifications via Slack.

The project utilizes a Python script that scrapes news websites, and a GitHub Action to schedule and automate the process. The GitHub Action runs the script, commits any changes to the message history file, and pushes them to the repository. This ensures that the project continuously delivers the latest news without manual intervention.

## Files
The project contains the following files:

- `requirements.txt`: Lists the required packages for the project.
- `scraper.py`: Contains the functions to scrape news and extract relevant information.
- `filter_data.py`: Processes the scraped data as Pandas Dataframes and filters the relevant information for the output.
- `extra_data.csv`: Contains a table of all possible news releases, their effect on the markets, and their significance. This data is merged with the scraped data.
- `main.py`: The main program that starts the webscraper and sends the scraped information to Slack.
- `message_history.txt`: Stores the history of sent messages to avoid sending duplicate notifications.
- `.github/workflows/main.yml`: The GitHub Actions workflow file to automate the script execution and update the message history.

## Usage
1. Clone the repository:

        git clone https://github.com/gabrieldeolaguibel/Economic-News-Webscraper

2. Change to the project directory:

        cd Economic-News-Webscraper

3. Install dependencies:

        pip install -r requirements.txt

4. Set up a Slack webhook by following the [Slack documentation](https://api.slack.com/messaging/webhooks).

5. Add your Slack webhook URL to the GitHub repository secrets with the key `WEBHOOK_URL`.

6. Configure the GitHub Action's schedule in the `.github/workflows/main.yml` file if needed (by default, it runs every 30 minutes).

7. The GitHub Action will now automatically run the script, scrape the news, filter relevant information, and send notifications to the specified Slack channel.


## Contribution
Contributions are welcome! To contribute to this project:
1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make changes or add new features.
4. Submit a pull request to the original repository.



