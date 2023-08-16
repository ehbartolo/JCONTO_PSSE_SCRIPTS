@rem test_all.bat
call mpjobs%PSSEVERSION% cmld
call mpjobs%PSSEVERSION% cmld_1d
call mpjobs%PSSEVERSION% cmld_3d
call mpjobs%PSSEVERSION% mp2d
call mpjobs%PSSEVERSION% mpaccc_1d
call mpjobs%PSSEVERSION% mperun
call mpjobs%PSSEVERSION% mpgrun
call mpjobs%PSSEVERSION% mpgrun_droop
call mpjobs%PSSEVERSION% mpgrun_govtuning
call mpjobs%PSSEVERSION% mpjobs
call mpjobs%PSSEVERSION% mppv
call mpjobs%PSSEVERSION% mpqv_1d
call mpjobs%PSSEVERSION% mpqv_2d
echo test_all finished!
PAUSE