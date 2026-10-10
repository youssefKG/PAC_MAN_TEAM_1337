# the number of times the game loop runs per second is known as frame rate


## About Game loop
In this version, we update lag at the beginning of the frame based on how much real time has passed.
We then perform a series of calls to update until we've caught up, and only then do we render the scene.
Sometimes, the call to render may happen in between two calls to update,
potentially causing an object to appear in the previous spot during an animation and not show any progression.
But by passing lag / MS_PER_UPDATE in to render,
we are telling the render function exactly how far in between the two updates we are,
and the renderer can guess the position the object should be in based on interpolation.
This method presents its own problems as well! For example,
if our object is going to collide with something in the next frame,
but our render function doesn't know that because the next update hasn't run yet,
it may guess that the object is somewhere where it shouldn't be.

Professional level game loops are much more complicated and must account for many other factors, such as GPUs and multithreading, and even the different ways that user input is processed across different devices.
The details of every game's game loop vary greatly, but the core pattern is always there- process user input, update the scene, and render the scene for the user to see.
