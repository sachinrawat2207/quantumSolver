import my_fft
import para
from set_device import ncp


def initcond(G):

    # Random initial conditions
    if para.initcond == 1:  
        ncp.random.seed(1)
        randval = ncp.random.uniform(0, 2*ncp.pi, (para.Nx, para.Ny))
        z = ncp.where(my_fft.ksqr**0.5 > my_fft.kx[para.Nx//2-1])
        psik = ncp.exp(1j*randval)
        psik[z] = 0
        G.wfc = my_fft.inverse_transform(psik)
        G.wfc = G.wfc/G.norm()**0.5
        G.V=0
    
    elif para.initcond == 2:
        a = 0.5
        b = 0.5
        c = 0.5
        d = 0.5
        phik = ncp.zeros((para.Nx, para.Ny), dtype=complex)
        for i in range(20):
            k = ncp.random.randint(50)
            phik[k, 0] = a
            phik[-k, 0] = b
            phik[0, k] = c
            phik[0, -k] = d
        G.wfc = my_fft.inverse_transform(phik)
        G.wfc = G.wfc/G.norm()**0.5
        G.V = 0

    elif para.initcond == 3:
        ncp.random.seed(1)
        randval = ncp.random.uniform(0, 2*ncp.pi, (para.Nx, para.Ny))
        z = ncp.where(my_fft.ksqr**0.5 > my_fft.kx[para.Nx//2-1])
        psik = ncp.exp(1j*randval)
        psik[z] = 0
        phi = my_fft.inverse_transform(psik)
        phi = ncp.abs(phi)**2
        phi = 2*ncp.pi*phi/ncp.max(phi)-ncp.pi
        G.wfc = ncp.exp(1j*phi)
        G.V = 0
        # G.wfc=G.wfc/G.norm()**0.5
    
    # Initial conditions from a file
    elif para.initcond == 4:
        pass
    
    


"""
def initcond(G):
    '''
    Initial wavefunction
    '''
    # G.wfc = (1/ncp.pi**(1/4))*ncp.exp(-(my_fft.x_mesh**2/2))+0j  #1D initial condition
    G.wfc = (1/(ncp.pi)**(1/2))*ncp.exp(-(my_fft.y_mesh**2+my_fft.x_mesh**2/2))+0j    #2D initial condition
    # G.wfc = (1/(ncp.pi)**(3/4))*ncp.exp(-(my_fft.z_mesh**2+my_fft.y_mesh**2 + my_fft.x_mesh**2)/2)+0j  # 3D initial condition   

    '''
    potential
    '''
    G.V=(para.gammax**2*my_fft.x_mesh**2+para.gammay**2*my_fft.y_mesh**2)/2
    # G.V = (para.gammax**2*my_fft.x_mesh**2+para.gammay**2 * my_fft.y_mesh**2+para.gammaz**2*my_fft.z_mesh**2)/2 #3D
    # del my_fft.x_mesh,my_fft.y_mesh,my_fft.z_mesh
"""
