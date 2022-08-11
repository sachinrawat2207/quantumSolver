import para
from set_device import ncp, pyfftw


def forward_transform(psi):
    return pyfftw.fftn(psi)/(para.Nx*para.Ny*para.Nz)

def inverse_transform(psik):
    return pyfftw.ifftn(psik)*(para.Nx*para.Ny*para.Nz)


# meshgrids
Dx = ncp.arange(-para.Nx//2, para.Nx//2)
kx = 2*ncp.pi*ncp.roll(Dx, para.Nx//2)/para.Lx
x = Dx*para.Lx/para.Nx
dkx = (kx[1]-kx[0])

Dy = ncp.arange(-para.Ny//2, para.Ny//2)
ky = 2*ncp.pi*ncp.roll(Dy, para.Ny//2)/para.Ly
y = Dy*para.Ly/para.Ny

Dz = ncp.arange(-para.Nz//2, para.Nz//2)
kz = 2*ncp.pi*ncp.roll(Dz, para.Nz//2)/para.Lz
z = Dz*para.Lz/para.Nz

if para.Ny == 1 and para.Nz == 1:
    x_mesh = x
    dV = x[1]-x[0]
    dkV = dkx
    ksqr = kx**2

elif para.Nz == 1:
    dky = (ky[1]-ky[0])
    x_mesh, y_mesh = ncp.meshgrid(x, y, indexing='ij')
    kx_mesh, ky_mesh = ncp.meshgrid(kx, ky, indexing='ij')
    ksqr = kx_mesh**2 + ky_mesh**2
    dV = (x[1]-x[0])*(y[1]-y[0])
    dkV = dkx*dky

else:
    dky = (ky[1]-ky[0])
    dkz = (kz[1]-kz[0])
    x_mesh, y_mesh, z_mesh = ncp.meshgrid(x, y, z, indexing='ij')
    kx_mesh, ky_mesh, kz_mesh = ncp.meshgrid(kx, ky, kz, indexing='ij')
    ksqr = kx_mesh**2 + ky_mesh**2 + kz_mesh**2
    dV = (x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0])
    dkV = dkx*dky*dkz


'''
def dealias(psik):
    z = ncp.where(ksqr**0.5>kx[para.Nx//3])
    psik[z] = 0
    return psik
'''
