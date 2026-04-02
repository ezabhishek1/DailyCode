It is basic permutation and combinations question.
 For example ways to fill n=4 place with k=3(BRGY) colours, for first place we have k options.B _ _ _ => now it can be any of k options. B B --  if B used then we have 3 options to fill next place. if B Y _ _ => if B not used we have k=4 options to fill the next place


## Approach
For every post, I maintain:

same = number of ways where the last two posts have the same color

diff = number of ways where the last two posts have different colors

For first post:

Ways = k

For second post:

same = k

diff = k * (k - 1)

From third post onwards:

To make current post same as previous post:

Previous two posts must be different

So:
same = diff

To make current post different:

Previous post can be anything

Choose one of (k - 1) different colors

So:
diff = (same + diff) * (k - 1)

Final answer:

same + diff