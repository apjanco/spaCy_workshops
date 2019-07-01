import spacy
import standoffconverter # standoff_to_xml, tree_to_standoff


def xml_to_jsonl(xml):
    standoff = standoffconverter.tree_to_standoff(xml)
    jsonl = {}
    jsonl['text'] = standoff[0]
    jsonl['spans'] = []
    for tag in standoff[1]:
        jsonl['spans'].append(tag)
    
    #change key names: begin to start, type to label
    for span in jsonl['spans']:
        span['start'] = span.pop('begin')
        span['label'] = span.pop('tag')
        del span['attrib']
        del span['depth']
    return  json.dumps(jsonl)
    #TODO standoff start and end values do not match spacy span values 	


def jsonl_to_xml(jsonl):    
    jsonl = json.loads(jsonl)
    text = jsonl['text']
    offset = 0
    
    for span in jsonl['spans']:

        new_text = f"<{span['label']}>" + text[span["start"] +offset : span["end"] + offset] +  f"</{span['label']}>"
        text = text[:span["start"] + offset] + new_text + text[span["end"] + offset:]
        offset += len(new_text) - (span["end"] - span["start"])
    
    return text

