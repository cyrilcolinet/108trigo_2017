/*
** EPITECH PROJECT, 2018
** 108trigo_2017
** File description:
** 108trigo tests (COSINUS)
*/

# include "units.h"

Test(trigo, cos_example, .init = redirect_std)
{
	system("./108trigo COS 4 5 9 3 3 5 0 1 9");
	cr_stdout_match_str("0.70\t-0.43\t-1.94"\
						"-0.16\t0.67\t-1.23"\
						"-0.06\t-0.15\t0.07");
}
