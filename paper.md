---
title: 'Gala: A Python package for galactic dynamics'
tags:
  - Python
  - Quantum turbulence
  - Bose-Einstein condensate


authors:
  - name: Sachin Singh Rawat
    orcid: 0000-0000-0000-0000
    equal-contrib: true
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: Shawan Kumar Jha
  - orcid: 0000-0000-0000-0000
    equal-contrib: true # (This is how you can denote equal contributions between multiple authors)
    affiliation: 2
  - name: Mahendra Kumar Verma
    affiliation: 3
  - name: Pankaj Kumar Mishra
    affiliation: 4

affiliations:
 - name: Department of Physics, Indian Institute of Technology - Kanpur, Uttar Pradesh - 208016, India
   index: 1
 - name: Department of Physics, Indian Institute of Technology - Guwahati, Asam - 781039, India
   index: 2
 - name: Department of Physics, Indian Institute of Technology - Kanpur, Uttar Pradesh - 208016, India
   index: 3
 - name: Department of Physics, Indian Institute of Technology - Guwahati, Asam - 781039, India
   index: 4
date: 09 August 2022
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary
The Gross-Pitaevskii equation(GPE) is a useful model to study the quantum turbulence in Bose-Einstein condensate at absolute zero temperature.
The Bose-Einstein condensate is a quantum fluid system and shows the behavior of superfluid. In quantum fluid, the wave nature of particles starts dominating i.e., the de Broglie wavelength of the particles becomes greater than the inter-atomic distances between the particles. 



# Statement of need

`Quantum solver` is an Astropy-affiliated Python package for galactic dynamics. Python
enables wrapping low-level languages (e.g., C) for speed without losing
flexibility or ease-of-use in the user-interface. The API for `Gala` was
designed to provide a class-based and user-friendly interface to fast (C or
Cython-optimized) implementations of common operations such as gravitational
potential and force evaluation, orbit integration, dynamical transformations,
and chaos indicators for nonlinear dynamics. `Gala` also relies heavily on and
interfaces well with the implementations of physical units and astronomical
coordinate systems in the `Astropy` package [@astropy] (`astropy.units` and
`astropy.coordinates`).

`Gala` was designed to be used by both astronomical researchers and by
students in courses on gravitational dynamics or astronomy. It has already been
used in a number of scientific publications [@Pearson:2017] and has also been
used in graduate courses on Galactic dynamics to, e.g., provide interactive
visualizations of textbook material [@Binney:2008]. The combination of speed,
design, and support for Astropy functionality in `Gala` will enable exciting
scientific explorations of forthcoming data releases from the *Gaia* mission
[@gaia] by students and experts alike.

# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

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
