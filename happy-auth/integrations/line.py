from integrations.base import BaseIntegration
import requests
from datetime import datetime


class LineIntegration(BaseIntegration):
    
    def login(self, data: dict):
        
        url = "https://access.line.me/oauth2/v2.1/authorize"
        params = {
            "response_type": "code",
            "client_id": 1656110429,
            "redirect_uri": "http://localhost:8000/healthcheck",
            "state": str(datetime.now()), # unique per request
            "scope": "profile%20openid"
        }
        response = requests.get(url = url, params = params)
        print(response.text.encode('utf8'))
