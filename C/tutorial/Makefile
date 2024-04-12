# this is the most simplest makefile example
# Note: @ in the make file will prevent echoing the command
ifeq ($(DEBUG),1)
   OPTS = -g
endif

helloWorld:
	gcc -o obj/helloWorld helloWorld.c

# this example shows how to include a C file with multiple file dependencies
helloMake: 
	gcc -o obj/helloMake helloMake.c helloFunc.c -I./include

farenheitCelsius:
	gcc -o obj/farenheitCelsius farenheitCelsius.c

farenheitCelsiusParams:
	gcc -o obj/farenheitCelsiusParams farenheitCelsiusParams.c	

characterIO:
	gcc -o obj/characterIO characterIO.c

characterCount:
	gcc -o obj/characterCount characterCount.c

wordCount:
	gcc -o obj/wordCount wordCount.c

histogramWord:
	gcc -o obj/histogramWord histogramWord.c

maxLine:
	gcc -o obj/maxLine maxLine.c

simpleStruct:
	gcc -o obj/simpleStruct simpleStruct.c