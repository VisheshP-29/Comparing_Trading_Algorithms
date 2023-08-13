#include <iostream>
#include <Python.h>

int main() {
    std::cout << "Comparing Trading Algorithms Personal Project" << std::endl;

    /*
     * Calling python code: Option 2
     * Using system calls
     * Current Status: working as intedned with no errors
     */
    system("python3 ../src/data_processing/DataProcessing.py");

    /*
     * Calling python code: Option 2
     * Using Python headers
     * Current Status: Got linker to link all necessary header files but getting segfault with PyModule_GetDict, currently debugging problem
     */
    /*
    Py_Initialize();
    setenv("PYTHONPATH","./data_processing",1);
    PyObject* pName = PyBytes_FromString("DataProcessing");
    PyObject* pModule = PyImport_Import(pName);
    PyObject* pDict = PyModule_GetDict(pModule);
    return 1;
    PyObject* pFunc = PyDict_GetItemString(pModule, (char*)"test");
    PyObject* pValue;
    PyObject* pResult;
    if (PyCallable_Check(pFunc))
    {
        pValue = Py_BuildValue("(i)", 5);
        PyErr_Print();
        printf("Let's give this a shot!\n");
        pResult=PyObject_CallObject(pFunc,pValue);
        PyErr_Print();
    } else 
    {
        PyErr_Print();
    }
    printf("Result is %ld\n",PyLong_AsLong(pResult));
    Py_DECREF(pValue);
    Py_DECREF(pModule);
    Py_DECREF(pName);
    Py_Finalize();
    */

    return 1;
}