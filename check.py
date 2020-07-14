#!/usr/bin/env python3

import sys
from doi2bib import set_proxy, convert


if len(sys.argv) > 1:
    set_proxy(sys.argv[1])

doi = '10.1109/aero.2014.6836462'
bib = '''@inproceedings{scharf2014adapt,
  doi = {10.1109/aero.2014.6836462},
  year = {2014},
  month = {mar},
  publisher = {{IEEE}},
  author = {Daniel P. Scharf and Martin W. Regehr and Geoffery M. Vaughan and Joel Benito and Homayoon Ansari and MiMi Aung and Andrew Johnson and Jordi Casoliva and Swati Mohan and Daniel Dueri and Behcet Acikmese and David Masten and Scott Nietfeld},
  title = {{ADAPT} demonstrations of onboard large-divert Guidance with a {VTVL} rocket},
  booktitle = {2014 {IEEE} Aerospace Conference}
}'''
assert(convert(doi) == bib)

doi = '10.1137/s0036144504446096'
bib = '''@article{gill2005snopt,
  doi = {10.1137/s0036144504446096},
  year = {2005},
  month = {jan},
  publisher = {Society for Industrial {\&} Applied Mathematics ({SIAM})},
  volume = {47},
  number = {1},
  pages = {99--131},
  author = {Philip E. Gill and Walter Murray and Michael A. Saunders},
  title = {{SNOPT}: An {SQP} Algorithm for Large-Scale Constrained Optimization},
  journal = {{SIAM} Review}
}'''
assert(convert(doi) == bib)

doi = '10.1007/978-0-387-40065-5'
bib = '''@book{na2006numerical,
  doi = {10.1007/978-0-387-40065-5},
  year = {2006},
  publisher = {Springer New York},
  title = {Numerical Optimization}
}'''
assert(convert(doi) == bib)

doi = '10.1016/j.automatica.2010.10.037'
bib = '''@article{accikmecse2011lossless,
  doi = {10.1016/j.automatica.2010.10.037},
  year = {2011},
  month = {feb},
  publisher = {Elsevier {BV}},
  volume = {47},
  number = {2},
  pages = {341--347},
  author = {Beh{\c{c}}et A{\c{c}}{\i}kme{\c{s}}e and Lars Blackmore},
  title = {Lossless convexification of a class of optimal control problems with non-convex control constraints},
  journal = {Automatica}
}'''
assert(convert(doi) == bib)

doi = '10.1287/moor.26.2.193.10561'
bib = '''@article{bental2001on,
  doi = {10.1287/moor.26.2.193.10561},
  year = {2001},
  month = {may},
  publisher = {Institute for Operations Research and the Management Sciences ({INFORMS})},
  volume = {26},
  number = {2},
  pages = {193--205},
  author = {Aharon Ben-Tal and Arkadi Nemirovski},
  title = {On Polyhedral Approximations of the Second-Order Cone},
  journal = {Mathematics of Operations Research}
}'''
assert(convert(doi) == bib)

doi = '10.2514/1.g002745'
bib = '''@article{lu2017introducing,
  doi = {10.2514/1.g002745},
  year = {2017},
  month = {feb},
  publisher = {American Institute of Aeronautics and Astronautics ({AIAA})},
  volume = {40},
  number = {2},
  pages = {193--193},
  editor = {Ping Lu},
  title = {Introducing Computational Guidance and Control},
  journal = {Journal of Guidance, Control, and Dynamics}
}'''
assert(convert(doi) == bib)
