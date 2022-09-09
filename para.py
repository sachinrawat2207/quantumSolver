from set_device import ncp
'''
For 1D set Ny=1,Nz=1,Lx=1,Lz=1
For 2D set Nz=1,Lz=1
'''
# Set box length
Lx = 32
Ly = 32
Lz = 1

# Set grid size 
Nx = 256
Ny = 256
Nz = 1

# choose initial condition
initcond=4

volume = Lx*Ly*Lz

tmax = 10  # Maximum time
dt = 0.001
nstep = int(tmax/dt)
Nn = 100
tstepMov = ncp.linspace(dt, tmax, Nn)

Nlin = 1000

