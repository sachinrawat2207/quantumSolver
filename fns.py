import para
import my_fft
from set_device import ncp


def my_integralR(psi):
    """Compute integral in real space
    """
    return my_fft.dv*ncp.sum(psi)

def my_integralK(psi):
    """Compute integral in k-space
    """
    return my_fft.dkV*ncp.sum(psi)

