#!/bin/bash - 
#===============================================================================
#
#          FILE: dualpane.sh
# 
#         USAGE: ./dualpane.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 15/10/14 11:26
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

tmux split-window
tmux select-pane -U
tmux split-window -h
tmux select-pane -D
tmux resize-pane -y 7
tmux clock-mode
tmux select-pane -U

