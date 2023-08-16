@rem run3538.bat
@echo OFF
Set PSSEVERSION=35
set PYVER=38
Set PYTHONCODE=scripts\
Set PYTHONHOME=C:\Users\jsm20\AppData\Local\Programs\Python\Python38\
SET PSSEPATH=C:\Program Files\PTI\PSSE%psseversion%\%psseversion%.2\
SET PSSPYPATH=%PSSEPATH%\PSSPY38
SET PATH=%PYTHONHOME%;%PYTHONHOME%SCRIPTs;%pssepath%PSSBIN;%pssepath%PSSLIB;%PATH%
Set INCLUDE=%pssepath%PSSLIB;%INCLUDE%
echo ﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂ
echo   %USERNAME%                           
echo.                                        
echo   PATHs set: PSS/E-35 + python 3.8.8   
echo ‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹
echo %date% %time%
