import subprocess
import datetime

print("🚀 Đang khởi động auto push...")

def run_git_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

try:
    # 1. Check có thay đổi không
    status, _ = run_git_command(["git", "status", "--porcelain"])

    if not status:
        print("✅ Không có thay đổi nào → không cần push")
    else:
        print("-> Có thay đổi, đang xử lý...")

        # 2. Add
        subprocess.run(["git", "add", "."], check=True)

        # 3. Commit (message theo thời gian)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"auto update {now}"

        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # 4. Pull trước (tránh conflict)
        subprocess.run(["git", "pull", "--rebase"], check=True)

        # 5. Push
        subprocess.run(["git", "push"], check=True)

        print("🎉 Đã push thành công!")

except subprocess.CalledProcessError as e:
    print("\n❌ Lỗi khi chạy Git:")
    print(e)