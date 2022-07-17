# Let’s discover easypeasy !

Hello, if you are reading this, you only have one step left before discovering your new favorite Python package: the long-awaited easypeasy. Easypeasy is the result of **10+ years** of thinking and observation of the Python language for scientific & analytics purposes. **As early adopters and ambassadors of the Python language in the European aerospace industry**, we watched how Python packages started to look like good old Fortran, and soon became as heavy as Java.

If you have never used the `print` command without the parentheses, you will find it difficult to understand the rest, but let's try. When we justified to our end users the choice to migrate from Java to Python, we highlighted the fact that each Java library included its own specific data format. **We don't want to waste time and effort converting from one data format to another** from one library to another.

**That was too complex: One package for Excel parsing ? One data format. One package for matrix inversion ? One data format.  One package for visualization ? One data format.** And at the end, that same 10x10 double array being converted against its will ... But it less and less true that Python still offers that simplicity. So ... you will be able now to execute complex scientific routines **without having to learn specific API you don't care about**. You know how to put your data in some array ? Great, that's all it takes !

And because **simplicity opens up science to as many people as possible**, we take particular care to qualify the numerical results you will get. It is not because a function returns a result that this result can be used to suppot a decision. **We use the exception mechanism so that a dubious numerical result shocks you as much as a syntax error.**

# Top features of easypeasy
Easypeasy is devoted to deliver you state of the art methods and latest research algorithms curated for engineering purposes. We'll maintain here a list of top features and link to demonstrative examples. And we'll start along:
- **sequencer**: an impressive research work that proposes to sort your data and find the underneath structure in it

# Top 3 spec of easypeasy
1. Any feature must expose a one line command that returns the result.
2. Any feature requiring data as an input must accept a Python list to feed that data.
3. Any usage limitation or domain restriction on a result must be escalated through Exception mechanism.

# This Python project implements circleci CI/CD !
Latest status:  [![RandomCraftr](https://circleci.com/gh/RandomCraftr/easypeasy.svg?style=svg)](https://app.circleci.com/pipelines/github/RandomCraftr/easypeasy)

# Maintenance tasks
Here is a list of maintenance tasks to execute on this package. Most of these tasks depends on some external event, such as a third party accepting some pull request.

| Task Id | Task Description | Status |
| ----------- | ----------- | ----------- |
|1| When pull request https://github.com/dalya/Sequencer/pull/5 will be completed, remove `sequencer` directory from `third _parties`, and define dependency to TheSequencer in the new version. Remove all dependencies specific to sequencer in this project dependencies.| Pending |
