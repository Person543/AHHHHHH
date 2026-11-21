import sys,os,json,random,csv
sys.path.insert(0,'.')
import scen_a,scen_b,scen_c,scen_x
OUT='out_scen'; os.makedirs(OUT,exist_ok=True); os.makedirs(OUT+'/quizlet_by_chapter',exist_ok=True)
BOOKS=[("Metasploit & Meterpreter",scen_a.DECKS),("Linux",scen_b.DECKS),("Windows",scen_c.DECKS),("Cross-Book",scen_x.DECKS)]
rng=random.Random(11); decks=[]
for book,dl in BOOKS:
    for code,name,items in dl:
        qs=[]
        for it in items:
            if it[0]=='mc':
                _,q,opts,ci,exp=it; pairs=list(enumerate(opts)); rng.shuffle(pairs)
                qs.append(dict(type='mc',q=q,options=[o for _,o in pairs],answer=[i for i,(oi,_) in enumerate(pairs) if oi==ci][0],exp=exp))
            else:
                _,q,a,exp=it; qs.append(dict(type='sa',q=q,answer=a,exp=exp))
        decks.append(dict(code=code,name=name,book=book,questions=qs))
def atext(q): return q['options'][q['answer']] if q['type']=='mc' else q['answer']
def front(q):
    if q['type']!='mc': return q['q']
    return q['q']+'  '+'  '.join(f'({chr(65+i)}) {o}' for i,o in enumerate(q['options']))
# Quizlet
with open(f'{OUT}/quizlet_ALL_flashcards.txt','w') as f:
    for d in decks:
        for q in d['questions']:
            f.write(f"{front(q)}\t{atext(q)}"+(f"  [{q['exp']}]" if q['exp'] else '')+"\n")
for d in decks:
    with open(f"{OUT}/quizlet_by_chapter/{d['code']}.txt",'w') as f:
        for q in d['questions']: f.write(f"{front(q)}\t{atext(q)}\n")
# Anki
with open(f'{OUT}/anki_ALL.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['Front','Back','Tags'])
    for d in decks:
        for q in d['questions']:
            back=atext(q)+('<br><br><i>'+q['exp']+'</i>' if q['exp'] else '')
            w.writerow([front(q),back,d['code']])
# GIFT
def g(s):
    for c in ['\\','~','=','#','{','}',':']: s=s.replace(c,'\\'+c)
    return s
with open(f'{OUT}/moodle_GIFT_ALL.txt','w') as f:
    for d in decks:
        f.write(f"\n$CATEGORY: $course$/{d['code']} {d['name']}\n\n")
        for i,q in enumerate(d['questions'],1):
            nm=f"{d['code']}-{i:02d}"
            if q['type']=='mc':
                f.write(f"::{nm}:: {g(q['q'])} {{\n")
                for j,o in enumerate(q['options']): f.write(("    =" if j==q['answer'] else "    ~")+g(o)+"\n")
                f.write(f"    #### {g(q['exp'])}\n}}\n\n")
            else:
                f.write(f"::{nm}:: {g(q['q'])} {{}}\n// MODEL ANSWER: {q['answer']}\n\n")
json.dump(decks,open(f'{OUT}/quiz_data.json','w'),indent=1)
print('decks',len(decks),'questions',sum(len(d['questions']) for d in decks))