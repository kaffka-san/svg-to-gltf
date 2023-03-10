bl_info = {
    "name" : "Convert SVG to GLTF",
    "blender": (2, 80, 0),
    "category" : "Export",
}
import bpy
import math
import os


class ExportSVGtoGLTFPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Export SVG to GLTF"
    bl_idname = "OBJECT_PT_export_svg_gltf"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Convert SVG to GLTF"

    def draw(self, context):
        layout = self.layout

        # Input directory path parameter
        layout.prop(context.scene, "svg_input_dir", text="Input Directory")

        # Output directory path parameter
        layout.prop(context.scene, "gltf_output_dir", text="Output Directory")

        # Export button
        layout.operator("object.export_svg_to_gltf", text="Export")

class OBJECT_OT_export_svg_to_gltf(bpy.types.Operator):
    """Operator which exports all SVG files in the input directory to GLTF files in the output directory"""
    bl_idname = "object.export_svg_to_gltf"
    bl_label = "Export SVG to GLTF"

    def execute(self, context):
       
              # Delete all objects
        for obj in bpy.context.scene.objects:
            bpy.data.objects.remove(obj, do_unlink=True)

        # Delete all collections except the default one
        for coll in bpy.data.collections:
            if coll.name != bpy.context.scene.collection.name:
                bpy.data.collections.remove(coll, do_unlink=True)
        
        
        input_dir = bpy.path.abspath(context.scene.svg_input_dir)
        output_dir = bpy.path.abspath(context.scene.gltf_output_dir)

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        

                    
        # Loop through each SVG file and import it
        svg_files = [f for f in os.listdir(input_dir) if f.endswith(".svg")]

        for svg_file in svg_files:
            # Set the filepath to the SVG file
            filepath = os.path.join(input_dir, svg_file)
            
            # Import the SVG file
            bpy.ops.import_curve.svg(filepath=filepath)
      
            bpy.ops.object.select_all(action='DESELECT') 
        # Join all curves into one object in the same Collection 
        for Coll in bpy.data.collections:
                for curve in Coll.objects:
                   # bpy.ops.object.select_all(action='DESELECT') 
                    curve.select_set(True)
                    bpy.context.view_layer.objects.active = curve
       
                bpy.ops.object.join()
                bpy.ops.object.select_all(action='DESELECT')

          
        for obj in bpy.context.scene.objects:
            
            svg_object = obj
            svg_object.select_set(True)

            svg_object.scale = (40,40,40)

            bpy.context.view_layer.objects.active = svg_object
           
            # Select the object and set the pivot point to the center of mass
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
          
            # Rotate object
            svg_object.rotation_euler.x = math.radians(90)
            # Set extrudion, bevel and resolution
            svg_object.data.extrude = 0.01
            svg_object.data.bevel_depth = 0.0015
            svg_object.data.resolution_u = 24
            svg_object.data.bevel_resolution = 8
            # Set the location of the object to (0,0,0)
            svg_object.location = (0,0,0)
           
            
            
            bpy.ops.object.select_all(action='DESELECT')
            svg_object.select_set(True)
            # Convert curve to mesh
            bpy.ops.object.convert(target='MESH')
            # Reset all transforms
            bpy.ops.object.transform_apply( location=True, rotation=True, scale=True )
            # Create simple UV map
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.smart_project()
            bpy.ops.object.mode_set(mode='OBJECT')
            #filename = svg_object.name 
            output_path = os.path.join(output_dir + svg_object.name )

            svg_object.select_set(True)
            # export to dir
            bpy.ops.export_scene.gltf(filepath=output_path, use_selection=True, export_format = 'GLTF_EMBEDDED')
            bpy.ops.object.select_all(action='DESELECT')
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ExportSVGtoGLTFPanel)
    bpy.utils.register_class(OBJECT_OT_export_svg_to_gltf)
    bpy.types.Scene.svg_input_dir = bpy.props.StringProperty(subtype='DIR_PATH')
    bpy.types.Scene.gltf_output_dir = bpy.props.StringProperty(subtype='DIR_PATH')

def unregister():
    bpy.utils.unregister_class(ExportSVGtoGLTFPanel)
    bpy.utils.unregister_class(OBJECT_OT_export_svg_to_gltf)
    del bpy.types.Scene.svg_input_dir
    del bpy.types.Scene.gltf_output_dir





