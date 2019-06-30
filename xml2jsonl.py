import spacy
import standoffconverter # standoff_to_xml, tree_to_standoff


def xml_to_jsonl(xml):
    standoff = standoffconverter.tree_to_standoff(xml)
    jsonl = {}
    jsonl['text'] = standoff[0]
    jsonl['spans'] = []
    for tag in standoff[1]:
        jsonl['spans'].append(tag)
    
    #change key names begin to start, type to label
    for span in jsonl['spans']:
        span['start'] = span.pop('begin')
        span['label'] = span.pop('tag')

    return  jsonl

	


def jsonl_to_xml(jsonl):
	for line in jsonl:
		standoff.append({
	    "begin": 42, # character position in plain text str
	    "end": 42, # character position in plain text str
	    "tag": "SOMETAG",
	    "depth": 0, # depth of the annotation wrt. to the other tags
	    "attrib": {...} # dict of attrib as in etree.attrib elements
  	    })
  	new_xml = standoffconverter.standoff_to_xml(plain, standoff)
  	return xml 

