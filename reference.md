---
layout: reference
---

## Glossary

{:auto_ids}
ADACS
:   Astronomy Data And Computing Services.
    For more info see [adacs.org.au](https://adacs.org.au/)

ASA
:   The Astronomical Society of Australia

HWSA
:   The Harley Wood School for Astronomy



## Git Cheatsheets for Quick Reference

*   A printable Git cheatsheet is [available here](https://about.gitlab.com/images/press/git-cheat-sheet.pdf). More material is available from the [GitLab basics guides website](https://docs.gitlab.com/ee/gitlab-basics/).
*   An [interactive one-page visualisation](http://ndpsoftware.com/git-cheatsheet.html)
    about the relationships between workspace, staging area, local repository, upstream repository, and the commands associated with each (with explanations).
* [Learning git branching](https://learngitbranching.js.org/ ) is an interactive tutorial, covering remotes, branching, merging, rebase and more

### Git Glossary

{:auto_ids}
changeset
:   A group of changes to one or more files that are or will be added
    to a single [commit](#commit) in a [version control](#version-control)
    [repository](#repository).

commit
:   To record the current state of a set of files (a [changeset](#changeset))
    in a [version control](#version-control) [repository](#repository). As a noun,
    the result of committing, i.e. a recorded changeset in a repository.
    If a commit contains changes to multiple files,
    all of the changes are recorded together.

conflict
:   A change made by one user of a [version control system](#version-control)
    that is incompatible with changes made by other users.
    Helping users [resolve](#resolve) conflicts
    is one of version control's major tasks.

merge
:   (a repository): To reconcile two sets of changes to a
    [repository](#repository).

repository
:   A storage area where a [version control](#version-control) system
    stores the full history of [commits](#commit) of a project and information
    about who changed what, when.

revision
:   A synonym for [commit](#commit).

version control
:   A tool for managing changes to a set of files.
    Each set of changes creates a new [commit](#commit) of the files;
    the version control system allows users to recover old commits reliably,
    and helps manage conflicting changes made by different users.

{% include links.md %}
