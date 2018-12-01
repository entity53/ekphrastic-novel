# I forced an AI to watch Santa Claus Conquers the Martians.

This is a project I completed for NaNoGenMo 2018. As the title suggests, I forced an AI -- specifically the Computer Vision tool from Microsoft's Cognitive Services -- to view and analyze 14,635 frames of the movie _Santa Claus Conquers the Martians_.

I added some syntax between captions to help it flow better and to convey the AI's lack of confidence about what it was seeing [final novel](novel.pdf) comes in at 64,566 words, which satisfies [the requirements](https://github.com/nanogenmo/2018).

There's really not much code here. The [ek.py](ek.py) script arranged the interface to Microsoft and saved all the image descriptions into a CSV. Then [write.py](write.py) read and arranged the resulting descriptions into something like a novel, using [Dominate](https://github.com/Knio/dominate) to generate an HTML file which [pdfkit](https://github.com/JazzCore/python-pdfkit) turns into a PDF.

Enjoy!