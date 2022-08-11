import para
from set_device import ncp
import my_fft


class GPE:

    def __init__(self):
        self.wfc = []
        self.V = []
        self.wfck =  []
             
    def set_arrays(self):
        if para.Nz==1 and para.Ny==1:
            self.wfc = ncp.zeros((para.Nx), dtype = ncp.complex128)
            self.wfck = ncp.zeros((para.Nx), dtype = ncp.complex128)
            self.V = ncp.zeros((para.Nx), dtype = ncp.float64)

        elif para.Nz==1:
            self.wfc = ncp.zeros((para.Nx, para.Ny), dtype = ncp.complex128)
            self.wfck = ncp.zeros((para.Nx, para.Ny), dtype = ncp.complex128)
            self.V = ncp.zeros((para.Nx, para.Ny), dtype = ncp.float64)

        else:        
            self.wfc = ncp.zeros((para.Nx, para.Ny, para.Nz), dtype = ncp.complex128)
            self.wfck = ncp.zeros((para.Nx, para.Ny, para.Nz), dtype = ncp.complex128)
            self.V = ncp.zeros((para.Nx, para.Ny, para.Nz), dtype = ncp.float64)
   

    def integral(self,psi):
        return ncp.sum(psi) * my_fft.dV

    #Calculation of  integral of space derivative part is done by using the fft
    def energy(self):
        self.wfck = my_fft.forward_transform(self.wfc) #for sstep_strang
        derivative2 = para.volume * ncp.sum(my_fft.ksqr * ncp.abs(self.wfck) ** 2)
        z = ncp.conjugate(self.wfc) * ((self.V + para.Nlin * ncp.abs(self.wfc) ** 2/2) * self.wfc)
        return self.integral(z.real) + derivative2.real / 2
    

    def rrms(self):
        if para.dimension == 2:
            return (self.integral(ncp.abs(self.wfc) ** 2 * (my_fft.x_mesh ** 2 + my_fft.y_mesh ** 2)))**.5
        return (self.integral(ncp.abs(self.wfc) ** 2 * (my_fft.z_mesh ** 2 + my_fft.x_mesh ** 2 + my_fft.y_mesh ** 2)))**.5


    def zrms(self):   
        return (self.integral(ncp.abs(self.wfc) ** 2 * my_fft.z_mesh ** 2) - (self.integral(ncp.abs(self.wfc) ** 2 * my_fft.z_mesh))**2)**.5     
       
        
    def xrms(self):
        return (self.integral(ncp.abs(self.wfc)**2 * my_fft.x_mesh**2) - (self.integral(ncp.abs(self.wfc)**2 * my_fft.x_mesh))**2)**.5
        
        
    def yrms(self):
        return (self.integral(ncp.abs(self.wfc)**2 * my_fft.y_mesh**2) - (self.integral(ncp.abs(self.wfc)**2*my_fft.y_mesh))**2)**.5
        
       
    def norm(self):
        return self.integral((ncp.abs(self.wfc))**2)
    

    def chempot(self):  
        self.wfck = my_fft.forward_transform(self.wfc)
        derivative2 = para.volume*ncp.sum(my_fft.ksqr * ncp.abs(self.wfck)**2)
        z = ncp.conjugate(self.wfc) * ((self.V + para.Nlin * ncp.abs(self.wfc)**2) * self.wfc)
        return self.integral(z.real) + derivative2.real/2


#---------------------------------------Additional functions-----------------------------------------------------

    def transfer_function(self):
        self.wfck = my_fft.forward_transform(self.wfc)
        Nlin_k = my_fft.forward_transform(para.Nlin * self.wfc*ncp.abs(self.wfc)**2+self.wfc*self.V)
        return (Nlin_k*ncp.conjugate(self.wfck)).imag
    
    # Computes flux of |psik|**2/2 
    def comp_flux(self):
        flux = ncp.zeros(para.Nx//2-1)
        temp = self.transfer_function()
        for i in range(para.Nx//2-2):
            z=ncp.where(my_fft.ksqr**.5<=my_fft.kx[i+1])
            flux[i] = -ncp.sum(temp[z])
        k=my_fft.kx[1:para.Nx//2]
        return k,flux

    def velocity(self):
        '''
        compute the velocity of the wavefunction
        '''
        theta=ncp.angle(self.wfc)
        thetak=my_fft.forward_transform(theta)
        vkx=1j*my_fft.kx_mesh*thetak
        vky=1j*my_fft.ky_mesh*thetak
        vx=my_fft.inverse_transform(vkx)
        vy=my_fft.inverse_transform(vky)
        return vx,vy
        

    def comp_KE(self):
        self.comp_omegak()
        KE_incomp = 1/(2*self.norm())*my_fft.dkV*(ncp.sum(ncp.abs(self.omegayik)**2)+ncp.sum(ncp.abs(self.omegayik)**2))
        KE_comp = 1/(2*self.norm())*my_fft.dkV*(ncp.sum(ncp.abs(self.omegayck)**2)+ncp.sum(ncp.abs(self.omegayck)**2))
        return KE_comp,KE_incomp  
    
    def comp_KEspectrum(self):
        self.comp_omegak()
        KE_incompk = 1/(2*self.norm())*(ncp.abs(self.omegayik)**2+ncp.abs(self.omegayik)**2)
        KE_compk = 1/(2*self.norm())*(ncp.abs(self.omegayck)**2+ncp.abs(self.omegayck)**2)
        KE_compk = self.spectrum(KE_compk)
        return KE_compk,KE_incompk

    def comp_omegak(self):
        vx,vy=self.velocity()
        # print("vx,vy:  ",vx,vy)
        omegax = ncp.abs(self.wfc)*vx
        omegay = ncp.abs(self.wfc)*vy
        omegaxk = my_fft.forward_transform(omegax)
        omegayk = my_fft.forward_transform(omegay)
        # print(my_fft.inverse_transform(omegax))
        my_fft.ksqr[0,0]=1
        self.omegaxck = my_fft.kx_mesh*(my_fft.kx_mesh*omegaxk+my_fft.ky_mesh*omegayk)/my_fft.ksqr
        self.omegayck = my_fft.ky_mesh*(my_fft.kx_mesh*omegaxk+my_fft.ky_mesh*omegayk)/my_fft.ksqr
        my_fft.ksqr[0,0]=0
        self.omegaxik=omegaxk-self.omegaxck
        self.omegayik=omegayk-self.omegayck


    def spectrum(self,quantity):
        quantity_s=ncp.zeros(para.Nx//2-1)
        for i in range(para.Nx//2-1):
            z=ncp.where((my_fft.ksqr**.5>=my_fft.kx[i]) & (my_fft.ksqr**.5 < my_fft.kx[i+1]))        
            quantity_s[i]=ncp.sum(quantity[z])
        k=my_fft.kx[1:para.Nx//2]
        return k,quantity_s