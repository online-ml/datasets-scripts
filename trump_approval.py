import pandas as pd


if __name__ == '__main__':

    # Load the polling data
    polls = pd.read_csv('approval_polllist.csv', parse_dates=['createddate'])
    top_pollsters = ['Gallup', 'Ipsos', 'Morning Consult', 'Rasmussen Reports/Pulse Opinion Research', 'YouGov']
    polls = polls.query('president == "Donald Trump" and subgroup == "All polls" and pollster in @top_pollsters')
    polls = polls[['pollster', 'createddate', 'adjusted_approve']]
    polls = polls.pivot_table(values='adjusted_approve', index='createddate', columns='pollster')

    # Extract the topline, which the approval score from FiveThirtyEight
    top_line = pd.read_csv('approval_topline.csv', parse_dates=['modeldate'])\
                 .query('president == "Donald Trump" and subgroup == "All polls"')\
                 .sort_values('modeldate')
    top_line = top_line[['modeldate', 'approve_estimate']]

    # Join the two together
    hist = top_line.join(polls, on='modeldate')
    hist['modeldate'] = hist['modeldate'].apply(lambda x: x.toordinal())
    hist = hist.rename(columns={
        'modeldate': 'ordinal_date',
        'approve_estimate': 'five_thirty_eight',
        'Rasmussen Reports/Pulse Opinion Research': 'rasmussen',
        'Gallup': 'gallup',
        'Ipsos': 'ipsos',
        'Morning Consult': 'morning_consult',
        'YouGov': 'you_gov'
    })
    hist = hist.ffill()
    hist = hist[~hist.isnull().any(axis='columns')]

    # Save
    hist.to_csv('trump_approval.csv', index=False)
