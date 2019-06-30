import spacy
import standoffconverter # standoff_to_xml, tree_to_standoff


def xml_to_jsonl(xml):
	tree = etree.fromstring(xml)
    standoffconverter.tree_to_standoff(tree)
    
    #re xml tag, type


	return jsonl 
'''{
    "text": "This is the kind of text, which includes tagged content inside it.",
    "spans": [
        {"start": 20, "end": 24, "label": "ner"},
        {"start": 41, "end": 47, "label": "different_ner"}
    ]
}'''


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

