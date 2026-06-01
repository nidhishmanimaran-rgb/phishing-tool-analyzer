import re

def detect_urgency(text):
    urgency_keywords = ["urgent", "immediate", "act now", "limited time", "deadline", "emergency"]
    text_lower = text.lower()
    found = [kw for kw in urgency_keywords if kw in text_lower]
    return bool(found), found

def detect_generic_greetings(text):
    generic_greetings = ["dear user", "hello customer", "dear valued customer", "hello friend"]
    text_lower = text.lower()
    found = [greeting for greeting in generic_greetings if greeting in text_lower]
    return bool(found), found

def detect_spelling_grammar_issues(text):
    common_mistakes = [
        "your'e", "recieve", "adress", "seperate", "occured", "definately",
        "congradulations", "accountt", "passw0rd", "verifiy", "urgant"
    ]
    text_lower = text.lower()
    issues = [mistake for mistake in common_mistakes if mistake in text_lower]

    if re.search(r'[!?]{2,}', text):
        issues.append("Repeated punctuation")

    if re.search(r'[A-Z]{3,}', text) and len(re.findall(r'[A-Z]{3,}', text)) > 3:
        issues.append("Excessive capitalization")

    if re.search(r'\.[ \t\n]+[a-z]', text):
        issues.append("Possible sentence capitalization issues")

    return bool(issues), issues