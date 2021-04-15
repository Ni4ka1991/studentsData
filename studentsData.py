#!/usr/bin/env Python3

students_first_name = []
students_last_name =  []
students_age = []



students_first_name.append( "Piter" )
students_last_name.append( "Bruck" )
students_age.append( 21 )


while True:
 studentData = ( input( "Enter the student data: first name last name age or x to exit >>> " ))
 if( studentData != "" ):
   splitData = studentData.split()

   students_first_name.append( splitData[0] )
   students_last_name.append( splitData[1] )
   students_age.append( splitData[2] )

 
   print( students_first_name )
   print( students_last_name )
   print( students_age )
   input( "hit ENTER to continue" )
 elif( studentData == "x"):
   break
 else:
   print( "You enter a empty string." )
   break
print( " * "*20 )

students_first_name[0]
students_last_name[0]
students_age[0]





