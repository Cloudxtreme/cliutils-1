cliutils
========

Some utils for linux cli for ubuntu.

Installation
============

1. Run `git clone https://github.com/mansonjesus/cliutils.git`
2. Then run `sh utils/updateutils`. This will link all scripts into /usr/local/bin.

Update
======

Running updateutils will pull automatically from this repository and link all new scripts.

Scripts Description
===================

* **kde/pwrdisable**: Disable KDE screensaver / power management for the number of minutes entered.
* **media/chapters**: Create a chapters.txt file with mkv file clips in folder. Needs avprobe.
* **utils/gitconf**: Prompt for global git config.
* **utils/updateutils**: Install and update this repository in a computer.
* **utils/updaterepos**: Update repo list given by ~/.local/repos.txt
* **system/cleankernel**: Search old linux kernel and linux headers and show in a menu for remove. Needs dialog package.
* **system/upgrade**: Run aptitude safe-upgrade and then cleans apt cache. Needs aptitude package.


