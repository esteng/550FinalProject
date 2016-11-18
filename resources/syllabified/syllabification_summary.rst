***************************
Syllabification information
***************************

After researching the topic and looking at some algorithms used by other teams, here is some information on syllabification:

There are generally two approaches for syllabification:

* Hardcoding an algorithm: This means writing a language specific algorithm with syllabification rules and exceptions written into the program. The overall rule sets are usually Max-Onset or the Sonority Sequencing Principle (the latter is more reliable intralingually but the hierarchy can vary between languages). For example, the Sylli syllabifier works well for Italian -- for which it was written -- but not very well on English, which has different rules/orthography. In Phon, the sonority hierarchy is written out for each language available, and the syllabifier works off of these files.
* Machine  learning approach: In this approach, the algorithm is trained on a test set and designed to 'learn' the syllabification rules of the language. They make use of Hidden Markov Models and other algorithms in order to syllabify in any language, and generally achieve good results.

Obviously, there are pros and cons to both methods. The first means that for each language you have to write something, while the second is more complicated and requires a greater degree of computer science knowledge. 

A somewhat eclectic option would be to use Adaptor Grammars. These are probabilistic context-free grammars which can be changed through a machine-learning process. Each segment is given a likelihood of being syllabic, factoring in SSP and Max Onset, as well as information about the language (ie can liquids/nasals be syllabic, etc). The machine-learning process adjusts this likelihood based on a training set. These are then the files that are used for syllabification. This combines the accuracy of hardcoding for a language we have information about, while still allowing new languages to be processed. It also allows us to include certain intuitions for languages where we have some information but not all. 