# Scaling Up Work with Batch (Non-interactive) Jobs

August 2021

**RCS Presents... seminar on how to transition to batch jobs (from interactive sessions) on HPC systems**

Working with code using GUI tools such as NoMachine is usually a default choice for many users. However, as the datasets grow larger, the task grows more complex, or the number of necessary repetitions increases, this approach is no longer scalable. Running batch (or background) jobs, where one does not interact with the program that is running, allows the user to scale one's work. On the HBSGrid cluster, for example, one can run hundreds of scripts at once, analyzing numerous data files simultaneously, or performing other parallelizable or automatable jobs. 

This transition to background-only, non-GUI work may seem daunting: how does the program know what files to work on or write out? How do I monitor its progress? How do I even start the program, let alone hundreds of them? This session will demystify the process of transitioning to running batch jobs, give you several approaches to make this transition, and highlight a few useful tools. 

## Narrative
Setup: You a have a folder with a number of data files (5? 20?) and a script file. Or you have a parameter sweep that will run over 100s of combinations of values. Doing this via a GUI program is cumbersome on slow. I'd like to streamline my approach for running this code repeatedly on different files.

## Code: 
My script file process_data.py takes an input file with numbers and will output a running sum after 10 values, printing out astatus line of how many #s have been seen so far every 1000 lines summed.

## Questions for attendees
* What do you like about using the GUI for running your script file?
* What do you (or would you) find limiting??

## Objectives:
* Know how to launch batch jobs from the terminal
* Know how to set up inputs and outputs
* Monitor the progress of your job
* Scaling up to larger numbers of files

## Steps:
* [Take Baby Steps: Run Your Script Code From the Terminal](1.Baby_steps.md)
  * Switch from GUI mode to launching an interactive job in the terminal
  * Run your code in batch
  * Using `bjobs` and its options for job information

* [Set Up Your Script's Inputs and Outputs](2.Input_outputs.md)
  * Abstract code to accept any input file and test change
  * Change code to make unique output file and test change
  * Use `bhist` its options to look at job details and past job information

* [Better Visibility With Progress of Jobs, Job Information, and Job Control](3.Better_visibility.md)
  * Get email notifications on job starts/ends (-B -N)
  * Make separate output and error logs (-o -e)
  * Make unique job output files with %J

* [Scaling up Work](4.Scaling_up.md)
  * Cluster Etiquette (on Scaling)
    * Ensure resource requests are appropriate
    * Bundle work: Don't overwhelm scheduler
    * Test small, run big
  * Bash `for..do` loops for one task, one job
  * Using job arrays for simpler job submissions and management


## For further investigation
* LSF documentation
    * Job control
    * Notifications
    * Log files
    * Job arrays
    * Writing submission scripts
* FASRC write-up on "Submitting Large Numbers of Files" (somewhat outdated)

