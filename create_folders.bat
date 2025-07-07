@echo off
setlocal

set BASEPATH=E:\pet_help_recommendation_systems\dataset

for %%F in (
    allergy bleeding cold diarrhea "ear infection" fever fracture infection limping
    mange normal parvo rabies tick tumor vomiting wound
) do (
    mkdir "%BASEPATH%\train\%%F"
    mkdir "%BASEPATH%\val\%%F"
)

echo ✅ Folders created inside train and val.
pause
