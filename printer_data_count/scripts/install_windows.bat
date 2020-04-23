call scripts/settings_windows.bat

call conda create -y -n %CONDA_ENV_NAME% python=3.7
call conda activate %CONDA_ENV_NAME%

call pip install -r requirements.txt
