---
title: 'Quantum Solver: A python GPU solver to studey turbulence in quantum system.'
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
  - orcid: 0000-0000-0000-0000
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

Turbulence is the complex and turbulent behaviour of the fluid flows. The turbulence in classical system is studied by using the navier strokes equation. Turbulence in quantum system  Quantum systems like Bose-Einsteins condensates differs from the classical system by various ways like zero viscocity and
The Gross-Pitaevskii equation(GPE) is a useful model to study the quantum turbulence in Bose-Einstein condensate at absolute zero temperature.
The Bose-Einstein condensate is a quantum fluid system and shows the behavior of superfluid. In quantum fluid, the wave nature of particles starts dominating i.e., the de Broglie wavelength of the particles becomes greater than the inter-atomic distances between the particles.

# Mathematics

The GPE(Gross-Pitaevskii equation)  is given by

\begin{equation}\label{eq:GPE}

\iota\hbar\frac{\partial\Psi}{\partial t}=-\frac{\hbar^2}{2m}\nabla^2\Psi+V(\bm{r},t)\Psi+g|\Psi|^2\Psi

\end{equation}

Where, $\Psi$ is the wavefunction, $V(\bm{r},t)$ is trapping potential, $g$ is the interaction term.

and refer to \autoref{eq:GPE} from text.

# Nmerical Scheme and functionalities

``Quantum Solver`` uses  pseudo specral scheme TSSP(Time Splitting Spectral method) [@bao2003numerical] to solve the dynamic of the GPE. The main advantage of using the TSSP scheme is that it is unconditionally stable scheme. ``Quantum solver`` is primarily designed for studing the turbulence in the quantum system. For these purposes the ``Quantum solver``is equipped with a number of features :

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

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References
