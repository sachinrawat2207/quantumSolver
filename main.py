from set_device import ncp, Target
from gpe import *
from time_advance import *
import init_cond
from pathlib import Path
import os
import h5py as hp

#Path to the folder to store data
path = Path(os.path.realpath(__file__)).parent
path = path/'postprocessing/wfcdata'
os.chdir(path)


G = GPE()
G.set_arrays()
init_cond.initcond(G)
print(G.velocity())


# Setting data storage path

'''
t = para.dt
j = 0
for i in range(para.nstep):
    time_adv_strang(G)

    filename = 'wfc_t%d.hdf5' % j
    if (para.tstore[j]-t)/para.dt < para.dt:
        f = hp.f = hp.File(filename, 'w')
        if Target == 'CPU':
            f.create_dataset('wfc', data=G.wfc)
        elif Target == 'GPU':
            f.create_dataset('wfc', data=ncp.asnumpy(G.wfc))
        f.create_dataset('t', data=t)
        f.close()
        j = j+1
    t = t+para.dt
'''
