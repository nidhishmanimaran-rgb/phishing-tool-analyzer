from flask import Flask, request, render_template, Response
from text_analyzer import detect_urgency, detect_generic_greetings, detect_spelling_grammar_issues
from link_checker import detect_suspicious_links, detect_fake_domains, detect_blacklisted_domains
from email_header_analyzer import analyze_headers
from attachment_analyzer import analyze_attachments
from risk_classifier import classify_risk
from report_generator import build_report

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email_text = request.form.get('email_text', '')
        email_headers = request.form.get('email_headers', '')
        attachments = request.files.getlist('attachments')

        urgency_present, urgency_found = detect_urgency(email_text)
        links_present, links_found = detect_suspicious_links(email_text)
        greetings_present, greetings_found = detect_generic_greetings(email_text)
        grammar_present, grammar_found = detect_spelling_grammar_issues(email_text)
        fake_domains_present, fake_domains_found = detect_fake_domains(email_text)
        blacklisted_present, blacklisted_found = detect_blacklisted_domains(email_text)
        header_issues_present, header_findings, spoofing_present, spoofing_found = analyze_headers(email_headers)
        attachment_risk_present, suspicious_attachments, attachment_names = analyze_attachments(attachments)

        risk, indicators, score = classify_risk(
            urgency_present,
            links_present,
            greetings_present,
            fake_domains_present,
            blacklisted_present,
            header_issues_present,
            spoofing_present,
            grammar_present,
            attachment_risk_present
        )
        
        reasons = []
        if urgency_found:
            reasons.append(f"Urgency keywords: {', '.join(urgency_found)}")
        if links_found:
            reasons.append(f"Suspicious links: {', '.join(links_found)}")
        if greetings_found:
            reasons.append(f"Generic greetings: {', '.join(greetings_found)}")
        if grammar_found:
            reasons.append(f"Grammar/spelling issues: {', '.join(grammar_found)}")
        if fake_domains_found:
            reasons.append(f"Fake domains: {', '.join(fake_domains_found)}")
        if blacklisted_found:
            reasons.append(f"Blacklisted domains: {', '.join(blacklisted_found)}")
        if header_findings:
            reasons.append(f"Header analysis: {', '.join(header_findings)}")
        if spoofing_found:
            reasons.append(f"Sender spoofing indicators: {', '.join(spoofing_found)}")
        if suspicious_attachments:
            reasons.append(f"Suspicious attachments: {', '.join(suspicious_attachments)}")
        elif attachment_names:
            reasons.append(f"Attachments detected: {', '.join(attachment_names)}")
        
        tips = []
        if risk == "Phishing":
            tips.append("Do not click any links or provide personal information.")
            tips.append("Verify the sender's email address.")
            tips.append("Contact the organization directly through official channels.")
        elif risk == "Suspicious":
            tips.append("Be cautious with links and attachments.")
            tips.append("Check for spelling errors or unusual requests.")
            tips.append("Review the email headers for SPF/DKIM/DMARC authentication issues.")
        else:
            tips.append("This email appears safe, but always stay vigilant.")
            tips.append("Double-check the sender headers and attachments if you remain unsure.")
        
        action = request.form.get('action')
        if action == 'export':
            report_text = build_report(
                email_text,
                email_headers,
                urgency_found,
                links_found,
                greetings_found,
                grammar_found,
                fake_domains_found,
                blacklisted_found,
                header_findings,
                spoofing_found,
                suspicious_attachments,
                attachment_names,
                risk,
                score,
                indicators,
                tips
            )
            return Response(
                report_text,
                mimetype='text/plain',
                headers={
                    'Content-Disposition': 'attachment; filename=phishing_analysis_report.txt'
                }
            )

        return render_template(
            'index.html',
            risk=risk,
            score=score,
            indicators=indicators,
            reasons=reasons,
            tips=tips,
            email_text=email_text,
            email_headers=email_headers
        )
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)