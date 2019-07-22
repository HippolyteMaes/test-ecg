Usage : python [-h] main.py path date_of_start


This programm uses Python 3.6, no other dependency

--------------------------------------------------

Bonus question: We want to efficiently host delineations online, and be able to
quickly download a range of it (e.g. the record between 2 and 3pm on the third
day). How would you achieve that ?

The main bottleneck would be reading the whole file to get a specific range as
the files should take a long time to go through when the records get bigger (eg several days, weeks, months). To mitigate this, each record should be split, each subfile containing a day (or another period of time depending on the performances) worth of record. This way the server could quickly split and merge files together according to the user wishes.

The server would idealy be a cloud based solution as it is reliable and adaptable to the load.
