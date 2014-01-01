
CC=gcc
CFLAGS= -fPIC -shared

text: text.c pokerlib.o
	${CC} ${CFLAGS} text.c pokerlib.o -s -o text

allfive: allfive.c pokerlib.o
	${CC} ${CFLAGS} allfive.c pokerlib.o -s -o allfive

libpoker.so: pokerlib.o
	${CC} -fPIC -shared $^ -o $@

pokerlib.o: pokerlib.c arrays.h
	${CC} -c ${CFLAGS} pokerlib.c -o pokerlib.o

#%.o : %.c
#        $(CC) -fPIC -shared -c $^ -o $@
