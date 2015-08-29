#!/usr/bin/env python

from gimpfu import *
from os.path import join

def process_HWRM_maps(image, __unused_drawable):
    
    type = "RGBA"
    mode = 0

    HWMaps = gimp.Image(image.width, image.height, RGB)
    
    for layer in image.layers:
        if "_GLOW.dds" in layer.name:
            glowLayer = layer
            
            redGLOW, greenGLOW, blueGLOW, alphaGLOW = pdb.plug_in_decompose(image, glowLayer, type, mode)
            
            #REFL map
            reflImage = pdb.gimp_image_duplicate(redGLOW)                     #Copy layer
            pdb.gimp_image_convert_rgb(reflImage)                               #Make sure it's in RGB mode
            reflLayer = reflImage.layers[0]                                     #Select the layer
            pdb.gimp_selection_all(reflImage)                                   #Select all of it
            pdb.gimp_edit_copy (reflLayer)                                      #Copy the layer
            newReflLayer = pdb.gimp_layer_new(HWMaps, HWMaps.width, 
                HWMaps.height, 1, "REFL", 100, 0)                               #New layer
            HWMaps.add_layer(newReflLayer)                                      #Add the newly created layer
            pdb.gimp_image_set_active_layer(HWMaps, newReflLayer)               #Make it active
            pdb.gimp_selection_all(HWMaps)                                      #Select everything
            selection = pdb.gimp_edit_paste(newReflLayer, 0)                    #Paste the layer
            pdb.gimp_floating_sel_anchor(selection)                             #Assign the pasted stuff to the layer
            
            #GLOW map
            glowImage = pdb.gimp_image_duplicate(greenGLOW)                     #Copy layer
            pdb.gimp_image_convert_rgb(glowImage)                               #Make sure it's in RGB mode
            glowLayer = glowImage.layers[0]                                     #Select the layer
            pdb.gimp_selection_all(glowImage)                                   #Select all of it
            pdb.gimp_edit_copy (glowLayer)                                      #Copy the layer
            newGlowLayer = pdb.gimp_layer_new(HWMaps, HWMaps.width, 
                HWMaps.height, 1, "GLOW", 100, 0)                               #New layer
            HWMaps.add_layer(newGlowLayer)                                      #Add the newly created layer
            pdb.gimp_image_set_active_layer(HWMaps, newGlowLayer)               #Make it active
            pdb.gimp_selection_all(HWMaps)                                      #Select everything
            selection = pdb.gimp_edit_paste(newGlowLayer, 0)                    #Paste the layer
            pdb.gimp_floating_sel_anchor(selection)                             #Assign the pasted stuff to the layer
            
            #SPEC map
            specImage = pdb.gimp_image_duplicate(blueGLOW)                       #Copy layer
            pdb.gimp_image_convert_rgb(specImage)                               #Make sure it's in RGB mode
            specLayer = specImage.layers[0]                                     #Select the layer
            pdb.gimp_selection_all(specImage)                                   #Select all of it
            pdb.gimp_edit_copy (specLayer)                                      #Copy the layer
            newSpecLayer = pdb.gimp_layer_new(HWMaps, HWMaps.width, 
                HWMaps.height, 1, "SPEC", 100, 0)                               #New layer
            HWMaps.add_layer(newSpecLayer)                                      #Add the newly created layer
            pdb.gimp_image_set_active_layer(HWMaps, newSpecLayer)               #Make it active
            pdb.gimp_selection_all(HWMaps)                                      #Select everything
            selection = pdb.gimp_edit_paste(newSpecLayer, 0)                    #Paste the layer
            pdb.gimp_floating_sel_anchor(selection)                             #Assign the pasted stuff to the layer
            
            #Cleanup Images
            pdb.gimp_image_delete(redGLOW)
            pdb.gimp_image_delete(greenGLOW)
            pdb.gimp_image_delete(blueGLOW)
            pdb.gimp_image_delete(alphaGLOW)
            pdb.gimp_image_delete(reflImage)
            pdb.gimp_image_delete(glowImage)
            pdb.gimp_image_delete(specImage)
            
        elif "_TEAM.dds" in layer.name:
            teamLayer = layer
            
            redTEAM, greenTEAM, blueTEAM, alphaTEAM = pdb.plug_in_decompose(image, teamLayer, type, mode)
            
            #TEAM map
            teamImage = pdb.gimp_image_duplicate(redTEAM)                       #Copy layer
            pdb.gimp_image_convert_rgb(teamImage)                               #Make sure it's in RGB mode
            teamLayer = teamImage.layers[0]                                     #Select the layer
            pdb.gimp_selection_all(teamImage)                                   #Select all of it
            pdb.gimp_invert(teamLayer)                                          #Invert color
            pdb.plug_in_colortoalpha(teamImage, teamLayer, (0,0,0))             #Remove the black
            pdb.gimp_edit_copy (teamLayer)                                      #Copy the layer
            newTeamLayer = pdb.gimp_layer_new(HWMaps, HWMaps.width, 
                HWMaps.height, 1, "TEAM", 100, 0)                               #New layer
            HWMaps.add_layer(newTeamLayer)                                      #Add the newly created layer
            pdb.gimp_image_set_active_layer(HWMaps, newTeamLayer)               #Make it active
            pdb.gimp_selection_all(HWMaps)                                      #Select everything
            selection = pdb.gimp_edit_paste(newTeamLayer, 0)                    #Paste the layer
            pdb.gimp_floating_sel_anchor(selection)                             #Assign the pasted stuff to the layer
            
            #STRP map
            strpImage = pdb.gimp_image_duplicate(greenTEAM)                       #Copy layer
            pdb.gimp_image_convert_rgb(strpImage)                               #Make sure it's in RGB mode
            strpLayer = strpImage.layers[0]                                     #Select the layer
            pdb.gimp_selection_all(strpImage)                                   #Select all of it
            pdb.gimp_invert(strpLayer)                                          #Invert color
            pdb.plug_in_colortoalpha(strpImage, strpLayer, (0,0,0))             #Remove the black
            pdb.gimp_edit_copy (strpLayer)                                      #Copy the layer
            newStrpLayer = pdb.gimp_layer_new(HWMaps, HWMaps.width, 
                HWMaps.height, 1, "STRP", 100, 0)                               #New layer
            HWMaps.add_layer(newStrpLayer)                                      #Add the newly created layer
            pdb.gimp_image_set_active_layer(HWMaps, newStrpLayer)               #Make it active
            pdb.gimp_selection_all(HWMaps)                                      #Select everything
            selection = pdb.gimp_edit_paste(newStrpLayer, 0)                    #Paste the layer
            pdb.gimp_floating_sel_anchor(selection)                             #Assign the pasted stuff to the layer
            
            #PAIN map
            painImage = pdb.gimp_image_duplicate(blueTEAM)                      #Copy layer
            pdb.gimp_image_convert_rgb(painImage)                               #Make sure it's in RGB mode
            painLayer = painImage.layers[0]                                     #Select the layer
            pdb.gimp_selection_all(painImage)                                   #Select all of it
            pdb.gimp_invert(painLayer)                                          #Invert color
            pdb.plug_in_colortoalpha(painImage, painLayer, (0,0,0))             #Remove the black
            pdb.gimp_edit_copy (painLayer)                                      #Copy the layer
            newPainLayer = pdb.gimp_layer_new(HWMaps, HWMaps.width, 
                HWMaps.height, 1, "PAIN", 100, 0)                               #New layer
            HWMaps.add_layer(newPainLayer)                                      #Add the newly created layer
            pdb.gimp_image_set_active_layer(HWMaps, newPainLayer)               #Make it active
            pdb.gimp_selection_all(HWMaps)                                      #Select everything
            selection = pdb.gimp_edit_paste(newPainLayer, 0)                    #Paste the layer
            pdb.gimp_floating_sel_anchor(selection)                             #Assign the pasted stuff to the layer
        
            #Cleanup Images
            pdb.gimp_image_delete(redTEAM)
            pdb.gimp_image_delete(greenTEAM)
            pdb.gimp_image_delete(blueTEAM)
            pdb.gimp_image_delete(alphaTEAM)
            pdb.gimp_image_delete(teamImage)
            pdb.gimp_image_delete(strpImage)
            pdb.gimp_image_delete(painImage)
    
    gimp.Display(HWMaps)


register(
    "python_fu_process_HWRM_maps",
    "Save all layers into separate files",
    "Save all layers into separate files",
    "Xercodo",
    "Xercodo",
    "2015",
    "<Image>/Filters/Map/Process HWRM Maps...",
    "*",
    [
        #(PF_DIRNAME, "directory", "Directory to put the images in", "/"),
        #(PF_STRING, "name_pattern", "Base file name. Output will be name__layer.tga", ""),
    ],
    [],
    process_HWRM_maps
)

main()