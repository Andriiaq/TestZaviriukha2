import pandas as pd

aws = pd.read_csv('acme_worksheet.csv')
aws.Date = (pd.to_datetime(aws.Date, format='%b %d %Y'))

new_aws = pd.pivot_table(aws, index='Employee Name', columns='Date', values='Work Hours')
new_aws.index.name = 'Name / Date'
new_aws.columns = new_aws.columns.strftime('%Y-%m-%d')
new_aws.fillna(0, inplace=True)
new_aws.to_csv('new_acme_worksheet.csv')
