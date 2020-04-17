// Clear DB
MATCH (n) DETACH DELETE n;

// Create Example data set
MERGE (then1:WORD { word: 'then'});
MERGE (you1:WORD { word: 'you'});
MERGE (will1:WORD { word: 'will'});
MERGE (know1:WORD { word: 'know'});
MERGE (the1:WORD { word: 'the'});
MERGE (truth1:WORD { word: 'truth'});
MERGE (and1:WORD { word: 'and'});
MERGE (the1:WORD { word: 'the'});
MERGE (truth1:WORD { word: 'truth'});
MERGE (will1:WORD { word: 'will'});
MERGE (set1:WORD { word: 'set'});
MERGE (you1:WORD { word: 'you'});
MERGE (free1:WORD { word: 'free'});

// See the data set
// MATCH (n) RETURN n;

MATCH (w1:WORD {word:'then'}), (w2:WORD {word:'you'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'you'}), (w2:WORD {word:'will'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'will'}), (w2:WORD {word:'know'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'know'}), (w2:WORD {word:'the'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'the'}), (w2:WORD {word:'truth'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'truth'}), (w2:WORD {word:'and'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'and'}), (w2:WORD {word:'the'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'the'}), (w2:WORD {word:'truth'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'truth'}), (w2:WORD {word:'will'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'will'}), (w2:WORD {word:'set'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'set'}), (w2:WORD {word:'you'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;
MATCH (w1:WORD {word:'you'}), (w2:WORD {word:'free'}) MERGE (w1)-[r:FOLLOWED_BY]->(w2) ON CREATE SET r.weight = 1.0 ON MATCH SET r.weight = r.weight + 1;

// See the graph
// MATCH (n) RETURN n;

// OPTIONAL
// Normalization alfa
// Lets normalize all off the the weights to range 0 to 1.0
// <<my_max>> = MATCH (n) -[r:FOLLOWED_BY]-> (m) RETURN sum(r.weight);
// MATCH (n) -[r:FOLLOWED_BY]-> (m) SET r.weight = r.weight / <<my_max>>;
// END OF OPTIONAL

// See the normalized graph
// MATCH (n) RETURN n;

// Now let's see the propablitiy distrubutution of words following the word 'truth'
<<sumOfAllWeights>> = MATCH (w1:WORD{word:'truth'}) -[r_all:FOLLOWED_BY]-> (w2:WORD) RETURN sum(r_all.weight);
MATCH (w3:WORD {word:'truth'}) -[r_follower:FOLLOWED_BY]-> (w4:WORD) RETURN w4.word, r_follower.weight / <<sumOfAllWeights>> ORDER BY r_follower.weight DESC;

// eof
