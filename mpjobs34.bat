@REM mpjobs34.bat
@rem use as: c:\..>mpjobs34 <ini file, no ext>
@rem		 c:\..>mpjobs34 cmld
@rem This setup uses PSSe v.34 and python 3.7
@echo OFF
if exist mpjobs_p37.pyc (
   @ECHO ON
   C:\Python37\pse_env\Scripts\python.exe mpjobs_p37.py %*
   @ECHO OFF
   ) else (
           if exist SCRIPTs\mpjobs_p37.pyc (
              @ECHO ON
              C:\Python37\pse_env\Scripts\python.exe SCRIPTs\mpjobs_p37.py %*
              )
           )
