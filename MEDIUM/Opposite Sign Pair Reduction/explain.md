Approach:

1. Since we have positive and negative values and their absolute values are going to be considered, so we need a type of data structure that can differentiate these two type of values, stack will be a good choice.

Now question comes, why stack? Let's try to understand

2. We will start traversing the asteroids array from beginning, and let's say if value is positive, we will directly push it into the stack(i.e., we are storing the right direction moving asteroids in separate stack)