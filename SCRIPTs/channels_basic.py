# channels.py" release 32.02.03
#print ' channels.py begin'
psspy.chsb(0,1,[-1,-1,-1,1,1,0])        # ANGLe channels
psspy.chsb(0,1,[-1,-1,-1,1,2,0])        # POWR channels = Pelec of machines
psspy.chsb(0,1,[-1,-1,-1,1,3,0])        # VARS channels = Qelec of machines
psspy.chsb(0,1,[-1,-1,-1,1,4,0])        # ETERM channels
psspy.chsb(0,1,[-1,-1,-1,1,7,0])        # SPEED channels
# BES kV Subsystem
psspy.bsys(1,1,[ 100., 500.],0,[],0,[],0,[],0,[])
psspy.chsb(1,0,[-1,-1,-1,1,13,0])       # VOLT channels for 138 kV buses
psspy.chsb(1,0,[-1,-1,-1,1,12,0])       # FREQ channels for 138 kV buses
#print ' channels.py ended'
