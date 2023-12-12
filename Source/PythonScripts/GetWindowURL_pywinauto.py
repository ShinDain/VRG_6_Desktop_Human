from pywinauto import Desktop

_curr_window = Desktop(backend="uia").window(title_re='.*Chrome.*')
_address_bar_wrapper = None

def _format_url(url):
    if url and not url.startswith("https://"): 
        return "http://" + url
    return url

def _findChromeProcess(ProcessExist):
    global _curr_window
    global _address_bar_wrapper
    if ProcessExist:
        _address_bar_wrapper = _curr_window.Edit.wrapper_object()
        return _address_bar_wrapper
    else:
        _address_bar_wrapper = None
        return -1 # Chrome Process Not Found

def GetCurrentURL():
    global _curr_window
    global _address_bar_wrapper
    ProcessExist = _curr_window.exists()
    if not ProcessExist or _address_bar_wrapper == None:
        rev = _findChromeProcess(ProcessExist)
        if rev == -1:
            return "Chrome Process Not Found"
    if _address_bar_wrapper != None:
        url = _address_bar_wrapper.iface_value.CurrentValue
        return _format_url(url)
    return "Fail To Get URL"

if __name__ == '__main__':
    while(True):
        val = input("현재 열려있는 Chrome의 URL을 획득하시려면 Enter를 눌러주세요 (종료=0)")
        if(val == '0'):
            break
        print(GetCurrentURL())
        print()
    input("Press Enter to end Program")