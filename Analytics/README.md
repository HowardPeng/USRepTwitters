# NLP Analysis #

## Introduction ## 
Tweet Scraper:
* Tweet ***T<sub>ij<sub>*** is the ***j*** th tweet from Representative ***i*** , where 1 ≤ ***j*** ≤ ***N<sub>i<sub>***
* Issue ***S<sub>k<sub>*** is the artificially pre-selected 100 strings (e.g. ***S<sub>1<sub>*** = "Human Right", ***S<sub>2<sub>*** = "Arm Sale", ***S<sub>3<sub>*** = "China", ...)

NLP Technology: word embedding funciton
* nlp: {arbitrary string} -> {50, 100, 200 or 300 dimensional real vector}
* How "close" 2 strings (say, ***a*** and ***b*** ) are: cosine-similarity( nlp( ***a*** ) , nlp( ***b*** ) )

## Our Approach ##
* Given every tweet data that every US representative has ever tweeted.
  * Which were collected on July 3th, 2017
* Given a word embedding function
  * GLOVE: 400k vocabulary trained over 6 billion tokens on WIKIPEDIA

1. Every tweet ***T<sub>ij<sub>*** is a point in the constellation of issues ***S<sub>1<sub>*** ... ***S<sub>100<sub>*** , 
    * where its ***k*** th coordinate is "cosine-similarity( nlp( ***T<sub>ij<sub>*** ) , nlp( ***S<sub>k<sub>*** ) )"
    * We can also calculate the mean and variance of tweets from Representative ***i*** , it show averagely how this Representative cares about certain issues.
2. In addition, any string (let us call it "keyword", e.g. "Taiwan", "South China Sea") is also a point in this constellation. We can calculate the distance (or any measurement that is similar to a metric) of this "keyword" to the mean of any Representative. This can serve as an indicator that how this Representative cares about this keyword.
