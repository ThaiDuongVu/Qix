@rem build game exe file for windows machine
@rem if pyinstaller not found then install it with pip
call pyinstaller --onefile main.py
call copy icon.png dist
call copy font.ttf dist