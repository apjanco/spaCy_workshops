# Introduction to natural language processing for DH research with spaCy - A fast and accessible library that integrates modern machine learning technology 

### Introduction to natural language processing for DH research with spaCy - A fast and accessible library that integrates modern machine learning technology.

This half-day workshop will introduce DH scholars to spaCy, a free and open-source library for text analysis. Developed by Matthew Hannibal and Ines Montari in Berlin, these programs offer a suite of tools for applied natural language processing that are fast, practical and allow for quick experimentation and evaluation of language models. These tools make it possible for individual scholars to quickly train statistical models that can infer customized categories in named entity recognition tasks, match phrases, and visualize model performance.  While comparable to the Natural Language Toolkit (NLTK), spaCy offers neural network models, integrated word vectors, dependency parsing and a variety of new features that are not available elsewhere. Participants will learn how to use spaCy for common research tasks in the Digital Humanities and gain an understanding of how spaCy compares with other tools for natural language processing.     

### Target audience and expected number of participants

This workshop would appeal to a similar audience as attended DH2018's Distant Viewing and Word Vectors workshops.  Our participants will have some existing familiarity with natural language processing and text analysis. Participants will leave the workshop with the skills needed to install dependencies, train a model on categories that are relevant to their research and run inference on text. They may have heard of spaCy and are interested in learning how it differs from NLTK. 

Each participant should bring a laptop computer to the workshop.  No other technology is required.  Links and instructions to install spaCy and Prodigy will be provided in advance of the workshop, but installation can also be completed in the first few minutes of the workshop.  

### Brief outline
Our team of three instructors has divided the session into three fifty-minute sessions with ten-minute breaks in between.  

In the first session, we will discuss the installation and basic use of spaCy.  We will introduce existing models and available tasks for language and image analysis.  These include basic phrase matching, part of speech identification (POS) and named entity extraction. We will demonstrate displacy, which is a highly useful tool to visualize a model's results.  By the end of the session, participants will be able to load a model and use it to identify basic linguistic features, such as the base form of words (lemma), POS, syntactic dependency, word shape and stop words.In a small introductory project, participants will use spaCy code in a pre-written notebook to generate individualized vocabulary lists for language learning.  The script will take a text as input and output a list of lemmata.  These lemmata can then be compared against a second text to produce a list of vocabulary.    

The second session will cover more advanced capabilities of spaCy.  We will discuss named entity recognition and rule-based matching. We will demonstrate how to use word vectors to measure semantic similarity. We will also show participants how to train new entities with spaCy.  We will also outline how new languages can be added to a spaCy model.  Participants will leave this session with ideas on how spaCy's customized models could be utilized in their own DH projects.   

The third session will focus on Prodigy, which is an annotation tool used to train and evaluate language models.  Building on knowledge from the second session, participants will learn how to use Prodigy to radically reduce the time needed to train new categories and entities using active learning.  Participants will learn how to train custom language categories and entities using Prodigy. Participants will leave the session with a clear end-to-end workflow from initial text or images, to training, to the application of trained models in research.    

### Tutorial instructors  
- Andrew Janco 
   -email: ajanco@haverford.edu
   - Andrew Janco is the Digital Scholarship Librarian at Haverford College. He completed his Ph.D. at the University of Chicago. Andy has a passion for inquiry-driven and community-engaged digital projects.  He is the lead developer working on a digital archive and research application for the Groupo de Apoyo Mutuo, Guatemala's oldest human rights organization. He also works on applied machine learning for humanities and social science research.  

- David Lassner
   -email: lassner@tu-berlin.de
   - David Lassner graduated (M.Sc.) in computer science at TU Berlin in 2017, focussing on machine learning with a minor in German literary studies. Mr. David Lassner is now a PhD candidate researching machine learning in the digital humanities at the group of machine learning at TU Berlin, where his main focus is the (machine-driven) analysis of literature.  

- Seth Bernstein
    -email: sfbernstein@gmail.com
   - Dr. Seth Bernstein is currently Assistant Professor in History at the Higher School of Economics (Russian Federation).  He holds a PhD in history from the University of Toronto (Canada). His current project, "Return to the Motherland: The Repatriation of Soviet Citizens after World War II," explores the brutal but transnational wartime experience and troubled return of some five million members of the Soviet wartime diaspora. Seth's work also uses digital techniques like GIS and massive textual databases to extract and visualize data. He posts his digital history findings occasionally at [abstractualized.com](abstractualized.com).

---

#### Unit II: Advanced Topics with spaCy
   (unit2/outline.ipynb)
   TEI XML is the de facto standard for digital scholarly editions. In order to make spaCy usable in the context of DH scholarship we present the design principles for conversion and show code examples to load TEI XML into spaCy for two different corpora: The German Text Archive (deutschestextarchiv.de, DTA) and the Berlin Intellectuals (berliner-intellektuelle.eu, BI). In case of DTA, a basic parser for plain text is presented with metadata annotation on document level. The resulting spaCy document objects can be used for classification such as authorship attribution.  
   In the case of BI which encompasses genetic encoding, character-level annotation techniques for document variants are presented. The resulting document variants are presented using displacy to offer a highly interactive exploration tool for such genetic editions.  
   Finally, the integration of word vectors in spaCy is presented by neglecting the built-in word vectors and loading pre-trained fasttext vectors. SpaCy itself currently (Dec. 2018) only encompasses seven languages and only word vectors for four of them. To emphasize the pursuit of language diversity within the DH community we show how to load and apply word vectors for 157 different languages into spacy.

   1. Basic Pipeline from TEI to Spacy with annotations on document-level

      1. load 50 TEI encoded XMLs from Deutsches Textarchiv
      2. Extract plain text and author GND
      3. Annotate each document with its author id

   2. A little more advanced Pipeline from TEI to Spacy annotations on character-level
   (This is based on a Twitter discussion between Ines Montani and me: https://twitter.com/_inesmontani/status/920294329570267136)
      1. load 50 TEI encoded XMLs from Berliner Intellektuelle
      2. Extract initial and last version
      3. annotate sub-tokens that have been added or deleted

   3. Loading word vectors from fasttext
   (This is based on https://github.com/explosion/spaCy/issues/1525)


---

Pre-Conference Workshops and Tutorials

Tutorials are normally half-day intensive introductions to specific techniques, software packages, or theoretical approaches with a small number of participants. Workshop proposals may take many forms, including proposals with a full slate of speakers and presentations, as well as proposals to issue an independent call for papers from which submissions will be chosen. Participants in pre-conference workshops and tutorials will be expected to register for the full conference as well as pay a small additional fee to the conference. Workshops are expected to be self-financing in terms of hardware and software needs.

Proposals should provide the following information:

Title and a brief description of the content or topic and its relevance to the Digital Humanities community (not more than 1500 words);
Full contact information for all tutorial instructors or workshop leaders, including a one-paragraph statement summarizing their research interests and areas of expertise;
Description of the target audience and expected number of participants (based, if possible, on past experience); and
Special requirements for technical support.
Additionally, tutorial proposals should include:

A brief outline showing that the core content can be covered in a half-day (approximately 3 hours, plus breaks). In exceptional cases, full-day tutorials may be supported.
And workshop proposals must include:

Intended length and format of the workshop (minimum half-day; maximum one-and-a-half days);
Any special requirements for attendees, including software installation (the conference will handle traditional technological support, but workshop organizers are expected to manage specific needs such as access to software, servers, etc.).  
If the workshop is to have its own call for participation, a deadline and date for notification of acceptances, and a list of individuals who have agreed to be part of the workshop’s Program Committee.
As with Multiple Paper Panel proposals, those submitting proposals for pre-conference workshops are advised to ensure that the constitution of the workshop reflects the constitution of the field and/or research topic that is being addressed and ADHO’s expressed commitment to diversity, or explicitly address problems in those areas.  In case the proposer’s own network is too limited, the Program Committee can advise them before submission on whom to contact to broaden the panel. Please contact the PC chairs Fabio Ciotti fabio [dot] ciotti [at] uniroma2 [dot] it or Elena Pierazzo elena [dot] pierazzo [at] univ-grenoble-alpes [dot] fr if you need advice.
