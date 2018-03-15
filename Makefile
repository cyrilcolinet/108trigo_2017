##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## Makefile
##

NAME 	=	108trigo

CC 		= 	gcc

TESTS 	=	tests/108trigo_cos_tests.c

CFLAGS 	= 	-Wall -Wextra

LDFLAGS	=	-lcriterion

OBJ 	= 	$(TESTS:.c=.o)

all:
		ln -s src/main.py $(NAME)
		chmod +x $(NAME)

clean:
		rm -rf file

fclean: clean
		chmod -x src/main.py
		rm -rf $(NAME)
		rm -rf units

re: 	fclean all

tests_run: fclean $(OBJ)
		$(CC) $(CFLAGS) $(LDFLAGS) $(OBJ) -o units
		./units
