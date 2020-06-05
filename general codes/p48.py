monthdays = {'Jan' : 31, 'Feb' : 28, 'Mar' : 31,
             'Apr' : 30, 'May' : 31, 'Jun' : 30,
             'Jul' : 31, 'Aug' : 31, 'Sep' : 30,
             'Oct' : 31, 'Nov' : 30, 'Dec' : 31}
months = monthdays.items()
months.sort(lambda f, s: cmp(f[1], s[1]))
for month, days in months:
    print ('There are',days,'days in',month)
     

