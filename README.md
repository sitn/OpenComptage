*OpenComptage* is a QGIS plugin to manage Canton Neuchâtel's Comptages.

The documentation is [here](https://opengisch.github.io/OpenComptage/).

* Purpose
  The purposes of the QGIS plugin are:
  - plan the future traffic measure
  - prepare the current traffic measure
  - import and management of the measure data
  - centralized management of the measure data


# Dev environnement on Windows

## First time or if you've changed QGIS version

Delete any existing .venv
Create .venv with the python of QGIS and copy .env file from QGIS installation folder:

```powershell
& "C:\Program Files\QGIS 3.40.9\apps\Python312\python.exe" -m venv .venv
cp "C:\Program Files\QGIS 3.40.9\bin\qgis-ltr-bin.env" .env
```

Create a simlink so the plugin being developed will be loaded directly in QGIS:

Run powershell as admin in the current directory:

```powershell
Start-Process powershell -Verb RunAs -ArgumentList "-NoExit -Command `"Set-Location -LiteralPath '$(Get-Location)'`""
```

Create symlink (adapt `<USERNAME>`):

```powershell
New-Item -ItemType SymbolicLink `
  -Path "C:\Users\<USERNAME>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\comptages" `
  -Target "$(Get-Location)\comptages"
```

Now you should see the plugin in the list of available plugins. 

Follow /docs/installation.md, the deployment section, step 1, 2 and 6. Finally add `GDAL_LIBRARY_PATH` to your `.env` according to step 1.

## Modify the loaded plugin

Activate venv and load dotenv file

```powershell
./venv/bin/activate
./load-env.ps1
```

You can edit the code and use plugin reloader extension to see the changes

