import io
import os
from pathlib import Path
from getters.input_getters import *




print("Web Automation v1.0 ")
print("Created by Pouya Moazzezi")
print("==========================================================")



project_path = Path(input("Where do you want to create the projects? [Default: Here]: "))
parent_directory = Path(project_path).parent   

while not (project_path.is_dir()): #if it doesn't Exist Creates it.

  if not(parent_directory.is_dir()):
    print("Please enter a valid directory")
    project_path = Path(input("Where do you want to create the projects? [Default: Here]: "))
  else: #if Parent Directory Exists
    make_folder_confirmation = get_confirmation_input(f"Do you want to make the folder: \"{project_path}\" y/n [y]: ", input, "y")
    Path.mkdir(project_path)


#==================================================== HTML ====================================================
html_name = get_file_name_input("Type a name for your html file name [index]: ", input, "index")

html_extention = get_file_extention_input("Your preferable html file extention (htm | html) [html]: ",
input,
["htm", "html"],
"html")


html_title_name = input("Type a title for your page [Document]: ")
if html_title_name == "":
  html_title_name = "Document"


#==================================================== Styles ====================================================

css_file_name = get_file_name_input("Type a name for your stylesheet file [style]: ", input, "style")

put_css_in_folder = get_confirmation_input("You want to put ccs files in folder? y/n [n]: ", input, "n")


style_folder_name = ""
if put_css_in_folder == "y":
  style_folder_name = get_folder_name_input("Type the name for your styles folder [css]: ", input, "css")


css_extention = get_file_extention_input("Type the name of stylesheet file extention (css | less | sass | scss) [css]: ",
input,
["css", "less", "sass", "scss"],
"css")

#==================================================== Styles ====================================================

js_name = get_file_name_input("Type a name for your script file name [script]: ", input, "script")

put_js_in_folder = get_confirmation_input("You want to put js file in a folder? y/n [n]: ", input, "n")

js_folder_name = "" 
if put_js_in_folder == "y":
  js_folder_name = get_folder_name_input("Type the name for your JavaScript folder [js]: ", input, "js")





if put_css_in_folder == "y":
  os.mkdir(style_folder_name) #if the variable "put_css_in_folder" is "y", it becomes like "style/", so it puts it into the folder


stylesheet_file = css_file_name + "." + css_extention
stylesheet_path = os.path.join(style_folder_name, stylesheet_file)
with open(os.path.join(project_path, stylesheet_path) , "w") as css:
    css.write('''*,
*::after,
*::before {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}''')


if put_js_in_folder  == "y":
  os.mkdir(js_folder_name)

js_file = js_name + ".js"
js_path = os.path.join(js_folder_name, js_file)
with open(os.path.join(project_path, js_path), "w") as js:
    js.write("")


html_file = html_name + ("." + html_extention)
html_path = os.path.join(html_file)
with open(os.path.join(project_path, html_path), "w") as html:
    html.write(f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="{stylesheet_path}" />
    <title>{html_title_name}</title>
  </head>
  <body>
    <script src="{js_path}"></script>
  </body>
</html>
''') # Replaces the title with given name, so as js and stylesheet file path

input("\nFiles were successfully created!\nPress ENTER to close the program")



#TODO: add a confirmation at the end
#TODO: add a "code <PATH>" via cmd
#TODO: learn about os in python
#TODO: Check if files are already there. 
#TODO: add an auto builder using default parameters
#TODO: Obey the Naming Conventions in Files and Folders

#================================================
#TODO: add an optional PATH request == DONE
#TODO: add validation via os.path.exists(path) == DONE
#TODO: add a html Title specifier == DONE