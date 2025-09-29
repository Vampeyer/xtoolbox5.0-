# XToolbox 5.2.4

I am **Vampeyer**,  
I am going to be handling this repo and its maintenance for the remainder of its time as of now.

Like an old golden pocketwatch, it would be a sin to see it rust away into nothing.

<article>
<img src='https://github.com/Vampeyer/xtoolbox5.0-/blob/master/img/1.png' alt='XToolbox Screenshot'>
<img src='https://github.com/Vampeyer/xtoolbox5.0-/blob/master/img/2.png' alt='XToolbox Screenshot'>
 </article>
---

## About XToolbox

XToolbox 5.2.2 is a toolbox built in Python CLI, using pyinstaller and rich, and optionally UPX.

It uses a formatted dictionary to neatly localize repositories and names of important downloads for various tools, making it easily configurable for your favorite tools and downloads.

Although originally based on the same design, XToolbox 5.2.2 is superior to the well-known toolbox from [nyxiereal](https://github.com/nyxiereal/XToolbox) as the code is greatly optimized for modular usability and readability.

This means it is easy to edit and rebuild yourself for you or your company's liking.

---

## Customization

- Feel free to set up your own names, categories, and URLs in the `tools_data.py` file, and rebuild to create your own toolbox of your most used tools or downloads.

- It's **SUPER EASY** - just change the tooling URL, category, name and description in the `tools_data.py`, and it will load and pull those downloads and ask you if you want to run them.

### Adding More Tool Data Files

Tooling data may be added into or removed from tooling data in the `tools_data.py` files, or by using the following structures to add more files for more downloads.

Adding a file to the structure is done such as:
- `tools_data3.py`
- `tools_data4.py` 
- `tools_data5.py`

All will be automatically and dynamically imported into the `main.py`.

---

## OS Compatibility

This build should be generally OS agnostic, meaning anything that can be built with pyinstaller on Linux, MacOS, etc. - just change the download URLs to something meaningful.

---

## Support

**GIVE ME A STAR** if you enjoy this repo - **I WORKED HARD FOR IT!**  
*(This is uber clean code too, ty.)*

---

## Building from Source

### Prerequisites

To build this project:

### 1. Create Python Virtual Environment
First create a python venv by typing in your command line:
```bash
python -m venv toolbox-env
```
*(this is already done here)*

### 2. Activate Your Python Environment
Then activate your python environment to keep all your dependencies in one working place for the repo:

**For Command Line:**
```bash
toolbox-env\Scripts\activate.bat
```

**For PowerShell:**
```powershell
toolbox-env\Scripts\activate.ps1
```

You should then have your activated environment for python. You can tell it's activated by seeing `(toolbox-env) C:\Users\>` in your shell.

To deactivate, just type: `deactivate`

*(Always use a python environment where your modules don't conflict.)*

When using the requirements.txt file, you can save all your dependencies by running:
```bash
pip freeze > requirements.txt
```

### 2.5. Install PyInstaller and Pip
Just to be safe:
```bash
pip install pyinstaller
```

### 3. Install Dependencies
To install packages from the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 4. Build the Executable

After all packages are installed, you need to build the .exe file.

**Recommended method:**
```bash
pyinstaller --name XToolBox-v2.1.2 --hidden-import=rich --noupx main.py
```

**Alternative method (if you have UPX.exe builder in the root directory):**
```bash
pyinstaller --name Xtoolbox2.1.2 --hidden-import=rich --upx-dir . main.py
```

*We recommend the first method for consistency.*

This will build a `build` and a `dist` folder. Whatever you named the .exe (in this case, `Xtoolbox2.1.2`) will be the name of the .exe file in the `dist` folder.
