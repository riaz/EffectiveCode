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