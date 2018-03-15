##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## Makefile
##

all:
	cat src/main.py > 108trigo
	chmod +x 108trigo

clean:
	rm -rf file

fclean: clean
	rm -rf 108trigo

re: 	fclean all
