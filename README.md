# Glitch an OBJ file in Blender

![img](https://github.com/hanswillem/Blender_Add-on_Glitch_OBJ/blob/master/example_img.png)

Download the add-on from this repo, install it, create a scene with at least one mesh object, and click on *Glitch OBJ*. 
The Blender 2.8 version has some sliders you can tweak to change the behaviour a bit.

That's it.

![img](https://github.com/hanswillem/Blender_Add-on_Glitch_OBJ/blob/master/messing_with_obj.png)

The add-on works by saving the scene as an .obj file and then corrupting the data. It shuffles lines around, replaces random numbers with random other numbers and some other stuff. When all that's done, it imports the - by then corrupted - .obj file again.

I used [this](http://www.srcxor.org/blog/3d-glitching/) as a guide.
