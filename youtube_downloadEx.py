from pytube import YouTube

def download_video(url, resolution="720p"):
  """
  YouTube 영상을 다운로드하는 함수입니다.

  Args:
    url: 다운로드하려는 YouTube 영상의 URL입니다.
    resolution: 다운로드하려는 해상도입니다. 기본값은 720p입니다.

  Returns:
    다운로드 성공 여부 (True/False)
  """
  try:
    yt = YouTube(url)

    # 해당 해상도의 스트림 찾기
    stream = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()
    if stream is None:
      print(f"{resolution} 해상도의 영상을 찾을 수 없습니다. 가장 높은 해상도로 다운로드합니다.")
      stream = yt.streams.get_highest_resolution()

    # 영상 다운로드
    print(f"다운로드 시작: {yt.title}")
    stream.download()
    print(f"다운로드 완료: {yt.title}")
    return True

  except Exception as e:
    print(f"다운로드 오류: {e}")
    return False

# 사용 예시
video_url = url = 'https://youtu.be/gvXsmI3Gdq8'

download_video(video_url)