import sys, json, random, html, os, csv
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import bank_a, bank_b, bank_c, extras
OUT=os.path.join(HERE,'out'); os.makedirs(OUT, exist_ok=True)

BOOKS=[("Initial Access with Metasploit and Meterpreter", bank_a.DECKS),
       ("Linux for Cyber Operations", bank_b.DECKS),
       ("Windows for Cyber Operations", bank_c.DECKS),
       ("Cross-Book Synthesis", extras.DECKS)]

rng=random.Random(7)
decks=[]
for book,dl in BOOKS:
    for code,name,items in dl:
        qs=[]
        for it in items:
            if it[0]=='mc':
                _,q,opts,ci,exp=it
                pairs=list(enumerate(opts)); rng.shuffle(pairs)
                new=[o for _,o in pairs]; nci=[i for i,(oi,_) in enumerate(pairs) if oi==ci][0]
                qs.append(dict(type='mc',q=q,options=new,answer=nci,exp=exp))
            else:
                _,q,a,exp=it
                qs.append(dict(type='sa',q=q,answer=a,exp=exp))
        decks.append(dict(code=code,name=name,book=book,questions=qs))

total=sum(len(d['questions']) for d in decks)

def ans_text(q):
    return q['options'][q['answer']] if q['type']=='mc' else q['answer']

# ---------- 1. Quizlet / generic flashcards (term TAB definition) ----------
with open(f'{OUT}/quizlet_ALL_flashcards.txt','w') as f:
    for d in decks:
        for q in d['questions']:
            f.write(f"{d['code']} | {q['q']}\t{ans_text(q)}\n")
os.makedirs(f'{OUT}/quizlet_by_chapter', exist_ok=True)
for d in decks:
    with open(f"{OUT}/quizlet_by_chapter/{d['code']}_{d['name'].split(' - ')[-1].replace(' ','_').replace('/','-')}.txt",'w') as f:
        for q in d['questions']:
            f.write(f"{q['q']}\t{ans_text(q)}\n")

# ---------- 2. Anki (CSV: Front,Back,Tags) ----------
with open(f'{OUT}/anki_ALL.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['Front','Back','Tags'])
    for d in decks:
        tag=d['code']+'::'+d['name'].split(' - ')[0].replace(' ','_')
        for q in d['questions']:
            back=ans_text(q)+('<br><br><i>'+q['exp']+'</i>' if q['exp'] else '')
            if q['type']=='mc':
                back = ans_text(q)+'<br><br><b>Options were:</b> '+' / '.join(q['options'])+'<br><br><i>'+q['exp']+'</i>'
            w.writerow([q['q'],back,tag])

# ---------- 3. Moodle GIFT ----------
def g(s):
    for c in ['\\','~','=','#','{','}',':']:
        s=s.replace(c,'\\'+c)
    return s
with open(f'{OUT}/moodle_GIFT_ALL.txt','w') as f:
    for d in decks:
        f.write(f"\n// ===== {d['code']} {d['name']} =====\n$CATEGORY: $course$/{d['book']}/{d['code']} {d['name']}\n\n")
        for i,q in enumerate(d['questions'],1):
            name=f"{d['code']}-{i:02d}"
            if q['type']=='mc':
                f.write(f"::{name}:: {g(q['q'])} {{\n")
                for j,o in enumerate(q['options']):
                    f.write(("    =" if j==q['answer'] else "    ~")+g(o)+"\n")
                f.write(f"    #### {g(q['exp'])}\n}}\n\n")
            else:
                f.write(f"::{name}:: {g(q['q'])} {{}}\n// MODEL ANSWER: {q['answer']}\n\n")

# ---------- 4. Aiken (multiple choice only) ----------
with open(f'{OUT}/aiken_MULTIPLE_CHOICE_ALL.txt','w') as f:
    for d in decks:
        for q in d['questions']:
            if q['type']!='mc': continue
            f.write(q['q'].replace('\n',' ')+'\n')
            for j,o in enumerate(q['options']):
                f.write(f"{chr(65+j)}. {o}\n")
            f.write(f"ANSWER: {chr(65+q['answer'])}\n\n")

# ---------- 5. Blackboard tab-delimited upload ----------
with open(f'{OUT}/blackboard_upload_ALL.txt','w') as f:
    for d in decks:
        for q in d['questions']:
            if q['type']=='mc':
                row=['MC',f"[{d['code']}] "+q['q']]
                for j,o in enumerate(q['options']):
                    row+= [o,'correct' if j==q['answer'] else 'incorrect']
            else:
                row=['ESS',f"[{d['code']}] "+q['q'],q['answer']]
            f.write('\t'.join(x.replace('\t',' ') for x in row)+'\n')

# ---------- 6. JSON ----------
json.dump(decks, open(f'{OUT}/quiz_data.json','w'), indent=1)
print('decks',len(decks),'questions',total,
      'mc',sum(1 for d in decks for q in d['questions'] if q['type']=='mc'),
      'sa',sum(1 for d in decks for q in d['questions'] if q['type']=='sa'))
