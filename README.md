cliutils
========

Some utils for linux cli for *ubuntu.

Installation
============

1. Create a dir for clone this repository. I.E. ~/msjcliutils.
2. Run git clone https://github.com/mansonjesus/cliutils.
3. Then run sh utils/updateutils. This will link all scripts into /usr/local/bin.

Update
======

Running updateutils will pull automatically from this repository and link all new scripts

Scripts Description
===================

* **utils/updateutils**: Install and update this repository in a computer.
* **system/cleankernel**: Search old linux kernel and linux headers and show in a menu for remove. Needs dialog package.
* **system/upgrade**: Run aptitude safe-upgrade and then cleans apt cache. Needs aptitude package.
* **media/chapters**: Create a chapters.txt file with mkv file clips in folder. Needs avprobe.

