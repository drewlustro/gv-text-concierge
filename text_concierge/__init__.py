import requests

GOOGLE_APP_NUMBER = '1066516637089'
GOOGLE_APP_CLIENT_ID = '1066516637089.apps.googleusercontent.com'
GOOGLE_APP_EMAIL = '1066516637089@developer.gserviceaccount.com'
GOOGLE_APP_PASSWORD = 'notasecret'

GOOGLE_OAUTH2_URL = 'https://accounts.google.com/o/oauth2/device/code'
#https://www.googleapis.com/auth/userinfo.profile
SCOPE = 'https://www.googleapis.com/auth/userinfo.email'

GMAIL_FEED_URL = 'https://mail.google.com/mail/feed/atom'

r = requests.post(GOOGLE_OAUTH2_URL, params={
                    'client_id': GOOGLE_APP_CLIENT_ID,
                    'scope': SCOPE })


