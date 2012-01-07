<!SLIDE bullets>

Essential tools for writing Python in the Oil and Gas industry
========================

- [http://durden.github.com/pyhou_oil](http://durden.github.com/pyhou_oil)

<!SLIDE smaller>

Luke Lee
========
.notes So who am I and why am I qualified to talk about this?  As most of you
know I was the lonely embedded systems C developer.  I recently got the
opportunity to write Python full time at BBR.  So, Ive only been a a developer
in the Oil/Gas industry for a few months.  This talk is meant to explain what
tools Ive learned in the past few months to start becoming a productive Python
developer in the energy business.

- Software Engineer at [Blueback Reservoir](http://www.blueback-reservoir.com/)
- Writing scientific computing/data mining applications in Python
- Previously embedded C Developer
- Django enthusiast

<!SLIDE smaller>

Overview
========
- Types of applications
- Why Python
- Tools

<!SLIDE smaller>

Tools
=====

- Pytables
- HDF5
- Numpy
- Scipy
- PyQt
- Qwt

<!SLIDE smaller>

PyTables
========
.notes Mostly C, not RDBMS replacement

- Read/write HDF5 files from Python
- Best for massive data sets
    - Lots of optimization for in-memory
    - 30 columns and 1 million entries using ~ 13 MB
- No concurrency
- Integrates with Numpy to boost performance (in memory buffers)
- Think of roughly as an ORM on top of HDF5 datastore
- https://github.com/PyTables/PyTables

<!SLIDE smaller>

Links
=====
- Code
    - [references](http://www.pinboard.in/u:durden/t:pyhou_oil/)
    - [presentation code](https://github.com/durden/pyhou_oil)
    - [showoff](https://github.com/schacon/showoff)

- Me
    - [@durden20](http://twitter.com/#!/durden20)
    - [http://github.com/durden](http://github.com/durden)
    - [http://www.lukelee.net](http://www.lukelee.net)
