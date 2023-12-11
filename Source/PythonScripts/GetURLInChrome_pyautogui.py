import pygetwindow as gw
import pyautogui
import pyperclip
import time

def get_active_window_url():
    # 현재 마우스 커서 위치의 활성 창 가져오기
    active_window = gw.getWindowsWithTitle(gw.getActiveWindowTitle())[0]

    # 활성 창이 크롬 브라우저인지 확인
    if "Chrome" in active_window.title:
        pyautogui.hotkey('ctrl', 'l')  # URL 전체 선택
        pyautogui.hotkey('ctrl', 'c')  # 클립보드로 복사
        pyautogui.hotkey('esc')  # 드래그 취소

        # 클립보드에서 URL 가져오기
        url = pyperclip.paste()
        return url
    else:
        return "현재 활성 창이 크롬 브라우저가 아닙니다."

# URL 출력
if __name__ == '__main__':
    while(1):
        url = get_active_window_url()
        print("현재 열려있는 크롬 창의 URL:", url)
        time.sleep(5)
