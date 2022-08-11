from pathlib import Path
import sys
import os
setpath = Path(os.path.realpath(__file__)).parent
sys.path.insert(0,str(setpath.parent))


# os.chdir(path/'wfcdata')

import matplotlib.pyplot as plt
import h5py as hp
import numpy as np
import matplotlib.pyplot as plt
from gpe import *
import para

G = GPE()
G.set_arrays()

# path='/Users/sachin/Desktop/postprocessing_data/wfcdatarandom' #Path to the folder where data is stored 
# path='/Users/sachin/Desktop/postprocessing_data/wfcmodesNlin1000'
path='/Users/sachin/Desktop/postprocessing_data/wfcrandomN1000t1000'
# path='/Users/sachin/Desktop/postprocessing_data/wfcinitcond2N1000t1000'
# path='/Users/sachin/Desktop/postprocessing_data/wfcinitcond2N1000t1000k50'

os.chdir(path)

showspectrum=True
showphase=False
showwfcabs=False
showflux=False


for i in [0,40]:#0,10,20,50,200,300,400,450,499,0,40
    file_name='wfc_t%d.hdf5'%i
    f=hp.File(file_name,'r')
    G.wfc=np.array(f['wfc'])
    t=np.array(f['t'])
    f.close()
    if showspectrum:
        G.wfck=my_fft.forward_transform(G.wfc)
        k,spectrumE=G.spectrum(ncp.abs(G.wfck)**2)
        plt.loglog(k,spectrumE,label='t=%1.2f'%t)
        plt.xlabel("k")
        plt.legend()
        plt.ylabel(r"$E(k)$")
        plt.xlim(right=k[-1]+1)
        # plt.ylim(bottom=0)
        # plt.title('t=%1.2f' %t)
        # plt.savefig('Ekt%d.png'%int(para.tmax))
        # plt.show()
        # plt.close()
plt.show()
if showphase:
    plt.imshow(ncp.angle(G.wfc),vmin=(ncp.angle(G.wfc)).min(),vmax=(ncp.angle(G.wfc)).max(),extent=[-para.Lx//2,para.Lx//2,-para.Lx//2,para.Lx//2])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()
    plt.show()
    plt.title('t=%1.2f' %t)
    # plt.savefig('phit%d.png'%int(para.tmax))
    plt.close()

if showwfcabs:
    plt.imshow(ncp.abs(G.wfc)**2,extent=[-para.Lx//2,para.Lx//2,-para.Lx//2,para.Lx//2])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()
    plt.title('t=%1.2f' %t)
    plt.show()
    plt.close()

if showflux:
    k,flux=G.comp_flux()
    plt.plot(k,flux)
    plt.xlabel("k")
    plt.ylabel(r"$\Pi(k)$")
    plt.xlim([0,k[-1]+1])
    plt.title('t=%1.2f' %t)
    plt.show()
    # plt.savefig('fluxt%d.png'%para.tmax)
    plt.close()





# plt.imshow(ncp.abs(G.wfc)**2,extent=[-para.Lx//2,para.Lx//2,-para.Lx//2,para.Lx//2])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.colorbar()
# plt.savefig('psi2t%d.png'%int(para.tmax))
# plt.close()



# k,flux=G.comp_flux()
# plt.plot(k,flux)
# plt.xlabel("k")
# plt.ylabel(r"$\Pi(k)$")
# plt.xlim([0,k[-1]+1])

# plt.savefig('fluxt%d.png'%para.tmax)
# plt.close()



# transfer=G.transfer_function()
# k,transfers=G.spectrum(transfer)
# plt.plot(k,transfers)
# plt.xlabel("k")
# plt.ylabel(r"$T(k)$")
# plt.xlim([0,k[-1]+1])
# plt.savefig('Tkt%d.png'%int(para.tmax))
# plt.close()


