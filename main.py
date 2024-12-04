import time
from i2v import generate_video_from_image
from checkstatus import query_video_generation_status
from getvideo import download_video
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()
api_key = os.getenv("API_KEY")


def main():
    # # 画像から動画生成を開始し、タスクIDを取得
    # image_path = "/Users/hikarimac/Documents/python/hailuo/comic, manga, eating, food, cake s-2934502518_declutter.png"
    # task_id = generate_video_from_image(image_path)

    # if not task_id:
    #     print("タスクIDの取得に失敗しました。")
    #     return
    task_id = "122331555329900544"
    print(f"取得したタスクID: {task_id}")

    # ステータスを確認し、成功したらダウンロード
    while True:
        status, file_id = query_video_generation_status(api_key, task_id)
        print(f"現在のタスクID: {task_id}, ステータス: {status}")
        if status == "Success":
            download_video(file_id)
            break
        elif status == "Fail":
            print("タスクが失敗しました。")
            break
        else:
            print("タスクがまだ処理中です。1分後に再確認します。")
            time.sleep(60)  # 1分待機


if __name__ == "__main__":
    main()
