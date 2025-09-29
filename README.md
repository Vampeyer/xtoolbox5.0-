
=========================================== |
XToolbox 5.2.2 -                            |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= |
I am Vampeyer ,                             |
I am going to be handling this repo and     |
its maintenance for the remainder of its    |
time as of now.                             |
                                            |
Like an old golden pocketwatch , it would   |
be a sin to see it rust away into nothing.  |
+++++++++++++++++++++++++++++++++++++++++++++
<img src='https://github.com/Vampeyer/xtoolbox5.0-/blob/master/img/1.png' > <img>

XToolbox 5.2.2 , is a toolbox that is built in python CLI , 
 using pyinstaller and rich and optionally  UPX. 

it uses a formatted dictionary , too neatly localize repositories and names of important 
downloads for various tools , so it is easily configurable for your favorite tools / downloads.

Although originally based on the same design , 
Xtoolbox 5.2.2 is superior to the well known toolbox
 from nyxiereal @ -  https://github.com/nyxiereal/XToolbox
As the code is greatly optimized for modular usability and readability. 
-
Meaning , it is easy to edit , and rebuild yourself for you or your companies liking. 
-


- Feel free too set up your own names , 
categories , and URL's in the tools_data.py file , 
and re build to create your own tool box of your most used tools , or downloads. 

- its  SUPER EASY - just change the tooling URL , category , name and description 
in the tools_data.py , and it will load and pull those downloads and ask you if  you want to run them. 

tooling data may be added into , or removed from tooling data , in the tools_data.py files , 
or by using the following structures , too add more files , for more downloads, 
adding a file to the structure is done such as ,  

tools_data3.py ,
tools_data4.py , 
tools_data5.py ,  etc , will all be 
   automatically and  dynamically imported in to the main.py 

   
-------------------------------------------------------------------------------------------
This build should be generally OS agnostic , meaning anything that 
can be built with pyinstaller on Linux , MacOs etc  just change the download URL's to something meaningful. 
-------------------------------------------------------------------------------------------

GIVE ME A STAR , if you enjoy this repo  ,  I WORKED HARD FOR IT ! 
( this is uber clean code too , ty.  ) 

-------------------------------------------------------------------------------------------------------------
 BUILDING FROM SOURCE . 


To build this project , 
1#  . First create a python venv by typing in your command line ,  
    - python -m venv toolbox-env  
        ( this is already done here -)

#2 Then  activate your python environment to keep all your dependencies in one 
    working place for the repo , by using ,     
    -  toolbox-env\Scripts\activate.bat - for command line , or  
    -  toolbox-env\Scripts\activate.ps1 - for powershell , etc. 

You should then have your activated environment for python. 
You can tell its activated by seeing  - (toolbox-env) C:\Users\> 
in your shell ,  

to deactivate , just type , deactivate. 
( always use a python environemnt where your modules dont conflict.)

When using the requirements.txt file , you can save all your dependencies 
by running this command - pip freeze > requirements.txt

But now ,  we need too install dependencies form this requirements.txt file , here , by installing those
packages


#2.5 - install pyinstaller and pip , just to be safe ,  
   - pip install pyinstaller⌈

#3 To install packages from a requirements.txt file  type:
    - pip install -r requirements.txt


After all the packages are installed ,

#4 you need too build the .exe file. 
        To do this , you can run

    - pyinstaller --name XToolBox-v2.1.2 --hidden-import=rich --noupx main.py  - 
            to build from the main.py file ,  
             or if you have UPX.exe builder as well in the root directory , 
             you may run  
    -pyinstaller --name Xtoolbox2.1.2 --hidden-import=rich --upx-dir . main.py

            we reccomend the first for consistency though


This will build a build and a dist folder ,  whatever you named the .exe , in this case ,  
Xtoolbox2.1.2 - that will be tha name of the .exe file , in the dist folder. 
