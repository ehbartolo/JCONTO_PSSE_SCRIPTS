@rem run3437.bat
@echo OFF
echo %date% %time%
Set PSSEVERSION=34
set PYVER=37
Set PYTHONCODE=scripts\
Set PYTHONHOME=C:\Python37\
SET PSSEPATH=%PROGRAMFILES(x86)%\PTI\PSSE%psseversion%\
SET PSSPYPATH=%PSSEPATH%\PSSPY37
SET PATH=%PYTHONHOME%;%PYTHONHOME%SCRIPTs;%pssepath%PSSBIN;%pssepath%PSSLIB;%PATH%
Set INCLUDE=%pssepath%PSSLIB;%INCLUDE%
echo ﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂ
echo   %USERNAME%                           
echo.                                        
echo   PATHs set: PSS/E-34 + python 3.7  
echo ‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹
echo.
