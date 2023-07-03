

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
import plotly.graph_objects as go
import urllib.request

# Open the URL with redirection handling

def main():
    # Load data

    csv_url = 'https://raw.githubusercontent.com/balazsfazekasdiss/pub1/tryingvscodealt/output.csv'
    with urllib.request.urlopen(csv_url, allow_redirects=True) as req:
        df = pd.read_csv(req)
    #df = pd.read_csv(csv_url)
    
    # Create a list of pages
    pages = ['Home', 'I. Literature Review', 'II. Methods used report', 'III. Visualizations', 'IV. CFA & SEM', 'V. Research Questions', 'VI. Appendix and Code']

    # Create a selectbox for navigation
    page = st.sidebar.selectbox('Page Navigation', options=pages)

    if page == 'Home':
        st.title('Balazs Fazekas Dissertation Intermediate Presentation')
        st.title('Promotor: Geert Molenberghs')

    elif page == 'I. Literature Review':
        st.title('Literature Review')
        st.write('To be added')
        pass  # You can add the content of the literature review here

    elif page == 'II. Methods used report':
        st.title('Methods Used Report')
        st.write('To be added')
        pass  # You can add the content of the methods used report here

    elif page == 'III. Visualizations':
        st.title('Visualizations')

        # For the visualizations section, you can still use a dropdown menu to select different visualizations
        visualizations = ['Histogram', 'Pie Chart', 'Radar Chart', 'Radar Chart 2', 'Wordcloud', 'Trend Chart']
        selected_visualization = st.selectbox('Select a visualization:', visualizations)

        if selected_visualization == 'Histogram':

            pass
            # Convert the 'score' column to integer type
            df['score'] = df['score'].astype(int)

            # Get the unique titles
            titles = df['title'].unique()

            # Add a selectbox to the sidebar:
            title = st.sidebar.selectbox('Select a movie:', titles)

            # Filter dataframe for the current title
            df_title = df[df['title'] == title]

            # Create a histogram
            fig = px.histogram(df_title, x="score", nbins=5)  # Set the number of bins to 5
            fig.update_traces(marker=dict(line=dict(width=1,color='DarkSlateGrey')))  # Add lines between bars
            fig.update_layout(title_text='Sentiment Score Distribution')
            st.plotly_chart(fig)  # Display the plot in Streamlit# Your code for the first visualization goes here

        elif selected_visualization == 'Pie Chart':
            pass
            # Get the unique titles
            titles = df['title'].unique()

            # Add a selectbox to the sidebar:
            title = st.sidebar.selectbox(
            'Select a movie:', titles)

            # Filter dataframe for the current title
            df_title = df[df['title'] == title]

            # Count the frequency of each score
            score_counts = df_title['score'].value_counts()

            # Create a pie chart
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.figure(figsize=(10, 6))
            plt.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%')
            plt.title(f'Distribution of Sentiment Scores for {title}')
            st.pyplot(plt)# Your code for the second visualization goes here

        elif selected_visualization == 'Radar Chart':
            pass
            # Create a radar chart for each movie
            categories = df['title'].unique()
            N = len(categories)

            values = df.groupby('title')['score'].mean().values.flatten().tolist()
            values += values[:1] # repeat the first value to close the circular graph

            plt.figure(figsize=(5,5))
            ax = plt.subplot(111, polar=True)

            plt.xticks(angles[:-1], categories, color='grey', size=8)
            ax.set_rlabel_position(0)
            plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=7)
            plt.ylim(0,5)

            ax.plot(angles, values, linewidth=1, linestyle='solid')
            ax.fill(angles, values, 'b', alpha=0.1)
            st.pyplot(plt.gcf())# Your code for the third visualization goes here

        elif selected_visualization == 'Radar Chart 2':
            pass
            df['score'] = df['score'].astype(int)

            # Get the average score for each movie
            average_scores = df.groupby('title')['score'].mean()

            # Add a multiselect to the sidebar:
            title = st.sidebar.multiselect('Select movies:', df['title'].unique())

            fig = go.Figure()

            for t in title:
              fig.add_trace(go.Scatterpolar(r=[average_scores[t]], theta=['Score'], fill='toself', name=t))

            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=True)

            st.plotly_chart(fig)  # Display the plot in Streamlit

        elif selected_visualization == 'Wordcloud':
            pass
            def wc(i):
              scores = df[df['score'] == i]
              joiner = ','.join(list(scores['content'].values))
              wordcloud = WordCloud(background_color="white", max_words=5000, contour_color='black')
              wordcloud.generate(joiner)

              plt.imshow(wordcloud, interpolation='bilinear')
              plt.axis("off")
              st.pyplot(plt.gcf())  # Display the plot in Streamlit

            for i in range(1,6):
              st.header(f'Wordcloud for scores of {i}')
              wc(i)# Your code for the fourth visualization goes here

        elif selected_visualization == 'Trend Chart':
            pass
            # Ensure your date column is in datetime format
            df['date'] = pd.to_datetime(df['date'])


            # Generate a list of unique movie titles
            movies = df['title'].unique().tolist()

            # Create a multiselect widget for movie titles
            selected_movies = st.multiselect('Choose movie titles', movies, default=movies)

            # Filter the dataframe based on the selected movies
            filtered_data = df[df['title'].isin(selected_movies)]

            # If there's any data to plot
            if not filtered_data.empty:

            # For each movie, calculate average score per day
              filtered_data = filtered_data.groupby(['date', 'title', 'content'])[['score']].mean().reset_index()

            # Create a time series plot
              fig = px.line(filtered_data, x='date', y='score', color='title', hover_data=['content'])

            # Update layout
              fig.update_layout(title="Sentiment Score Timeline", xaxis_title="Date", yaxis_title="Sentiment Score", legend_title="Movie Title", hovermode="closest")

            # Display the figure
              st.plotly_chart(fig)

            else:
              st.write("No data to display.")# Your code for the fourth visualization goes here

    elif page == 'IV. CFA & SEM':
        st.title('CFA & SEM')
        st.write('To be added')
        pass  # You can add the content of the CFA & SEM here

    elif page == 'V. Research Questions':
        st.title('Research Questions')
        st.write('Answers and Results to be added')
        research_question = ['Movie Popularity', 'Movie Critics and Movie Reviews', 'Social Media Popularity', 'Festival Success', 'Social Media Platforms']
        selected_question = st.selectbox('Select a Research Question:', research_question)
        if selected_question == 'Movie Popularity':
            st.write('Can a movie’s popularity on social media predict its success at film festivals, like the Oscars and others?') # You can add the content of the research questions here
            st.write('Does the popularity of a movie affect its success at film festivals?')
            st.write('Does an absolute frequency measure of popularity, indicated by the number of mentions and hashtags, matter more than the sentiment (positive/negative) behind the popularity?')
            pass
        elif selected_question == 'Movie Critics and Movie Reviews':
            st.write('Do movie critics and movie reviews affect the success of movies at film festivals?')
            pass
        elif selected_question == 'Social Media Popularity':
            st.write('Does social media popularity matter more than traditional movie reviews for a movie’s success at film festivals?')
            pass
        elif selected_question == 'Festival Success':
            st.write('Does the success of a movie at one festival affect its success at other festivals?')
            pass
        elif selected_question == 'Social Media Platforms':
            st.write('Which platform was the best at predicting success? Which platform, if any, had the most noticeable effect on movies’ success?')
            st.write('Does the success of a movie at film festivals, especially Oscars, affect its popularity on social media?')
            pass

    elif page == 'VI. Appendix and Code':
        st.title('Appendix and Code')
        st.write('To be added')

if __name__ == '__main__':
    main()
