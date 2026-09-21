from youtube_transcript_api import YouTubeTranscriptApi

video_id = "dQw4w9WgXcQ"

transcript = YouTubeTranscriptApi().fetch(video_id)

for snippet in transcript:
    print(snippet.text)