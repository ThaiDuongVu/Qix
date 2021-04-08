@rem build game exe file for windows machine
@rem if pyinstaller not found then install it with pip
call mkdir qix
call copy icon.png qix
call copy font.ttf qix
call pyinstaller --onefile --noconsole --distpath ./qix --name qix --icon=FILE.ico main.py