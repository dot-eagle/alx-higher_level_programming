/* ##include <python.h> */
#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the Python struct
 *
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	unsigned int b;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (b = 0; b < PyList_Size(p); b++)
		printf("Element %d: %s\n", b, Py_TYPE(PyList_GetItem(p, b))->tp_name);
}


