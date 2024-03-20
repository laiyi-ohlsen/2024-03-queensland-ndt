import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

from queries import au_stats, queensland_stats_city, queensland_stats_asn, queensland_median_city, queensland_median_asn
# Create API client.
project_id = 'measurement-lab'
location = 'US'
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(project=project_id, location=location,credentials=credentials)

# Get Data

# df = client.query(au_stats.query).to_dataframe()
# df.to_csv('data/au_stats.csv', index=False)  

# df = client.query(queensland_stats_city.query).to_dataframe()
# df = df[df['total'] > 1000]
# df.to_csv('data/queensland_stats_city.csv', index=False)  

# df = client.query(queensland_median_city.query).to_dataframe()
# df.to_csv('data/queensland_median_city.csv', index=False)  

# df = client.query(queensland_stats_asn.query).to_dataframe()
# df.to_csv('data/queensland_stats_asn.csv', index=False)


df = client.query(queensland_median_asn.query).to_dataframe()
df.to_csv('data/queensland_median_asn.csv', index=False)