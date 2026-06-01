import os

SUSPICIOUS_EXTENSIONS = {
    '.exe', '.scr', '.pif', '.bat', '.cmd', '.js', '.jar', '.vbs', '.wsf',
    '.zip', '.7z', '.rar', '.iso', '.msi', '.ps1', '.docm', '.xlsm', '.pptm'
}

SUSPICIOUS_CONTENT_TYPES = {
    'application/x-msdownload',
    'application/javascript',
    'application/x-sh',
    'application/x-bat',
    'application/x-msdos-program'
}


def analyze_attachments(files):
    attachments = [file for file in files if file.filename]
    if not attachments:
        return False, [], []

    suspicious = []
    attachment_names = []

    for attachment in attachments:
        filename = os.path.basename(attachment.filename)
        attachment_names.append(filename)
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in SUSPICIOUS_EXTENSIONS or attachment.content_type in SUSPICIOUS_CONTENT_TYPES:
            suspicious.append(filename)

    return bool(suspicious), suspicious, attachment_names
