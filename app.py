from flask import Flask, request, render_template
from text_analyzer import detect_urgency, detect_generic_greetings
from link_checker import detect_suspicious_links, detect_fake_domains, detect_blacklisted_domains
from risk_classifier import classify_risk

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email_text = request.form['email_text']
        
        urgency_present, urgency_found = detect_urgency(email_text)
        links_present, links_found = detect_suspicious_links(email_text)
        greetings_present, greetings_found = detect_generic_greetings(email_text)
        fake_domains_present, fake_domains_found = detect_fake_domains(email_text)
        blacklisted_present, blacklisted_found = detect_blacklisted_domains(email_text)
        
        risk, indicators, score = classify_risk(urgency_present, links_present, greetings_present, fake_domains_present, blacklisted_present)
        
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
        
        tips = []
        if risk == "Phishing":
            tips.append("Do not click any links or provide personal information.")
            tips.append("Verify the sender's email address.")
            tips.append("Contact the organization directly through official channels.")
        elif risk == "Suspicious":
            tips.append("Be cautious with links and attachments.")
            tips.append("Check for spelling errors or unusual requests.")
        else:
            tips.append("This email appears safe, but always stay vigilant.")
        
        return render_template('index.html', risk=risk, score=score, indicators=indicators, reasons=reasons, tips=tips, email_text=email_text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)