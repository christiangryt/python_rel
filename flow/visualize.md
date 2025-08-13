Using curses, print paths as they are solved. Along with constraints and iteration number.     

A cool visual that at best makes it slightly slower.

# Plan

Windows: Each flow gets their own window. Make a function that can write internally in these windows and display.  

Place these windows (hopefully dynamically). Atleast make it so each window is visible. And that there is space for the constriants to be showed off.

Constraints could also be its own window.

## Colors

Make color pairs equal to number of flows.  

I.e. curses.init_color({nr}, r, g, b)   

> In my terminal i can have 256 color pairs, more than enough
