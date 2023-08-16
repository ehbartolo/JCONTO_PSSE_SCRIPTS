# grun_droop.py - 4 mpjobs + mpgrun_droop.ini
from __future__ import print_function
#** Set paths, import modules, define run vars
#{----------------------------------------------------------------------------}
#import os, sys
#import time,datetime
#pythoncode = 'SCRIPTs\\'
#if os.environ['PYTHONCODE']:
#   pythoncode = os.environ['PYTHONCODE']
#sys.path.append(pythoncode)
#import JCtools
#My  = {}
#ierr, My = JCtools.readIni('mpGrun_droop.ini',My,1)
#My['PYVER']= 37
#My['PSSEVERSION'] = 34
#My['XVAR'] = 21
# =============================================================================================
debug = My['DEBUG']
if My['PYVER']>= 37:
   timeb = time.perf_counter()
else:
   timeb = time.clock()
exec('import psse{}'.format(My['PSSEVERSION']))
import psspy
import pssarrays
if debug:
   print('Python ver %s'%sys.version) #parentheses necessary in python 3.
   print(psspy.psseversion())
   print(sys.executable)
   
with JCtools.redirect_stdout():     #to suppress PSSe message when loading
     if 'BUSDIM' in My:
         psspy.psseinit(My['BUSDIM'])
     else:
         psspy.psseinit()
#import redirect
#redirect.psse2py()
# =============================================================================================
# =============================================================================================
# 2. Multiple subplots in a figure, but one trace in each subplot
def subplots_one_trace(outfile,pltfile,outvrsn=0):
    import dyntools

    chnfobj = dyntools.CHNF(outfile,outvrsn=outvrsn)
    
    chnfobj.set_plot_page_options(size='letter', orientation='portrait')
    chnfobj.set_plot_markers('square', 'triangle_up', 'thin_diamond', 'plus', 'x',
                             'circle', 'star', 'hexagon1')
    chnfobj.set_plot_line_styles('solid', 'dashed', 'dashdot', 'dotted')
    chnfobj.set_plot_line_colors('blue', 'red', 'black', 'green', 'cyan', 'magenta', 'pink', 'purple')

    optnfmt  = {'rows':2,'columns':1,'dpi':300,
                'showttl'    : False,
                'showoutfnam': False,
                'showlogo'   : True,
                'legendtype' :1,
                'addmarker'  :True}

    optnchn = {1:{'chns':[1,'1+v'], 'title':'Speed of Mac'},
               2:{'chns':[2,'v*1000'], 'title':'Pmec  of Mac'}
              } #Pmec

    chnfobj.set_plot_legend_options(loc='lower center', 
                                    borderpad=0.2, 
                                    labelspacing=0.5,
                                    handlelength=1.5, 
                                    handletextpad=0.5, 
                                    fontsize=8, 
                                    frame=False)

    chnfobj.xyplots(optnchn,optnfmt,pltfile)
    
    chnfobj.plots_close()
    
    return          
#__________________________________________________________________
title1     = My['TITLE1']   
title2     = My['TITLE2']   
studyname  = My['STUDYNAME']
StudyType  = My['STUDYTYPE']
cnvfile    = My['CNVFILE']      
snpfile    = My['SNPFILE']      
Genbus     = My['GENBUS']     
initloading= My['INITLOADING']
Pdelta     = My['PDELTA']     
simtime    = My['SIMTIME']    
#__________________________________________________________________
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
zyxvars  = JCtools.ZYXvars(My)    #ZYX vars= [[studyi,zyxmsg],[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey]]
studyi   = zyxvars[0][0] 
zyxmsg   = zyxvars[0][1]
xvarpath = zyxvars[1][0]
xvarkey  = zyxvars[1][1]
#***************************************************
#** Set file names:
outfile = '%s%s.out'%(My['OUTSPATH'],studyi)
logfile = '%s%s.log'%(My['LOGSPATH'],studyi)
plotfile= '%s%s.pdf'%(My['PLOTSPATH'],studyi)
#***************************************************
sys.stdout = open(logfile,'w') # redirect all prints to this log file
#___________________________________________________________
print ('****************************************************')
print ('   Scenario <%s>'%studyi)
print ('   %s - %s'%(My['TITLE1'], My['TITLE2']))
print ('')
print ('   {:%Y-%b-%d   %H:%M:%S}'.format(datetime.datetime.now()))
print ('****************************************************')
print ('')
#___________________________________________________________
# run a dynamic simulation:
print (zyxmsg)
psspy.case(cnvfile)
psspy.rstr(snpfile)
#
psspy.change_plmod_con(206,'1','IEESGO',7,My['XVAR'])  # droop sensitivity

psspy.dynamics_solution_params([99,_i,_i,_i,_i,_i,_i,_i],
                               [0.8,_f, 0.001, 0.004,_f,_f,_f,_f],'')
psspy.gstr(Genbus,initloading,Pdelta,outfile)
psspy.grun(simtime,99,99,0)

#plotting [next 3 lines]- It issues warnings but it still creates plots!!
#         could it be that psspy cannot run within a process?
outlst = [outfile,]

subplots_one_trace(outfile,plotfile)

if My['PYVER']>=37:
   timee = time.perf_counter()
else:
   timee = time.clock()  
deltasecstr = '%10.2f'%(timee-timeb)
deltasec = float(deltasecstr)
My['RETURN'] = [deltasec,studyi]
byebye = '    Scenario %s completed in %10.2f sec.'%(studyi,timee-timeb)
print (byebye)
sys.stdout.close()                # ordinary file object
sys.stdout = sys.__stdout__
print (byebye)
