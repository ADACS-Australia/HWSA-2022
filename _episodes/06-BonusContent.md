---
title: "Bonus Content"
teaching: 0
exercises: 0
questions:
- "What else is there?"
---

## Automation
### Aliases
A basic form of automation is the use of aliases.
The goal here is to save you a bunch of keyboard or mouse clicks.
Some common examples:
~~~
# long list all files
alias ll='ls -al'

# open ds9 and press about 20 buttons to get the interface set up just the way I like
alias ds9='~/Software/ds9/ds9 -scalelims -0.2 1 -tile -cmap cubehelix0 -lock frame wcs -lock scale yes -lock colorbar yes -lock crosshair wcs

# run stilts and topcat and not have to bother with the java invocation
alias stilts='java -jar ~/Software/topcat/topcat-full.jar -stilts'
alias topcat='java -jar ~/Software/topcat/topcat-full.jar'

# activate my favorite python3 environment
alias py3='source ~/.py3/bin/activate'
~~~
{: .language-bash}