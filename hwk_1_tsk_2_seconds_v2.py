# 2) Normal code (w/function) / let's test the 1st mode
scndsenter = int(input('Enter time in seconds: '))
def corr_dsply (sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   min = sec // 60
   sec %= 60

   return "%02d:%02d:%02d" % (hour, min, sec)

print (' \nThe second way:')
print("The correct time display is:",corr_dsply(scndsenter), "(hh:mm:ss)")
