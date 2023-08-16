MPjobs
Author: José Conto, jconto@ieee.org

MPjobs is a parallel processing engine for python scripts.  It will run as many instances of a target script as CPU are available in your pc.
When applied to power system studies with PSSE, it is able to run multple PSSe studies in parallel. 
This release is compatible with PSSe v.33 to v.35
Demo examples for PSSe studies include ACCC, PV, QV and transient stability studies.

Unzip all files at a working folder and rename files: *.tab to *.bat

At the working folder, open a CMD window (=DOS window) by double-clicking on the link appropiate for your set up:
_dos33   link: to run PSSe v.33 with python 2.7
_dos3437 link: to run PSSe v.34 with python 3.7
_dos3538 link: to run PSSe v.35 with python 3.8
Each link loads 'internally' a corresponding bat file located at the SCRIPTs folder, run3x.bat 
(where x is 3, 4, or 5 to amtch the selection of PSSe version) 
It is this bat file that set a few environ variables suitable to its PSSe version.

Once the CMD window is open, run the demo data set as:
	[Warning: update the *.ini file used as data input and activate the corresponding "psspypath" for your set up:
	//PsspyPath  = C:\Program Files (x86)\PTI\PSSE33\PSSBIN
	//PsspyPath  = C:\Program Files (x86)\PTI\PSSE34\PSSPY27
	//PsspyPath  = C:\Program Files (x86)\PTI\PSSE34\PSSPY37
	//psspyPath  = C:\Program Files\PTI\PSSE35\35.2\PSSPY38
	]
Use the command "mpjobs33" to run PSSe v.33 with python 2.7:
[In *.ini file:
PsspyPath  = C:\Program Files (x86)\PTI\PSSE33\PSSBIN
//PsspyPath  = C:\Program Files (x86)\PTI\PSSE34\PSSPY27
//PsspyPath  = C:\Program Files (x86)\PTI\PSSE34\PSSPY37
//psspyPath  = C:\Program Files\PTI\PSSE35\35.2\PSSPY38
]
	c:\..>mpjobs33 cmld[.ini]			//ext of input data file, INI file, is optional

Use the command "mpjobs34" to run PSSe v.34 with python 3.7:
[In *.ini file:
//PsspyPath  = C:\Program Files (x86)\PTI\PSSE33\PSSBIN
//PsspyPath  = C:\Program Files (x86)\PTI\PSSE34\PSSPY27
PsspyPath  = C:\Program Files (x86)\PTI\PSSE34\PSSPY37
//psspyPath  = C:\Program Files\PTI\PSSE35\35.2\PSSPY38
]
	c:\..>mpjobs34 cmld

Use the command "mpjobs35" to run PSSe v.35 with python 3.7:
Note: Thise setup is for PSSe v.35.2.1
PSSev.35 allows for multiple sub-version to be installed, therefore adjustment to 
path names are needed to account for them. Update "mpjobs35.bat" and "run35.bat" as needed.
[In *.ini file:
//PsspyPath  = C:\Program Files (x86)\PTI\PSSE33\PSSBIN
//PsspyPath  = C:\Program Files (x86)\PTI\PSSE34\PSSPY27
//PsspyPath  = C:\Program Files (x86)\PTI\PSSE34\PSSPY37
psspyPath  = C:\Program Files\PTI\PSSE35\35.2\PSSPY38
]
	c:\..>mpjobs35 cmld

All the included tests can be run at once with the bat command:
	c:.\\..>test_all
	
More information is available in the document 'MPjob_wiki.docx'
