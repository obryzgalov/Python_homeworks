# Correct time display from entered second

# 1) Mumbai-style code :-)
scndsenter = int(input('Enter time in seconds: '))

scnd = scndsenter % (24*3600) # there can't be more than 84600 sec in a day
hours = scnd // 3600
minutes = (scnd - (hours*3600))//60 #(sectotal - hours_in_sec) // sec_in_min
scndrmn = scnd - hours*3600 - minutes*60 #sectotal - hours_in_sec - min_in_sec
print (' \nMumbai way:')
print ("The correct time display is: {:02}:{:02}:{:02} (hh:mm:ss)". format(hours, minutes, scndrmn))




