# main.py
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Envoyer une requête GET pour récupérer le contenu du site
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parser le contenu HTML du site
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraire tous les paragraphes <p>
        paragraphs = soup.find_all('p')
        text_content = ' '.join([para.get_text() for para in paragraphs])
        
        return text_content
    else:
        return "Échec de la récupération du contenu."
