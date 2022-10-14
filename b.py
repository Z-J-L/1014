import os 

disk_path = 'dd/'
disk_file = os.listdir( disk_path )
txt_path = 'now.txt'
f = open( txt_path, 'w' )

for i in disk_file:
    stringx = 0
    f.write('Hello World')
    
    
    
    
f.close()