import random
import dominate
from dominate.tags import *
import pdfkit
from datetime import datetime


novel = ''
lines = []
paragraphs = []
tl = []
tl.append([])
tp = []
with open("data.tsv") as f:
	data = f.readlines()

for l in data:
	img,txt = l.split("\t")
	lines.append(txt)


# run through the generated lines to remove the duplicate sentences 
for l in range(1,len(lines)):
	# check for duplicates
	if (lines[l] != lines[l - 1]):

		# Make a new list of lines for each '.....'
		# These will become paragraphs later.
		if (lines[l] == '.....\n'):
			tl.append([])
		else:
			tl[-1].append(lines[l].replace("\n",""))
		
# Now work through each list of lines to make occasional compounds.
# Combine them into a string eventually
compounder = 0
chapterCount = 2
tl[0][0]

tp.append("Chapter 1: " + tl[0].pop(0).capitalize())
for pa in tl:
	

	if (random.randint(0,100) < 3):
		tp.append(["Chapter " + str(chapterCount) + ": " + pa.pop(0).capitalize()])
		chapterCount += 1
		tp.append('')
	else:
		tp.append('')

	# two possible accumulation bits, if set, concat with appropriate
	# punctuation.
	for s in range(len(pa)):
		
		# figure out where in a sequence I am.
		if (compounder == 0 and random.randint(0,100) < 80 and s < len(pa) - 5):
			compounder = 1
		elif (compounder == 1):
			compounder = 2
		elif (compounder == 2):
			compounder = 0

		ins = [pa[s].capitalize(), "There's " + pa[s], "I see " + pa[s], "I see " + pa[s], "I see " + pa[s], "I see " + pa[s], "It's sort of like " + pa[s], "I guess that's just " + pa[s], "Now it's " + pa[s], "Or " + pa[s], "That's definitely " + pa[s]]

		# I guess a switch/case would be nicer looking here, but this should work
		if (compounder == 0):
			tp[-1] += random.choice(ins) + ". "
		elif (compounder == 1):
			tp[-1] += random.choice(ins) + random.choice([" and then "," and ","; ", " with "," just before "," followed by "])
		elif (compounder == 2):
			tp[-1] += pa[s] + random.choice([". ",". ",". ",". ",". ","? "])


doc = dominate.document(title='I forced an AI to watch "Santa Clause Conquers the Martians"')

with doc.head:
	style(
	"""
			body{

				font-size:116pt;
				
			} 
			h1,h2 {
				font-family:Helvetica, Arial, sans-serif;
			}

			h1 {
				width: 78%;
				margin: 0 auto;
				text-align:center;
				padding-top: 4em;
			}
			h2 {
				padding:5em 0 1em;
				page-break-before: right; 
				
			}

			#content {
			    display: table;
			}

			#pageFooter {
			    display: table-footer-group;
			}

			#pageFooter:after {
			    counter-increment: page;
			    content: counter(page);
			}


	""")

with doc:

	h1("I forced an AI to watch ", em("Santa Clause Conquers the Martians"))

	h2("Prologue")
	p("The title of this book says it all, but to be more specific, I used Microsoft Cognitive Services Computer Vision to analyze and generate descriptions for 14,635 frames of ", em("Santa Clause Conquers the Martians"), ", a not so great Christmas movie about exactly what the title says it's about.")
	p("-- Zach Whalen, for NaNoGenMo 2018")
	p("This particular file generated at " + str(datetime.now()))

	with div(id='content'):
		div(id='pageFooter', text="Page ")

		for chunk in tp:

			if ("Chapter" in str(chunk)):
				h2(chunk)
			else:
				p(chunk)

with open('novel.html','w') as f:			
	f.write( doc.render() )

pdfoptions = {
    'page-size': 'Letter',
    'margin-top': '1.5in',
    'margin-right': '1.0in',
    'margin-bottom': '1.0in',
    'margin-left': '1.0in'
 }


pdfkit.from_string(str(doc.render()), 'novel.pdf', options = pdfoptions)

	
