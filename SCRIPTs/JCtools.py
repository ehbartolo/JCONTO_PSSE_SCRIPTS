# -*- coding: iso-8859-15 -*-
# JCtools.py
# developed by José Conto
# All source snippets are dedicated to the public domain. Do with them as you see fit under fair use.
# tested with python 27
#
''' Modules, Functions, Classes
import os,sys
import glob      #The glob module exports a single function
import csv
import zipfile
import contextlib
def redirect_stdout(new_target=None):
def zipcheck(zfilename):
def ziphas(filen,zfilename):
def ziplist(zfilename):
def zipit(fname, zfilename):
def zipdir(path, extension, zfilename):
def unzip1(fname, zfilename):
def unzip1as(fname, newname, zfilename):
def unzip(path, zfilename):
def Disclaimer():
def IsInt(s):
def IsFloat(s):
def IsList(s):
def IsTuple(s):
def IsNumber(s1):
def IsAllDigits(str):
    import string
def sign(x):
def setype(x):
def WhatType(x):
def float_mindec(csvline):
    def LTfloat(LT,xLT):
def fnameDic(myfile):
def makeFname(Fname,postfix,prefrix=''):
def readlst(xlist,pos):
def File2Str(myfile, option=None):
def flst2lst(myfile,option=None):
def File2List(myfile,option=None,encoding=None,lofl=False):
          import codecs
def List2File(mylist,myfile,open4='w',eol='\n'):
def List2Dic(mylist,upcase=1,nocomment=True):
def List2Str(mylist,prefix='',suffix='\n'):
def Liststr2Str(mylist,suffix=''):
def Liststr2sqlstr(mylist):
def List2Strlst(mylist):
def List2Txt(mylist,prefix='',suffix='\n', header=None):
def Listrec2CSVstr(alist):
def List2D2CSVtxt(alist):
def Tuple2List(a):
def List2Tuple(a):
def List2SQLinsertstr(mylist):
def Comma2Space(linetxt):
def str2csv(xstr):
def Str2File(S,myfile,open4='w',header=None):
def argINI():
def subtractLists(list1,list2):
def CSVfile_read(fileName,numeric=False):
def phraseinList(mylist, phrase):
def asciiCompress(source, level=9):
    import zlib, base64
def asciiDecompress(compress):
    import zlib, base64
def stringToBase64(s,encoding='utf-8'):
    import base64
def base64ToString(b):
    import base64
def str2float(strx):
def tosinglespace(s):
def STRremovecomment(mystr,char):
def trimbetwenquotes(tmpstr,quote="'"):
def commaspaceStr2List(tmpstr):
def strsplit2(line,char=None):
def EmptyStr(mystr):
def wordth(s,k):
def firstcharpos(strx):
def isleadchar(s,h):
def lineComment(mystr,char):
def inlineComment(mystr,char):
def iterate(*vars):
    def iterate_2D(x,y):
def frange(x0,y,s):
def betweenchars_replace(mystr,bchar,ichar,jchar):
def betweenchars_replaceall(mystr,bchar,ichar,jchar):
def betweenchars(mystr,bchar,echar=None):
def getblockstr(beginstr,endstr,mystr,pos=0):
def getblocklst(beginstr,endstr,mylst,pos=None):
def NoDuplist(t):
def deleteChar(Mystr, char):
def rightstr(s,n):
def leftstr(s,n):
def reversestr(s): return s[::-1]
def copyword(Anystr, Wordpos, SepStr=' '):
def wordCount(strX,Pattern):
def Varsreplace(datastr,varlst):
def replaceVars(source, My, target=None):
def count_letters(word, char):
def find_files(pattern, search_path='.\\', rootname=False, case=None):
def find_files_deep(pattern,search_path='.\\'):
def rmgeneric(path, __func__):
def dirRemoveAll(path):
def pyexist(pycode):
def scriptfullname(scriptsfx,My):
def vecMaker(filekey,beginkey,endkey,stepkey):
def vectorpx(vector,CPU):
def ZYXcount(My):
def ZYXvars(My,zyxmsg='scenario'):
def ZYXvecs(My):
def getStudyi(My):
def nlstruns(*args):
def PDFrotate(pdfile,angle):
       import PyPDF2
def dirCreate(FullPathName):
def dirmake(path):
def diacsort(i,j):
def triacsort(i,j,k):
def array2dict(keysv, valuesv,case='UP'):
def dicarrayidx(mydic, dickey,item):
def arrayfloat(n, word=None):
def arrayint(n, word=None):
def arraystr(n, word=None):
def indexof(mylst,value,col=0,pos=0,tol=0.0001):
def mapvectors(a,b,c):
def inrangeupperval(Curve,Q):
def npointupperval(nCap,Csingle,Qmin,Q):
def interpolate(P1,P2,x):
def XY(PQcurve,P):
def relativepercentfx(y,yref):
def AreaTrapezoidal(xarray, yarray):
def appendStrF(S,finalf,options=''):
def appendF(myfiles,finalf,options='n',comment='//'):
def Filedelete(file):
def delf(deletethis):
def delfiles(deletethis):
def getsectionlst(rawlst,section):
def dicVal(Word,keystr):
def iniread(Fname,debug=False):
def readIni(Fname,My,debug=False):
def CSVappendV(My):
def ChannelEquation(Valstr,My):
def Add_path(mypath):
def run_from_dos():
def dirlst(myfiles):
def ReadAllCtgs(CtgFname,ctgformat):
def SetDWGcwd():
def printDict(aDict, br='\n', html=0,
def _launch_ultraedit(infile):
def _launch_notepad(infile):
def _ShowErrorInNotepad(errmsg):
    import tempfile
def _run_dos_command(doscmd):
def _run_dos_command_wait(doscmd):
def myrmdir(dirpath):
def _decode_arg(i_argument, v_argument):
def bsyset(sid=-1,basekv=[],areas=[],buses=[],owners=[],zones=[]):
    import psspy
def subsystem_data(sid,name,attributes,inservice=True):
    from itertools import groupby
    from operator  import itemgetter
    import psspy
class log_class:
    def open(self,fname,option='w'):
    def close(self):
    def write(self,txt):                    #print to log file, no return line
    def writeln(self,txt):                  #print to log file + return line
    def writeprint(self,txt):               #print to console & log file
def PUvector(vectin):
def plot_xy(x,y):
    import matplotlib.pyplot as plt
def plot2p1f(pp,vec3xy,My):
    import matplotlib.pyplot as plt
def plotx2y(vec2xy,My):
    import matplotlib.pyplot as plt
def plot_pd_allinone(series_df,My):
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
def plot_pd_nxm(df,My):
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
def plotline(x, y, Labelst,marker=None,linestyle='-'):
   import matplotlib.pyplot as plt

--------------------
This is a collection/library of various PYTHON functions ranging
from Type-testing and File I/O to String Manipulation and other
Mathematical Functions.
--------------------
# regex to handle various comment styles.
#expression = re.compile(r"""
#                            ^\s*?           # start with space(s), multiple ,once or zero times
#                            [/*#'!]         # start with /*, // or #
#                            .*?             # follow with anything, repeat it, once or more
#                         """,re.VERBOSE)
# ----------------------------------------------------------------------------------------------------
#       How to import it:
#       # add user's code folder
#       try:
#           temp = os.environ['PYTHONCODE']
#           if temp:
#              PythonCode = temp
#       except:
#           PythonCode = 'c:\\code\\python'
#       while PythonCode[-1]=='\\':
#             PythonCode = PythonCode[0:-1]
#       print 'PythonCode=',PythonCode
#       if PythonCode not in sys.path:
#          sys.path.append(PythonCode)
#       #
#       import JCtools
##############################################################################################
'''
import os,sys
import glob      #The glob module exports a single function
                 #also called glob, which takes a filename pattern
                 #and returns a list of all the filenames that match that pattern
#import pandas as pd
#import numpy as np

import csv
import zipfile
#_____________________________________________________________________________________________
import contextlib
@contextlib.contextmanager
def redirect_stdout(new_target=None):
    # sometimes you don't care about messages.
    if new_target is None:
       new_target = open(os.devnull, 'w')
    old_target, sys.stdout = sys.stdout, new_target # replace sys.stdout
    try:
       yield new_target # run some code with the replaced stdout
    finally:
       sys.stdout = old_target # restore to the previous value
#_____________________________________________________________________________________________
def info():
    txt = '''
    JCtools is a library of various PYTHON functions ranging
    from Type-testing and File I/O to String processing and other
    Mathematical functions.'''
    return txt
#_____________________________________________________________________________________________
def zipcheck(zfilename):
    state = False
    if zipfile.is_zipfile(zfilename):
       state = True
    return state

def ziphas(filen,zfilename):
    z = zipfile.ZipFile(zfilename)
    return filen in z.namelist()

def ziplist(zfilename):
    files = []
    z = zipfile.ZipFile(zfilename)
    for name in z.namelist():
            if name.endswith('.zip'):
                    file(name, 'wb').write(z.read(name))
                    ziplist(name)
                    os.remove(name)
            elif not name.endswith('/'):
                    files.append(name)
    return files

def zipit(fname, zfilename):
    if zipcheck(zfilename):
        if ziphas(fname,zfilename): return
        z = zipfile.ZipFile(zfilename, "a")
    else:
        z = zipfile.ZipFile(zfilename, "w")
    z.write(fname)
    z.close()
    return

def zipdir(path, extension, zfilename):
    for each in os.listdir(path):
        if each.endswith(extension):
           try: zipit(path + each,zfilename)
           except IOError: None

def unzip1(fname, zfilename):
    z = zipfile.ZipFile(zfilename, "r")
    file(fname, 'wb').write(z.read(fname))
    z.close()

def unzip1as(fname, newname, zfilename):
    z = zipfile.ZipFile(zfilename, 'r')
    file(newname, 'wb').write(z.read(fname))
    z.close()

def unzip(path, zfilename):
    z = zipfile.ZipFile(zfilename, "r")
    for each in z.namelist():
        if not each.endswith('/'):
           root, name = os.path.split(each)
           directory = os.path.normpath(os.path.join(path, root))
           if not os.path.isdir(directory):
              os.makedirs(directory)
           file(os.path.join(directory, name), 'wb').write(z.read(each))
#_____________________________________________________________________________________________
def Disclaimer():
    lines = """
  Copyright 2011 ERCOT
  All rights reserved.
  
                        DISCLAIMER
  
  This PYTHON program has been prepared by the Electric Reliability
  Council Of Texas (ERCOT) for its internal use and for a particular
  purpose; it may contain errors or be or become obsolete. If you 
  agree to the use of this PYTHON program, you agree to the terms of
  this User Agreement ("Agreement") set out below.  If you do not
  agree with the terms of this User Agreement, do not use this PYTHON
  program.
  
  ALL INFORMATION CONTAINED HEREIN IS PROVIDED "AS IS" WITHOUT ANY
  WARRANTIES OF ANY KIND. ERCOT, ITS ELECTED AND APPOINTED OFFICIALS,
  EMPLOYEES AND ASSIGNS MAKE NO REPRESENTATIONS WITH RESPECT TO SAID
  INFORMATION AND DISCLAIM ALL EXPRESS AND IMPLIED WARRANTIES AND
  CONDITIONS OF ANY KIND, INCLUDING WITHOUT LIMITATION, REPRESENTATIONS,
  WARRANTIES OR CONDITIONS REGARDING ACCURACY, TIMELINESS, COMPLETENESS,
  NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR ANY PARTICULAR
  PURPOSE.  The specific suitability for any use of this program and its
  accuracy should be confirmed by the user prior to its use. Use it at
  your own risk.
  
  While every precaution has been taken in the preparation of this
  program, ERCOT ASSUMES NO RESPONSIBILITY TO YOU OR ANY THIRD PARTY
  FOR THE CONSEQUENCES OF ANY INTERRUPTION, INACCURACY, ERROR OR
  OMISSION, RESULTING FROM THE USE OF INFORMATION CONTAINED IN THIS CODE
  AND ITS ASSOCIATED OUTPUT.  ERCOT SHALL NOT BE LIABLE TO YOU OR ANY
  THIRD PARTY FOR, AND YOU AGREE TO INDEMNIFY ERCOT, ITS DIRECTORS,
  OFFICERS, EMPLOYEES, AND REPRESENTATIVES FOR ANY CLAIMS, DAMAGES, OR
  LOSSES RESULTING FROM, DAMAGE OF ANY KIND ARISING DIRECTLY OR
  INDIRECTLY OUT OF OR RELATING TO YOUR USE OF THIS IPLAN PROGRAM
  (INCLUDING ANY BREACH OF THIS AGREEMENT), INCLUDING, BUT NOT LIMITED
  TO, ANY LOST PROFITS, LOST OPPORTUNITIES, SPECIAL INCIDENTAL, DIRECT,
  INDIRECT OR CONSEQUENTIAL DAMAGES, EVEN IF ERCOT IS ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE OR OF A CLAIM, OR POTENTIAL CLAIM, BY
  ANOTHER PARTY, INCLUDING A CLAIM FOR PUNITIVE DAMAGES.
  """
    return lines
# Functions for Data-type assessment
def IsInt(s):
    """ Is the given string an integer?  no decimal point accepted """
    try:
          i  = int(s)
          ok = 1
    except ValueError:
          ok = 0
    return ok

def IsFloat(s):
    """ Is the given string a float?"""
    try:
           f  = float(s)
           ok = 1
    except ValueError:
           ok = 0
    return ok

def IsList(s):
    """ Is the given string a list?"""
    s = str(s)
    ok= 0
    if s[0]=='[':
     if s[-1]==']':
        try:
                f  = eval(s)
                ok = 1
        except ValueError:
                ok = 0
    return ok

def IsTuple(s):
    """ Is the given string a tuple?"""
    s = str(s).strip()
    ok= 0
    if s[0]=='(':
     if s[-1]==')':
        try:
               f  = eval(s)
               ok = 1
        except ValueError:
               ok = 0
    return ok

def IsNumber(s1):
    cnv= s1
    ok = 0
    #print 's1:-%s-'%s1
    if s1 != None:
        """ Is the given string an integer?  no decimal point accepted """
        try:
               cnv= int(s1)
               ok = 1
        except ValueError:
               pass

        if ok==0:        
           try:       # Is the given string a float?      
                  cnv= float(s1)
                  ok = 1
           except ValueError:
                  pass
    return cnv

def IsAllDigits(str):
    """ Is the given string composed entirely of digits? """
    import string
    match = string.digits
    ok = 1
    for letter in str:
        if letter not in match:
           ok = 0
           break
    return ok

def sign(x):
    s=0
    if IsInt(x):
       if x>=0: s=1
    elif IsFloat(x):
         if x>=0: s=1
    return s

def setype(x):
    OK = ''
    if   isinstance(x, int):
         OK= int(x)
    elif isinstance(x, float):
         OK= float(x)
    elif isinstance(x, str):
         OK= x
    return OK

def WhatType(x):
    OK = ''
    if   isinstance(x, int):   OK='INTEGER'
    elif isinstance(x, float): OK='FLOAT'
    elif isinstance(x, str):   OK='STRING'
    elif isinstance(x, list):  OK='LIST'
    elif isinstance(x, dict):  OK='DICT'
    elif isinstance(x, tuple): OK='TUPLE'
    return OK

def float_mindec(csvline):
    # converts 1.0000 to 1.0 <- minimum decimals
    def LTfloat(LT,xLT):
        for x in LT:
            if   IsInt(x):
                 y = int(x)
            elif IsFloat(x):
                 y = float(x)
            else:
                 y = x
            xLT.append(y)
        return xLT
        
    newL = None
    if   WhatType(csvline)=='STRING':
         M = []
         L = csvline.split(',')
         xL = LTfloat(L,M)
         newL = ''
         for elem in xL:
             newL += str(elem)+','
         newL = newL[:-1]
    elif WhatType(csvline)=='LIST':
         M = []
         L = csvline
         newL = LTfloat(L,M)
    elif WhatType(csvline)=='TUPLE':
         M = ()
         L = csvline
         newL = LTfloat(L,M)
         
    return newL

def fnameDic(myfile):
    #return dic of strings as [path, root, ext]
    pathi = os.path.dirname(myfile)
    if pathi:
       pathi += '\\'
    base = os.path.basename(myfile)
    rootfn, ext = os.path.splitext(base)
    #if len(ext) not in [3,4,5]:
    #   ext = ''
    #   rootfn = base
    names = {}
    names['PATH'] = pathi
    names['ROOT'] = rootfn
    names['EXT']  = ext
    return names

def makeFname(Fname,postfix,prefrix=''):
    #normal use: mylog = JCtools.makeFname(oldFnam,'.log')
    names = fnameDic(Fname)
    newFname  = names['path']+prefix+root+postfix
    return newFname

def readlst(xlist,pos):
    if WhatType(xlist)== 'LIST':
       item = xlist[pos]
    else:
       item = xlist
    return item
#________________________________________________________________________________________
def File2Str(myfile, option=None):
    '''
    usage:   mystr = File2Str(myfile, ['NOBLANK','@','#'])
             result -> No blank lines, no lines starting with @ or #
    '''
    S = ''
    if option:
       Slst = File2List(myfile)
       for line in Slst:
           if len(line.strip())<1:
              if 'NOBLANK' in option: continue
           elif line[0] in option: continue
           S += line + '\n'
    else:
      try:
         fx = open(myfile,'r')
         S = fx.read()
         fx.close()
      except IOError:
        print('ERROR {} - while Open {} for Read operation'.format(IOError,myfile))
    #string S contains \n as needed
    return S

def flst2lst(myfile,option=None):
    '''
    It reads *.lst files to a list. Usually single entry per line
    usage:   mystr = File2List(myfile, option=['/@;#',0])
             result -> No blank lines, no lines starting with /,@,; or #
    '''
    options = ''
    option0= False
    if option:
       if   WhatType(option)=='LIST':
            if 0   in option: option0 = True        #filter out empty lines
            options = option[0]                     #comment line first char
       elif WhatType(option)=='STRING':
            options = option
    mylist = []
    if os.path.isfile(myfile):
       fx = open(myfile,'r')
       content = fx.read()
       xlst = content.split('\n')
       fx.close()
       if option:
          for line in xlst:
              if len(line.strip())>1:
                 if options:
                    if line[0] in options: continue     #bypass comment lines
                 yline = line.strip()
                 yvalue = yline           
              elif option0:                 #filter out empty lines
                 continue
              else:
                 yvalue = line
              mylist.append(yvalue)             
       else: mylist = xlst
    return mylist

def File2List(myfile,option=None,encoding=None,lofl=False):
    '''
    usage:   mystr = File2List(myfile, option=['/@;#','e',0])
             result -> No blank lines, no lines starting with @ or #
                      or 'e': do eval
    '''
    options = ''
    optione= False
    option0= False
    if option:
       if   WhatType(option)=='LIST':
            if 0   in option: option0 = True        #filter out empty lines
            if 'e' in option: optione = True        #do eval
            options = option[0]                     #comment line first char
       elif WhatType(option)=='STRING':
            if option== 'e':     #do eval
               optione = True
            else:
               options = option
    mylist = []
    if os.path.isfile(myfile):
       if encoding:
          import codecs
          fx = codecs.open(myfile,encoding=encoding,errors='ignore')
       else:
          fx = open(myfile,'r')
       content = fx.read()
       xlst = content.split('\n')
       fx.close()
       if option:
          for line in xlst:
              if len(line.strip())>1:
                 if options:
                    if line[0] in options: continue     #bypass comment lines
                 yline = line.strip()
                 if optione:
                    try:
                        yvalue = eval(yline)
                    except:
                        yvalue = yline      #is a string
                 else:
                    yvalue = yline           
              elif option0:                 #filter out empty lines
                 continue
              else:
                 yvalue = line
              mylist.append(yvalue)             
       else: mylist = xlst
    return mylist

def List2File(mylist,myfile,open4='w',eol='\n'):
    '''
    mylist = ['aaa','bb','ccc'....] or
    mylist = [['a','b','caa'],['bb','ccc']....]
    '''
    fx = open(myfile,open4)
    # mylist is a list of strings
    #print 'mylist'
    for rec in mylist:
        rectype = WhatType(rec)
        if rectype=='LIST':
           #print rec
           recstr = ','.join(str(i) for i in rec)
           #for k in range(len(rec)):
           #    if k==0: recstr  = str(rec[k])
           #    else:    recstr += ','+str(rec[k])
        else:     #= string
           recstr = rec
        if eol:
           recstr += eol
        fx.write(recstr)
    fx.close()
    return

def List2Dic(mylist,upcase=1,nocomment=True):
    # mylist = 2D-list of two entries per 'record'
    # mylist = ['1,a','2,b'....]
    mydic = {}  
    #print 'List2Dic  mylist=',mylist
    for k2d in mylist:
        if len(k2d)<1: continue
        if nocomment:
           if k2d[0]=='/': continue
        k2dlst = k2d.split(',')    #['1','name']
        #print k2dlst
        key = str(k2dlst[1])
        if   upcase>0:
             key = key.upper()
        elif upcase<0:
             key = key.lower()
        mydic[key] = int(k2dlst[0])
    return mydic

def List2Str(mylist,prefix='',suffix='\n'):
    # mylist = list of strings
    mystr = ''
    for k in range(len(mylist)):
        if k==0:      #header!
           mystr = str(mylist[k])+suffix
        else:
           mystr += prefix+str(mylist[k])+suffix
    #print "%s -> %s"%(mylist,mystr)
    return mystr

def Liststr2Str(mylist,suffix=''):
    # mylist is a list of strings
    # 
    mystr = ''
    for k in range(len(mylist)-1):
        mystr += str(mylist[k])+suffix
    mystr += str(mylist[k+1])
    #print "%s -> %s"%(mylist,mystr)
    return mystr

def Liststr2sqlstr(mylist):
    # mylist is a list of strings
    mystr = ""
    for k in range(len(mylist)-1):
        mystr += "'%s',"%mylist[k]
    mystr += "'%s'"%mylist[k+1]
    #print "%s -> %s"%(mylist,mystr)
    return mystr
    
def List2Strlst(mylist):
    # mylist = [[1,b],[2,a]]
    # strlst = ['1,b','2,a']
    strlst = []
    for line in mylist:
        t1 = ','.join(str(i) for i in line)
        strlst.append("%s"%t1)
    return strlst   

def List2Txt(mylist,prefix='',suffix='\n', header=None):
    # mylist = list of strings
    mystr = ''
    for k in range(len(mylist)):
        if header and k==0:
           mystr = str(mylist[k])+suffix
        else:
           mystr += prefix+str(mylist[k])+suffix
    #print "%s -> %s"%(mylist,mystr)
    return mystr

def Listrec2CSVstr(alist):
    # alist = [b,a]
    # CSVstr = 'b,a'
    CSVstr = ','.join(str(i) for i in alist)
    return CSVstr   

def List2D2CSVtxt(alist):
    '''
     alist = [[b1,a1],[b2,a2],[b3,a3],
     CSVtxt = 'b1,a1\n
               b2,a2\n
               b3,a3\n'
    '''
    CSVtxt = ''
    for xlst in alist:
        CSVtxt += '%s\n'%','.join(str(i) for i in xlst)
    return CSVtxt   

def Tuple2List(a):
    b = []
    for x in  a:
        b.append(x)
    return b

def List2Tuple(a):
    b = ()
    for x in  a:
        b.append(x)
    return b
    
def List2SQLinsertstr(mylist):
    # mylist = [1,b]]
    # strlst = "1,'b'"
    first = True
    for ele in mylist:
        xtype = WhatType(ele)
        if xtype=='STRING':
           if first: ts  = "'%s'"%ele
           else:     ts += ",'%s'"%ele
        else:
           if first: ts  = "%s"%ele
           else:     ts += ",%s"%ele
        if first: first= False
    return "%s"%ts
#_______________________________________________________
def Comma2Space(linetxt):
    line2 = linetxt.replace(',',' ')
    line  = line2.strip()   
    return line
#_______________________________________________________
def str2csv(xstr):
    # str = "  aa bb, ' cc ' 'd d' "
    # out = "aa,bb,'cc','d d'"
    #print (' in =%s'%xstr)
    ystr = betweenchars_replace(xstr,"'",' ','|')
    zstr = betweenchars_replace(ystr,'"',' ','|')
    line2 = zstr.replace(',',' ')
    line3 = line2.strip()  
    line4 = tosinglespace(line3)
    line2 = line4.replace(' ',',')
    line3= betweenchars_replace(line2,"'",'|',' ')
    outstr= betweenchars_replace(line3,'"','|',' ')
    #print ('out=%s'%outstr)
    return outstr
#_______________________________________________________
def Str2File(S,myfile,open4='w',header=None):
    #string S contains \n as needed
    #open4= 'w' to re-write
    #       'a' to append
    #       't' to append to top of file
    #       'e' to bypass if file exist
    #header writes to the top of the file, contains \n as needed
    #try:
    #  fout = open(myfile,open4)         #open file for block output
    #  fout.write(S)
    #  fout.close()
    #  OK = 0
    #except IOError:
    #  print 'Error while Open for Write operation of %s' % myfile
    #  OK = 1
    #return OK
    try:
      OK = 0
      if   open4.lower()=='e':
           if os.path.isfile(myfile):
              print('Warning - Bypass writing operation for %s'%myfile)
              return OK
           else:
              open4='w'        
      elif open4.lower()=='t':
           with open(myfile, 'r+') as f:
                S += f.read()
           open4='w'
      elif open4.lower()=='a':
           pass
      else:
           open4='w'
      fout = open(myfile,open4)
      if header:
         fout.write(header)
      fout.write(S)
      fout.close()
      
    except IOError:
      print('Error %s in Str2File write operation of %s'%(IOError,myfile))
      OK = 1
    return OK

def argINI():
    if len(sys.argv) >1:
       INIfile = sys.argv[1]
    else:
       froot,ext = os.path.splitext(sys.argv[0])
       #froot = path\\core_ver_other
       if '_' in froot:
          froot = froot.split('_')[0]        #=core
       INIfile   = os.path.basename(froot)
    root,ext = os.path.splitext(INIfile)
    if not ext:
       INIfile += '.ini'
    
    return INIfile

def subtractLists(list1,list2):
    newList1 = []
    for e in list1:
        if not isInList(list2,e):
            newList1.append(e)
    return newList1

def CSVfile_read(fileName,numeric=False):
    data = []
    if not os.path.exists(fileName):
        print("Error in readCsvFile(%s): File %s doesn't exist!\n" %(fileName, fileName))
        return False, data
    #data = [[float(x) for x in rec] for rec in csv.reader(fileName, delimiter=',')]
    f = open(fileName,'r')
    if not f:
        print("Error in readCsvFile(%s): Cannot open file %s!\n" %(fileName, fileName))
        return False, data
    i = -1
    for row in csv.reader(f):
        i += 1
        if numeric:
          try: 
            row1 = [float(x) for x in row]
          except:
            print('ERROR - %s,'%i,row)
        else:
           row1 = row
        data.append(row1)
        #if i < 10:
        #   print 'row=',row1
    f.close()
    return True, data

def phraseinList(mylist, phrase):
    OK = False
    for x in mylist:
        if phrase in x:
           OK = True
           break
    return OK    

#/////////  compress STRINGS    ////////////////////
def asciiCompress(source, level=9):
    import zlib, base64
    """ compress data to printable ascii-code """
    compress = zlib.compress(source,level)
    csum = zlib.crc32(compress)
    enbase64 = base64.encodestring(compress)
    return enbase64, csum

def asciiDecompress(compress):
    import zlib, base64
    """ decompress result of asciiCompress """
    debase64 = base64.decodestring(compress)
    csum = zlib.crc32(debase64)
    source = zlib.decompress(debase64)
    return source, csum

def stringToBase64(s,encoding='utf-8'):
    import base64
    return base64.b64encode(s.encode(encoding))

def base64ToString(b):
    import base64
    return base64.b64decode(b).decode(encoding)
    
#/////////  STRINGS    /////////////////////////
def str2float(strx):
    if IsFloat(strx):
        fx = float(strx)
    else:
        fx = 0.0
    return fx
    
def tosinglespace(s):
    # if separchar is space, convert multiple space to single space
    # if word in quotes, space does not change
    s1 = s.strip()
    s  = s1.expandtabs()  #expand tabs
    x=''
    space = False
    inquotes= False
    for k in range(len(s)):
        #print inquotes,'\t', k,'\t_%s_'%s[k],space
        if s[k]=="'" or s[k]=='"':
           x += s[k]
           inquotes = not inquotes
           space = False
           continue
        if inquotes: 
           x += s[k]
           continue
        if s[k]==" ":
           if space: continue
           x += s[k]
           space = True
        else:
           space= False
           x += s[k]
    return x

def STRremovecomment(mystr,char):
    oldlst = Str2List(mystr)
    newlst = []
    for line in oldlst:
        if EmptyStr(line): continue
        if line[0] ==char: continue
        newlst.append(line)
    return List2Str(newlst)

def trimbetwenquotes(tmpstr,quote="'"):
    '''trim word in string between quotes. Example:
    Input  oldstr = "11011 ' USRMDL' 1 'UHRSG ' 5   0 12  25  4 7 11001  '1' 11009 '1' 0  ' '  0  ' '  0  ' '  0  ' '"
    Output outstr = "11011 'USRMDL' 1 'UHRSG' 5   0 12  25  4 7 11001  '1' 11009 '1' 0  ''  0  ''  0  ''  0  ''"
    '''
    outstr = tmpstr
    lstr = len(tmpstr)
    inquote = False
    word = ''
    for i in range(lstr):
        if tmpstr[i]==quote:
           inquote = not inquote
           continue
        if inquote:
           word += tmpstr[i]
           #print word
           continue
        else:
           if word:
              word1 = quote+word+quote
              word2 = quote+word.strip()+quote
              #print 'word1=[%s], word2=[%s]'%(word1,word2)
              outstr = outstr.replace(word1,word2)
              word = ''
    return outstr

# ----------------------------------------------------------------------------------------------------
def commaspaceStr2List(tmpstr):
    '''Split string first at comma and then by space. Example:
    Input  tmpstr = a1       a2,  ,a4 a5 ,,,a8,a9
    Output strlst = ['a1', 'a2', ' ', 'a4', 'a5', ' ', ' ', 'a8', 'a9']
    '''
    strlst = []
    commalst = tmpstr.split(',')
    for each in commalst:
        eachlst = each.split()
        if eachlst:
            strlst.extend(eachlst)
        else:
            strlst.extend(' ')

    return strlst

def strsplit2(line,char=None):
    #PRINT '|  since Y2000.                       |'
    #returns ['PRINT',"'|  since Y2000.                       |'"]
    flag = False
    strflag = False
    word = ''
    linelst = []
    if not char: char = ' '
    for c in line:
        if c==char and not strflag:
           if flag:
              linelst.append(word)
              word = ''
              flag = False
           continue
        flag = True
        if c=="'":
           strflag = not strflag
        word += c
    if flag:
       linelst.append(word)
    return linelst

def EmptyStr(mystr):
    OK = False
    str2 = mystr.strip()
    #print 'EmptyStr=',str2,'-'
    if str2:
       OK = False
    elif len(str2)==0:
         OK = True
    return OK

def wordth(s,k):
    s2 = s.strip()
    s3 = s2.split()
    return s3[k]

def firstcharpos(strx):
    i = -1
    for i in range(len(strx)):
        if strx[i]== ' ': continue
        break
    return i

def isleadchar(s,h):
    OK = False
    s1 = s.upper()
    s2 = s1.split('\n')
    for s3 in s2:
        s4 = s3.strip()
        if h.upper() == s4[:len(h)]:
           OK = True
    return OK

def lineComment(mystr,char):
    OK = False
    str2 = mystr.strip()
    if str2[0] == char:
       OK = True
    return OK

def inlineComment(mystr,char):
    newstr = mystr
    inLComment = ''
    if mystr.find(char)>0:
       newstr = mystr.split(char)[0]
       inLComment= char+mystr.split(char)[1]
    return newstr, inLComment

def iterate(*vars):
    '''
    usage:  iterate(x,y,z)
    or      w= [x,y,z]  #x,y,z are lists
            iterate(w)
    ________________
    in    x= ['a', 'b']
          y= [1, 2]
    out   [['a', 1], ['a', 2], ['b', 1], ['b', 2]]
    ________________

    in    x= ['a', 'b']
          y= [1, 2]
          z= ['m.c', 'n.py']
    out   [['a', 1, 'm.c'], ['a', 1, 'n.py'],
           ['a', 2, 'm.c'], ['a', 2, 'n.py'],
           ['b', 1, 'm.c'], ['b', 1, 'n.py'],
           ['b', 2, 'm.c'], ['b', 2, 'n.py']]
    '''
    def iterate_2D(x,y):
        result = []
        for i in x:
            for j in y:
                if isinstance(i, list):
                   z = i[:]
                else:
                   z = [i]
                z.extend([j])
                result.append((z))
        return result
    #print 'len(vars):%s'%len(vars)
    #print 'vars:',vars
    #print 'vars[0]:',vars[0]
    #if isinstance(args, list):
    #  for var in args:
    if   len(vars)==1:
         if isinstance(vars, tuple):
            args = vars[0]
    else:
         args = vars[:]
    #print 'len(args):%s'%len(args)
    if not isinstance(args[0], list):
       return args
    if   len(args)==1:
         xy = args[0]
    elif len(args)==2:
         xy = iterate_2D(args[0],args[1])
    else: #len(args)>2
         xy = iterate_2D(args[0],args[1])
         for xlst in args[2:]:
             xy= iterate_2D(xy,xlst)
    return xy

def frange(x0,y,s):
    # float range function - [1.2,1.4,1.6]
    #x0 - START value
    #y  - END value
    #s  - STEP
    tol = s/1000.0
    l = []
    l.append(x0)
    x = float(x0)
    while True:
       x += s
       if s>0:
          if x-y >tol: break
       else:
          if y-x >tol: break
       l.append(x)
    return l

def betweenchars_replace(mystr,bchar,ichar,jchar):
    ''' replace phrase between bchar, the ichar for jchar
    only for first occurrance
    if bchar=[ then echar = ]
    if bchar=( then echar = )
    if bchar={ then echar = }
    if bchar=< then echar = >
    '''
    newstr = mystr
    phrase = ''
    if   bchar=='[':
         phrase = betweenchars(mystr,bchar,']')
    elif bchar=='(':
         phrase = betweenchars(mystr,bchar,')')
    elif bchar=='{':
         phrase = betweenchars(mystr,bchar,'}')
    elif bchar=='<':
         phrase = betweenchars(mystr,bchar,'>')
    else:   
        strX = mystr.split(bchar)
        if len(strX)> 2:
           phrase = strX[1]
    if phrase:
        phrase = phrase.replace(ichar,jchar)
        newstr = strX[0]+bchar+phrase+bchar
        newstr += bchar.join(strX[2:])
    return newstr

def betweenchars_replaceall(mystr,bchar,ichar,jchar):
    ''' replace phrase between bchar, the ichar for jchar
    if bchar=[ then echar = ]
    if bchar=( then echar = )
    if bchar={ then echar = }
    if bchar=< then echar = >
    for ichar=,  jchar=^
    in :BOSQUESW.BOSQUESW_CC1,CombinedCycle,252,"[150144, 150145]","[150144, 150145]","['BOSQUESW.BSQSU_3','BOSQUESW.BSQSU_4']",
    out:BOSQUESW.BOSQUESW_CC1,CombinedCycle,252,"[150144^ 150145]","[150144^ 150145]","['BOSQUESW.BSQSU_3'^'BOSQUESW.BSQSU_4']",

    '''
    newstr = ''
    tmpstr = mystr[:]
    lenk1 = len(tmpstr)
    k=0
    while True:
        k += 1     
        #print '_______k=%s_________________'%k
        #print 'in tmpstr=',tmpstr
        #print 'newstr=',newstr
        phrase = ''
        if   bchar=='[':
             phrase = betweenchars(tmpstr,bchar,']')
        elif bchar=='(':
             phrase = betweenchars(tmpstr,bchar,')')
        elif bchar=='{':
             phrase = betweenchars(tmpstr,bchar,'}')
        elif bchar=='<':
             phrase = betweenchars(tmpstr,bchar,'>')
        else:   
            strX = tmpstr.split(bchar)
            if len(strX)> 2:
               phrase = strX[1]
            else:
               newstr += tmpstr
               break
        if phrase:      #at k=1, phrase= [150144, 150145]
            phrase = phrase.replace(ichar,jchar)
            #print '1phrase=',phrase
            tmp2 = tmpstr[:tmpstr.find(bchar)]+bchar+phrase+bchar
            #print '1tmp2=',tmp2
            newstr += tmp2
            #print '1newstr=',newstr
            #print lenk1, len(newstr)
            if lenk1>len(newstr):
               tmpstr = mystr[len(newstr):]
               #print '1tmpstr=',tmpstr
        else:
            break
        #print 'out tmpstr=',tmpstr
        #print 'bchar _%s_'%bchar
        if not bchar in tmpstr:
           newstr += tmpstr
           break
        if k>10:break
    return newstr

def betweenchars(mystr,bchar,echar=None):
    # get phrase between begin char (bchar) and the [optional] end char (echar)
    phrase = ''
    if not echar:
       echar = bchar
    if bchar!=echar:
       posb = mystr.find(bchar)
       #print (mystr,bchar,echar)
       #print (posb)
       if posb >=0 and mystr.find(echar,posb+1)>0:
          phrase = mystr[mystr.find(bchar)+1:mystr.find(echar)]
    else:
       if bchar=='"':
           if "'" in mystr:
              mystr = mystr.replace("'",'')
       n = mystr.count(bchar)
       if n==0:
          phrase = mystr
       elif n==2:
           strX = mystr.split(bchar)
           #print ('strX=',strX)
           if len(strX)> 1:
              phrase = strX[1]
    return phrase

def getblockstr(beginstr,endstr,mystr,pos=0):
    flag = False
    newstr = ''
    mylst = mystr.split('\n')
    for line in mylst:
        lineup = line.upper()
        if isleadchar(lineup,beginstr.upper()):
           flag = True
        if flag:
           newstr += line+'\n'
           if lineup.find(endstr.upper())>=0:
              break
    return newstr

def getblocklst(beginstr,endstr,mylst,pos=None):
    flag = False
    block = []
    if pos:
       k = pos-1
    else:
       k = -1
    #print(' ** NOW IN GETBLOCKLST **')
    while 1:
        k +=1
        line = mylst[k]
        lineup = line.upper()
        #print(line)
        if not flag:
           if isleadchar(lineup,beginstr.upper()):
              flag = True
              block.append(line)
              if lineup.find(endstr.upper())>=0:   #case begin & end in same line
                 break
        else:
           block.append(line)
           if lineup.find(endstr.upper())>=0:
              break
    return block

def NoDuplist(t):
    """ Return a list of the elements in t in arbitrary order,
        but without duplicates. """
    u = []
    for x in t:
        if x not in u:
           u.append(x)
    return u


def deleteChar(Mystr, char):
    Newstr = ''
    for ix in range(len(Mystr)):
        if Mystr[ix] != char:
           Newstr = Newstr + Mystr[ix]
    return Newstr

def rightstr(s,n):
    newstr = s[len(s)-n:]
    return newstr

def leftstr(s,n):
    newstr = s[:n]
    return newstr

def reversestr(s): return s[::-1]

def copyword(Anystr, Wordpos, SepStr=' '):
    if SepStr:
       tmplst = Anystr.split(SepStr)
    else:
       tmplst = Anystr.split()
    if   Wordpos > 0 and Wordpos <= len(tmplst)-1:
         word = tmplst[Wordpos-1]
    elif Wordpos < 0 and abs(Wordpos) <= len(tmplst):
         word = tmplst[Wordpos]
    else:word = ''
    return word

def wordCount(strX,Pattern):
    count = 0        
    for i in range(len(strX)):        
        if strX[i].upper() == Pattern:
           count += 1
    return count

def Varsreplace(datastr,varlst):
    #print 'varlst =', varlst
    for i in range(len(varlst)):
        str1 = '%'+str(i+1)+'%'
        #print('  var %s replaced with %s'%(str1,str(varlst[i])))
        datastr = datastr.replace(str1,str(varlst[i]))
    return datastr

def replaceVars(source, My, target=None):
    if os.path.isfile(source):
       filesource = True
       strX = File2Str(source)
       sourcedic = fnameDic(source)
    else:
       filesource = False
       strX = source
       root,ext = os.path.splitext(source)
       if ext:
          print('ERROR - bad file %s'%source)
          return source
       # source is a multiline string         
    # update var definition if needed
    if 'NVARS' in My:
       nVars = My['NVARS']
    else:
       count = 0
       for key, value in list(My.items()):
           if key[0]=='%':
              count += 1
       nVars = count
    for i in range(nVars):
        newphrase = ''
        stri = '%'+str(i+1)+'%'
        phrase = My[stri]
        
        CPid = -1                              # %1% = title1 & RRSrule + "pct rule" = phrase
        CPhraselst = []                        # phrase = title1 & RRSrule + ^0
        while '"' in phrase:                   # CPhraselst = ['pct rule']
              CPid += 1
              CPhrase = betweenchars(phrase,'"')
              if CPhrase:
                 CPhraselst.append(CPhrase)
                 phrase = phrase.replace('"'+CPhrase+'"','^'+str(CPid))
              
        phraselst = phrase.split()
        if len(phraselst)<2: continue           # direct replacement [%3% = RRSrule]
        for j in range(len(phraselst)):         # do direct replacement for My vars
            if phraselst[j][0] in '+-*/_&': continue
            if phraselst[j][0] == '^':          #is a quoted string
               CPid = int(phraselst[j][1:])
               phraselst[j] = CPhraselst[CPid]
               continue
            if phraselst[j].upper() in My:
               phraselst[j] = My[phraselst[j].upper()]
        if 'DEBUG' in My and phraselst:
           print('1 phraselst:',phraselst)
        
        evaln = 1
        for j in range(len(phraselst)):
            #print phraselst[j],
            if str(phraselst[j])[0] in '+-*/_&': continue
            if   IsInt(phraselst[j]):
                 evaln *= 1
            elif IsFloat(phraselst[j]):
                 evaln *= 1
            else:
                 evaln *= 0    #a string
                 break
            #print evaln
        if evaln == 1:           #numeric values
           newphrase = eval(' '.join([str(j) for j in phraselst]))
        else:                    #string values
           for j in range(len(phraselst)):  #concatenate all elements
               newphrase += str(phraselst[j])
               newphrase  = newphrase.strip()
           if '+' in newphrase:
                     newphrase = newphrase.replace('+','')
           if '&' in newphrase:
                     newphrase = newphrase.replace('&',' ')
        My['jc'+str(i+1)] = newphrase

    lchr = '%'
    if filesource:
       if sourcedic['EXT']=='.BAT':
          lchr = ''

    if 'DEBUG' in My:
       print('2 My')
       for keyname, keyvalue in list(My.items()):
           if '%' in keyname:
              print('%s=%s-'%(keyname,keyvalue))

    for i in range(nVars-1,-1,-1):
        str1 = '%'+str(i+1)+'%'
        str2 = '%'+str(i+1)+lchr
        #print 'Now replace var ',str1
        if 'jc'+str(i+1) in My:   # for VAR operation
           stri = 'jc'+str(i+1)
        else:
           stri = My[str1].upper()
        try:
           strX = strX.replace(str2,str(My[stri]))
           if 'DEBUG' in My:
              print('  var %s replaced with %s'%(str2,str(My[stri])))
        except:
           pass
    # save file
    if filesource: # save updated file 
        newfnamepath = sourcedic['PATH']
        if 'SUBFOLDER' in My:
           newfnamepath += My['SUBFOLDER']
           if not os.path.exists(newfnamepath):
              os.makedirs(newfnamepath)              
        if sourcedic['ROOT'][0]=='_':
           newfnamesource = sourcedic['ROOT'][1:]+'_'
        else:
           newfnamesource = sourcedic['ROOT']+'_'
        newfname = newfnamepath+newfnamesource+sourcedic['EXT']
        #print 'newfname:%s'%newfname
        if   target:
             newfname = target
        elif 'SCRIPTSAVE' in My:
             if My['SCRIPTSAVE']:
                newfname = newfnamepath+newfnamesource+My['STUDYI']+sourcedic['EXT']
             
        Str2File(strX,newfname)
        strX = newfname
    return strX

def count_letters(word, char):
    count = 0
    for c in word:
        if char == c:
           count += 1
    return count

#{{{{{{{{{    DIR & FILES }}}}}}}}}}}}}}}}}}}}}}
#def find_files(search_path,pattern):
#    """Given a search path, yield all files matching the pattern"""
#    return glob.glob(os.path.join(search_path,pattern))

def find_files(pattern, search_path='.\\', rootname=False, case=None):
    """Given a search path, yield all files matching the pattern
    usage:  find_files('*.ctg', search_path='outs\\')
    """
    if count_letters(pattern, '*')==2:       # single string like *flat32_*.out
       root,ext = os.path.splitext(pattern)
       key = root.replace('*','')
       npattern = '*%s'%ext 
       allmatchlst = glob.glob(os.path.join(search_path,npattern))
       matchlst = []
       for fn in allmatchlst:
           fnbase = os.path.basename(fn)
           if key in fnbase:
              matchlst.append(fn)
    elif os.path.isfile(pattern):       # single string like flat32.out
         matchlst = [pattern]
    else:
       matchlst = glob.glob(os.path.join(search_path,pattern))    # single string like flat3*.out
                
    for i in range(len(matchlst)):
        if rootname:
           match = os.path.basename(matchlst[i])
        else:
           match = matchlst[i]
        if '.' in match[0]:
           matchlst[i] = match[2:]
        if case:
           if   case.upper()=='UPPER':
                matchlst[i] = matchlst[i].upper()
           elif case.upper()=='LOWER':
                matchlst[i] = matchlst[i].lower()
    return matchlst
    
def find_files_deep(pattern,search_path='.\\'):
    filefound = []
    if not search_path:
       search_path='.\\'
    for root, dirs, files in os.walk(search_path):
        filefound += find_files(pattern,root)
    return filefound

def rmgeneric(path, __func__):
    """ RemoveAll:
    Clean up a directory tree from root. The directory need not be empty.
    The starting directory is not deleted. """
    ERROR_STR= """Error removing %(path)s, %(error)s """
    try:
        __func__(path)
        #print 'Removed ', path
    except OSError as xxx_todo_changeme:
        (errno, strerror) = xxx_todo_changeme.args
        print(ERROR_STR % {'path' : path, 'error': strerror })

def dirRemoveAll(path):
    if not os.path.isdir(path): return
    files=os.listdir(path)
    for x in files:
        fullpath=os.path.join(path, x)
        if os.path.isfile(fullpath):
            f=os.remove
            rmgeneric(fullpath, f)
        elif os.path.isdir(fullpath):
            RemoveAll(fullpath)
            f=os.rmdir
            rmgeneric(fullpath, f)

# ----------------------------------------------------------------------------------------------------
def pyexist(pycode):
    pytest = None     # *.py *.bat
    if not os.path.isfile(pycode):
       root,ext = os.path.splitext(pycode)
       pytest = root+'.pyc'
       if not os.path.isfile(pytest):
          pytest = root+'_p27.pyc'
          if not os.path.isfile(pytest):
             pytest = None
    else:
       pytest = pycode  
    return pytest
    
def scriptfullname(scriptsfx,My):
    #scriptsfx = i = 1, 2,..,such that scriptstr = My['SCRIPTi']
    #scriptstr = dir\Addwind.py my.ini 80  //My.ini & 80 = args to the PY script
    tmplst = My['SCRIPT'+str(scriptsfx)].split()
    #print tmplst
    scriptARG = ''
    if len(tmplst)>1:
       scriptARG = ' '.join(tmplst[1:])      # string with 2 args: 'My.ini 80'
    script_orig = tmplst[0]                  #original path+script, no arguments
    My['SCRIPT_ORIG'] = script_orig          #original path+script, no arguments
    if script_orig.upper() in My:
       if script_orig.upper() in ['XVAR','YVAR','ZVAR']:
          if WhatType(My[script_orig.upper()])== 'STRING':
             testdic = fnameDic(My[script_orig.upper()])
             #print testdic
             if testdic['EXT']:
                zyxfilepath  = script_orig.upper().replace('VAR','FILE')
                zyxfilepath += 'PATH'     #like XFILEPATH
                #zyxfilepath = zyxfilepath[:-1]         #delete last character
                script_orig  = My[zyxfilepath] + My[script_orig.upper()]
                #print 'script_orig:%s'%script_orig

    scriptName = fnameDic(script_orig)
    
    scriptest = pyexist(script_orig)
    if not scriptest:              # script not on the working folder or giving folder
       basefn = scriptName['ROOT']+scriptName['EXT']
       script = My['SCRIPTPATH']+ basefn
       #print '2script:%s'%script
       scriptest = pyexist(script)
       if not scriptest:                        # script not on the SCRIPTs folder
          if 'USERCODEPY' in os.environ:
             script = os.environ['USERCODEPY']+'\\'+ basefn
             scriptest = pyexist(script)
    if scriptest:
       script = scriptest
    else:
       script = script_orig
    if script[0]=='@':
       sys.argv.append(script)
       sys.argv.append('@')

    #print 'script, scriptARG=', script,'-', scriptARG
    return script, scriptARG

#{----------------------------------------------------------------------------}
def vecMaker(filekey='',beginkey=None,endkey=None,stepkey=None):
    vec = []
    filekeypath = ''
    floatdelta = 0.00000001
    if filekey:     #=Xfile or Yfile..
       if os.path.isfile(filekey):
          filekeypath = os.path.dirname(filekey)+'\\'
          for line in File2List(filekey,'/#;[@'):
              #input = aa\bb.csv  /comment
              if WhatType(line)=='STRING':
                  xline = line.split('/')
                  if len(xline)>1:
                     yline = xline[0].strip()       #no comment
                  else:
                     yline = line.strip()
                  #input = aa,bb,csv      /CSV line
                  zline = yline.split(',')    
                  if len(zline)>1:
                     wline = zline[0].strip()       #first entry
                  else:
                     wline = yline.strip()
                  if not wline: continue
              else:
                  wline = line
              vec.append(wline)
       elif '*' in filekey:     #like filekey = abc/*.out
          pathx = os.path.dirname(filekey)
          basefn= os.path.basename(filekey)
          vec = find_files(basefn,pathx)
       else:
          print('error_vecMaker: File %s does not exist.'%filekey)
    else:
       if beginkey!= None and endkey!=None and stepkey!=None:
          #print 'Y values:', beginkey, endkey, stepkey
          if IsInt(endkey) and IsInt(beginkey) and IsInt(stepkey) :       #integers
             if stepkey==0:
                print('error_vecMaker: stepkey value =%s'%stepkey)
             else:
                value = beginkey
                vec.append(value)
                if stepkey>0:
                   while value < endkey:
                      value += stepkey
                      vec.append(value)
                elif stepkey<0:
                   while value > endkey:
                      value += stepkey
                      vec.append(value)
          else:                                           #floats
             endkey  = float(endkey)
             beginkey= float(beginkey)
             stepkey = float(stepkey)
             if stepkey==0.0:
                print('error_vecMaker: stepkey value =%s'%stepkey)
             else:
                value = beginkey
                vec.append(value)
                if stepkey>0.0:
                   while value < endkey:
                         if abs(value-endkey)<floatdelta: break
                         value += stepkey
                         vec.append(value)
                elif stepkey<0.0:
                   while value > endkey:
                         if abs(value-endkey)<floatdelta: break
                         value += stepkey
                         vec.append(value)
    return vec, filekeypath
#{----------------------------------------------------------------------------}
def vectorpx(vector,CPU):
    #split a long vector into equal size per CPU (=4)
    #input: list with n-entries (100)
    #output: 4 files with 25 entries (100/4)
    #print vector,CPU
    MPPvec = []
    for i in range(CPU):
        MPPvec.append([])
    
    i = -1
    for j in range(len(vector)):
        i+= 1        
        if i== CPU:
           i = 0
        #print i,j
        MPPvec[i].append(vector[j])
    return MPPvec

#{----------------------------------------------------------------------------}
def ZYXcount(My):
    if 'ZVEC' in My:
       zcount = len(My['ZVEC'])
       if not zcount: zcount=1
    if 'YVEC' in My:
       ycount = len(My['YVEC'])
       if not ycount: ycount=1
    xcount = len(My['XVEC'])
    tcount = xcount*ycount*zcount
    countvec = [tcount,xcount,ycount,zcount]
    return countvec
    
def ZYXvars(My,zyxmsg='scenario'):
    # expected format of My['ZVAR']: path\fname.ext
    zvarkey = ''
    zvarpath= ''
    if 'ZVAR' in My:
       if isinstance(My['ZVAR'],str):
          zvarkey,zext = os.path.splitext(My['ZVAR'])
       else:
          zvarkey = str(My['ZVAR'])
       if 'ZFILE' in My:
          zvarpath= '%s\\'%os.path.dirname(My['ZFILE'])
    # expected format of My['YVAR']: path\fname.ext
    yvarkey = ''
    yvarpath= ''
    if 'YVAR' in My:
       if isinstance(My['YVAR'],str):
          yvarkey,yext = os.path.splitext(My['YVAR'])
       else:
          yvarkey = str(My['YVAR'])
       if 'YFILE' in My:
          yvarpath= '%s\\'%os.path.dirname(My['YFILE'])
    # expected format of My['XVAR']: path\fname.ext
    xvarkey = ''
    xvarpath= ''
    if 'XVAR' in My:    
       if isinstance(My['XVAR'],str):
          xvarkey,xext = os.path.splitext(My['XVAR'])
       else:
          xvarkey = str(My['XVAR'])
       if 'XFILE' in My:
          xvarpath= '%s\\'%os.path.dirname(My['XFILE'])
    #studynames = [str(My['STUDYNAME']),str(My['STUDYTYPE'])]
    #study = '_'.join([i for i in [_f for _f in studynames if _f]])
    study = getStudy(My)
    zyxnames = [study,zvarkey,yvarkey,xvarkey]
    #studyi= '_'.join([i for i in [_f for _f in zyxnames if _f]])
    studyi= '_'.join([i for i in filter(None,zyxnames)])
    # zyxmsg
    if 'PI' in My:
       zyxmsg += ' %s-'%My['PI']
    else:
       zyxmsg += ' '   
    if 'RUNI' in My:
       zyxmsg += '%s'%My['RUNI']
    if 'ZVAR' in My:
       zyxmsg += ' Z=%s,'%My['ZVAR']
    if 'YVAR' in My:
       zyxmsg += ' Y=%s,'%My['YVAR']
    if 'XVAR' in My:
       zyxmsg += ' X=%s' %My['XVAR']
    return [[studyi,zyxmsg],[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey]]

def ZYXvecs(My):
    VECS = []
    for k in ['Z','Y','X']:
        VECk = k+'VEC'
        FILEk= k+'FILE'
        if VECk not in My:
           vec = ['']
           if FILEk in My:
              vec = File2List(My[FILEk],option=[r'''/#;[@''',0])
        else:
           vec = My[VECk]
        if VECk == 'XVEC':
           if vec == ['']:
              vec = []
        VECS.append(vec)       
    return VECS

def getStudyi(My):
    zyxvars  = ZYXvars(My)            #ZYX vars= [[studyi,study],[xvarpath,xvarkey],
                                      #                          [yvarpath,yvarkey],
                                      #                          [zvarpath,zvarkey],zyxmsg]
    studyi   = zyxvars[0][0]          #= studyname_studytype_Zvar_Yvar_Xvar    
    return studyi
    
def getStudy(My):
    strlist = ['%s'%My['STUDYNAME'],'%s'%My['STUDYTYPE']]
    #study = '_'.join([i for i in [_f for _f in strlist if _f]])
    study= '_'.join([i for i in filter(None,strlist)])
    return study

def nlstruns(*args):
    # args are any number of list vars, > 0
    # returns total vars combination: len(x)*len(y)*len(z)
    total = 1
    for lsti in args:
        #print lsti
        if len(lsti)>0:
           total *= len(lsti)
        else:
           total = 0
           break
    return total

def PDFrotate(pdfile,angle):
    try:
       import PyPDF2
    except 'ImportError':
       print(' Module PyPDF2 not found, as needed for pdf page rotation.')
       print(' install it and rerun.')
       return ''
    pdf_in    = open(pdfile, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()     
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(angle)
        pdf_writer.addPage(page)    
    newpdf = '%s_rotated.pdf'%pdfile
    pdf_out = open(newpdf, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
    return newpdf
#{----------------------------------------------------------------------------}
def dirCreate(FullPathName):
    if not os.path.isdir(FullPathName): os.mkdir(FullPathName)

def dirmake(path):
    """Construct the directory "path", creating any missing intermediates.
       import os, sys
    """

    # If the path is not a directory, construct its parent...
    if not os.path.isdir(path):
        head, tail = os.path.split(path)
        #print head, '-',tail

        if head != "":
            try:
                makedir(head)
            except:
                print("Can't create directory %s"%(head))
                raise sys.exc_info()[0](sys.exc_info()[1])

    # And so we can definitely construct the final directory
    # (since by now we know that all its parents exist ;)
    if not os.path.isdir(path):
        print('Making %s...'%(path))
        os.mkdir(path)

# parse - sort routines
def diacsort(i,j):
    vect = [int(i),int(j)]
    vect.sort()
    return vect[0],vect[1]

def triacsort(i,j,k):
    vect = [int(i),int(j),int(k)]
    vect.sort()
    return vect[0],vect[1],vect[2]

# ----------------------------------------------------------------------------------------------------
def array2dict(keysv, valuesv,case='UP'):
    '''Convert 2 arrays to a dictionary
    Returns dictionary as {keysv:valuesv}
    '''
    tmpdict = {}
    for i in range(len(keysv)):
        if case=='UP':
           tmpdict[keysv[i].upper()] = valuesv[i]
        else:
           tmpdict[keysv[i].lower()] = valuesv[i]
    return tmpdict

def dicarrayidx(mydic, dickey,item):
    '''Find indexes of an item in a dictionary array.
       Returns index such:
       item = mydic[dikey][index]
    '''
    idx = -1
    for i in range(len(mydic[dickey])):
        if item == mydic[dickey][i]:
           idx = i
           break
    return idx

def arrayfloat(n, word=None):
    strlst = []
    varstr = None
    if WhatType(word)== 'FLOAT': varstr = word
    #for i in range(n): strlst.append(varstr)
    strlst = [varstr]*n
    return strlst

def arrayint(n, word=None):
    strlst = []
    varstr = None
    if WhatType(word)== 'INTEGER': varstr = word
    #for i in range(n): strlst.append(varstr)
    strlst = [varstr]*n
    return strlst

def arraystr(n, word=None):
    strlst = []
    varstr = ''
    if word: varstr = word
    #for i in range(n): strlst.append(varstr)
    strlst = [varstr]*n
    return strlst

def indexof(mylst,value,col=0,pos=0,tol=0.0001):
    #value= int, float or string
    #side = 0 -> search for exact value in mylst, good for integer values
    #side = -1 -> search for slot where value is in mylst, return lower bound, good for float array, return first instance
    #side =  1 -> search for slot where value is in mylst, return upper bound, good for float array, return first instance
    #col = 0 -> column id in a matrix to use as the searching col
    #pos = start index to perform scan
    found = False
    #print mylst
    #print 'value=',value, IsFloat(value)
    searchrange = list(range(pos,len(mylst)))
    for k in searchrange:
        if WhatType(mylst[k])=='LIST' or WhatType(mylst[k])=='TUPLE':
           listval = mylst[k][col]
        else:
           listval = mylst[k]
        if abs(listval-value) < tol:
           found = True
           n = k
        else:  
           if k == len(mylst)-1: break       #last idx
           elif mylst[k]<=value and value < mylst[k+1]:
                found = True
                if abs(mylst[k]-value) <= abs(value-mylst[k+1]):
                   n = k
                else:
                   n = k+1
                break
    
    if not found: n=None
    return n

def mapvectors(a,b,c):
    d = []
    for i in range(len(a)): d.append(None)
    for i in range(len(a)):
        k = indexof(b,a[i])
        d[i] = c[k]
    return d
#-------------------------------------------------------------------
def inrangeupperval(Curve,Q):
    #assigne the upper-bound value of segment where Q lies
    #Curve=[0.0,0.05,0.075,0.1,0.125,0.15,0.175,0.2,0.25]
    C = Curve[-1]    #max
    for i in range(len(Curve)):
        if Q <= Curve[i]:
           C  = Curve[i]
           break
    return C

def npointupperval(nCap,Csingle,Qmin,Q):
    Qmax = Csingle * float(nCap)
    if   Q  <= Qmin:  C = Qmin
    elif Q  >  Qmax:  C = Qmax      # max
    else:
         n = int(Q/Csingle)
         if (Q % Csingle) >= (Csingle/2):
             n += 1
         C = Qmin + Csingle * float(n)
    return C

def interpolate(P1,P2,x):
    #P1 = (X1,Y1)  # point as tuple
    #P2 = (X2,Y2)  # point as tuple
    if   x==P1[0]: y= P1[1]
    elif x==P2[0]: y= P2[1]
    else:
         m = (P2[1]-P1[1])/(P2[0]-P1[0])
         y = P1[1] + m*(x-P1[0])
    return y

def XY(PQcurve,P):
    #PQcurve=[(0.0,0.0),(0.45,0.32),(0.90,0.42),(1.35,0.59),(1.80,0.85)] #V80
    #PQcurve=[(0.0,0.0),(0.25,0.575),(0.5,0.667),(0.75,0.787),(1.0,1.0)] #V47 in pu
    Pmax = PQcurve[-1][0]
    if   P <= 0.0: Q = 0.0
    elif P > Pmax: Q = PQcurve[-1][1]
    else:
         Q = PQcurve[-1][1]
         for i in range(len(PQcurve)):
             if P <= PQcurve[i][0]:
                Q = interpolate(PQcurve[i-1],PQcurve[i],P)
                break
    return Q
    
# relative percentage function:
def relativepercentfx(y,yref):
    if abs(yref) < 0.001:
       val = -0.0
    else:
       val = (y-yref)/yref
    return val*100.0        # in percentage

# Trapezoidal Area
def AreaTrapezoidal(xarray, yarray):
    xyarea = 0
    for t in range(1,len(xarray)):
        xyarea += (xarray[t]-xarray[t-1])*(yarray[t]+yarray[t-1])
    return xyarea*0.5

#-------------------------------------------------------------------
def appendStrF(S,finalf,options=''):
    #options = 'wfv'   
    if 'v' in options:    #verbose
        if options:
           print('add "%s" to file %s with options %s'%(S,finalf,options))
        else:
           print('add "%s" to file %s'%(S,finalf))
    if S:
       if os.path.isfile(finalf):
          deststr = File2Str(finalf)
       else:
          deststr = ''        
       if 'w' in options:   #overwrite
          deststr = ''

       if 'f' in options:   #append to front of existing destination file
          if deststr:
             finalstr = S + deststr
       else:               #append to end of existing destination file
          if deststr:
             finalstr = deststr + S
    
       Str2File(finalstr,finalf)
    return

def appendF(myfiles,finalf,options='n',comment='//'):
    #option = 'wnfvl'
    #w = overwrite finalf
    #l = filenames given in a *.lst file
    #n = add filename to finalf before append
    #v = verbose, print filename
    #l = L = myfiles is a txt list file, with one line per filename
    #        to provide an order to appending
    if options:
       if IsInt(options):     # for compatibility ..,1)  ->  ..,'n')
          options = 'n'
       options = options.lower() 
    if myfiles:
       deststr = ''
       if not 'w' in options and os.path.isfile(finalf):
          deststr = File2Str(finalf)

       sourcestr = ''
       if 'l' in options:   #myfiles is a file with filenames, one per line
          filelst = File2List(myfiles) 
       else:
          filelst = glob.glob(myfiles)
       
       if 'v' in options:   #verbose
          print(myfiles)
       for filex in filelst:
           if not filex: continue
           if not os.path.isfile(filex): continue
           if 'v' in options:   #verbose
              print(filex)
           if 'n' in options:   #add filename 
              sourcestr += '%s* %s \n'%(comment,filex)
           sourcestr += File2Str(filex)
           if not sourcestr[-1]=='\n':
              sourcestr += '\n'
              if 'v' in options:
                 print('eol added to ',filex)
        
       finalstr = sourcestr     
       if 'f' in options:   #append to front of existing destination file
          if deststr:
             finalstr += '\n' + deststr + '\n'
       else:               #append to end of existing destination file
          if deststr:
             finalstr = deststr + '\n' + finalstr + '\n'
    
       Str2File(finalstr,finalf)
    return
#-------------------------------------------------------------------
def Filedelete(file):
    if os.path.isfile(file):
       os.remove(file)

def delf(deletethis):
    # delete files -> *.dyr or bb\\aaa.dyr
    mypath = os.path.dirname(deletethis)
    myfile = os.path.basename(deletethis)
    roottarget,exttarget = os.path.splitext(myfile)
    if  roottarget=='*':
        """delete file(s) in dir"""
        n = 0
        for root, dirs, files in os.walk(mypath):
            for file in files:
                xroot,xext =  os.path.splitext(file)
                if xext.upper() == exttarget.upper():
                   #print 'root=',root,'- dirs=', dirs, '- file=',file
                   try:
                      if root:
                         os.remove(root+'\\'+file)
                         #print file
                      else:
                         os.remove(file)
                      n += 1
                   except:
                      print("*** Unable to delete %s"%file)
        print("file %s x %s deleted."%(deletethis,n))
    elif '*' in deletethis:
        n = 0
        for file in glob.glob(deletethis):
            try:
                os.remove(file)
                n += 1
                #print "*** %s deleted" % file
            except:
                print("*** Unable to delete %s" % file)
    else:  #delete single file if found
        if os.path.isfile(deletethis):
           os.remove(deletethis)
           print("*** file %s deleted"%(deletethis))
        else:
           print("*** file %s not found - delete request ignored."%(deletethis))

def delfiles(deletethis):
    n = 0
    for file in glob.glob(deletethis):
          try:
              os.remove(file)
              n += 1
          except:
              print("*** Unable to delete %s" % file)
    if n > 0:
        print("file %s x %s deleted." % (deletethis,n))
#{----------------------------------------------------------------------------}
def getsectionlst(rawlst,section):
    sectionlst = []
    for line in rawlst:
        if line.strip()=='':continue
        if line.strip()[0]==';':continue
        if line.strip()[0]=='[':
           sectionX = betweenchars(line,'[',']')
           continue
        if sectionX.upper() == section:
           sectionlst.append(line)
    return sectionlst

#{----------------------------------------------------------------------------}
def dicVal(Word,keystr):
    #in str, search if Phrase XXX exist
    #when given an str command PHRASE=CatB
    OK = ''
    key = Word.split('=')[0]
    key = key.strip()
    if key.upper() == keystr:
       OK = Word.split('=')[1]
    return OK.strip()

#{----------------------------------------------------------------------------}   
def iniread(Fname,debug=False):
    My = {}
    if debug:
       print('in readINI:')
       print('cwd:',os.getcwd())
    if not os.path.isfile(Fname):
       # check if INIs dir exist
       if not os.path.isfile('INIs\\'+Fname):
          print('ERROR - INI file %s not found.'%Fname)
          return My

    i=0
    multiline = False
    mline = ''
    for line in File2List(Fname,'/#;[@'):
        i += 1
        linex = line.strip()
        if len(linex)<1: continue

        if linex[0] in '/#;[@': continue
        
        yline = linex
        if '/' in yline:      #does in-line comment begins with /?
           xline = yline.split('/')[0]
           yline = xline.strip()
        if ';' in yline:      #does in-line comment begins with ;?
           xline = yline.split(';')[0]
           yline = xline.strip()
        if len(yline)<1: continue
        if debug:
           print('linex=', linex)
        #check if multiline
        if   not multiline:
             if not ('=' in linex): continue
             zline = yline.split('=')
             if debug:
                print('yline=', yline)
                print('zline:%s'%zline)
             if len(zline)<1: continue
             keyvaluestr = zline[1].strip()
             if len(keyvaluestr)<1:
                keyvaluestr = ''
             elif keyvaluestr in ['"""',"'''",'[','{']:
                  multiline = True
                  mline += keyvaluestr
                  if debug:
                     print('0mline:%s'%mline)
                  continue
        else:
             if debug:
                print('1mline:%s'%yline)
             keyvaluestr = yline
             if len(keyvaluestr)<1:
                keyvaluestr = ''
             elif keyvaluestr.strip() in ['"""',"'''",']','}']:  #works for multi-line text
                  multiline = False
                  mline += keyvaluestr.strip()
                  keyvaluestr = mline
                  if debug:
                     print('mline=', keyvaluestr)               
                  mline = ''
             else:
                mline += '%s\n'%keyvaluestr
                #if WhatType(keyvaluestr)=='STRING':
                #else:
                #   mline += keyvaluestr
                continue

        if keyvaluestr:
           try:
               #print '5keyvaluestr:%s'%keyvaluestr 
               keyvalue = eval(keyvaluestr)
               if debug:
                  print('after eval, keyvalue:%s'%keyvalue)
                  print('-%s- converted to -> -%s-'%(keyvaluestr,keyvalue))
           except:
               #leftkey = keyvaluestr[:5]         #is a string
               leftkey = keyvaluestr.split('(')[0]   #is a string
               #print 'leftkey:%s'%leftkey
               if leftkey.upper() == 'FRANGE':   #format: frange(2,8,2)
                  rangestr = betweenchars(keyvaluestr,'(',')')
                  rlst = rangestr.split(',')
                  keyvalue = frange(rlst[0],rlst[1],rlst[2])
                  if debug:
                     print('[%s] converted to -> '%keyvaluestr,keyvalue)
               elif leftkey.upper() == 'ITERATE':   #format: iterate(Tth,Vstall,Tstall)
                    #tested on MPjobs\cmld_iterate.ini & scenarios.py
                    rangestr = betweenchars(keyvaluestr,'(',')')
                    rlst = rangestr.split(',')                    #=['Tth','Vstall','Tstall']
                    My_rlst = [My[k.upper()] for k in rlst]
                    #print 'My_rlst=', My_rlst
                    keyvalue = iterate(My_rlst)
               else:
                  keyvalue = keyvaluestr
                #check if it is an environ var
                #domain = %userdomain% and environ var userdomain =  
                #domain = 
               if keyvalue[0]=='%' and keyvalue[-1]=='%':
                  keyvalue = keyvalue.strip('%')
                  if keyvalue in os.environ:
                     keyvalue = os.environ[keyvalue]
                     if debug:
                        print('environ %s = %s'%(keyvaluestr,keyvalue))
                  else: continue
        else:
            keyvalue = ''
        keyname = zline[0].strip().upper()
        My[keyname] = keyvalue
    return My

#{----------------------------------------------------------------------------}   
def readIni(Fname,My,debug=False):
    inidic = iniread(Fname,debug)
    if inidic:
       My.update(inidic)
            
       My['INIFILE'] = Fname
       rootfn, ext = os.path.splitext(Fname)
       My['INIROOT'] = rootfn
       err = 0
    else:
       err = 1
    if 'DEBUG' in My:
       if My['DEBUG']==1:
          print(' INIfile=%s'%Fname)
          for keyname, keyvalue in list(My.items()):
              print('%s=%s_'%(keyname,keyvalue))
    return err, My

# ----------------------------------------------------------------------------------------------------
def CSVappendV(My):
    study  = My['STUDY']
    studyi = My['STUDYI']
    if 'PLOTEXPFN' in My:
       if not My['PLOTEXPFN']:   #if empty
          My['PLOTEXPFN'] = My['STUDYI']+'.dat'
    channelexpfn = My['OUTPATH']+My['PLOTEXPFN']
    if not os.path.isfile(channelexpfn):
       print(' File NOT found= %s'%(channelexpfn))
       return
    # Open the output CSV file or create it
    Allchanfn = My['OUTPATH']+My['STUDY']+'.csv'
    if os.path.isfile(Allchanfn):
       firsttime =  False
       tmpf = open(My['OUTPATH']+'tmp.dat','w')
       achf = open(Allchanfn,'r')
       for i in range(4):
           data = achf.readline()
           tmpf.write(data)
       data = achf.readline()
       data = data.replace('\n', '')
       tmpf.write(data+','+studyi+'\n')
    else:
       firsttime =  True
       achf = open(Allchanfn,'w')
       achf.write(My['TITLE1']+'\n')
       achf.write(My['TITLE2']+'\n')
       achf.write(My['CSVAPPENDVMSG']+'\n')
       achf.write('Scenario:,'+study+'\n')
       achf.write('Time,'+studyi+'\n')
    # process each line in the new channel file
    print('CSVappendV: Vertically appending %s to %s'%(channelexpfn,Allchanfn))
    for line in File2List(channelexpfn,option='/#;[@'):
       #if len(line.strip())==0:continue    #blank line
       linex = line.split()
       if (not IsFloat(linex[0])) or (not IsFloat(linex[1])):continue
       linexlen = len(linex)
       if firsttime:
          achf.write(linex[0]+','+ChannelEquation(linex[1])+'\n')
       else:
          data = achf.readline()
          data = data.replace('\n', '')
          for k in range(linexlen):
              if k==0:continue
              data += ','+ChannelEquation(linex[k])
          tmpf.write(data+'\n')

    achf.close()
    if not firsttime:
       tmpf.close()
       Filedelete(Allchanfn)
       os.rename(My['OUTPATH']+'tmp.dat',Allchanfn)
    return 'OK'

def ChannelEquation(Valstr,My):
    x = Valstr
    if 'CHANNELEQ' in My:
       if My['CHANNELEQ']!='':
          equation = My['CHANNELEQ'].upper()
          equation = equation.replace('A',Valstr)
          x = eval(equation)
    return str(x)

#{----------------------------------------------------------------------------}
def psspyver(str):
    # str expected: C:\Program Files (x86)\PTI\PSSE34\PSSPY37
    # or            C:\Program Files\PTI\PSSE35\35.2\PSSPY38
    while str[-1]=='\\':
          str = str[0:-1]
    tmp = str.split('\\')
    last = tmp[-1]
    #print (str)
    #print (last)
    if last.upper()=='PSSBIN':
       ver = '27'
    else:
       ver = last[-2:]
    return int(ver)

def psseversion(str):
    # str expected: C:\Program Files (x86)\PTI\PSSE34\PSSPY37
    # or            C:\Program Files\PTI\PSSE35\35.2\PSSPY38
    while str[-1]=='\\':
          str = str[0:-1]
    tmp = str.split('\\')
    last = tmp[-2]
    if '.' in last:
        ver = int(float(last))
    else:
        ver = last[-2:]
    return int(ver)
#{----------------------------------------------------------------------------}
def Add_path(mypath):
    #Add pssepath when runnnig from DOS Python Interpreter
    os.environ['PATH'] = mypath + ';' + os.environ['PATH']
    sys.path.insert(1,mypath)
#{----------------------------------------------------------------------------}
# run_from_psse = boolean function to check if runnnig from DOS Python Interpreter
def run_from_dos():
    OK = False
    exename = sys.executable
    p, nx   = os.path.split(exename)
    nx      = nx.lower()
    #print 'exename:',exename
    #print 'nx:',nx
    #print sys.argv
    if nx in ['python.exe', 'pythonw.exe']:
       OK = True      
    return OK
# --------------------------------------------------------------------------------------------------
def dirlst(myfiles):
    files = []
    if myfiles:
       files = glob.glob(myfiles)
    return files

# --------------------------------------------------------------------------------------------------
def ReadAllCtgs(CtgFname,ctgformat):
# PSSe Contingency data block sample:
# Contingency '   670 KRUM         138   1990 KRUM MBZ     138 1 '
#    Open branch from bus   670 to bus  1990 ckt 1  /     670 KRUM         138   1990 KRUM MBZ     138 1
# end
# usage:     AllCtgs = ReadAllCtgs(ctgfiles,'VSAT')

    AllCtg = []
    try:
       ctgf = open(CtgFname, 'r')
    except IOError:
       return

    if   ctgformat=='PSSE':
         beginword = 'CONTINGENCY'
         beginword = 'CONTINGENCY'
         endword   = 'END'
         commentchr= '/'
    elif ctgformat=='VSAT':
         beginword = '{CONTINGENCY}'
         beginword2= '{CONTINGENCY'
         endword   = '{END'
         commentchr= '/'

    EOF = False
    while True:
          currentrow = ctgf.readline()
          if currentrow=='': break           #EOF
          currentrow = currentrow.strip()
          if len(currentrow)<1: continue
          if currentrow[0]==commentchr: continue
          currentrow = currentrow.upper()
          JCstr = currentrow.split()[0]
          if JCstr == endword: continue
          if JCstr == beginword or JCstr == beginword2:
             block = []
             block.append(currentrow)
             finish = False
             while not finish:
               currentrow = ctgf.readline()
               if currentrow=='':
                  EOF = True
                  break                #EOF
               currentrow = currentrow.strip()
               #print 'currentrow:',currentrow
               if len(currentrow)<1:       #no empty line in ctg block
                  continue
               currentrow = currentrow.upper()
               block.append(currentrow)
               JCstr = currentrow.split()
               if JCstr[0] == endword:
                  finish = True
                  AllCtg.append(block)
          if EOF: break
    ctgf.close()
    return AllCtg
# --------------------------------------------------------------------------------------------------
# Set the current working directory for PSS/E

def SetDWGcwd():
    main_dir = os.getcwd().upper()
    for subfolder in ['CASES','SCRIPTS','PARCC']:
        if '\\'+subfolder in main_dir:
           main_dir = main_dir.replace('\\'+subfolder,'')
    return main_dir

#{----------------------------------------------------------------------------}
def dictprint(d,sortKey=0):
    printDict2(d,sortKey)

def printDict2(d,sortKey=0):
    d_view = [ (k,v) for k,v in d.items() ]
    if sortKey==1:
       d_view.sort()               # natively sort tuples by first element
    elif sortKey==-1:
         d_view.sort(reverse=True)               # natively sort tuples by first element
    for k,v in d_view:
        print ("%s: %s"%(k,v))
        
def printDict(aDict, br='\n', html=0,
              keyAlign='l',   sortKey=0,
              keyPrefix='',   keySuffix='',
              valuePrefix='', valueSuffix='',
              leftMargin=0,   indent=1 ):
    '''
return a string representive of aDict in the following format:
    {
     key1: value1,
     key2: value2,
     ...
     }

Spaces will be added to the keys to make them have same width.

sortKey: set to 1 if want keys sorted;
keyAlign: either 'l' or 'r', for left, right align, respectively.
keyPrefix, keySuffix, valuePrefix, valueSuffix: The prefix and
   suffix to wrap the keys or values. Good for formatting them
   for html document(for example, keyPrefix='<b>', keySuffix='</b>'). 
   Note: The keys will be padded with spaces to have them
         equally-wide. The pre- and suffix will be added OUTSIDE
         the entire width.
html: if set to 1, all spaces will be replaced with '&nbsp;', and
      the entire output will be wrapped with '<code>' and '</code>'.
br: determine the carriage return. If html, it is suggested to set
    br to '<br>'. If you want the html source code eazy to read,
    set br to '<br>\n'

version: 04b52
author : Runsun Pan
require: odict() # an ordered dict, if you want the keys sorted.
         Dave Benjamin 
         http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/161403

Example:

>>> a={'C': 2, 'B': 1, 'E': 4, (3, 5): 0}

>>> print printDict(a)
{
 'C'   :2,
 'B'   :1,
 'E'   :4,
 (3, 5):0
}

>>> print printDict(a, sortKey=1)
{
 'B'   :1,
 'C'   :2,
 'E'   :4,
 (3, 5):0
}

>>> print printDict(a, keyPrefix="<b>", keySuffix="</b>")
{
 <b>'C'   </b>:2,
 <b>'B'   </b>:1,
 <b>'E'   </b>:4,
 <b>(3, 5)</b>:0
}

>>> print printDict(a, html=1)
<code>{
&nbsp;'C'&nbsp;&nbsp;&nbsp;:2,
&nbsp;'B'&nbsp;&nbsp;&nbsp;:1,
&nbsp;'E'&nbsp;&nbsp;&nbsp;:4,
&nbsp;(3,&nbsp;5):0
}</code>

>>> b={'car': [6, 6, 12], 'about': [15, 9, 6], 'bookKeeper': [9, 9, 15]}

>>> print printDict(b, sortKey=1)
{
 'about'     :[15, 9, 6],
 'bookKeeper':[9, 9, 15],
 'car'       :[6, 6, 12]
}

>>> print printDict(b, keyAlign="r")
{
        'car':[6, 6, 12],
      'about':[15, 9, 6],
 'bookKeeper':[9, 9, 15]
}
'''   
    if aDict:

        #------------------------------ sort key
        if sortKey:
            dic = aDict.copy()
            keys = list(dic.keys())
            keys.sort()
            for k in keys:
                aDict[k] = dic[k]
            
        #------------------- wrap keys with ' ' (quotes) if str
        tmp = ['{']
        ks = [type(x)==str and "'%s'"%x or x for x in list(aDict.keys())]

        #------------------- wrap values with ' ' (quotes) if str
        vs = [type(x)==str and "'%s'"%x or x for x in list(aDict.values())] 

        maxKeyLen = max([len(str(x)) for x in ks])

        for i in range(len(ks)):

            #-------------------------- Adjust key width
            k = {1            : str(ks[i]).ljust(maxKeyLen),
                 keyAlign=='r': str(ks[i]).rjust(maxKeyLen) }[1]
            
            v = vs[i]        
            tmp.append(' '* indent+ '%s%s%s:%s%s%s,' %(
                        keyPrefix, k, keySuffix,
                        valuePrefix,v,valueSuffix))

        tmp[-1] = tmp[-1][:-1] # remove the ',' in the last item
        tmp.append('}')

        if leftMargin:
          tmp = [ ' '*leftMargin + x for x in tmp ]
          
        if html:
            return '<code>%s</code>' %br.join(tmp).replace(' ','&nbsp;')
        else:
            return br.join(tmp)     
    else:
        return '{}'


# -Under test begin-------------------------------------------------------------------------------------------------
def _launch_ultraedit(infile):
    cmdexe = os.environ['COMSPEC']
    ultexe = 'C:\\"Program Files"\\"IDM Computer Solutions"\\UltraEdit\\UEDIT32.EXE'
    fname = '"%s"' % infile
    os.spawnv(os.P_NOWAIT, cmdexe, [cmdexe, '/c', ultexe, fname])

def _launch_notepad(infile):
    cmdexe = os.environ['COMSPEC']
    notepad = 'notepad.exe'
    fname = '"%s"' % infile
    os.spawnv(os.P_WAIT, cmdexe, [cmdexe, '/c', notepad, fname])

def _ShowErrorInNotepad(errmsg):
    import tempfile
    fd, tmpfnam = tempfile.mkstemp(text=True)
    os.close(fd)
    tmpfobj = open(tmpfnam, 'w')
    tmpfobj.write(errmsg)
    tmpfobj.close()
    _launch_notepad(tmpfnam)
    os.remove(tmpfnam)
    raise RuntimeError()

def _run_dos_command(doscmd):
    try:
        cmdpath = os.environ['COMSPEC']
        os.spawnv(os.P_NOWAIT, cmdpath, [cmdpath, '/c', doscmd])
    except:
        try:
            cmdpath = os.environ['WINDIR'] + '\\system32\\cmd.exe'
            os.spawnv(os.P_NOWAIT, cmdpath, [cmdpath, '/c', doscmd])
        except:
            raise 'ERROR: Could not find %s file to run..\n'

def _run_dos_command_wait(doscmd):
    try:
        cmdpath = os.environ['COMSPEC']
        os.spawnv(os.P_WAIT, cmdpath, [cmdpath, '/c', doscmd])
    except:
        try:
            cmdpath = os.environ['WINDIR'] + '\\system32\\cmd.exe'
            os.spawnv(os.P_WAIT, cmdpath, [cmdpath, '/c', doscmd])
        except:
            raise 'ERROR: Could not find {} file to run..\n'


def myrmdir(dirpath):
    if dirpath[-1] == os.sep:
        dirpath = dirpath[:-1]
    if debug > 99:
        print('**** myrmdir *** ', dirpath)
    items = os.listdir(dirpath)
    for f in items:
        if f == '.' or f == '..':
            continue
        path = dirpath + os.sep + f
        if os.path.isdir(path):
            if debug > 99:
                print('Deleting', path)
            myrmdir(path)
        else:
            if debug > 99:
                print('Deleting', path)
            os.unlink(path)
        try:
            os.rmdir(dirpath)
            if debug > 6:
                print('Deleted:', dirpath)
        except:
            if debug > 99:
                print('rmdir failed!', dirpath)

def _decode_arg(i_argument, v_argument):
    global debug
    global strGUI
    global chkBASKV
    if i_argument > 3:
        if debug > 0:
            print('*** WARNING: More args than expected!')
    else:
        value = ''
        h_Arg = v_argument.upper()
        for char in h_Arg:
            if char in '0123456789':
                value = value + char

        if value != '':
            debug = int(value)
        if h_Arg == 'FULL':
            strGUI = 'FULL'
        if h_Arg == 'NOBASKV':
            chkBASKV = 1

#_______________________________________________________________________
def bsyset(sid=-1,basekv=[],areas=[],buses=[],owners=[],zones=[]):
    ''' Function bsyset - to set a buses subsystem using bsys.
     
        bsyset(sid=-1,basekv=[],areas=[],buses=[],owners=[],zones=[])
        
        e.g.1: subsystem creation for a group of buses
        # Genbus+POIbus Subsystem
        sid = 1
        BUSES = [Genbus,POIbus]                  #Set to whatever buses(s)
        #ierr = psspy.bsys(sid, usekv, basekv, numarea, areas, numbus, buses, numowner, owners, numzone, zones)
        ierr  = bsyset(sid, buses=BUSES)

        e.g.2: subsystem creation for an area
        # select all buses in area 5
        sid = 1
        AREAS = [5,]                  			#Set to whatever area(s) you want to select
        ierr  = bsyset(sid, areas=AREAS)
    '''
    import psspy

    ierr  = 0
    if 0 <= sid and sid <= 11:
       if basekv and len(basekv)==2:
          usekv  = 1
       else:
          usekv  = 0
          basekv = [0.0,0.0]
       ierr = psspy.bsys(sid,
                         usekv,basekv,
                         len(areas),areas,
                         len(buses),buses,
                         len(owners),owners,
                         len(zones),zones)
    return ierr       
#_______________________________________________________________________
def subsystem_data(sid, name, attributes, **kwargs):
    """
    Have you ever looked at the PSSE subsystem data retrieval API (Chapter 8 in the PSSE API guide)?
    With it you can get information about branches and buses (and other elements like machines) for an entire subsystem.
    So how would we go about getting a list of all of the bus numbers in subsystem 2?                        
    ierr, busnumbers = psspy.abusint(sid=2, string="NUMBER")

    Things become tricky when we want the bus names and the bus numbers though.

    ierr, busnumbers = psspy.abusint(sid=2, string="NUMBER")
    ierr, busnames = psspy.abuschar(sid=2, string="NAME")

    We had to know that the NAME attribute uses a different API call to the NUMBER attribute. 
    If we wanted to get the bus per unit voltage we would need another API call again, 
    and if we wanted the total in service fixed bus shunt in MW and MVar a fourth API call would be required.

    four function calls is three too many:

    ierr, busnumbers = psspy.abusint(sid=2, string="NUMBER")
    ierr, busnames   = psspy.abuschar(sid=2, string="NAME")
    ierr, busvoltages= psspy.abusreal(sid=2, string="PU")
    ierr, bus_shunts = psspy.abuscplx(sid=2, string="SHUNTACT")

    Each of the return values from the API is a nested list. If you wanted to get the name and pu voltage for bus number 340:

    getting name and pu voltage for bus number 340

    bus_index= busnumbers[0].index(340)
    voltage  = busvoltages[0][bus_index]
    name     = busnames[0][bus_index]

    Using the new subsystem_info function is easy. Lets get the bus numbers, names, pu voltages and actual shunt values for subsystem id 2:

    >>> businfo = subsystem_info('bus', ['NUMBER', 'NAME', 'PU', 'SHUNTACT'], sid=2)
    >>> print businfo
    [(205, 'CATDOG', 1.01, complex(0.4, 0)),
     (203, 'CATDOG2', 0.99, complex(0, 0)),
     ... ]
     
    All of the information we were looking for is organised neatly into rows, rather than separate columns. Here is how we made that function.

    How does this work?

    The new function relies on some helpful design choices in the original PSSE subsystem data retrieval api.
    Each of the functions are named using a regular pattern:

         abusint,
         abuscplx,
         amachint,
         aloadint
         
    a element type api data type

    a bus int

    There is a lookup function called abustypes (we'll call it types) which will return a character string that represents each of the api data types. For example

    >>> psspy.abustypes("NUMBER")
    "I"

    We ask the types function about each of the attributes the user has requested. 
    So a query like ["NUMBER", "NAME", "PU"] might return ["I", "R", "C"], being int, real and char respectively.

    Use a dictionary to store functions

    Ok, so we can find a character "I", "R", "C" that represents the API type. 
    Translating that character into the correct retrieval function to use is the clever part.

    There is a Python dictionary to look up the corresponding API call for the attribute requested. 
    So asking for "NUMBER" which returns "I" from the types function will retrieve the psspy.abusint function from the dictionary. 
    Using a dictionary to look up a function like this is called the 'dispatch table pattern' 
    (example 4.16 in the Python Cookbook if you have a copy)

    Grouping related calls to the API together

    The difficult part is grouping and returning the API calls in rows and in the order they were requested. 
    The itertools groupby function is used to group related API calls together 
    so if we requested ["NUMBER", "TYPE", "NAME"] we might get ["I", "I", "C"] from abustypes.

    The groupby will group the two consecutive "I" api calls together so we can make one function call:

    abusint(string=["NUMBER", "TYPE"])

    instead of two function calls:

    abusint(string="NUMBER") # and
    abusint(string="TYPE")

    Transpose columns to rows

    Finally, we use the built in zip function to transpose a list of columns into a list of rows

    >>> zip(*[[1,2,3], [4,5,6]])
    [(1,4), (2, 5), (3,6)]

    Posted by whit Aug 19th, 2011
    
    Returns list of tuples of requested attributes from the PSS(r)E subsystem API
    for the given subsystem id and subsystem element name.
    
    sid: list only information for elements in this subsystem id (-1, all elements by default).

    e.g.1 - to retrieve bus attributes "NAME", "NUMBER" and "PU" for all buses (sid = -1 default)
                subsystem_data(sid, 'bus', ["NAME", "NUMBER", "PU"])

    e.g.2 - to retrieve mach attributes 'NUMBER','ID','PGEN','PMAX', in 
                sid = 1
                AREA= [1,2...] #Set to whatever area(s) you want to adjust
                err = psspy.bsys(BSYS, 1, 1, 1, AREA)
                macdata = subsystem_data(sid,'mach', ['NUMBER','ID','PGEN','PMAX'])

    where the 'bus' attributes "name" argument comes from the original PSS(r)E 
    subsystem API naming convention found in Chapter 8 of the PSS(r)E API:
                   name
        abusint  # bus
        amachint # mach <- uses AZO values from the bus group 
        aloadint # load <- uses AZO values from the Load group!!!

    Keyword Args (unlimited):
      **kargs [optional]:
         to customize the function call, depend on type of network element.
         i.e: for bus, mach, load family: flag=2 to include all buses, default to flag=1, only in-service buses.
         for brn family: owner, ties, flag, entry
    """
    from itertools import groupby
    from operator  import itemgetter
    import psspy
    _i = psspy.getdefaultint()
    _f = psspy.getdefaultreal()
    _c = psspy.getdefaultchar()
    attr_type = itemgetter(0)    
    name = name.lower()
    gettypes = getattr(psspy, 'a%stypes' % name)
    apilookup = {'C': getattr(psspy, 'a%schar'% name),
                 'I': getattr(psspy, 'a%sint' % name),
                 'R': getattr(psspy, 'a%sreal'% name),
                 'X': getattr(psspy, 'a%scplx'% name),  
                 }
    ierr, attr_types = gettypes(attributes)
    all = list(zip(attr_types, attributes))
    #print ('all:',all)
    #for k, group in groupby(zip(attr_types, attributes), key=attr_type):
    result = []
    #for k, group in groupby(all), key=attr_type):
    for k, strings in all:
        func     = apilookup[k]
        #strings  = list(zip(*group)[1])
        #strings = [all[i][1] for i in range(len(all)) if k==all[i][0]]
        #strings = [all[i][1] for i in range(len(all))]
        #print ('k,strings = ',k,strings)
        if name in ['bus','mach','lod','load','genbus','fxshntbus','fxshunt','swsh','area','owner','zone','indmac','indmacbus']:
           flag = _i
           for key, value in kwargs.items():
               if key=='flag':
                  flag= value
           ierr, res= func(sid, string=strings, flag= flag)
        elif name in ['2trmdc','multitrmdc','vscdc']:
           ties = _i
           flag = _i
           for key, value in kwargs.items():
               if key=='ties':  ties = value
               if key=='flag':  flag = value
           ierr, res= func(sid, string=strings, ties=ties, flag= flag)
        elif name in ['flow']:
           owner= _i
           ties = _i
           flag = _i
           for key, value in kwargs.items():
               if key=='owner': owner= value
               if key=='ties':  ties = value
               if key=='flag':  flag = value
           ierr, res= func(sid, string=strings, owner=owner, ties=ties, flag= flag)
        elif name in ['facts']:
           ties = _i
           flag = _i
           fcttyp= _i
           for key, value in kwargs.items():
               if key=='ties':  ties = value
               if key=='flag':  flag = value
               if key=='fcttyp': entry= value
           ierr, res= func(sid, string=strings, ties=ties, flag= flag, fcttyp=fcttyp)
        elif name in ['factsbus']:
           ties = _i
           flag = _i
           entry= _i
           fcttyp= _i
           for key, value in kwargs.items():
               if key=='ties':  ties = value
               if key=='flag':  flag = value
               if key=='entry': entry= value
               if key=='fcttyp': entry= value
           ierr, res= func(sid, string=strings, ties=ties, flag= flag, fcttyp=fcttyp, entry=entry)
        elif name in ['2trmdcconv','multitrmdcconv','vscdcconv']:
           ties = _i
           flag = _i
           entry= _i
           for key, value in kwargs.items():
               if key=='ties':  ties = value
               if key=='flag':  flag = value
               if key=='entry': entry= value
           ierr, res= func(sid, string=strings, ties=ties, flag= flag, entry=entry)
        elif name in ['brn','trn','tr3','wnd']:
           owner= _i
           ties = _i
           flag = _i
           entry= _i
           for key, value in kwargs.items():
               if key=='owner': owner= value
               if key=='ties':  ties = value
               if key=='flag':  flag = value
               if key=='entry': entry= value
           ierr, res= func(sid, string=strings, owner=owner, ties=ties, flag= flag, entry=entry)
        elif name in ['zmut']:
           owner= _i
           ties = _i
           flag = _i
           brns = _i
           for key, value in kwargs.items():
               if key=='owner': owner= value
               if key=='ties':  ties = value
               if key=='flag':  flag = value
               if key=='brns':  brns= value
           ierr, res= func(sid, string=strings, owner=owner, ties=ties, flag= flag, brns=brns)
        else:
           ierr, res= func(sid, string=strings)
        result.extend(res)

    #return zip(*result)
    if len(result)>1:
       final = list(zip(*result))
    else:
       final = result[0]
    return final

class log_class:
    """  A class is used to handle log file operations so that <log> can be a global variable
         usage:
            logfile = "mylog.log"     # Name log file
            log.open(logfile)         # open log for writing
            log.open(logfile,'a')     # open log for appending
            log.write(" **** Program **** Version="+programversion)
            ...
            log.writeprint(" warning: %s"%errstr)
            ...
            log.close()
            
        if __name__ == '__main__':
           log = log_class()  # create log object - a global variable
           main()           
    """
    
    def __init__(self):
        _logfile = None
    def open(self,fname,option='w'):
        #option = w -> over writing
        #option = a -> append writing
        self._logfile = open(fname, option)
    def close(self):
        try: self._logfile.close()
        except: pass
    def write(self,txt):                    #print to log file, no return line
        if txt: self._logfile.write(txt)
    def writeln(self,txt):                  #print to log file + return line
        try:
            if txt!="": self._logfile.write(txt+'\n')
        except: pass
    def writeprint(self,txt):               #print to console & log file
        try:
            if txt!="":
                print(txt)                     #print to console
                self._logfile.write(txt+'\n') #print to log file
        except: pass

# -Under test end-------------------------------------------------------------------------------------------------
def PUvector(vectin):
    if abs(vectin[0]) < 1e-09:
       return 1,vectin
    vectout = []
    for k in range(len(vectin)):
        vectout.append(vectin[k]/vectin[0])
    return 0,vectout
#_______________________________________________________________________________
#_______________________________________________________________________________
              #plotting:
#_______________________________________________________________________________
#_______________________________________________________________________________
# do a XY plot
def plot_xy(x,y):
    import matplotlib.pyplot as plt
    plt.plot(x,y)
    #plt.grid()
    #plt.show()

#___________________________________________________________________________________
def plot2p1f(pp,vec3xy,My):
    '''
    vec3xy = [[x1,y1],[x2,y2],[x3,y3]] is a list of 3 pair-list with series-like data
    My is a dictionary with multiple variables to customize plot, like titles, pdfile, legends, etc.
        My['COLORPIC']= ['r-','b-','g-']
        My['COLORAXE']= ['b','g']
        My['TITLE']   = 'title'
        My['YLABEL']  = ['Power','Freq']
        My['PLOTSHOW']= True
        My['GRIDON']  = True
        My['LEGENDON']= True
        My['LEGENDLABELS'] = ['Power','Freq']
        My['LEGENDFONTSIZE']= 9
        My['LEGENDLOC'] = 'best'
    '''
    import matplotlib.pyplot as plt
    #figsize = My['FIGSIZE']
    colorpic = My['COLORPIC']        # colorpic = ['r-','b-','g-']
    coloraxe = My['COLORAXE']        # coloraxe = ['b','g']
    #xlabel  = My['XLABEL']
    ylabel   = My['YLABEL']          # ylabel = ['aa','bb']
    title    = My['TITLE']           # title  = 'ddd'
    titlepage= My['TITLEPAGE']       # titlepage= 'hhh'
    if 'TITLEFONTSIZE' in My:
       titlefontsize= My['TITLEFONTSIZE']
    else:
       titlefontsize= 9
    if 'PLOTSHOW' in My:
       plotshow= My['PLOTSHOW']
    else:
       plotshow= True
    if 'GRIDON' in My:
       gridON= My['GRIDON']
    else:
       gridON= False
    if 'LEGENDON' in My:
       legendON= My['LEGENDON']
    else:
       legendON= True
    if 'LEGENDLABELS' in My:    #["Measured PWR", "Simulated PWR", "Frequency"]
       legendlabels= My['LEGENDLABELS']
    else:
       legendlabels= My['YLABEL']
    if 'LEGENDFONTSIZE' in My:
       legendfontsize= My['LEGENDFONTSIZE']
    else:
       legendfontsize= 9
    if 'LEGENDLOC' in My:
       legendloc= My['LEGENDLOC']
    else:
       legendloc= 'best'
    #_____________________________________________
    x1  = vec3xy[0][0]
    y1  = vec3xy[0][1]
    x2  = vec3xy[1][0]
    y2  = vec3xy[1][1]
    x3  = vec3xy[2][0]
    y3  = vec3xy[2][1]
    #_____________________________________________
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    if 'YSCALE' in My:
       ax1.set_ylim(My['YSCALE'][0],My['YSCALE'][1])
    if 'XSCALE' in My:
       ax1.set_xlim(My['XSCALE'][0],My['XSCALE'][1])
    l1, = ax1.plot(x1,y1,colorpic[0])
    l2, = ax1.plot(x2,y2,colorpic[1])
    ax1.set_ylabel(ylabel[0])
    ax2 = ax1.twinx()
    if 'XSCALE' in My:
       ax2.set_xlim(My['XSCALE'][0],My['XSCALE'][1])
    l3, = ax2.plot(x3,y3,colorpic[2])
    #ax2.set_ylabel('Frequency (Hz)', color='g')
    fig.suptitle(titlepage)
    plt.title(title,fontsize=titlefontsize)
    for tl in ax2.get_yticklabels():
        tl.set_color(coloraxe[1])
    if gridON== True: ax1.grid()
    plt.legend([l1, l2, l3],
               legendlabels,
               fontsize=legendfontsize,
               loc=legendloc)
    if plotshow: plt.show()
    pp.savefig(fig)
    plt.close(fig)
#___________________________________________________________________________________
def plotx2y(vec2xy,My):
    '''
    vec2xy = [[x1,y1],[x2,y2]] is a list of 2 pair-list with series-like data
    My is a dictionary with multiple variables to customize plot,
       like titles, pdfile, legends, etc.
    My['COLORPIC']= ['r-','g-']
    My['COLORAXE']= ['b','g']
    My['YLABEL']  = ['Power','Freq']
    My['PLOTSHOW']= True
    My['GRIDON']  = True
    My['LEGENDON']= True
    My['LEGENDLABELS'] = ['Power','Freq']
    My['LEGENDLOC'] = 'best'
    '''
    import matplotlib.pyplot as plt
    #figsize = My['FIGSIZE']
    colorpic= My['COLORPIC']        # colorpic = ['r-','g-']
    coloraxe= My['COLORAXE']        # colorpic = ['b','g']
    #xlabel  = My['XLABEL']
    ylabel  = My['YLABEL']          # ylabel = ['aa','bb']
    #titles  = My['TITLES']
    if 'PLOTSHOW' in My:
       plotshow= My['PLOTSHOW']
    else:
       plotshow= True
    if 'GRIDON' in My:
       gridON= My['GRIDON']
    else:
       gridON= False
    if 'LEGENDON' in My:
       legendON= My['LEGENDON']
    else:
       legendON= True
    if 'LEGENDLABELS' in My:
       legendlabels= My['LEGENDLABELS']
    else:
       legendlabels= My['YLABEL']
    if 'LEGENDFONTSIZE' in My:
       legendfontsize= My['LEGENDFONTSIZE']
    else:
       legendfontsize= 9
    if 'LEGENDLOC' in My:
       legendloc= My['LEGENDLOC']
    else:
       legendloc= 'best'
    #_____________________________________________
    x1  = vec2xy[0][0]
    y1  = vec2xy[0][1]
    x2  = vec2xy[1][0]
    y2  = vec2xy[1][1]
    #_____________________________________________
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    l1,=ax1.plot(x1, y1,colorpic[0])
    ax1.set_ylabel(ylabel)
    ax2 = ax1.twinx()
    l2,=ax2.plot(x2,y2,colorpic[1])
    ax2.set_ylabel(ylabel2, color=coloraxe[1])
    for tl in ax2.get_yticklabels():
        tl.set_color(coloraxe[1])
    if gridON: plt.grid()
    if legendON:
       plt.legend([l1, l2],
                  legendlabels,
                  fontsize=legendfontsize,
                  loc=legendloc)
    if plotshow: plt.show()
    plt.close(fig)
#___________________________________________________________________________________
def plot_pd_allinone(series_df,My):
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    '''
    series_df is a pandas DataFrame with series-like data, with
              time as its first array
    My is a dictionary with multiple variables to customize plot,
       like titles, pdfile, legends, etc.
    '''
    plotfile = My['PLOTFILE']
    legendON = My['LEGENDON']
    plotshow = My['PLOTSHOW']
    with PdfPages(plotfile) as pdf:   
         #fig = plt.figure(figsize=(12,12))
         fig = series_df.plot(legend=legendON).get_figure()
         if plotshow: plt.show()
         pdf.savefig(fig)
         #plt.close()
#___________________________________________________________________________________
def plot_pd_nxm(df,My):
    '''
    df is a pandas DataFrame with series-like data, with
       time as its first array
    My is a dictionary with multiple variables to customize plot,
       like titles, pdfile, legends, etc.
    '''
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    colmax  = df.shape[1]
    plotfile= My['PLOTFILE']
    plotref = My['PLOTREF'] 
    plotmax = My['PLOTMAX']         #the code is limited to less than 10 plots per page
    curvemax= My['CURVEMAX']
    xlabel  = My['XLABEL']
    ylabel  = My['YLABEL']
    titles  = My['TITLES']
    figsize = My['FIGSIZE']
    legendON= My['LEGENDON']
    fontsize= My['FONTSIZE']
    newpage = True 
    pageid  = 0  
    ncurves = 0
    pdf     = PdfPages(plotfile)
    for column in range(colmax):
        ncurves += 1
        if newpage:
           newpage = False
           pageid += 1
           newplot = True
           plotid  = 0
           fig = plt.figure(figsize=figsize) # inches
        if newplot:
           newplot = False
           curveid = 0
           plotid += 1
           plot_num = plotref + plotid
           plt.subplot(plot_num)
        curveid +=1
        #print ncurves, pageid, plotid, curveid
        df[df.columns[column]].plot(legend=legendON, 
                                    #layout=(3, 2), 
                                    #sharex=True, 
                                    #sharey=True
                                    )
        plt.grid()
        plt.xlabel(xlabel)   #default to label of x-signal
        plt.ylabel(ylabel)
        plt.title(titles)
    
        # change font size
        plt.rcParams.update({'font.size': fontsize})
         
        if   column == colmax-1:
             plt.tight_layout()
             pdf.savefig(fig)
        elif curveid == curvemax:
             newplot = True
             if plotid+1 > plotmax:
                newpage = True
                plt.tight_layout()
                pdf.savefig(fig)
    pdf.close()
#___________________________________________________________________________________
def plotline(x, y, Labelst,marker=None,linestyle='-'):
   import matplotlib.pyplot as plt
   plt.xlabel(Labelst[0])
   plt.ylabel(Labelst[1])
   plt.title(Labelst[2])
   plt.legend()       #shows the labels
   if marker:
      plt.plot(x, y, marker=marker)
   else:
      plt.plot(x, y)    
   plt.show()
   return
   #Marker Code> Marker Displayed  |  Linestyle Code Line style Displayed    | Color Code Color Displayed                                       
   #  '.'       point              |      -    Solid Line                    |    r Red                                                         
   #  ','       pixel              |      - -  Dashed Line                   |    b Blue                                                        
   #  'o'       circle             |      :    Dotted Line                   |    g Green                                                       
   #  'v'       triangle_down      |      -.   Dash-Dotted Line              |    c Cyan                                                        
   #  '^'       triangle_up        |      None No Connecting Lines           |    m Magenta                                                     
   #  '<'       triangle_left      |                                         |    y Yellow                                                      
   #  '>'       triangle_right     |                                         |    k Black                                                       
   #  '1'       tri_down           |                                         |    w White                                                       
   #  '2'       tri_up             |                                         |                                                                  
   #  '3'       tri_left           |                                         |    color='blue')        # specify color by name -  color='blue'                                                               
   #  '4'       tri_right          |                                         |    color='g')           # short color code (works for rgb & cmyk)                                          
   #  's'       square             |                                         |    color='0.75')        # Greyscale as 0 to 1 - color='0.75'                                               
   #  'p'       pentagon           |                                         |    color='#FFDD44')     # Hex color code (RRGGBB from 00 to FF)                                            
   #  '*'       star               |                                         |    color=(1.0,0.2,0.3)) # RGB tuple, between 0 and 1                                                       
   #  'h'       hexagon1           |                                         |    color='chartreuse')  # all html color names are supported;                                              
   #  'H'       hexagon2           |                                         |                                              
   #  '+'       plus               |                                         |                                              
   #  'x'       x                  |                                         |                                              
   #  'D'       diamond            |                                         |                                              
   #  'd'       thin_diamond       |                                         |                                              
   #  '|'       vline              |                                         |                                              
   #  '_'       hline              |                                         |                                              
   #                                                                                                                                                                     
   # Basic Plotting with Python and Matplotlib                                                                                  
   # This guide assumes that you have already installed NumPy and Matplotlib for your Python distribution.                         
   # You can check if it is installed by importing it:                                                                             
   #     import numpy as np                                                                                                        
   #     import matplotlib.pyplot as plt # The code below assumes this convenient renaming                                         
   #                                                                                                                               
   # For those of you familiar with MATLAB, the basic Matplotlib syntax is very similar.                                           
   # Line plots                                                                                                                 
   # The basic syntax for creating line plots is plt.plot(x,y),                                                                 
   # where x and y are arrays of the same length that specify the (x; y) pairs making the line.                                 
   # For example, let''s plot the cosine function from -2 to 1.                                                                 
   # Let's do a discretization (grid) of the values along the x-axis, and evaluate the function on each x value.                
   # This can typically be done with numpy.arange or numpy.linspace.                                                            
   #                                                                                                                            
   #     xvals = np.arange(-2, 1, 0.01)   # Grid of 0.01 spacing from -2 to 10                                                  
   #     yvals = np.cos(xvals)            # Evaluate function on xvals                                                          
   #     plt.plot(xvals, yvals)           # Create line plot with yvals against xvals                                           
   #     plt.show()                       # Show the figure                                                                     
   #                                                                                                                            
   # You should put the plt.show command last after you have made all relevant changes to the plot.                             
   # You can create multiple figures by creating new figure windows with plt.figure().                                          
   # To output all these figures at once, you should only have one plt.show command at the very end.                            
   # Also, unless you turned the interactive mode on, the code will be paused until you close the figure window.
   #
   # Suppose we want to add another plot, the quadratic approximation to the cosine function.
   # We do so below using a different color and line type.
   # We also add a title and axis labels, which is highly recommended in your own work.
   # Also note that we moved the plt.show command to the end so that it shows both plots.
   #
   #     newyvals = 1 - 0.5 * xvals**2    # Evaluate quadratic approximation on xvals
   #     plt.plot(xvals, newyvals, 'r--') # Create line plot with red dashed line
   #     plt.title('Example plots')
   #     plt.xlabel('Input')
   #     plt.ylabel('Function values')
   #     plt.show()                       # Show the figure (remove the previous instance)
   #
   # The third parameter supplied to plt.plot above is an optional format string.
   # The particular one specified above gives a red dashed line.
   # See the extensive Matplotlib documentation online for other formatting commands,
   # as well as many other plotting properties that were not covered here:
   # http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.plot
# --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
   word = 'I am JCtools'
   print(word, reversestr(word))
   My = {}
   # path is a directory of which you want to list
   directories = os.listdir( '.\\' )
   for file in directories:
       if '.ini' in file:  
          print (file)
          ierr, My = readIni(file, My, 0)
          for keyname, keyvalue in list(My.items()):
              print('%s=%s-'%(keyname,keyvalue))
          break
