import requests
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()
api_key = os.getenv("API_KEY")


def download_video(file_id):
    url = f"https://api.minimaxi.chat/v1/files/retrieve?file_id={file_id}"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    response = requests.get(url, headers=headers)

    # レスポンスの詳細を表示
    # print("ステータスコード:", response.status_code)
    # print("Content-Type:", response.headers.get("Content-Type"))
    # print("レスポンスの長さ:", len(response.content))

    # レスポンスが成功した場合、ダウンロードURLを取得
    if response.status_code == 200:
        response_json = response.json()
        download_url = response_json.get("file", {}).get("download_url")
        if download_url:
            video_response = requests.get(download_url)
            if video_response.status_code == 200:
                # ファイルIDを使って動画の名前を付ける
                video_path = f"/Users/hikarimac/Documents/python/hailuo/output/{file_id}_video.mp4"
                with open(video_path, "wb") as video_file:
                    video_file.write(video_response.content)
                print(
                    f"ビデオが正常にダウンロードされました！ファイル名: {file_id}_video.mp4"
                )
            else:
                print(
                    "ビデオのダウンロードに失敗しました。ステータスコード:",
                    video_response.status_code,
                )
        else:
            print("ダウンロードURLが見つかりませんでした。")
    else:
        print(
            "ビデオのダウンロードに失敗しました。ステータスコード:",
            response.status_code,
        )
        print(response.text)


# # 例として、関数を呼び出す
# download_video("212083760619682")
