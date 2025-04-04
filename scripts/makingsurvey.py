from google.oauth2 import service_account
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

SERVICE_ACCOUNT_FILE = 'service_account.json'
SCOPES = ['https://www.googleapis.com/auth/forms.body']

# creds = service_account.Credentials.from_service_account_file(
 #   SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# service = build('forms', 'v1', credentials=creds)


with open('../index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')


question = "choose best fish, no more than 4"


answers = []
for dt in soup.find_all('dt'): 

    dds = dt.find_next_siblings('dd',limit=2)
 
    answer_text = dds[0].get_text(strip=True)
    image_url = dds[1].get_text(strip=True)  
        
    answers.append({'text': answer_text, 'image': image_url})
    

    print(answers)

