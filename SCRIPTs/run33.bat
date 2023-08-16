@rem run33.bat - PATHs set for PSS/E-33 + python 2.7
@echo OFF
echo %date% %time%
Set PSSEVERSION=33
set PYVER=27
Set PYTHONCODE=scripts\
Set PYTHONHOME=c:\python27\
SET PSSEPATH=%PROGRAMFILES(x86)%\PTI\PSSE%psseversion%\
SET PSSPYPATH=%PSSEPATH%PSSBIN\
SET PATH=%PYTHONHOME%;%pssepath%PSSBIN;%pssepath%PSSLIB;%PATH%
Set INCLUDE=%pssepath%PSSLIB;%INCLUDE%
echo ﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂﬂ
echo   %USERNAME%
echo.
echo   PATHs set for PSS/E-33 + python 2.7
echo ‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹
echo.
