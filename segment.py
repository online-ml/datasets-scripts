import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('segment.dat', sep=' ', header=None)
    df.columns = [
        'region-centroid-col',
        'region-centroid-row',
        'region-pixel-count',
        'short-line-density-5',
        'short-line-density-2',
        'vedge-mean',
        'vegde-sd',
        'hedge-mean',
        'hedge-sd',
        'intensity-mean',
        'rawred-mean',
        'rawblue-mean',
        'rawgreen-mean',
        'exred-mean',
        'exblue-mean',
        'exgreen-mean',
        'value-mean',
        'saturation-mean',
        'hue-mean',
        'category'
    ]
    df = df.drop(columns='region-pixel-count')
    df['category'] = df['category'].map({
        1: 'brickface',
        2: 'sky',
        3: 'foliage',
        4: 'cement',
        5: 'window',
        6: 'path',
        7: 'grass'
    })
    df = df.astype({'region-centroid-col': int, 'region-centroid-row': int})
    df.to_csv('segment.csv.zip', index=False)
