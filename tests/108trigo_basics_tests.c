/*
** EPITECH PROJECT, 2018
** 108trigo_2017
** File description:
** basics tests
*/

# include "units.h"

Test(trigo, make_re, .init = redirect_std)
{
	int res = 0;

	res = system("make re");
	cr_assert_eq(res, 0);
}

Test(trigo, bad_usage, .init = redirect_std)
{
	system("./108trigo");
	cr_stderr_match_str("Missing arguments.\nUsage: ./108trigo fun a0 a1 a2 ...");
}

Test(trigo, display_help, .init = redirect_std)
{
	system("./108trigo --help");
	cr_stdout_match_str("USAGE"\
						"\t./108trigo fun a0 a1 a2....\n"\
						"DESCRIPTION"\
						"\tfun\tfunction to be applied, among at least \"EXP\", \"COS\", \"SIN\", \"COSH\" and \"SINH\""\
						"\tai\tcoeficients of the matrix");
}

Test(trigo, invalid_arguments_number, .init = redirect_std)
{
	system("./108trigo COS 3 4");
	cr_stderr_match_str("Missing arguments.\nUsage: ./108trigo fun a0 a1 a2 ...");
}
