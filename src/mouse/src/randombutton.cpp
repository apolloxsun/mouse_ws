#define RAYGUI_IMPLEMENTATION
#include "raylib.h"
#include "../include/raygui.h"
#include <iostream>
#include <random>
#include "ros/ros.h"
#define buttonX 200
#define buttonY 200

float randomCoordinateX(int cW);
float randomCoordinateY(int cH);


int main()
{
    srand((unsigned) time(NULL));
    InitWindow(2560, 1660, "Random Button Generator");

    int screenWidth = GetMonitorWidth(GetCurrentMonitor());
    int screenHeight = GetMonitorHeight(GetCurrentMonitor());
    SetWindowSize(screenWidth, screenHeight);

    SetTargetFPS(60);
    GuiSetStyle(DEFAULT, TEXT_SIZE, 30);
    GuiSetIconScale(3);
    float x,y;

    int button = 0;

    while (!WindowShouldClose())
    {
        int currentWidth = GetScreenWidth();
        int currentHeight = GetScreenHeight();

        BeginDrawing();
        ClearBackground(DARKGRAY);

        
    
        if(button == 0) {
            button = 1 + (rand() % 4);
            x = randomCoordinateX(currentWidth);
            y = randomCoordinateY(currentHeight);
        }
        else if(button == 1){
            if(GuiButton((Rectangle){x,y, 150,80}, "button")){
            button = 0;}}
        else if(button == 2){
            if(GuiButton((Rectangle){x,y, 55,55}, "#02#")){
            button = 0;}}
        else if(button == 3){
            if(GuiButton((Rectangle){x,y, 50,50}, "#128#")){
            button = 0;}}
        else if(button == 4){
            if(GuiButton((Rectangle){x,y, 150,60}, "#100# Tab")){
            button = 0;}}
        else{break;}

        EndDrawing();
    }

    CloseWindow();
    return 0;
}

float randomCoordinateX(int cW){
    float x;
    x = 1 + (rand() % (cW - buttonX));
    return x;
}

float randomCoordinateY(int cH){
    float y;
    y = 1 + (rand() % (cH - buttonY));
    return y;
}