from tkinter import messagebox
import inspect


def safe_command(func, *args):
    # 전달된 함수가 필요한 인자의 수를 가져옴
    expected_args = len(inspect.signature(func).parameters)
    if len(args) != expected_args:
        raise TypeError(f"{func.__name__}() takes {expected_args} positional argument(s) but {len(args)} were given")

    def wrapper():
        try:
            func(*args)
        except Exception as e:
            messagebox.showerror("오류", f"예외 발생: {str(e)}")

    return wrapper
