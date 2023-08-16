@rem mpjobs33.bat
@rem use as: c:\..>mpjobs33 <ini file, no ext>
@rem		 c:\..>mpjobs33 cmld
@rem This setup uses PSSe v.33 and python 2.7
@echo OFF
if exist mpjobs_p27.pyc (
   @ECHO ON
   %PYTHONHOME%python mpjobs_p27.pyc %1
   @ECHO OFF
   ) else (
           if exist SCRIPTs\mpjobs_p27.pyc (
              @ECHO ON
              %PYTHONHOME%python SCRIPTs\mpjobs_p27.pyc %1
              )
           )
@echo mpjobs ended!
