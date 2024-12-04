import requests
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()
api_key = os.getenv("API_KEY")


def query_video_generation_status(api_key, task_id):
    url = f"https://api.minimaxi.chat/v1/query/video_generation?task_id={task_id}"
    headers = {
        "authorization": f"Bearer {api_key}",
        "content-type": "application/json",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        status = data.get("status", "Unknown")
        # print(f"Task ID: {task_id}, Status: {status}")
        if status == "Success":
            file_id = data.get("file_id")
            # print(f"File ID: {file_id}")
            return status, file_id
        elif status == "Fail":
            print("The task failed.")
            return status, None
        else:
            print("The task is still processing.")
            return status, None
    else:
        print(f"Failed to query status. HTTP Status Code: {response.status_code}")
        return "Error", None


# # 使い方の例
# task_id = "122331555329900544"
# query_video_generation_status(api_key, task_id)
