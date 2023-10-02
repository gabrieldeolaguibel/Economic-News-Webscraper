# Economic News Webscraper
[![GitHub stars](https://img.shields.io/github/stars/gabrieldeolaguibel/Economic-News-Webscraper)](https://github.com/gabrieldeolaguibel/Economic-News-Webscraper/stargazers)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4A154B?style=flat)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=flat&logo=slack&logoColor=white)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/gabrieldeolaguibel/)

## Table of Contents
- [Overview](#overview)
- [Files](#files)
- [Usage](#usage)
- [Contribution](#contribution)
- [Contact](#contact)


## Overview
This Economic News Webscraper is an open-source project designed to improve the efficiency of delivering high-impact macroeconomic news from the US, UK, and EU regions. Developed by myslef, a quantitative analyst at EDEN Fund (school endowment fund), this project automatically scrapes news events every 30 minutes, filters relevant information, and sends notifications via Slack.

The project utilizes a Python script that scrapes news websites, and a GitHub Action to schedule and automate the process. The GitHub Action runs the script, commits any changes to the message history file, and pushes them to the repository. This ensures that the project continuously delivers the latest news without manual intervention.

<p align="center">
  <img src="https://www.linkpicture.com/q/WhatsApp-Image-2023-05-03-at-12.15.41-AM.jpeg" alt="Screenshot 1" width="300" height="400" style="margin: 0 10px;">
  <img src="https://www.linkpicture.com/q/WhatsApp-Image-2023-05-03-at-12.15.21-AM.jpeg" alt="Screenshot 2" width="300" height="400" style="margin: 0 10px;">
</p>



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

## Future Improvements

While this project already provides a valuable service, there are plans to further enhance and expand its capabilities. Some of the ambitious future improvements include:

1. Utilizing AI and natural language processing (NLP) to better understand and interpret news articles, resulting in more accurate and relevant notifications.
2. Expanding the scope of the project to include additional news sources and markets for a broader range of economic news coverage.
3. Implementing a sentiment analysis module to gauge market sentiment and predict potential market reactions to news events.
4. Developing a user interface (UI) to allow users to customize the types of news they receive, such as choosing specific regions, sources, or keywords.
5. Integrating the project with various trading platforms to enable automated trading based on the news events and analysis provided.
6. Providing a summary and visualization of past news events and market reactions to enable users to identify trends and patterns over time.

Stay tuned for these exciting developments and more as the project evolves!


## Contact

If you have any questions, suggestions, or just want to get in touch, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/gabrieldeolaguibel/).



## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information




