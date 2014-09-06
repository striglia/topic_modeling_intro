Section 3: Automatic Topic Identification!
------------------------


Our goal for this section is to:

1. You can use your own code from the last section or (if you prefer or did not finish) this section's pre-built code.
2. Classify some businesses with the `naive_mexican_classifier` in `classify.py`. Where does it work well? Are there businesses it does not work on?
3. Write your own improved version of the classifier!
4. How can we compare these two classifiers? How do we know which one does a better job?


Bonus
--------------
Try using the
[Gensim](http://radimrehurek.com/gensim/wiki.html#latent-dirichlet-allocation)
library to learn these topics automatically!

Gensim will require the `scipy` and `numpy` libraries, so it may be somewhat
tricky to install on your machine. You might find
[conda](http://www.continuum.io/blog/conda) useful as a tool to install these
libraries.

Expert
--------------
Try using Gensim's [similarity
queries](http://radimrehurek.com/gensim/similarities/docsim.html) to identify
which other businesses are most like a target business.
