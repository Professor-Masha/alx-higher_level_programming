#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

     // funtions fo printing elements of the list.
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_GET_SIZE(p);
    printf("[.] bytes object info\n");

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes: ", size <= 10 ? size : 10);
    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        printf("%02hhx", PyBytes_AS_STRING(p)[i]);
        if (i + 1 < size && i + 1 < 10) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid PyFloatObject\n");
        return;
    }

    printf("[.] float object info\n");

    double value = PyFloat_AS_DOUBLE(p);
    printf("  value: %f\n", value);
}
