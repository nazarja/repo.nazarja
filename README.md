# repository.nazarja
Repository for Kodi addons

# Structure of Repository
/addons - your addons
/generator - contains the repo generator and a run file
/repo - contains an index.html for github pages and the most recent repoistory zip
/xml - contains the addons xml and md5 xml
/zips - contains all zips of your addons

# How to use repo generator
1. place your addons in /addons
2. open a terminal in the root folder
3. in terminal type: python generator/run.py 


# Automatic Creation
1. index file will be created and link updated to current repo
2. current repo zip will be placed in /repo folder and old repo zip removed
3. addons xml and md5 will be created or updated
4. zips of addons will be created and added to zips folder
5. fanart and icon will be placed in correct folders in the addons zip folder
