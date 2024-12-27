"""
%mprun

A random sample of 25,000 superheroes has been loaded into your session as an array called sample_indices. This sample is a list of indices that corresponds to each superhero's index selected from the heroes list.

A function named calc_bmi_lists has also been created and saved to a file titled bmi_lists.py. For convenience, it is displayed below:

def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis
Notice that this function performs all necessary calculations using list comprehension (hence the name calc_bmi_lists()). Dig deeper into this function and analyze the memory footprint for performing your calculations using lists:

Load the memory_profiler package into your IPython session.
Import calc_bmi_lists from bmi_lists.
Once you've completed the above steps, use %mprun to profile the calc_bmi_lists() function acting on your superheroes data. The hts array and wts array have already been loaded into your session.

How much memory do the list comprehension lines of code consume in the calc_bmi_lists() function? (i.e., what is the total sum of the Increment column for these four lines of code?)

Correct! Using a list comprehension approach allocates anywhere from 0.1 MiB to 5 MiB of memory to calculate your BMIs.

If you run %mprun multiple times within your session, you may notice that the Increment column reports 0.0 MiB for all lines of code. This is due to a limitation with the magic command. After running %mprun once, the memory allocation analyzed previously is taken into account for all consecutive runs and %mprun will start from the place the first run left off.

Now that we've profiled the calc_bmi_lists() function, let's see if you can do better with a different approach."""

