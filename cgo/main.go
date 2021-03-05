package main

/*
#cgo LDFLAGS: -ldl
#include <dlfcn.h>
#include <library.hpp>
typedef int (*someFunc) (const int s);

int bridge_someFunc(someFunc f, const int s) {
    return f(s);
}
*/
import "C"

func main() {
	libpath := C.CString("./libProject.so")
	imglib := C.dlopen(libpath, C.RTLD_LAZY)
	fp := C.dlsym(imglib, C.CString("print_value"))
	C.bridge_someFunc(C.someFunc(fp), C.int(10000))
	// fmt.Print(imghandle)
}
