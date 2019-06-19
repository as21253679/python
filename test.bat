@ECHO OFF

:loop 
	choice /t 2 /d y /n >nul
	start "" "C:\Windows\System32\calc.exe"
	goto loop

PAUSE
ECHO finish
