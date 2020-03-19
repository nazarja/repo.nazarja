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

# Repository Addon Structure

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="{ YOUR_KODI_REPO_ID }" name="{ YOUR_KODI_REPO_NAME }" version="1.0.0" provider-name="{ YOUR_KODI_NAME }">
    <extension point="xbmc.addon.repository" name="{ YOUR_KODI_REPO_NAME }">
        <dir>
            <info compressed="false">https://raw.githubusercontent.com/{ YOUR_GITHUB_USERNAME }/{ YOUR_GITHUB_REPO_NAME }/master/xml/addons.xml</info>
            <checksum>https://raw.githubusercontent.com/{ YOUR_GITHUB_USERNAME }/{ YOUR_GITHUB_REPO_NAME }/master/xml/addons.xml.md5</checksum>
            <datadir zip="true">https://raw.githubusercontent.com/{ YOUR_GITHUB_USERNAME }/{ YOUR_GITHUB_REPO_NAME }/master/zips/</datadir>
        </dir>
    </extension>
    <extension point="xbmc.addon.metadata">
        <summary lang="en_GB"></summary>
        <description lang="en_GB"></description>
        <platform>all</platform>
        <assets>
            <icon>icon.png</icon>
            <fanart>fanart.jpg</fanart>
        </assets>
    </extension>
</addon>
