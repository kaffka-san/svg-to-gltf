# Blender 3D Icon Creator Script

This script allows you to create 3D icons from SVG files with depth and bevel, UV mapping, and the origin at the center. It then exports the icon as a GLTF file.
This script was created with the help of Chat GPT, a large language model trained by OpenAI.
## Requirements
Blender version 2.8 or higher
Python 3.7 or higher

## Installation
To install an add-on in Blender, follow these steps:

1. Download the add-on as a .zip file or .py file from a GitHub.
2. Open Blender and go to "Edit" > "Preferences".
3.  In the Preferences window, select the "Add-ons" tab.
4. Click on the "Install" button at the top right corner of the window.
5. Navigate to the location of the downloaded add-on file and select it.
6. Click on the "Install Add-on" button.

Once the add-on is installed, it will be listed in the Add-ons tab. You can enable or disable the add-on by clicking on the checkbox next to its name.

## Updating an Add-On
If a new version of the add-on is available, follow these steps to update it:

1. Download the latest version of the add-on from the source.
2. Open Blender and go to "Edit" > "Preferences".
3. In the Preferences window, select the "Add-ons" tab.
4. Find the add-on you want to update and click on the "Remove" button to uninstall it.
5. Follow the steps above to install the new version of the add-on.

## Usage
1. Open Blender and go to the "Object Properties" panel sidebar. Just press "N" shortcut
2. Click on the "Convert SVG to GLTF" tab to open the panel.
3. Enter the input directory where your SVG files are located.
4. Enter the output directory where you want to save your GLTF files.
5. Click on the "Export" button to run the script.

The script will automatically 
import the SVG files from the input directory 
create 3d mesh with the bevel, uv map, 
origin in the center of the geometry, 
paced it in the center, 
apllied all transform and then export them as GLTF files to the output directory.

## YouTube tutorial 
Short  video   witch explains  how to install and use plug-in [ YouTube link](https://youtu.be/Ulq4zR8as2Q)



## License
This script is licensed under the MIT License. See the LICENSE file for details.
