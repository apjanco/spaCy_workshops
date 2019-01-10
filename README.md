### Introduction to natural language processing for DH research with spaCy - A fast and accessible library that integrates modern machine learning technology.

This half-day tutorial will introduce DH scholars to spaCy, a free and open-source library for text analysis. Developed by Matthew Hannibal and Ines Montari in Berlin, spaCy offers a suite of tools for applied natural language processing (NLP) that are fast, practical and allow for quick experimentation and evaluation of language models. These tools make it possible for individual scholars to quickly train models that can infer customized categories in named entity recognition tasks, match phrases, and visualize model performance.  While comparable to the Natural Language Toolkit (NLTK), spaCy offers neural network models, integrated word vectors, dependency parsing and a variety of new features that are not available elsewhere. Participants will learn how to use spaCy for common research tasks in the Digital Humanities and gain an understanding of how spaCy compares with other tools for NLP. We will also work with Prodigy, which is an annotation and active learning tool from the makers of spaCy. Prodigy allows a single researcher to quickly fine-tune a model for greater accuracy on a specific task or to train new categories and entities for recognition.  This simple web-application can also be used to crowdsource annotations. 

### Target audience and expected number of participants

This tutorial would appeal to a similar audience as attended DH2018's distant viewing and word vectors workshops.  Given attendance at those workshops, we expect around 25-30 participants would register for our tutorial.  Our participants will probably have some existing familiarity with natural language processing, text analysis, and TEI. Participants will leave the tutorial with the skills needed to install dependencies, train a model on categories that are relevant to their research and run inference on a text. They may have heard of spaCy and are interested in learning how it differs from NLTK.   

Our instructors come from a range of backgrounds in machine learning, the humanities, and information science. This diversity of perspectives and use cases of spaCy will appeal to a large DH audience and help participants to connect what they've learned with their own research.  

Each participant should bring a laptop computer to the tutorial.  No other technology is required.  Links and instructions to install spaCy and Prodigy will be provided in advance of the tutorial, but installation can also be completed in the first few minutes.  

### Brief outline
Our tutorial is composed of three 45-minute sessions with ten-minute breaks in between, followed by a 15-minute concluding discussion.  

In the first session, we will discuss the installation and basic use of spaCy. We will introduce existing models and available tasks for language analysis. 

These include basic phrase matching, part of speech identification (POS) and named entity extraction. We will demonstrate displacy, which is a highly useful tool to visualize a model's results.  
By the end of the session, participants will be able to load a model and use it to identify basic linguistic features, such as the base form of words (lemma), part of speech, syntactic dependency, word shape and stop words. In a small introductory project, participants will use spaCy code in a prepared notebook to generate individualized vocabulary lists for foreign language learning.  The script will take a text as input and output a list of lemmata.  These lemmata can then be compared against a second text to produce a customized vocabulary list for a reader to consult when reading the second text.    

The second session will cover more advanced capabilities of spaCy. TEI XML is the de facto standard for digital scholarly editions. In order to make spaCy usable in the context of DH scholarship we present the design principles for conversion and show code examples to load TEI XML into spaCy for two different corpora: The German Text Archive (deutschestextarchiv.de, DTA) and the Berlin Intellectuals (berliner-intellektuelle.eu, BI). In case of DTA, a basic parser for plain text will be developed during the tutorial with metadata annotation on document level. The resulting spaCy document objects will be used for classification such as authorship attribution. For this classification task, the Convolutional Neural Network of the spaCy TextCategorizer module will be used.  
In the case of BI which encompasses genetic encoding, character-level annotation techniques for document variants are presented. The resulting document variants are presented using displacy to offer a highly interactive exploration tool for such genetic editions.  
Finally, the integration of word vectors in spaCy is presented by neglecting the built-in word vectors and loading pre-trained fasttext vectors. SpaCy itself currently (Dec. 2018) only encompasses seven languages and only word vectors for four of them. To emphasize the pursuit of language diversity within the DH community we show how to load and apply word vectors for 157 different languages into spacy.
  
The third session will focus on Prodigy, which is an annotation tool used to train and evaluate spaCy language models.  Building on knowledge from the second session, participants will learn how to use Prodigy to quickly train new categories and entities on existing language models.  Prodigy utilizes a method called active learning in which human input and automated learning are both used to update the model.  Prodigy sorts the model's uncertain results and strategically asks for user input.  These annotations are then used to update the model on new categories or to improve accuracy with a specific task. In this session, participants will learn how to train custom language categories and entities using Prodigy.  
Participants will leave the session with a clear end-to-end workflow from an initial text, to training, to the application of trained models.  Building on Unit II, we will use the new model to automatically update a TEI document with the new categories and data.   

After the sessions, the instructors will open a group conversation about the strengths and weaknesses of spaCy and prodigy for DH scholarship based on the experiences in the tutorial. The discussion should allow participants to identify specific use-cases for their scholarly work.

### Tutorial instructors  

- Session I, Seth Bernstein
    -email: sfbernstein@gmail.com
   - Seth Bernstein is Assistant Professor of History at the Higher School of Economics (Russian Federation).  He holds a PhD in history from the University of Toronto (Canada). He is the author of Raised under Stalin: Young Communists and the Defense of Socialism (Cornell, 2017). His current project is "Return to the Motherland: The Repatriation of Soviet Citizens after World War II." Seth's work also uses digital techniques like GIS and massive textual databases to extract and visualize data.  

- Session II, David Lassner
   -email: lassner@tu-berlin.de
   - David Lassner graduated (M.Sc.) in computer science at TU Berlin in 2017, focussing on machine learning with a minor in German literary studies. Mr. David Lassner is now a PhD candidate researching machine learning in the digital humanities at the group of machine learning at TU Berlin, where his main focus is the (machine-driven) analysis of literature.  

- Session III, Andrew Janco 
   -email: ajanco@haverford.edu
   - Andrew Janco is the Digital Scholarship Librarian at Haverford College. He completed his Ph.D. in History at the University of Chicago and MS in Information Science at the University of Illinois. Andy has a passion for inquiry-driven and community-engaged digital projects.  He is the lead developer of a digital archive and research application for the Groupo de Apoyo Mutuo, Guatemala's oldest human rights organization.  Andy has experience organizing two previous tutorials on spaCy and Prodigy.  He works on applied machine learning for research applications in humanities and social science scholarship.  
