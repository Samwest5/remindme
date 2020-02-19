import os
import slack
import datetime
import time
import json

slack_token = os.environ["REMINDMETOKEN"]

last_checked_time = ""

with open("officeHours.json", "r") as file:
  office_hours = json.load(file)

day_mapping = {
  0: "Monday",
  1: "Tuesday",
  2: "Wednesday",
  3: "Thursday",
  4: "Friday",
  5: "Saturday",
  6: "Sunday"
}

def get_time():
  current_time = datetime.datetime.now()
  current_day = day_mapping[datetime.datetime.now().weekday()]
  return f"{current_day} {current_time.hour}:{current_time.minute}"

def send_reminder(body, target_channel):
  print('here too')
  web_client.chat_postMessage(
    channel=target_channel,
    text=f"@channel Office Hours beginning in 30 minutes:\n *{body}* ",
    as_user=True
  )

def is_office_hours(time):
  return time in office_hours

def bot():
  global last_checked_time
  time.sleep(1)
  current_time = get_time()
  if is_office_hours(current_time) and current_time != last_checked_time:
    for overlap in office_hours[current_time]:
      send_reminder(overlap[0], overlap[1])
  last_checked_time = current_time

web_client = slack.WebClient(token=slack_token)
while True:
  bot()
    
