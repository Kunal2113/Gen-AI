!pip install datasets transformers[sentencepiece]

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

classifier("food was amazing was extravagent")

classifier("Food was bad and ambience is so gloomy")

classifier("the water bottle is very good it keeps cold water for long time|")

classifier(["he is a good boy but he is so lazy","he is rich by money but not with the nature","apple is good but taste was awfull"])

summary=pipeline(model='t5')

zero_shot = pipeline('zero-shot-classification')

zero_shot('''The film industry or motion
picture industry comprises the technological and commercial institutions of
filmmaking, i.e., film production companies, film studios, cinematography,
animation, film production, screenwriting, pre-production, post-production,
film festivals, distribution, and actors. Though the expense involved in
making film almost immediately led film production to concentrate under
the auspices of standing production companies, advances in affordable
filmmaking equipment,as well as an expansion of opportunities to acquire investment capital  from outside the fim industry itself,
have allowed independent film production to evolve.

In 2019 the global box office was worth $42.2 billion.[1]When including box ofiice and home entertainment revenue, the global
film industry was worth $136 billion in 2018.
[2]Hollywood is the world oldest national fim industry ,
and largest in terms of box-office gross revenue.''',
   candidate_labels = ['education' ,'business','techniology','food','science','cinema'])



zero_shot("India won 2 gold medals in olympics ",candidate_labels=['education ','sports','business'])

generator= pipeline('text-generation')

generator('In this course we are going to learn about')

ner=pipeline('ner')

ner("Iran and US are in war with each other")

pipe = pipeline("question-answering",model="ahotrod/electra_large_discriminator_squad2_512")

import os
os.environ['HF_TOKEN']='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'
