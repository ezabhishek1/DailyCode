    💚 Stable Marriage (Using Queue)
🧠 Intuition (Think Like This)
👉 Imagine:

Men are proposing 💌

Women are choosing 🤔

💡 Rule:

A woman never settles for worse

A man keeps trying until accepted


Approach
Let n be the number of men and women.

Create a ranking array for women.

rank[w][m] tells how much woman w likes man m.

Smaller rank means higher preference.

Keep a queue of free men.

Every free man proposes to the next woman in his preference list.

If the woman is free:

Match them.

Else if the woman likes this new man more than her current partner:

Break her old match.

Match her with the new man.

Put the old man back into the free queue.

Continue until all men are matched.

Finally, build the answer where result[i] is the woman matched with man i.

----------------------------------------------------------------------