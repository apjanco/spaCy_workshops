from sklearn.model_selection import train_test_split


def evaluate(tokenizer, textcat, docs, cats):

    tp = 0.0   # True positives
    fp = 1e-8  # False positives
    fn = 1e-8  # False negatives
    tn = 0.0   # True negatives
    for i, doc in enumerate(textcat.pipe(docs)):
        gold = cats[i]
        for label, score in doc.cats.items():
            if label not in gold:
                continue
            if score >= 0.5 and gold[label] >= 0.5:
                tp += 1.
            elif score >= 0.5 and gold[label] < 0.5:
                fp += 1.
            elif score < 0.5 and gold[label] < 0.5:
                tn += 1
            elif score < 0.5 and gold[label] >= 0.5:
                fn += 1
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f_score = 2 * (precision * recall) / (precision + recall)
    return {'textcat_p': precision, 'textcat_r': recall, 'textcat_f': f_score}


def get_textcat(nlp):
    if 'textcat' not in nlp.pipe_names:
        textcat = nlp.create_pipe('textcat')
        nlp.add_pipe(textcat, last=True)
    else:
        # otherwise, get it, so we can add labels to it
        textcat = nlp.get_pipe('textcat')
        
    return textcat


def split_train_test(docs):
    
    labels = [doc._.author for doc in docs]
    labels_unique = list(set(labels))
    labels = [{author:True if label == author else False for author in labels_unique} for label in labels]
    
    return train_test_split(docs, labels)


