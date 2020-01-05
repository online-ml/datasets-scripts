import pandas as pd
from scipy.io import arff


if __name__ == '__main__':

    phishing = arff.loadarff('PhishingData.arff')
    df = pd.DataFrame(phishing[0]).astype(int)
    df = df.rename(columns={
        'SFH': 'empty_server_form_handler',
        'popUpWidnow': 'popup_window',
        'SSLfinal_State': 'https',
        'Request_URL': 'request_from_other_domain',
        'URL_of_Anchor': 'anchor_from_other_domain',
        'web_traffic': 'is_popular',
        'URL_Length': 'long_url',
        'age_of_domain': 'age_of_domain',
        'having_IP_Address': 'ip_in_url',
        'Result': 'is_phishing'
    })
    df = df.query('is_phishing != 0')
    df['is_phishing'] = df['is_phishing'].replace({-1: 0})
    df.to_csv('phishing.csv.gz', index=False)
