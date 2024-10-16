input_data = open ('output.txt','r')
data = input_data.read( )
data = data.split()
b = int(data[0])
q = int(data[1])
n = int(data[2])
gempr = 0 
for i in range (1,n+1):
    gtmpr= b*(q**i-1)

output_data = open('output.txt','w')
output_data.write()

input_data.close('output.txt','r')
output_data.close('output.txt','w')