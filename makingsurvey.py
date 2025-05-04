from google.oauth2 import service_account
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import os

SERVICE_ACCOUNT_FILE = '/home/rybokot/Desktop/northernpikee.github.io/scripts/klucz/service_account.json'





creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=['https://www.googleapis.com/auth/forms', 
                'https://www.googleapis.com/auth/drive']
    )
forms_service = build('forms', 'v1', credentials=creds)
drive_service = build('drive', 'v3', credentials=creds)



with open('/home/rybokot/Desktop/northernpikee.github.io/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')


question = "choose best fish, no more than 4"

path='https://raw.githubusercontent.com/northernpikee/northernpikee.github.io/refs/heads/main/'

answers = []
for dt in soup.find_all('dt'): 

    dds = dt.find_next_siblings('dd',limit=2)
 
    answer_text = dds[0].get_text(strip=True)
    image_tag = dds[1].find('img')
    if image_tag:
     image=image_tag['src'] 
     image_url=path+image
     answers.append({'text': answer_text, 'image': image_url})
    else: None
    
    
    
print(answers)

SERVICE_ACCOUNT_FILE = 'klucz/service_account.json'
SCOPES = ['https://www.googleapis.com/auth/forms.body']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('forms', 'v1', credentials=creds)



form = {
    "info": {
        "title": "fish of the april",
    }
}
result = service.forms().create(body=form).execute()




question_request = {
    "requests": [{
        "createItem": {
            "item": {
                "title": "choose best fish, no more than 4",  # Question text
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "CHECKBOX",  # Radio buttons (single choice)
                            "options": [
                                { 
                                    "value": ans['text'],  # Answer text
                                    "image": {
                                        "sourceUri": ans['image'],  # Image URL
                                        "altText": ans['text']      # Alt text
                                    }
                                } for ans in answers  # Loop through answers
                            ],
                            "shuffle": False  # Keep original order
                        }
                    }
                }
            },
            "location": {"index": 0}  # Add as first question
        }
    }]
}

service.forms().batchUpdate(
    formId=result["formId"], body=question_request).execute()


drive_service.permissions().create(
            fileId=result["formId"],
            body={
                'type': 'user',
                'role': 'writer',
                'emailAddress': 'mtrznadel3@gmail.com'
            },
            sendNotificationEmail=False
        ).execute()

print(f"✅ Survey created: https://docs.google.com/forms/d/{result['formId']}/edit")




