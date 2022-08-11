import para
import my_fft
from set_device import ncp


#-----------------------------------------TSSP scheme-----------------------------------------
def tssp_stepr(G,dt):
    return G.wfc * ncp.exp(-1j * (G.V + para.Nlin * (G.wfc*G.wfc.conj())) * dt)
def tssp_stepk(G,dt):
    return G.wfck * ncp.exp(-1j * (my_fft.ksqr/2) * dt)

# For real time evolution
def time_adv_strang(G):
    G.wfc = tssp_stepr(G,para.dt/2)
    G.wfck = my_fft.forward_transform(G.wfc)
    G.wfck = tssp_stepk(G,para.dt)
    G.wfc = my_fft.inverse_transform(G.wfck)
    G.wfc = tssp_stepr(G,para.dt/2)

# For imaginary time evolution
def time_adv_gstate_strang(G):
    G.wfc = tssp_stepr(G,-1j*para.dt/2)
    G.wfck = my_fft.forward_transform(G.wfc)
    G.wfck = tssp_stepk(G,-1j*para.dt)
    G.wfc = my_fft.inverse_transform(G.wfck)
    G.wfc = tssp_stepr(G,-1j*para.dt/2)
    G.wfc=G.wfc/(para.volume * ncp.sum(ncp.abs(my_fft.forward_transform(G.wfc))**2))**.5


#-----------------------------------------RK4 scheme-----------------------------------------
def compute_RHS(G,psik):
    psi=my_fft.inverse_transform(psik)
    psi=-1j*(my_fft.ksqr*psik/2+my_fft.forward_transform((para.Nlin*ncp.abs(psi)**2+G.V)*psi))
    return psi

def time_adv_RK4(G):
    k1=para.dt*G.compute_RHS(G.wfck)
    k2=para.dt*G.compute_RHS(G.wfck+k1/2)
    k3=para.dt*G.compute_RHS(G.wfck+k2/2)
    k4=para.dt*G.compute_RHS(G.wfck+k3)
    G.wfck = G.wfck+(k1+2*k2+2*k3+k4)/6
    G.wfc = my_fft.inverse_transform(G.wfck)   # Not necessary, but for for postprocessing the data