import time
import schedule
from datetime import datetime
from zoomus import ZoomClient

# Zoom API credentials
API_KEY = 'YOUR_ZOOM_API_KEY'
API_SECRET = 'YOUR_ZOOM_API_SECRET'

client = ZoomClient(API_KEY, API_SECRET)

# Function to get the meeting participants
def get_meeting_participants(meeting_id):
    response = client.meeting.get(id=meeting_id)
    if response.status_code == 200:
        meeting_info = response.json()
        participants = meeting_info.get('participants', [])
        return participants
    else:
        print(f"Error getting meeting participants: {response.text}")
        return []

# Function to send a chat message
def send_chat_message(user_id, message):
    response = client.chat_post_message(
        to_contact=user_id,
        message=message
    )
    print(f"Sent message to {user_id}: {response}")

# Function to get participants in a specific breakout room
def get_breakout_room_participants(meeting_id, breakout_room_name):
    participants = get_meeting_participants(meeting_id)
    breakout_room_participants = []
    
    for participant in participants:
        if participant.get('breakout_room') == breakout_room_name:
            breakout_room_participants.append(participant['user_id'])
    
    return breakout_room_participants

# Function to remind for breaks in a specific breakout room
def break_reminder(meeting_id, breakout_room_name, break_time):
    participants = get_breakout_room_participants(meeting_id, breakout_room_name)
    message = f"In 5 minutes it is time for a break at {break_time}! 🕒"
    
    for user_id in participants:
        send_chat_message(user_id, message)

# Meeting ID and breakout room name
MEETING_ID = 'YOUR_MEETING_ID'
BREAKOUT_ROOM_NAME = 'YOUR_BREAKOUT_ROOM_NAME'

# Schedule the reminders
def schedule_weekday_reminders():
    if datetime.today().weekday() < 5:  # Monday to Friday are 0-4
        schedule.every().day.at("10:25").do(break_reminder, meeting_id=MEETING_ID, breakout_room_name=BREAKOUT_ROOM_NAME, break_time="10:30")
        schedule.every().day.at("11:55").do(break_reminder, meeting_id=MEETING_ID, breakout_room_name=BREAKOUT_ROOM_NAME, break_time="12:00")
        schedule.every().day.at("14:55").do(break_reminder, meeting_id=MEETING_ID, breakout_room_name=BREAKOUT_ROOM_NAME, break_time="15:00")
        schedule.every().day.at("16:25").do(break_reminder, meeting_id=MEETING_ID, breakout_room_name=BREAKOUT_ROOM_NAME, break_time="16:30")

# Initialize the schedule
schedule_weekday_reminders()

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)