import cgi
values = cgi.FieldStorage()
t1 = values.getfirst( "t1", "none")
output_file = open("out_1.txt", "a")
output_file.write(t1)
output_file.close()