# Immigrants Flows in Italy

This repository contains the first coursework for the Data Science Project. An inphographic regarding Migration flows in Italy is constructed and discussed.

The reference dataset is [LiberiamoliTutti!](/https://github.com/ondata/liberiamoli-tutti/tree/main/sbarchi-migranti)
In these directories is organized the submission of the work according to the structure of a data science project, as discussed in class. 
Specifically:
- **data**: contains all the data: [raw](./data/raw) coming from the reference above, and  [cleaned](./data/cleaned) the re-organized one. In addition, in [econosans](./data/econosans)  are contained the .ttf files used for the fonts, and a geojons.file used for the plots.
- **src**: contains different .py files used in the cleaning steps of the dataset. Not much cleaning was required as the raw data was already pre-processed. Some steps of reorganization are done, and all .py functions have the comments regarding what done.
- **analyses**: contains different jupyter notebooks to be run separately, to obtain the different plots.
- **makefile**: contains make_cleaned_data.ipynb, to be run to reorganize the data according to the functions contained in src. Instead inphographic.ipynb is the jupyter notebook to be run to combine the plots as the inphographic as required. 
- **outputs**: stores all the .png outputs
- **reports**: contains the md file [notes to editor](./reports/notes_to_editor.md) of the notes to the editor. 

To reproduce the work is then suggested to: 
- 1: create the data files running [here](./makefile/make_cleaned_data.ipynb)
- 2: run the ALL analyses in the folder [here](./analyses)
- 3: combine all of them in the desired infographic by running [here](./makefile/infographic.ipynb)



