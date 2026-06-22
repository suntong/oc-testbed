
# OpenCode AI Factory bash init
bind 'set enable-bracketed-paste off'
export HISTCONTROL=ignoreboth
bind '"\ep":history-search-backward'
bind '"\en":history-search-forward'
alias xselc="xclip -selection clipboard -i"
alias xselp="xclip -selection clipboard -o"
umask 002
umask
alias dir='ls -lF '
alias hf='history | grep -E'
alias ht='history | tail -50'
alias dv="dirs -v"
alias cdd='pushd '
alias ..='cd ..'
alias psh='PS1="\n\w\\\$ "'
psh
