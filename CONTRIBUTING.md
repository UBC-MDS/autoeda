---
editor: 
  markdown: 
    wrap: 72
---

# Contributing

We welcome any input, feedback, bug reports, and contributions to the
**AutoEDA** package. This project aims to be a lightweight Python
package designed to automate the most common and time consuming steps of
Exploratory Data Analysis (EDA).

Your contributions can help us:

-   Improve functions performance and usability
-   Incorporate additional features
-   Refine visualizations
-   Expand documentation

All contributions, suggestions, and feedback you submit are accepted
under the [Project's license](LICENSE). You represent that if you do not
own copyright in the code that you have the authority to submit it under
the [Project's license](LICENSE). All feedback, suggestions, or
contributions are not confidential.

## Example Contributions

You can contribute in many ways, for example:

-   [Report bugs](#report-bugs)
-   [Fix Bugs](#fix-bugs)
-   [Implement Features](#implement-features)
-   [Write Documentation](#write-documentation)
-   [Submit Feedback](#submit-feedback)

### Report Bugs {#report-bugs}

Report bugs here -\>
[issues](https://github.com/UBC-MDS/autoeda/issues).

**If you are reporting a bug, please follow the template guidelines. The
more detailed your report, the easier and thus faster we can help you.**

### Fix Bugs {#fix-bugs}

Look through the GitHub issues for bugs. Anything labelled with `bug`
and `help wanted` is open to whoever wants to implement it. When you
decide to work on such an issue, please assign yourself to it and add a
comment that you'll be working on that, too. If you see another issue
without the `help wanted` label, just post a comment, the maintainers
are usually happy for any support that they can get.

### Implement Features {#implement-features}

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement
it. As for [fixing bugs](#fix-bugs), please assign yourself to the issue
and add a comment that you'll be working on that, too. If another
enhancement catches your fancy, but it doesn't have the `help wanted`
label, just post a comment, the maintainers are usually happy for any
support that they can get.

### Write Documentation {#write-documentation}

AutoEDA could always use more documentation, whether as part of the
official documentation, in docstrings, or even on the web in blog posts,
articles, and such. Just [open an
issue](https://github.com/UBC-MDS/autoeda/issues) to let us know what
you will be working on so that we can provide you with guidance.

### Submit Feedback {#submit-feedback}

The best way to send feedback is to file an issue at this link [AutoEDA
issues](https://github.com/UBC-MDS/autoeda/issues). If your feedback
fits the format of one of the issue templates, please use that. Remember
that this is a volunteer-driven project and everybody has limited time.

## Get Started!

Ready to contribute? Here's how to set up AutoEDA for local development.

1.  Fork the https://github.com/UBC-MDS/autoeda repository on GitHub.

2.  Clone your fork locally (*if you want to work locally*)

    ``` shell
    git clone git@github.com:your_name_here/autoeda.git
    ```

3.  [Install hatch](https://hatch.pypa.io/latest/install/).

4.  Create a branch for local development using the default branch
    (typically `main`) as a starting point. Use `fix` or `feat` as a
    prefix for your branch name.

    ``` shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.

5.  When you're done making changes, apply the quality assurance tools
    and check that your changes pass our test suite. This is all
    included with tox

    ``` shell
    hatch run test:run
    ```

6.  Commit your changes and push your branch to GitHub. Please use
    [semantic commit messages](https://www.conventionalcommits.org/).

    ``` shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7.  Open the link displayed in the message when pushing your new branch
    in order to submit a pull request.

### Testing Your Changes

Before submitting your changes, ensure that:

1.  **Your code runs without errors**: Test all modified modules and
    functions
2.  **Dependencies are documented**: Update `requirements.txt` if you
    add new packages (TBC)

### Creating a Pull Request

Provide a clear title and detailed description of your changes: - What
problem does it solve? - What are the key results or improvements? - Are
there any limitations or concerns?

Your PR will be reviewed, and you may receive feedback or requests for
changes.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for
all contributors. We expect all participants to:

-   Be respectful and considerate in communications
-   Welcome newcomers and help them get started
-   Accept constructive criticism gracefully

## Questions and Discussions

If you have questions or want to discuss ideas before contributing:

-   Open an issue with the `question` or `discussion` label
-   Reach out to the maintainers
-   Share your ideas and get feedback before investing significant time

## Acknowledgments

Thank you for your interest in contributing to **AutoEDA**. Every
suggestion, bug report, or enhancement no matter how small helps improve
the quality, usability, and reliability of this package.

By contributing, you are helping make exploratory data analysis more
accessible, nicer, and less time consuming for data scientists and
analysts. Together, we can build better tools that support clearer
insights and stronger data driven decisions.

We truly appreciate your time and effort in supporting this project.

------------------------------------------------------------------------

*This document was inspired by the [Altair
CONTRIBUTING.md](https://github.com/vega/altair/blob/main/CONTRIBUTING.md)
and adapted for the Sepsis Survival Prediction Project.*
