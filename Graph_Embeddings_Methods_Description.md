# Graph Embeddings Description

This document describes the basic graph embedding methods.


## Word2vec
[Word2vec](https://towardsdatascience.com/graph-embeddings-the-summary-cc6075aba007) is an embedding method that transforms words into embedding vectors. Similar words should have similar embeddings. Word2vec uses the skip-gram network which is the neural network with one hidden layer. The skip-gram is trained to predict the neighbor word in the sentence. This task is named a fake task since it is just used in a training phase. The network accepts the word at the input and is optimized such that it predicts the neighbor words in a sentence with high probability. The figure below shows the example of input words (marked with green) and words that are predicted. With this task authors achieve that two similar words have similar embeddings since it is likely that two words with similar meaning have similar neighborhood words.

![](http://mccormickml.com/assets/word2vec/training_data.png)

The network is going to learn statistics from the number of times each pairing shows up. So, for example, the network is probably going to get many more training samples (“Soviet”, “Union”) than it is of (“Soviet”, “Sasquatch”). When the training is finished, if you give it the word “Soviet” as input, then it will output a much higher probability for “Union” or “Russia” than it will for “Sasquatch”.

![](http://mccormickml.com/assets/word2vec/skip_gram_net_arch.png)

There is no activation function on the hidden layer neurons, but the output neurons use **softmax**.

## Node2vec

The node2vec framework learns low-dimensional representations for nodes in a graph by optimizing a neighborhood preserving objective. The objective is flexible, and the algorithm accommodates for various definitions of network neighborhoods by simulating biased random walks. Specifically, it provides a way of balancing the exploration-exploitation tradeoff that in turn leads to representations obeying a spectrum of equivalences from homophily to structural equivalence.

![](https://snap.stanford.edu/node2vec/walk.png)

After transitioning to node `v` from `t`, the return hyperparameter, `p` and the hyperparameter, `q` control the probability of a walk staying inward revisiting nodes (t), staying close to the preceding nodes (x1), or moving outward farther away (x2, x3).

![](https://snap.stanford.edu/node2vec/homo.png)

## DeepWalk

[Deepwalk](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf) is a concept in graph theory that enables the traversal of a graph by moving from one node to another, as long as they are connected to a common edge.
If you represent each node in a graph with an arbitrary representation vector, you can traverse the graph. The steps of that traversal could be aggregated by arranging the node representation vectors next to each other in a matrix.

The latent representations is what become the input for a neural network. The neural network, based on what nodes and how often the nodes were encountered during the walk, can predict a node feature or classification.

![](https://miro.medium.com/max/1400/1*CAkJLYcq1ilhdDn7tAZVYg.png)

The method used to make predictions is skip-gram, just like in Word2vec architecture for text. Instead of running along the text corpus, DeepWalk runs along the graph to learn an embedding. The model can take a target node to predict it’s “context”, which in the case of a graph, means it’s connectivity, structural role, and node features.

## Sources
 - [Graph Embeddings — The Summary](https://towardsdatascience.com/graph-embeddings-the-summary-cc6075aba007)
 - [Word2Vec Tutorial - The Skip-Gram Model](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)
 - [node2vec: Scalable Feature Learning for Networks](https://snap.stanford.edu/node2vec/)
 - [DeepWalk: Online Learning of Social Representations](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf)
