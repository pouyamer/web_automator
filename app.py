import io
import os

print("Web Automation v0.5.0 ")
print("Created by Pouya Moazzezi")
print("==========================================================")

project_path = input("\nWhere do you want to create the projects? [Default: Here]\t")
parent_directory = os.path.dirname(project_path)

if project_path.strip() == "":
  project_path = ""

while not (os.path.isdir(project_path) or project_path == ""): #if it doesn't Exist Creates it.
  if project_path.strip() == "":
    project_path = ""
  if not(os.path.isdir(parent_directory)):
    print("Please enter a valid directory")
    project_path = input("\nWhere do you want to create the projects? [Default: Here]\t")
  else: #if Parent Directory Exists
    make_folder_confirmation = input("Do you want to make the folder: " + project_path + " y/n [y]\t")
    if make_folder_confirmation.strip() == "":
      make_folder_confirmation = "y"
    while not (make_folder_confirmation == "y" or make_folder_confirmation == "n"):
      print("Didn't catch that.")
      make_folder_confirmation = input("Do you want to make the folder: " + project_path + " y/n [y]\t")

    os.mkdir(project_path)


#==================================================== HTML ====================================================
html_name = input("\nType a name for your html file name [index]\t")
if html_name.strip() == "":
  html_name = "index"

html_extention = input("\nYour preferable html file extention (htm | html) [html]\t")
if html_extention.strip() == "":
  html_extention = "html"

while (html_extention != "htm" and html_extention != "html"):
  print("Didn't catch that.")
  html_extention = input("\nYour preferable html file extention (htm | html) [html]\t")
  if html_extention.strip() == "":
    html_extention = "html"

html_title_name = input("\nType a title for your page [Document]\t")
if html_title_name.strip() == "":
  html_title_name = "Document"


#==================================================== Styles ====================================================

css_file_name = input("\nType a name for your stylesheet file [style]\t")
if css_file_name.strip() == "":
  css_file_name = "style"

put_css_in_folder = input("\nYou want to put ccs files in folder? y/n [n]\t")
if put_css_in_folder.strip() == "":
  put_css_in_folder = "n"

while not(put_css_in_folder == "y" or put_css_in_folder == "n"):
  print("Didn't catch that.")
  put_css_in_folder = input("\nYou want to put stylesheet file in a folder? y/n [n]\t")
  if put_css_in_folder.strip() == "":
    put_css_in_folder = "n"


style_folder_name = ""
if put_css_in_folder == "y":
  style_folder_name = input("\nType the name for your styles folder [css]\t")
  if style_folder_name.strip() == "" :
    style_folder_name = "css"


css_extention = input("\nType the name of stylesheet file extention (css | less | sass | scss) [css]\t")
if css_extention.strip() == "":
  css_extention = "css"

while not(css_extention == "css" or css_extention == "scss" or css_extention == "sass" or css_extention == "less"):
  css_extention = input("\nType the name of stylesheet file extention (css | less | sass | scss) [css]\t")
  if css_extention.strip() == "":
    css_extention = "css"


#==================================================== Styles ====================================================

js_name = input("\nType a name for your script file name [script]\t")
if js_name.strip() == "":
  js_name = "script"

put_js_in_folder = input("\nYou want to put js file in a folder? y/n [n]\t")
if put_js_in_folder.strip() == "":
  put_js_in_folder = "n"

js_folder_name = "" 
if put_js_in_folder.strip() == "y":
  js_folder_name = input("\nType the name for your JavaScript folder [js]\t")
  if js_folder_name.strip() == "" :
    js_folder_name = "js"




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
    html.write('''<!DOCTYPE html>
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
'''.replace("{html_title_name}", html_title_name)
  .replace("{stylesheet_path}", stylesheet_path)
  .replace("{js_path}", js_path)) # Replaces the title with given name, so as js and stylesheet file path

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