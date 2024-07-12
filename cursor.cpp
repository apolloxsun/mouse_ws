/*#include <iostream>
#include <X11/Xlib.h>
#include <X11/cursorfont.h>
#include <X11/Xcursor/Xcursor.h>


int main(int argc, char **argv){

    Display *display;
    Window window;
    int screen;
    Cursor cursor;

    display = XOpenDisplay(NULL);

    cursor = XCreateFontCursor(display, XC_hand2);
    
    std::cout << "mesaj" << std::endl;

    XcursorImage *image = XcursorShapeLoadCursor(display, cursor);
    
    return 0;
}*/
#include <X11/Xlib.h>
#include <X11/extensions/Xfixes.h>
#include <X11/Xcursor/Xcursor.h>
#include <X11/cursorfont.h>
#include <iostream>
#include <unordered_map>
#include <thread>  
#include <chrono>

/*std::unordered_map<unsigned int, std::string> cursorNames = {
    {10, "arrow"},
    {11, "hand2"},
    {XC_watch, "watch"},
    {XC_xterm, "xterm"},
    // Add more cursor shapes as needed
};*/

int main() {
    Display *display;
    int screen;

    /* Open connection to X server */
    display = XOpenDisplay(NULL);
    if (display == NULL) {
        std::cerr << "Cannot open display" << std::endl;
        return 1;
    }

    screen = DefaultScreen(display);

    /* Query the current cursor image */

    
    while(True){
    XFixesCursorImage *cursorImage = XFixesGetCursorImage(display);
    if (cursorImage == NULL) {
        std::cerr << "Failed to get cursor image" << std::endl;
        XCloseDisplay(display);
        return 1;
    }
    int cursorShape = cursorImage->cursor_serial;
    std::cout << cursorShape;
    if(cursorShape == 11){
        std::cout << "There is a button\n";
    }
    else{
        std::cout << "There is no button\n";
    }
        XFree(cursorImage);
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }


    // Cleanup 

    XCloseDisplay(display);

    return 0;
}

