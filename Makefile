##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## Makefile
##

NAME 	=	108trigo

CC 		= 	gcc

TESTS 	=	tests/108trigo_basics_tests.c 			\
			tests/108trigo_cos_tests.c 				\
			tests/108trigo_utils.c

CFLAGS 	= 	-Wall -Wextra -I./include

LDFLAGS	=	-lcriterion

OBJ 	= 	$(TESTS:.c=.o)

all:
		cd src/
		echo -e "#!/bin/sh\npython3 main.py" > src/project
		chmod +x src/project
		echo -e "#!/bin/sh\n./src/project" > $(NAME)
		chmod +x $(NAME)

clean:
		rm -rf src/project
		rm -rf $(OBJ)

fclean: clean
		chmod -x src/main.py
		rm -rf $(NAME)
		rm -rf units

re: 	fclean all

tests_run: fclean $(OBJ)
		$(CC) $(CFLAGS) $(LDFLAGS) $(OBJ) -o units
		./units
