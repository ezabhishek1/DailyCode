
# Approach:

### 1. 

Since we have positive and negative values and their absolute values are going to be considered, so we need a type of data structure that can differentiate these two type of values, stack will be a good choice.

Now question comes, why stack? Let's try to understand.

### 2.

 We will start traversing the asteroids array from beginning, and let's say if value is positive, we will directly push it into the stack(i.e., we are storing the right direction moving asteroids in separate stack)

### 3.

 If we get a negative value, i.e., opposite direction asteroid, then we need to apply conditions according to the question:

We will compare this value with top of the stack, bcoz stack is containing the opposite direction asteroids and will take part in collision.

If the absolute of current negative value(i.e., it's size) is greater than the top of stack, then we will pop it out according to question, and we will keep on doing it till this condition gets true.

After this, we can have three choices,

#### 1.
 the stack becomes empty, i.e., the negative asteroid has greater size than all opposite direction asteroids, so simply push it into answer vector.

#### 2. 
or the size of negative asteroid is less than the top value, then do nothing in this case, keep the positive value in the stack for further negative values.

#### 3.
 or the negative value has same size as stack top value, in this case, both will collide, so simply pop the value.

