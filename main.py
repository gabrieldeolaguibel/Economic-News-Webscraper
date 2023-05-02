import calendar
import pandas as pd
from datetime import datetime, timezone, timedelta
from scraper import create_scraper, fetch_calendar_page, send_post_request, parse_calendar_data
from filter_data import clean_df, merge_dfs, drop_tentative, apply_timezones, add_datetime, filter_past_events, clean_date
from dotenv import load_dotenv
import os
import requests



def get_current_year_month_day():
    # Get current year, month, day
    current_year = str(datetime.now().year)
    current_month = str(datetime.now().strftime('%B').capitalize())
    today = str(int(datetime.now().strftime('%d')))
    # Get first day of the month
    first = str(int(datetime.now().replace(day=1).strftime('%d')))
    # Get last day of the month
    end = str(calendar.monthrange(int(current_year), int(datetime.strptime(current_month, '%B').month))[1])
    return current_month, first, current_year, end
    #print(current_year, current_month, today, first, end)

def scrape_economic_data():
    scraper = create_scraper()
    security_value = fetch_calendar_page(scraper)
    response_text = send_post_request(scraper, security_value, get_current_year_month_day()[0], get_current_year_month_day()[1], get_current_year_month_day()[2], get_current_year_month_day()[3])
    df = parse_calendar_data(response_text)

    df = clean_df(df)

    df2 = pd.read_csv('extra_data.csv')
    df = merge_dfs(df, df2)

    df = drop_tentative(df)

    # Define the time zone offsets
    gmt_minus_5 = timezone(timedelta(hours=-5))  # USA zone
    gmt_plus_1 = timezone(timedelta(hours=1))  # Spain zone

    df = apply_timezones(df, gmt_minus_5, gmt_plus_1)

    df = add_datetime(df)

    df = filter_past_events(df)

    df = clean_date(df)

    return df

def save_message_data(message_data_array):
    with open("message_history.txt", "w") as f:
        for message in message_data_array:
            f.write(message + "\n")

def load_message_data():
    message_data_array = []
    try:
        with open("message_history.txt", "r") as f:
            for line in f:
                message_data_array.append(line.strip())
    except FileNotFoundError:
        # If the file does not exist, return an empty array
        pass
    return message_data_array

def send_to_slack(row, webhook_url):
    payload = {
        "blocks": [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": "Macro News!"}
            },
            {
                "type": "section",
                "text": {"type": "plain_text", "text": f"{row['Currency']}: {row['Event']}"}
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Result:*\n{row['Actual']}"},
                    {"type": "mrkdwn", "text": f"*Forecast:*\n{row['Forecast']}"},
                    {"type": "mrkdwn", "text": f"*Previous:*\n{row['Previous']}"},
                    {"type": "mrkdwn", "text": f"*Effect:*\n{row['Effect']}"},
                    {"type": "mrkdwn", "text": f"*Why it matters:*\n{row['why_it_matters']}"},
                ]
            },
            {
                "type": "context",
                "elements": [
                    {"type": "plain_text", "text": f"Date: {row['Date']}"},
                    {"type": "plain_text", "text": f"Time: {row['Europe_time_military']}"},
                ]
            },
            {"type": "divider"},
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://www.linkpicture.com/q/1645628917769.jpeg",
                        "alt_text": "EDEN_logo"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "Economic Webscraper by *Gabriel de Olaguibel*"
                    }
                ]
            }
        ]
    }
    requests.post(url=webhook_url, json=payload)

def process_data_rows(df, webhook_url):
    message_data_array = load_message_data()
    for index, row in df.iterrows():
        data_string = 'Date : {}, Time : {}, Currency : {}, Event : {}, Actual : {}, Forecast : {}, Previous : {}, Effect : {},  why_it_matters : {}'.format(row['Date'], row['Europe_time_military'], row['Currency'], row['Event'], row['Actual'], row['Forecast'], row['Previous'], row['Effect'], row['why_it_matters'])

        if data_string not in message_data_array:
            message_data_array.append(data_string)
            save_message_data(message_data_array)
            send_to_slack(row, webhook_url)

if __name__ == "__main__":
    # Usage
    load_dotenv()
    webhook_url = os.getenv('WEBHOOK_URL')
    final_df = scrape_economic_data()
    process_data_rows(final_df, webhook_url)
    print(final_df)