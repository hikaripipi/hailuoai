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
    # 画像とプロンプトを設定
    image_path = "/Users/hikarimac/Documents/python/hailuo/2girls, {{{comic}}}, manga,  s-2538467477.png"
    prompt = ""

    # 生成したい動画の数を指定
    # 生成したい動画の数を指定
    num_videos = 3
    task_ids = []

    # すべての動画生成リクエストを送信
    for i in range(num_videos):
        print(f"動画 {i+1} の生成リクエストを送信中...")
        task_id = generate_video_from_image(image_path, prompt)
        if task_id:
            task_ids.append(task_id)
        else:
            print(f"動画 {i+1} のタスクIDの取得に失敗しました。")

    # すべてのタスクのステータスを確認
    while task_ids:
        for task_id in task_ids[:]:  # コピーを使ってループ中にリストを変更
            status, file_id = query_video_generation_status(api_key, task_id)
            print(f"タスクID: {task_id}, ステータス: {status}")
            if status == "Success":
                download_video(file_id)
                task_ids.remove(task_id)  # 成功したタスクをリストから削除
            elif status == "Fail":
                print(f"タスクID {task_id} が失敗しました。")
                task_ids.remove(task_id)  # 失敗したタスクをリストから削除

        if task_ids:
            print("まだ処理中のタスクがあります。1分後に再確認します。")
            time.sleep(60)  # 1分待機


if __name__ == "__main__":
    main()
