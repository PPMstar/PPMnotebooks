1/2 Mesa functions
3. Would like to be able to use prof_compare to do this type of plot for yprofile instances
   but the data_plot function only recognises some attributes and cannot plot T9 and other
   computed attributes. Also should all outputs be in cgs?
4. Best to leave as is unless there is need for a power spectra reader in ppm
5/6. Made two new functions for plotting figures like this. The docstring of vprofs() mentioned
   a function vprof_time that would do this but didn't exist, so I made vprof_time
7. Modified V-evolution to be more general
8. Not sure if it warranted a method since it is a straight forward plot but none the less introduced
   get_mach_number and plot_mach_number
9. Made a get_p_top method and a plot_p_top method
10.Made function L_H_L_He_comparison(), doesn't quite match the plot, but I think that the F4
11.Made function yprofile.Aprof_time()
12.Some bug fixes in upper_boundary_ut to match the functions that are called in Fig.14/upper_boundary_ut_F4.ipynb
20.plot_boundary_evolution() works fine for this. Looks a little different because sparse is 1 not 10 as in original
   should add optional sparse parameter to function
21.Added function get_r_int() to ppm.py to return r_int similarly to get_upper_boundary(), also modified plot_boundary_evolution()
   to plot r_int and to display an insert.
22.Added plot_entrainment_rates() function to the yprofile class.
27.Good as is?
29.Not sure if I should bother with the stuff in the moms files
