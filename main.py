import comment_analysis
import inputs
import intro_and_outro
import plotgraph
import youtube_api_request


def main():
    try:
        intro_and_outro.intro()
        video_id = inputs.get_video_id()
        max_count = inputs.get_max_count()
        response = youtube_api_request.api_request(video_id,max_count)
        comments = inputs.get_comments(response)
        sentiments = comment_analysis.analyse_comments(comments)
        print("Positive=",sentiments['Positive']," Negative=",sentiments['Negative']," Neutral=",sentiments['Neutral'])
        plotgraph.bar_graph(sentiments)
        intro_and_outro.outro()
    except:
        print("An error occurred")

if __name__ == "__main__":
    main()