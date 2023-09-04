def get_video_id():
    video_id = input("Enter the video id to do comment analysis:")
    return video_id
#def get_api_key:


def get_comments(response):
    comments=[]
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
    return comments
def get_max_count():
    max_count=input("Enter maximum number of comment to analyse (default=100) :")
    if not max_count:
        max_count=100
    return int(max_count)

