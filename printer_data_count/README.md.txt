# RICOH Data Scrape

In an ideal world, you don't have to worry about EOL. Unfortunately, it's not like that. In my case, RICOH's print counter has reached its EOL and won't service it unless the machines are upgraded (make $ rain). Fortunately, there's a fix so the supply department doesn't have to look up the print count one by one. Alas, we'll be using this script to generate a report and adding a CRON job for scheduling. The uploaded script will be as minimalist as possible for easier customizability.

## Install

### Windows 10
1. Install [Miniconda Python 3.7](https://docs.conda.io/en/latest/miniconda.html#windows-installers)
2. Install [Git](https://git-scm.com/download/win)
3. Launch the Anaconda Prompt and run the following commands
```bash
git clone https://github.com/marcmaceira/work-scripts.git
cd work-scripts/printer_data_count
scripts\install_windows.bat
```
4. Run `run_windows.bat`

## Run
In the Anaconda Prompt
```bash
cd C:\path\to\printer_data_count
run_windows.bat
```
