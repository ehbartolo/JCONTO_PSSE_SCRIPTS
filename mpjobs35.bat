@REM mpjobs35.bat
@rem use as: c:\..>mpjobs35 <ini file, no ext>
@rem		 c:\..>mpjobs35 cmld
@rem This setup uses PSSe v.35 and python 3.8
@echo OFF
if exist mpjobs_p38.pyc (
   @ECHO ON
   %PYTHONHOME%python mpjobs_p38.pyc %*
   @ECHO OFF
   ) else (
           if exist SCRIPTs\mpjobs_p38.pyc (
              @ECHO ON
              %PYTHONHOME%python SCRIPTs\mpjobs_p38.pyc %*
              )
           )

