import re
from text_analyzer import detect_urgency, detect_generic_greetings
from link_checker import detect_suspicious_links, detect_fake_domains, detect_blacklisted_domains
from risk_classifier import classify_risk

def main():
    print("Phishing Detection Tool - Stage 2")
    print("Paste the email text below (press Enter twice to finish):")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    email_text = "\n".join(lines)
    
    urgency_present, urgency_found = detect_urgency(email_text)
    links_present, links_found = detect_suspicious_links(email_text)
    greetings_present, greetings_found = detect_generic_greetings(email_text)
    fake_domains_present, fake_domains_found = detect_fake_domains(email_text)
    blacklisted_present, blacklisted_found = detect_blacklisted_domains(email_text)
    
    risk, indicators, score = classify_risk(urgency_present, links_present, greetings_present, fake_domains_present, blacklisted_present)
    
    print(f"\nRisk Level: {risk}")
    print(f"Risk Score: {score}")
    print("Indicators Found:")
    for indicator, found in indicators.items():
        print(f"- {indicator}: {'Yes' if found else 'No'}")
    
    reasons = []
    if urgency_found:
        reasons.append(f"Urgency keywords: {', '.join(urgency_found)}")
    if links_found:
        reasons.append(f"Suspicious links: {', '.join(links_found)}")
    if greetings_found:
        reasons.append(f"Generic greetings: {', '.join(greetings_found)}")
    if fake_domains_found:
        reasons.append(f"Fake domains: {', '.join(fake_domains_found)}")
    if blacklisted_found:
        reasons.append(f"Blacklisted domains: {', '.join(blacklisted_found)}")
    
    if reasons:
        print("Details:")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("No suspicious indicators found.")

if __name__ == "__main__":
    main()