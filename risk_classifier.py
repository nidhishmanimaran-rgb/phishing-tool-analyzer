def classify_risk(
    urgency_present,
    links_present,
    greetings_present,
    fake_domains_present,
    blacklisted_present=False,
    header_issues_present=False,
    spoofing_present=False,
    grammar_issues_present=False,
    attachment_risk_present=False
):
    indicators = {
        "Urgency": urgency_present,
        "Suspicious URL": links_present,
        "Generic Greeting": greetings_present,
        "Fake Domain": fake_domains_present,
        "Blacklisted Domain": blacklisted_present,
        "Header Authentication Issues": header_issues_present,
        "Sender Spoofing": spoofing_present,
        "Grammar/Spelling Issues": grammar_issues_present,
        "Suspicious Attachments": attachment_risk_present
    }
    
    risk_score = 0
    if urgency_present:
        risk_score += 1
    if links_present:
        risk_score += 2
    if greetings_present:
        risk_score += 1
    if fake_domains_present:
        risk_score += 2
    if blacklisted_present:
        risk_score += 3
    if header_issues_present:
        risk_score += 2
    if spoofing_present:
        risk_score += 3
    if grammar_issues_present:
        risk_score += 1
    if attachment_risk_present:
        risk_score += 2
    
    if risk_score >= 8:
        risk = "Phishing"
    elif risk_score >= 4:
        risk = "Suspicious"
    else:
        risk = "Safe"
    
    return risk, indicators, risk_score