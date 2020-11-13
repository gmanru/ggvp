from django.core.management.base import BaseCommand
from django.conf import settings

from core.models import Playlist

q=[]
filename = '29_02_2020.txt'
datefromfile = filename[:-4]

with open(filename,encoding="cp1251") as f:
    i=0
    for row in f :
        i+=1
        if i >3:
            
            num_hour_txt=row[0:2]
            track_txt=row[6:37]
            artist_txt=row[38:69]
            lenght_txt=row[70:75]
            if lenght_txt != "=====":
                start_txt=row[79:87]
                if start_txt !="        ":
                    end_txt=row[88:96]
                    '''a = []
                    a.append(num_hour)
                    a.append(track)
                    a.append(artist)
                    a.append(lenght)
                    a.append(start)
                    a.append(end)'''
        
                    m = Playlist(date = datefromfile,
                                    num_hour =num_hour_txt,
                                 track =   track_txt,
                                 artist  = artist_txt,
                                 lenght = lenght_txt,
                                 start = start_txt,
                                 end =end_txt  
                                    
                                    )

                    m.save()