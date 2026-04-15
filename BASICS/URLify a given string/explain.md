what are we doing here?
@ we will resize the string  capacity.

@ we are counting the spaces in the given string and then 
as we know that we have to insert '%20'
so these are 3 characters(spaces) and we are replacing the space which acquire 1 character(space)
so pre space we need to add 2 extra space to the given string 
so we are using there :
      int newLen=len+2*spaces;

at the end we are keeping 2 pointers 
    i:    one are the end of the original string
    j:   2nd at the  end of the resized string

while i >=0
if at i pointer we strike space we add %20 from backward else we shift that char to the j pointer .