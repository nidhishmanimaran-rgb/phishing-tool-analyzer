import re

def load_blacklist():
    try:
        with open('blacklist.txt', 'r') as f:
            return set(line.strip().lower() for line in f if line.strip())
    except FileNotFoundError:
        return set()

BLACKLIST = load_blacklist()

def detect_suspicious_links(text):
    # Simple regex for URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text)
    suspicious = [url for url in urls if url.startswith('http://') or not any(domain in url for domain in ['paypal.com', 'google.com', 'microsoft.com', 'amazon.com'])]
    return bool(suspicious), suspicious

def detect_fake_domains(text):
    # Extract domains from URLs
    url_pattern = r'http[s]?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    domains = re.findall(url_pattern, text)
    known_domains = ['paypal.com', 'google.com', 'microsoft.com', 'amazon.com', 'apple.com']
    fake = [domain for domain in domains if domain not in known_domains]
    return bool(fake), fake

def detect_blacklisted_domains(text):
    url_pattern = r'http[s]?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    domains = re.findall(url_pattern, text)
    blacklisted = [domain for domain in domains if domain.lower() in BLACKLIST]
    return bool(blacklisted), blacklisted