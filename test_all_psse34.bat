@rem test_all.bat
call SCRIPTs\run3437.bat
call mpjobs34 cmld
call mpjobs34 cmld_1d
call mpjobs34 cmld_3d
call mpjobs34 mp2d
call mpjobs34 mpaccc_1d
call mpjobs34 mperun
call mpjobs34 mpgrun
call mpjobs34 mpgrun_droop
call mpjobs34 mpgrun_govtuning
call mpjobs34 mpjobs
call mpjobs34 mppv
call mpjobs34 mpqv_1d
call mpjobs34 mpqv_2d
echo test_all finished!
PAUSE