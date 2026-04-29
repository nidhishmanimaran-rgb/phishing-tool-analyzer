def classify_risk(urgency_present, links_present, greetings_present, fake_domains_present, blacklisted_present=False):
    indicators = {
        "Urgency": urgency_present,
        "Suspicious URL": links_present,
        "Generic Greeting": greetings_present,
        "Fake Domain": fake_domains_present,
        "Blacklisted Domain": blacklisted_present
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
        risk_score += 3  # Higher for blacklisted
    
    if risk_score >= 7:
        risk = "Phishing"
    elif risk_score >= 3:
        risk = "Suspicious"
    else:
        risk = "Safe"
    
    return risk, indicators, risk_score