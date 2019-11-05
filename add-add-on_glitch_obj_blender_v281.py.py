bl_info = {
    'name' : 'Glitch',
    'author' : 'Hans Willem Gijzel',
    'version' : (0, 1),
    'blender' : (2, 81, 0  ),
    'location' : 'View 3D > Tools > Glitch',
    'description' : 'Glitches meshes',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'Glitch'
    }


#imports
import bpy
import random

#setup some global scene properties
class glitchPropertyGroup(bpy.types.PropertyGroup):
    bpy.types.Scene.prop_shuffleVertices = bpy.props.FloatProperty(min=0, max=1, name='Shuffle Verts', default=.1)
    bpy.types.Scene.prop_randomNumbers = bpy.props.FloatProperty(min=0, max=1, name='Random Numbers', default=.1)
    bpy.types.Scene.prop_removeFaces = bpy.props.FloatProperty(min=0, max=1, name='Remove Faces', default=.1)

#the obj file is saved to and loaded from the temp folder
exportedFile = bpy.app.tempdir + 'modelExport.obj'
glitchedFile = bpy.app.tempdir + 'modelGlitched.obj'

#export obj
def main_exportOBJ():
    bpy.ops.export_scene.obj(filepath = exportedFile, use_materials = False)

#import OBJ
def main_importOBJ():
    #delete all objects in scene
    bpy.ops.object.select_all(action = 'SELECT')
    bpy.ops.object.delete(use_global = False)

    #open glitched file
    bpy.ops.import_scene.obj(filepath = glitchedFile)

#change numbers in obj file
def main_randomNumbers(n):
    if n != 0:
        main_exportOBJ()
        f = open(exportedFile)
        fn = open(glitchedFile, 'w')
        for l in f:
            if l[0] == 'v':
                if random.random() < n:
                    rn1 = random.choice(range(10))
                    rn2 = random.choice(range(10))
                    l = [str(rn1) if i == str(rn2) else i for i in l]

            fn.write(''.join(l))

        f.close()
        fn.close()
        main_importOBJ()
    else:
        pass

#shuffle vertex lines
def main_shuffleVertices(n):
    if n != 0:
        main_exportOBJ()
        f1 = open(exportedFile)
        f2 = open(exportedFile)
        fn = open(glitchedFile, 'w')

        a = [l for l in f1 if l[0:2] == 'v ']
        random.shuffle(a)

        for l in f2:
            if l[0:2] == 'v ':
                if random.random() < n:
                    l = a[random.choice(range(len(a)))]

            fn.write(''.join(l))

        f1.close()
        f2.close()
        fn.close()
        main_importOBJ()
    else:
        pass

#remove faces
def main_removeFaces(n):
    if n != 0:
        main_exportOBJ()
        f = open(exportedFile)
        fn = open(glitchedFile, 'w')

        for l in f:
            if l[0] == 'f':
                if random.random() < n:
                    l = ''

            fn.write(''.join(l))

        f.close()
        fn.close()
        main_importOBJ()
    else:
        pass

#not used right now
def flatShadingAllObjects():
    for i in bpy.data.objects:
        if i.type == 'MESH':
            for p in i.data.polygons:
                p.use_smooth = False

def main_glitch(n1, n2, n3):
    main_shuffleVertices(n1)
    main_randomNumbers(n2)
    main_removeFaces(n3)

# --------------------------------------------------------------------------------------------------------------------------------------------

#panel class
class GLITCHPANEL_PT_Panel(bpy.types.Panel):
    #panel attributes
    """Tooltip"""
    bl_label = 'Glitch'
    bl_idname = 'GLITCH_PT_Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Glitch'
    
    #draw loop
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        col.prop(context.scene, 'prop_shuffleVertices', slider=True)
        col.prop(context.scene, 'prop_randomNumbers', slider=True)
        col.prop(context.scene, 'prop_removeFaces', slider=True)
        col.operator('script.glitch', text='Glitch!')
         
#operator class
class GLITCH_OT_Operator(bpy.types.Operator):
    #operator attributes
    """Tooltip"""
    bl_label = 'Glitch'
    bl_idname = 'script.glitch'
    
    #poll - if the poll function returns False, the button will be greyed out
    @classmethod
    def poll(cls, context):
        return 2 > 1
    
    #execute
    def execute(self, context):
        n1 = bpy.context.scene.prop_shuffleVertices
        n2 = bpy.context.scene.prop_randomNumbers
        n3 = bpy.context.scene.prop_removeFaces
        main_glitch(n1, n2, n3)
        return {'FINISHED'}
        
#registration
classes = (
    GLITCHPANEL_PT_Panel,
    GLITCH_OT_Operator,
    glitchPropertyGroup
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


#enable to test the addon by running this script
if __name__ == '__main__':
    register()
