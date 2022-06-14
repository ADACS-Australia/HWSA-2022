---
title: "Best Practices In Scientific Computing"
teaching: 30
exercises: 30
questions:
- "What does best practice mean?"
- "What are the top N things to do?"
- "What are the top N things to avoid?"
---

# Best Practices In Scientific Computing
Borrowed and adapted from computer science and software engineering.

- Good code etiquette
  - Efficiency vs clarity
  - Readability
  - Naming things
  - Rule of three
  - KISS
  - 90-90 rule
  - Documentation
  - Testing
  - Optimization
  - Version control
  
In this lesson we will focus on repetition, version control, testing, documentation, and repetition.

To demonstrate the utility of these topics we'll be working on a common task - analyzing meteorite falls around the world.

## Version control
Don't loose track of your working versions.
Online backup is a bonus but not essential.
Collaborative work is nice but not essential.
merge/rebase/branch are nice but not essential.

## Testing
Testing is not hard, and we already do it so let's just embrace that.

Anything that you do to validate your work is testing.
- making plots
- writing to STDOUT
- checking known cases

Automation is nice, but not essential for testing.

Think about how you will validate your work as you develop your data collection and methodology.

## Documentation
Many levels:
- README.md
- `--help` or docstrings (Python)
- userguid.pdf
- myproject.readthedocs.io

Consider the audience:
- users
- developers
- you in 6 months time

## Avoiding repetition
Repeated code means repeated opportunity for mistakes and inconsistencies.