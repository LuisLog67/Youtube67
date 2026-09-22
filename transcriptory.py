from youtube_transcript_api import YouTubeTranscriptApi

video_id = "Af6i6ChAVTw"

transcript = YouTubeTranscriptApi().fetch(video_id)

for snippet in transcript:
    print(snippet.text)