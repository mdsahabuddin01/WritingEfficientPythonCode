#Code profiling is a technique used to describe how long, and how often, various parts of a program are executed. 

#converts the heights and weights of our favorite superheroes from metric units to Imperial units.
def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

What are the necessary steps you need to take in order to profile the convert_units() function acting on your superheroes data if you'd like to see line-by-line runtimes?

Use %load_ext line_profiler to load the line_profiler within your IPython session.

Use %lprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line runtimes.
