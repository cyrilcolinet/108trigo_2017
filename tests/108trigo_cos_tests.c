/*
** EPITECH PROJECT, 2018
** 108trigo_2017
** File description:
** 108trigo tests (COSINUS)
*/

# include <criterion/criterion.h>
# include <criterion/redirect.h>
# include <stdlib.h>

void redirect_std(void)
{
	cr_redirect_stderr();
	cr_redirect_stdout();
}

Test(trigo, example_cos, .init = redirect_std)
{
	int res = system("make re");

	cr_assert_eq(res, 0);
}
