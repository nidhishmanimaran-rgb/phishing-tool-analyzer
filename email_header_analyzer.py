import re

AUTH_RESULT_RE = re.compile(r'(spf|dkim|dmarc)\s*=\s*(pass|fail|neutral|softfail|none)', re.IGNORECASE)
HEADER_DOMAIN_RE = re.compile(r'^{name}:\s*<?[^@<\s]+@([^\s>]+)>?', re.IGNORECASE | re.MULTILINE)


def _find_auth_result(headers_text, tag):
    if not headers_text:
        return None

    pattern = re.compile(rf'{tag}\s*=\s*(pass|fail|neutral|softfail|none)', re.IGNORECASE)
    match = pattern.search(headers_text)
    if match:
        return match.group(1).lower()
    return None


def _extract_domain_from_header(headers_text, header_name):
    if not headers_text:
        return None

    pattern = re.compile(rf'^{header_name}:\s*<?[^@<\s]+@([^\s>]+)>?', re.IGNORECASE | re.MULTILINE)
    match = pattern.search(headers_text)
    if match:
        return match.group(1).lower()
    return None


def analyze_headers(headers_text):
    headers_text = headers_text or ''
    headers_text = headers_text.strip()
    if not headers_text:
        return False, ["No headers provided"], False, ["No headers provided"]

    spf = _find_auth_result(headers_text, 'spf')
    dkim = _find_auth_result(headers_text, 'dkim')
    dmarc = _find_auth_result(headers_text, 'dmarc')

    header_findings = []
    if spf:
        header_findings.append(f"SPF={spf}")
    if dkim:
        header_findings.append(f"DKIM={dkim}")
    if dmarc:
        header_findings.append(f"DMARC={dmarc}")
    if not header_findings:
        header_findings.append("No SPF/DKIM/DMARC authentication results found")

    from_domain = _extract_domain_from_header(headers_text, 'From')
    return_path_domain = _extract_domain_from_header(headers_text, 'Return-Path')
    if not return_path_domain:
        return_path_domain = _extract_domain_from_header(headers_text, 'Envelope-From')

    spoofing_reasons = []
    spoofing_present = False

    if from_domain and return_path_domain and from_domain != return_path_domain:
        spoofing_present = True
        spoofing_reasons.append(
            f"From domain ({from_domain}) differs from envelope domain ({return_path_domain})"
        )

    if spf and spf != 'pass':
        spoofing_present = True
        spoofing_reasons.append(f"SPF authentication result is {spf}")

    if dkim and dkim != 'pass':
        spoofing_present = True
        spoofing_reasons.append(f"DKIM authentication result is {dkim}")

    if dmarc and dmarc != 'pass':
        spoofing_present = True
        spoofing_reasons.append(f"DMARC authentication result is {dmarc}")

    header_issues_present = spoofing_present or any(
        result in {'fail', 'softfail', 'neutral', 'none'}
        for result in [spf, dkim, dmarc]
        if result is not None
    )

    return header_issues_present, header_findings, spoofing_present, spoofing_reasons
