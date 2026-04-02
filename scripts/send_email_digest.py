#!/usr/bin/env python3
import json
import os
import smtplib
from email.mime.text import MIMEText
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIGEST_PATH = ROOT / 'output' / 'email_digest.json'


def main() -> int:
    if not DIGEST_PATH.exists():
        raise SystemExit('Missing output/email_digest.json')

    data = json.loads(DIGEST_PATH.read_text())
    to_addr = os.getenv('DIGEST_EMAIL_TO', data.get('to', ''))
    from_addr = os.getenv('SMTP_FROM', '')
    smtp_host = os.getenv('SMTP_HOST', '')
    smtp_port = int(os.getenv('SMTP_PORT', '465'))
    smtp_user = os.getenv('SMTP_USER', '')
    smtp_pass = os.getenv('SMTP_PASS', '')

    if not all([to_addr, from_addr, smtp_host, smtp_user, smtp_pass]):
        raise SystemExit('Missing SMTP/DIGEST_EMAIL_TO configuration')

    lines = [
        'Weekly Personalized-LLMs arXiv Digest',
        f"Date: {data.get('date', '')}",
        'Source: arXiv only',
        ''
    ]

    items = data.get('items', [])
    if not items:
        lines.append('No qualified new papers this week.')
    else:
        lines.append(f'Accepted papers: {len(items)}')
        lines.append('')
        for idx, item in enumerate(items, start=1):
            lines.extend([
                f'{idx}. {item.get("title", "")}',
                f'Category: {item.get("category", "")}',
                f'Link: {item.get("link", "")}',
                'Summary:',
                item.get('summary', ''),
                ''
            ])

    msg = MIMEText('\n'.join(lines), 'plain', 'utf-8')
    msg['Subject'] = data.get('subject', 'Weekly Personalized-LLMs arXiv Digest')
    msg['From'] = from_addr
    msg['To'] = to_addr

    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(smtp_user, smtp_pass)
        server.sendmail(from_addr, [to_addr], msg.as_string())

    print(f'Email sent to {to_addr}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
