import nltk
from nltk.tokenize import word_tokenize

#nltk.download()--- used to download any required packages from nltk module during runtime
#nltk.help.upenn_tagset(tag_code)---used to know about any tag_code i.e CC,CD,DT,EX...

print("enter text:")
text=input()
print("")


words=word_tokenize(text)#tokenize the given text into words

tag_text=nltk.pos_tag(words)#assign parts of speech(pos) tags to the tokens

#meaning for pos tags
tag_dict={'CC':'Coordinating conjunction',
          'CD':'Cardinal number',                          
          'DT':'Determiner',
	  'EX':'Existential there',
	  'FW':'Foreign word',
	  'IN':'Preposition or subordinating conjunction',
	  'JJ':'Adjective',
	  'JJR':'Adjective, comparative',
	  'JJS':'Adjective, superlative',
	  'LS':'List item marker',
	  'MD':'Modal',
	  'NN':'Noun, singular or mass',
	  'NNS':'Noun, plural',
	  'NNP':'Proper noun, singular',
	  'NNPS':'Proper noun, plural',
	  'PDT':'Predeterminer',
	  'POS':'Possessive ending',
	  'PRP':'Personal pronoun',
	  'PRP$':'Possessive pronoun',
	  'RB':'Adverb',
	  'RBR':'Adverb, comparative',
	  'RBS':'Adverb, superlative',
	  'RP':'Particle',
	  'SYM':'Symbol',
	  'TO':'to',
	  'UH':'Interjection',
 	  'VB':'Verb, base form',
	  'VBD':'Verb, past tense',
	  'VBG':'Verb, gerund or present participle',
	  'VBN':'Verb, past participle',
	  'VBP':'Verb, non-3rd person singular present',
	  'VBZ':'Verb, 3rd person singular present',
	  'WDT':'Wh-determiner',
	  'WP':'Wh-pronoun',
	  'WP$':'Possessive wh-pronoun',
 	  'WRB':'Wh-adverb'}

for i in tag_text:
    a,b=i
    try:
        #special characters cause error i.e ',' '.' 
        print(a+"---"+tag_dict[b])
    except:     
        print(i)
