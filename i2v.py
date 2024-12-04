import requests
import json
import base64
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()
api_key = os.getenv("API_KEY")
url = "https://api.minimaxi.chat/v1/video_generation"


def generate_video_from_image(image_path):
    # 画像をbase64にエンコード
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    payload = json.dumps(
        {
            "model": "video-01",
            "prompt": "1girl eating cake",
            "first_frame_image": f"data:image/jpeg;base64,{base64_image}",
        }
    )

    headers = {"authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        response_data = response.json()
        task_id = response_data.get("task_id")
        print(f"タスクID: {task_id}")
        return task_id
    else:
        print("動画生成リクエストが失敗しました。")
        return None


# # 関数を呼び出す
# generate_video_from_image(
#     "/Users/hikarimac/Documents/python/hailuo/comic, manga, eating, food, cake s-2934502518_declutter.png"
# )
