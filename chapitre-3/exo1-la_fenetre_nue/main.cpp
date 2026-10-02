#include <iostream>
#include "NKWindow/NkWindow.h"

using namespace nkentseu;
int main() {
    NkWindowConfig config;
    config.title  = "Fenetre";
    config.width  = 1280;
    config.height = 720;

    NkWindow fenetre(config);
    if (!fenetre.IsValid()) {
        return 1;
    }

    while (fenetre.IsOpen()) {
        NkEvents().PollEvents();
    }
}
