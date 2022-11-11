---
mtitle: 'Quantum Solver: A python GPU solver to study turbulence in quantum system.'
tags:
  - Python
  - Quantum turbulence
  - Bose-Einstein condensate
  - Quantum Fluids
  


authors:
  - name: Sachin Singh Rawat
    orcid: 0000-0002-5701-7247
    equal-contrib: true
    affiliation: 1
  - name: Shawan Kumar Jha
  - orcid: 0000-0003-4582-8787
    equal-contrib: true 
    affiliation: 2
  - name: Mahendra Kumar Verma
  - orcid: 0000-0002-3380-4561
    affiliation: 1
  - name: Pankaj Kumar Mishra
  - orcid: 0000-0003-4907-4724
    affiliation: 2

affiliations:
 - name: Department of Physics, Indian Institute of Technology - Kanpur, Uttar Pradesh - 208016, India
   index: 1
 - name: Department of Physics, Indian Institute of Technology - Guwahati, Asam - 781039, India
   index: 2

date: 19 August 2022

bibliography: resources/paper.bib
---
# Summary

Turbulence in classical fluids till date defies a proper quantitave model for many of it's aspects. Quantum fluids exhibit various interesting properties such as quantized cirulation of vorticity (unlike classical fluids where ortivity takes continuous values) and zero viscosity. This makes the study of turublence in these systems rather unique and stiduying it may help us shed some light on aspects of this long standing problem of turbulence. Bose-Einstein condensate is a type of quantum fluid system formed when a dilute gas of bosons is cooled down to a temperature close to absolute zero. One can study turbulence phenomenon in atomic Bose-Einstein condensates(BECs) by using the Gross-Pitaevskii equation, a type of non-linear Schr&ouml;dinger equation. It is given by

\begin{equation}\label{eqn:GPE}
\iota\hbar\partial_t\Psi(\vec{r},t) = -\frac{\hbar^2}{2m}\nabla^2\Psi(\vec{r},t) + V(\vec{r},t)\Psi(\vec{r},t) + g|\Psi(\vec{r},t)|^2\Psi(\vec{r},t)
\end{equation}

where, $\Psi(\vec{r},t)$ is the macroscopic complex wave function,  $m$ is the atomic mass, $V(\vec{r},t)$ is the trapping potential, $g=\frac{4\pi\hslash^2a_s}{m}$ is the nonlinear interaction parameter and $a_s$ denotes the scattering length for the interaction of the atomic particles.

# Statement of Need
Quantum Solver is robust and easy to use and having capablities of running for both GPU and CPU. Quantum solver is specifically designed to study the quantum turbulence in Bose-Einstein condendates. There are no pakages available to solve GPE in 1D, 2D and 3D in python which can run on a GPU. However, there exist packages that can solve the GP Equation including GPELab[@Antoine2014] (GPU acceleration unavailable) for MATLAB and cuda-enabled, GPUE[@schloss2018gpue] (complicated to work with) for C++.

# Numerical Scheme and functionalities

``Quantum Solver`` uses a pseudo-spectral scheme, TSSP (Time Splitting Spectral method) [@bao2003numerical] to solve the dynamics of the GPE. The main advantage of using the TSSP scheme is that it is unconditionally stable scheme.The dimensionless form of GPE is given by

\begin{equation}\label{eqn:ndGPE}
\iota\psi(\vec{r},t)= -\frac{1}{2}\nabla^2\psi(\vec{r},t) + V(\vec{r},t)\psi(\vec{r},t) + g|\psi(\vec{r},t)|^2\psi(\vec{r},t)
\end{equation}

For time interval $\Delta t$ between $t=t_n$ and $t=t_{n+1}$, one can solve eq(\ref{eqn:ndGPE}) numerically by splitting it into two steps. The first step is

\begin{equation}\label{eq:sstep1}
\iota \partial_t\psi = -\frac{1}{2}\nabla^2\psi
\end{equation}

The second step is


\begin{equation}\label{eq:sstep2}
\iota \partial_t\psi = V\psi + g|\psi|^2\psi
\end{equation}

By taking a fourier trasnform of eq(\ref{eq:sstep1}), one can convert the PDE into an ODE which can be solved exactly in Fourier space and the wavefunction in real space can be retrieved by taking an inverse fourier transform.
For $t \ \epsilon \ [t_n,t_{n+1}]$, $|\psi|^2$  remains almost constant therefore, eq(\ref{eq:sstep2}), now just an ODE, can be solved exactly in $t_n$ and $t_{n+1}$.

Between $t_n$ and $t_{n+1}$, the two steps are connected through strang splitting:

\begin{eqnarray}
\psi_n^{(1)} = \psi_n e^{-\iota(V + g|\psi_n|^2)\frac{\Delta t}{2}} \\
\hat{\psi}_n^{(2)} = \hat{\psi}_n^{(1)}e^{-\iota\frac{\vec{k}^2}{2}\Delta t} \\
\psi_{n+1} = \psi_n^{(2)} e^{-\iota(V + g|\psi_n^{(2)}|^2)\frac{\Delta t}{2}}
\end{eqnarray}

where, $\hat{\psi}^{(1)}$ is Fourier transform of $\psi^{(1)}$ and $\psi_n^{(2)}$ is inverse Fourier transform of $\hat{\psi}_n^{(2)}$.

One can calculate the ground state for a given system  by using imaginary time proppogation method wherein all the eigenstates except the groundstate of the system decay with time. In imaginary time propagation method, $t$ is replaced by -$\iota t$ and then evolved.

``Quantum solver`` is primarily designed for studying turbulence in quantum systems. For these purposes, ``Quantum solver``is equipped with a number of features :

1. Dynamics evolution using either GPU or CPU by changing a switch.
2. Ground state calculation using imaginary time propagation method.

3. Computation of different types of quantities relevant to sutdy turbulence phenomenon in BECs including, but not limited to, various spectrum (Kinetic energy spectrum (compressible and incompressible), Particle number spectrum etc.) and fluxes.

# Results
We have validated our code by following ways:
1. To validate the ground state being obtained, we compared results obtained with ``Quantum Solver` to those obtained in [Ref_MURUGANANDAM] and [REF_BAO_GROUND_STATE] using finite difference methods[TO BE VERIFIED]. The results are in good agreement (Table below).

2. To validate the dynamic evolution of a state, we compared our results with bao et al.[@bao2003numerical]. For the following condition:
 $V=\frac{1}{2}(x^2+\gamma_y^2y^2+\gamma_z^2z^2)$ and $\psi(\vec{r},0)=\frac{(\gamma_y\gamma_z)^{1/4}}{\sqrt{(\pi\epsilon_1)^{3/4}}}e^{-\frac{(x^2+\gamma_yy^2+\gamma_zz^2)}{2\epsilon_1}}$ 
where, $\gamma_y=2.0, \ \gamma_z=4.0, \ \epsilon_1=\frac{1}{4}  \ \kappa_3=0.1$. 
Fig(\ref{fig:1}) shows the comparisons of rms values of $x,y,z$ at different times of quantum solver with bao et al.[@bao2003numerical]. The results obtained from the ``Quantum solver`` are in good agreement with the results obtained from the bao et al. for the same set of initial condition.

![The lines in the figure shows the rms values obtained from the quantum solver and dots shows the results obtained from the  bao et al[@bao2003numerical].\label{fig:1}](resources/figcond1.jpg)


# Acknowledgements

# References


