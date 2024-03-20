# streamlit_app.py

import streamlit as st
import plotly.express as px
import pandas as pd

from queries import au_stats, queensland_stats_city, queensland_stats_asn, queensland_median_city

# Set up tabs


tab1, tab2, tab3 = st.tabs(["Australia", "Queensland Per City", "Queesnland Per ASN"])


# ---------------- Austrailia ----------------
with tab1:
    st.header("Australia Per State")


    # Get Data
    df = pd.read_csv('data/au_stats.csv')
    df_ = df.rename(columns={"state":"State", 'average':'Average Tests Per Day', 'total': 'Total Tests in 2024'})
    st.table(df_)

    # Total
    fig = px.pie(df, values='total', names='state', 
                 title='Total Number of Tests in Australia Per State in 2024')
    st.plotly_chart(fig)

    #Average
    df = df.sort_values(by=['average'], ascending=False)
    fig = px.bar(df, x='state', y='average', 
                 title='Average Tests Per Day in Australia Per State in 2024',
                 color='average')
    fig.update_layout(xaxis_title='State', yaxis_title="Average")
    st.plotly_chart(fig)

        # Get Median Data
    df = pd.read_csv('data/au_median.csv')
    df_ = df.rename(columns={"state":"State", 
                             'median_download':'Median Download (Mb/s)', 
                             'median_upload': 'Median Upload (Mb/s)',
                             'testcount': 'Number of Tests'})
    st.table(df_)


    # Plot Median Download
    df = df.sort_values(by=['median_download'], ascending=False)
    fig = px.bar(df, x='state', y='median_download', 
                 title='Median Download Per State in Australia in 2024',
                 color='median_download')
    fig.update_layout(xaxis_title='State', 
                      yaxis_title="Median Download (Mb/s)")
    fig.update_coloraxes(colorbar_title_text="Mb/s")
    st.plotly_chart(fig)

    # Plot Median Upload
    df = df.sort_values(by=['median_upload'], ascending=False)
    fig = px.bar(df, x='state', y='median_upload', 
                 title='Median Upload (Mb/s) Per State in Australia in 2024',
                 color='median_upload')
    fig.update_layout(xaxis_title='State', yaxis_title="Median Upload (Mb/s)")
    fig.update_coloraxes(colorbar_title_text="Mb/s")
    st.plotly_chart(fig)

# ---------------- Queensland Per City ----------------
with tab2: 
    st.header("Queensland Per City")

    st.subheader("Stats")

    # Get Stats Data
    df = pd.read_csv('data/queensland_stats_city.csv')
    df_ = df.rename(columns={"state":"State", 'average':'Average Tests Per Day', 'total': 'Total Tests in 2024'})
    st.table(df_)

    # Total
    fig = px.pie(df, values='total', names='city', title='Total Number of Tests in Queensland Per City in 2024')
    fig.update_traces(textposition='inside')
    st.plotly_chart(fig)

    #Average
    df = df.sort_values(by=['average'], ascending=False)
    fig = px.bar(df, x='city', y='average', 
                 title='Average Tests Per Day in Queensland Per City in 2024',
                 color='average')
    fig.update_layout(xaxis_title='City', yaxis_title="Average")
    st.plotly_chart(fig)

    st.subheader("Median Performance")

    # Get Median Data
    df = pd.read_csv('data/queensland_median_city.csv')
    df_ = df.rename(columns={"city":"City", 
                             'median_download':'Median Download (Mb/s)', 
                             'median_upload': 'Median Upload (Mb/s)',
                             'testcount': 'Number of Tests'})
    st.table(df_)

    # Plot Median Download
    df = df.sort_values(by=['median_download'], ascending=False)
    fig = px.bar(df, x='city', y='median_download', 
                 title='Median Download Per City in Queensland in 2024',
                 color='median_download')
    fig.update_layout(xaxis_title='City', yaxis_title="Median Download (Mb/s)")
    fig.update_coloraxes(colorbar_title_text="Mb/s")
    st.plotly_chart(fig)

    # Plot Median Upload
    df = df.sort_values(by=['median_upload'], ascending=False)
    fig = px.bar(df, x='city', y='median_upload', 
                 title='Median Upload Per City in Queensland in 2024',
                 color='median_upload')
    fig.update_layout(xaxis_title='City', yaxis_title="Median Upload (Mb/s)")
    fig.update_coloraxes(colorbar_title_text="Mb/s")
    st.plotly_chart(fig)

# ---------------- Queensland Per ASN ----------------
with tab3: 
    st.header("Queensland Per Top 10 Autonomous System Name (ASN)")

    st.subheader("Stats")

    # Get Data
    df = pd.read_csv('data/queensland_stats_asn.csv')
    df_ = df.rename(columns={"state":"State", 'average':'Average Tests Per Day', 'total': 'Total Tests in 2024'})
    st.table(df_)

    # Total
    fig = px.pie(df, values='total', names='ASName', title='Total Number of Tests in Queensland Per Top 10 ASN in 2024')
    st.plotly_chart(fig)

    #Average
    df = df.sort_values(by=['average'], ascending=False)
    fig = px.bar(df, x='ASName', y='average', 
                 title='Average Tests Per Day in Queensland Per Top 10 ASN in 2024',
                 color='average')
    fig.update_layout(xaxis_title='ASN', yaxis_title="Average")
    st.plotly_chart(fig)

    st.subheader("Median Performance")

    # Get Median Data
    df = pd.read_csv('data/queensland_median_asn.csv')
    df_ = df.rename(columns={"ASName":"ASN", 
                             'median_download':'Median Download (Mb/s)', 
                             'median_upload': 'Median Upload (Mb/s)',
                             'testcount': 'Number of Tests'})
    st.table(df_)

    # Plot Median Download
    df = df.sort_values(by=['median_download'], ascending=False)
    fig = px.bar(df, x='ASName', y='median_download', 
                 title='Median Download Per Top 10 ASN in Queensland in 2024',
                 color='median_download')
    fig.update_layout(xaxis_title='ASN', yaxis_title="Median Download (Mb/s)")
    fig.update_coloraxes(colorbar_title_text="Mb/s")
    st.plotly_chart(fig)

      # Plot Median Upload
    df = df.sort_values(by=['median_upload'], ascending=False)
    fig = px.bar(df, x='ASName', y='median_upload', 
                 title='Median Upload (Mb/s) Per Top 10 ASN in Queensland in 2024',
                 color='median_upload')
    fig.update_layout(xaxis_title='ASN', yaxis_title="Median Upload (Mb/s)")
    fig.update_coloraxes(colorbar_title_text="Mb/s")
    st.plotly_chart(fig)