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