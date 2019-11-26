import email
import warnings

import pandas as pd

from bs4 import BeautifulSoup


def parse_body(message):
    """Parses text body from email message object with BeautifulSoup.

    Parameters:
        message (email.Message object): Loaded email with Python standard library email module.

    Returns:
        body (str): Email text body.

    """
    body = ''

    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get('Content-Disposition'))

            if (content_type in ['text/html', 'text/txt'] and
                'attachment' not in content_disposition):
                body = part.get_payload(decode=True)
                break
    else:
        body = message.get_payload(decode=True)

    return BeautifulSoup(body, 'html5lib').get_text()


def stream_trec07p(dataset_path):
    """2007 TREC’s Spam Track dataset.

    The data contains 75,419 chronologically ordered items, i.e. 3 months of emails delivered
    to a particular server in 2007. Spam messages represent 66.6% of the dataset.
    The goal is to predict whether an email is a spam or not.

    Parsed features are: sender, recipients, date, subject, body.

    Parameters:
        dataset_path (str): The directory where the data is stored.

    Yields:
        tuple: 5 features (`sender`, `recipients`, `date`, `subject`, `body`) and `y` the target.

    References:
        1. `TREC 2007 Spam Track Overview <https://trec.nist.gov/pubs/trec16/papers/SPAM.OVERVIEW16.pdf>`_

    """
    warnings.filterwarnings('ignore', category=UserWarning, module='bs4')

    with open(f'{dataset_path}/full/index') as full_index:
        for row in full_index:
            label, filepath = row.split()
            ix = filepath.split('.')[-1]

            with open(f'{dataset_path}/data/inmail.{ix}', 'rb') as email_file:
                message = email.message_from_binary_file(email_file)
                yield (
                    message['from'],
                    message['to'],
                    message['date'],
                    message['subject'],
                    parse_body(message),
                    label
                )


if __name__ == '__main__':
    dataset_path = 'trec07p'
    parsed_emails = [parsed_email for parsed_email in stream_trec07p(dataset_path)]

    columns = ['sender', 'recipients', 'date', 'subject', 'body', 'y']
    df = pd.DataFrame(parsed_emails, columns=columns)

    df.to_csv('trec07p.csv.zip', index=False)
