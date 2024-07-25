#include <X11/Xlib.h>
#include <X11/extensions/Xfixes.h>
#include <X11/Xcursor/Xcursor.h>
#include <X11/cursorfont.h>
#include <iostream>
#include <unordered_map>
#include <thread>  
#include <chrono>

int findHandCursorSerial();

int main() {
    Display *display;
    int screen;

    display = XOpenDisplay(NULL);
    if (display == NULL) {
        std::cerr << "Cannot open display" << std::endl;
        return 1;
    }

    while(True){
        XFixesCursorImage *cursorImage = XFixesGetCursorImage(display);
        if (cursorImage == NULL) {
            std::cerr << "Failed to get cursor image" << std::endl;
            XCloseDisplay(display);
            return 1;
        }
        const char* cursorName = cursorImage->name;
        std::cout << cursorName << std::endl;
        unsigned long cursorShape = cursorImage->cursor_serial;
        std::cout << cursorShape;
            if(cursorShape == 0){
                std::cout << "There is a button\n";
            }
            else{
                std::cout << "There is no button\n";
            }
                XFree(cursorImage);
                std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    XCloseDisplay(display);

    return 0;
}

int findHandCursorSerial(){


}