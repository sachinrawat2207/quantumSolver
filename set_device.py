Target = 'CPU'

if Target=='CPU':
    import numpy as ncp
    import pyfftw.interfaces.numpy_fft as pyfftw
    
else:
    import cupy as ncp
    import cupy.fft as pyfftw
    # import cupy.core._accelerator as _acc
    # _acc.set_routine_accelerators(['cub'])
    # _acc.set_reduction_accelerators(['cub'])

