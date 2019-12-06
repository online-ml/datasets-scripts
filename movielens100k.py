import datetime
import numpy as np
import pandas as pd


if __name__ == '__main__':

    # Load and process ratings
    names = ['user', 'item', 'rating', 'timestamp']
    dtype = {'user': str, 'item': str, 'rating': np.float64}

    def date_parser(timestamp):
        return datetime.datetime.fromtimestamp(float(timestamp))

    df = pd.read_csv('ml-100k/u.data', sep='\t', names=names, dtype=dtype,
                     parse_dates=['timestamp'], date_parser=date_parser)

    df['timestamp'] = df['timestamp'].map(lambda x: x.value)
    df.sort_values(by='timestamp', inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Load and process item infos
    names = [
        'item',
        'title',
        'release_date',
        'video_release_date',
        'imdb_url',
        'unknown',
        'action',
        'adventure',
        'animation',
        'children_s',
        'comedy',
        'crime',
        'documentary',
        'drama',
        'fantasy',
        'film_noir',
        'horror',
        'musical',
        'mystery',
        'romance',
        'sci_fi',
        'thriller',
        'war',
        'western'
    ]

    to_remove = ['video_release_date', 'imdb_url']
    usecols = [name for name in names if name not in to_remove]

    dtype = {name: np.uint8 for name in names[5:]}
    dtype['item'] = str

    item_infos = pd.read_csv('ml-100k/u.item', sep='|', engine='python', names=names, dtype=dtype,
                             usecols=usecols, parse_dates=['release_date'])

    item_infos['release_date'] = item_infos['release_date'].map(lambda x: x.value)
    item_infos['title'].replace('unknown', np.nan, inplace=True)

    genres = item_infos.drop(columns=['item', 'title', 'release_date'])

    item_infos['genre'] = genres.apply(
        lambda row: ', '.join([genre for genre, occurs in zip(genres.columns, row) if occurs]),
        axis=1
    )

    item_infos = item_infos[['item', 'title', 'release_date', 'genre']]

    # Load and process user infos
    names = ['user', 'age', 'gender', 'occupation', 'zip_code']
    dtype = {'user': str, 'age': np.uint8}

    user_infos = pd.read_csv('ml-100k/u.user', sep='|', names=names, dtype=dtype)

    user_infos['occupation'].replace('none', np.nan, inplace=True)

    # Merge everything together and save to csv file
    df = df.merge(item_infos, how='left', on='item')
    df = df.merge(user_infos, how='left', on='user')

    df.to_csv('ml_100k.csv', sep='\t', index=False)
