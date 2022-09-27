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

Quantum fluid systems exhibit various interesting properties such as zero viscosity and quantized vortex cirulation that aren't found in classical fluid systems. Bose-Einstein condensate is a type of quantum fluid system formed when a dilute gas of bosons is cooled down to a temperature close to absolute zero. One can study turbulence phenomenon in atomic Bose-Einstein condensates(BECs) by using the Gross-Pitaevskii equation, a type of non-linear Schr&ouml;dinger equation. It is given by

\begin{equation}\label{eqn:GPE}
\iota\hbar\partial_t\Psi(\vec{r},t) = -\frac{\hbar^2}{2m}\nabla^2\Psi(\vec{r},t) + V(\vec{r},t)\Psi(\vec{r},t) + g|\Psi(\vec{r},t)|^2\Psi(\vec{r},t)
\end{equation}

where, $\Psi(\vec{r},t)$ is the macroscopic complex wave function,  $m$ is the atomic mass, $V(\vec{r},t)$ is the trapping potential, $g=\frac{4\pi\hslash^2a_s}{m}$ is the nonlinear interaction parameter and $a_s$ denotes the scattering length for the interaction of the atomic particles.

# Statement of Need

# Numerical Scheme and functionalities

``Quantum Solver`` uses a pseudo specral scheme, TSSP (Time Splitting Spectral method) [@bao2003numerical] to solve the dynamics of the GPE. The main advantage of using the TSSP scheme is that it is unconditionally stable scheme.The dimensionless for of GPE is given by

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
\hat{\psi}_n^{(2)} = \hat{\psi}_n^{(1)}e^{-\iota\frac{\textbf{k}^2}{2}\Delta t} \\
\psi_{n+1} = \psi_n^{(2)} e^{-\iota(V + g|\psi_n^{(2)}|^2)\frac{\Delta t}{2}}
\end{eqnarray}

where, $\hat{\psi}^{(1)}$ is Fourier transform of $\psi^{(1)}$ and $\psi_n^{(2)}$ is inverse Fourier transform of $\hat{\psi}_n^{(2)}$.

Ground State Calculations:

Ground state for a given system are calculated by using imaginary time method wherein all the eigenstates except the groundstate of the system decay with time. To accomplish this one replaces t with -it and renormalises the wavefunction after every iteration.

``Quantum solver`` is primarily designed for studying turbulence in quantum systems. For these purposes, ``Quantum solver``is equipped with a number of features :

1. Dynamics evolution using either GPU or CPU by changing a switch.
2. Computation of different types of spectrumm (Energy spectrum, Particle number spectrum etc.) and flux.
3. Vortex tracking (2D).

# Results

# Citations

- `[@author:2001]` -> "(Author et al., 2001)"

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:

- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

# Acknowledgements

# References
