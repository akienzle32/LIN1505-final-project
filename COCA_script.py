import spacy
nlp = spacy.load("en_core_web_sm")

def read_coca_file(filename):
    sentences = []
    sentence = []
    for l in open(filename, errors='ignore'):
        flds = l.strip('\n').split('\t')
        sentence.append(flds[0])
        if flds[0] in '.?!':
            sentences.append(' '.join(sentence))
            sentence = []
    return sentences

filename = #change to your filename

corpus = read_coca_file(filename)


#verb classes from Levin (1993)
wipe_class = {'bail', 'buff', 'dab', 'distill', 'dust', 'erase', 'expunge', 'flush', 'leach', 'lick', 'pluck', 'polish', 'prune', 'purge', 'rinse', 'rub', 'scour', 'scrape', 'scratch', 'scrub', 'shave', 'skim', 'smooth', 'soak', 'squeeze', 'strain', 'strip', 'suck', 'suction', 'swab', 'sweep', 'trim', 'wash', 'weed', 'whisk', 'winnow', 'wipe', 'wring', 'brush', 'comb', 'file', 'filter', 'hoover', 'hose', 'iron', 'mop', 'plow', 'rake', 'sandpaper', 'shear', 'shovel', 'siphon', 'sponge', 'towel', 'vacuum'}
clear_class = {'clean', 'clear', 'empty', 'drain'}
P = {'from', 'off'}

do = None
of = None
prep = None
pobj = None

wipe_of = []
wipe_from = []

clear_of = []
clear_from = []



for l in corpus:
    #only run nlp on lines with verbs from wipe- or clear-classes
    verb_found = False
    for v in wipe_class or clear_class or {'empt', 'eras', 'expung', 'prun', 'purg', 'rins', 'scrap', 'shav', 'squeez', 'swep', 'wip', 'fil', 'hos', 'rak', 'spong'}:
        if v in l:
            verb_found = True
    if verb_found == False:
        continue
    else:
        #extract wipe-class hits
        for sentence in nlp(l).sents:
            for w in sentence:
                tag = ''
                if w.pos_ == 'VERB' and w.lemma_ in wipe_class:
                    for wi in w.children:
                        if wi.dep_ == 'prt':
                            break
                            #do not include particle verbs like 'wipe off'
                        if wi.dep_ == 'dobj':
                            do = wi
                            if do != None:
                                for wj in do.children:
                                    #append of-hits to a list
                                    if wj.dep_ == 'prep' and wj.lemma_ == 'of':
                                        of = wj
                                        if of != None:
                                            for x in of.children:
                                                #tag hits with a possessive in the NP complement to 'of' 
                                                if x.dep_ == 'pobj':
                                                    pobj = x
                                                    for y in pobj.children:
                                                        if y.dep_ == 'poss':
                                                            tag = 'POSS'
                                            wipe_of.append(str(sentence) + ' ' + tag)        
                                for wk in w.children:
                                    #append from/off hits to a separate list 
                                    if wk.dep_ == 'prep' and wk.lemma_ in P:
                                        prep = wk
                                        if prep != None:
                                            wipe_from.append(sentence)
                if w.pos_ == 'VERB' and w.lemma_ in clear_class:
                    for wi in w.children:
                        if wi.dep_ == 'prt':
                            break
                            #do not include particle verbs like 'clean off'
                        if wi.dep_ == 'dobj':
                            do = wi
                            if do != None:
                                for wj in do.children:
                                    #append of-hits to a list
                                    if wj.dep_ == 'prep' and wj.lemma_ == 'of':
                                        of = wj
                                        if of != None:
                                            clear_of.append(sentence)
                                for wk in w.children:
                                    #append from/off hits to a separate
                                    if wk.dep_ == 'prep' and wk.lemma_ in P:
                                        prep = wk
                                        if prep != None:
                                            clear_from.append(sentence)
                                            
#write all wipe-class hits to file, along with the number for total of-hits and from/off hits
hits_file = open('hits_file.txt', 'w')
hits_file.write('wipe of-hits = ' + str(len(wipe_of)))
for x in wipe_of:
    hits_file.write('\n\n' + str(x))
hits_file.write('\n\n\n\n' + 'wipe from-hits = ' + str(len(wipe_from)))
for x in wipe_from:
    hits_file.write ('\n\n' + str(x))
    
#write all clear-class hits to same file, along with number for hits    
hits_file.write('\n\n\n\n\n\n' + 'clear of-hits = ' + str(len(clear_of)))
for y in clear_of:
    hits_file.write('\n\n' + str(y))
hits_file.write('\n\n\n\n' + 'clear from-hits = ' + str(len(clear_from)))
for y in clear_from:
    hits_file.write('\n\n' + str(y))
hits_file.close()
