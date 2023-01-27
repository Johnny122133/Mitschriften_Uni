# Mitschriften_Uni

## Rules
1. Read the README
2. pull before push!! (use VS-Code/source control)  
3. don't edit the settings_json.tex file
4. Read Rule 1.
5. Reconsider all your life choices (imediatly and thoroughly)

## Structure
+ ExamplesV2... has examples for LaTex commands.  
+ KnowledgeBase.pdf... some chaotig LaTex description.  
+ No text in main file. Write text in .tex files and import them where needed (\import{folder/name.tex}  
+ No blanks or strange characters in file names. **Name files meaningfully!**  
    + Folders: as folder names imply.

> *at some point all of the subjects will be added into one main .tex file. For the moment the subjects are seperated.*

## Git
### new
+ select empty folder/rightclick /git bash here / git clone + link (git repository, link) (use rightclick einfügen)

### in VS-Code:
+ button commit/commit message in top line/checkmark in right topp corner
+ sync

### in git terminal
+ git add --all (only when tere was a new file created)
+ git commit -am "commit message"
+ git pull
+ git push

## Setup  
*Download git for git usage. The rest is for writing LaTex in VS-Code.*  
instead of VS-Code LaTex can also be edited online in overleafe. No settup needed. Account has to be created.  

### Git
+ download git: https://gitforwindows.org/  
    *git needs to be installed to use git*  

### VS-Code
+ VS-Code: https://code.visualstudio.com/download  
+ LaTexWorkshop Extensions:https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop  
    for editing, syntax highlighting and completion and building of .tex files.  
+ Prettify: https://marketplace.visualstudio.com/items?itemName=siegebell.prettify-symbols-mode  
    to display \alpha as $\alpha$ in source.

*for prettify to work copy the settings_json.tex file and replace your current setting.json in VS Code with it.*


### Tex
+ install Tex: https://tug.org/texlive/  
__necessarry for using LaTex in VS-Code (or any other editor besides online ones like overleave)!!__  
