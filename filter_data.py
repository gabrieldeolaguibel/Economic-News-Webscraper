import pandas as pd
from datetime import datetime, timezone, timedelta

def clean_df(df):
    df.drop(columns=['void', 'Detail_void', 'Graph_void', 'Impact'], inplace=True)
    df['Date'].replace(to_replace='', value=None, method='ffill', inplace=True)
    df['Time'].replace(to_replace='', value=None, method='ffill', inplace=True)
    df.drop(labels=df[df['Event'] == ''].index, inplace=True)
    df.insert(len(df.columns), 'Effect', None)
    df.insert(len(df.columns), 'why_it_matters', None)
    df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%a%b %d').strftime('%a, %b %d'))
    return df

def merge_dfs(df, df2):
    merged_df = df.merge(df2, on='Event', how='left')
    merged_df['Effect'] = merged_df['Effect_y'].fillna(merged_df['Effect_x'])
    merged_df['why_it_matters'] = merged_df['why_it_matters_y'].fillna(merged_df['why_it_matters_x'])
    merged_df = merged_df.drop(columns=['Effect_x','Effect_y','why_it_matters_x','why_it_matters_y'])
    return merged_df

def drop_tentative(df):
    df.drop(labels=df[df['Time'] == 'Tentative'].index, inplace=True)
    df.drop(labels=df[df['Time'] == 'All Day'].index, inplace=True)
    return df

def convert_time(time_str, from_time_zone, to_time_zone):
    time = datetime.strptime(time_str, '%I:%M%p').replace(tzinfo=from_time_zone)
    time = time.astimezone(to_time_zone)
    return time.strftime('%I:%M%p')

def apply_timezones(df, from_time_zone, to_time_zone):
    df['Europe_time'] = df['Time'].apply(convert_time, args=(from_time_zone, to_time_zone))
    df['Europe_time_military'] = df['Europe_time'].apply(lambda x: datetime.strptime(x, '%I:%M%p').strftime('%H:%M'))
    df.drop(columns=['Europe_time'], inplace=True)
    return df

def add_datetime(df):
    year = datetime.now().strftime('%Y')
    df['Datetime'] = df['Date'] + ' ' + year + ', ' + df['Time']
    df['Datetime'] = pd.to_datetime(df['Datetime'], format='%a, %b %d %Y, %I:%M%p')
    return df

def filter_past_events(df):
    date_actual = datetime.now() - timedelta(hours=6)
    df = df[df['Datetime'] <= date_actual]
    return df

def clean_date(df):
    df['Date'] = df['Date'].str.replace('(.*, )', '', regex=True)
    return df