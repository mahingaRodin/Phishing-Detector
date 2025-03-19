import pandas as pd # type: ignore
import requests # type: ignore
import re
from bs4 import BeautifulSoup # type: ignore
from urllib.parse import urlparse
from nltk.tokenize import word_tokenize # type: ignore
import nltk # type: ignore


nltk.download('punkt')

#function to load phishing urls from phishtank 
def get_phishing_urls():
    url = "https://phishstats.info/phish_score.csv"
    df = pd.read_csv(url)
    phishing_urls = df['url'].tolist()
    return phishing_urls

# Function to extract features from a URL
def extract_url_features(url):
    parsed_url = urlparse(url)
    return {
        "url_length": len(url),
        "domain_age": 0,  # We will compute later
        "https": 1 if parsed_url.scheme == "https" else 0,
        "num_subdomains": len(parsed_url.netloc.split(".")) - 1
    }

# Function to extract text from a website
def get_website_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except:
        return ""

# Example: Load phishing data and extract features
phishing_urls = get_phishing_urls()
phishing_features = [extract_url_features(url) for url in phishing_urls[:10]]

print(phishing_features)