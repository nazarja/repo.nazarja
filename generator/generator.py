import os
import re
import shutil
import hashlib
import zipfile

#============================#

class Generator:

    def __init__(self):
        self.current_path = os.getcwd()
        self.addons_path =os.path.join(self.current_path, 'addons')
        self.repo_path = os.path.join(self.current_path, 'repo')
        self.zips_path = os.path.join(self.current_path, 'zips')
        self.xml_path = os.path.join(self.current_path, 'xml')
        self.index_file = os.path.join(self.repo_path, 'index.html')
        self.addons_file = os.path.join(self.xml_path, 'addons.xml')
        self.md5_file = os.path.join(self.xml_path, 'addons.xml.md5')

    #============================#

    def remove_binaries(self):
        for root, dirs, files in os.walk(self.addons_path):
            for f in files:
                if f.lower().split('.')[-1] in ['pyo', 'pyc']:
                    file_name = os.path.join(root, f)
                    try: os.unlink(file_name)
                    except Exception as e: print('Remove Binaries ERROR: ' + str(e))

    #============================#

    def create_addons_xml(self):
        addons = os.listdir(self.addons_path)
        addons_xml = u'<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n'

        for addon in addons:
            try:
                addon_path = os.path.join(self.addons_path, addon)
                xml_path = os.path.join(addon_path, 'addon.xml')
                xml_lines = open(xml_path, 'r', encoding='utf-8').read().splitlines()
            
                addon_xml = ''
                version = None

                for line in xml_lines:
                    if 'version="' in line and 'id="' in line and version is None:
                        version = re.compile('version="(.+?)"').findall(line)[0]

                    addon_xml += line.rstrip() + '\n'
                addons_xml += addon_xml.rstrip() + '\n\n'
                self.create_zips(addon_path, addon, xml_path, version)

                if 'repository.' in addon:
                    # remove old repo zip
                    for root, dirs, files in os.walk(self.repo_path):
                        for f in files:
                            if f.startswith('repository'):
                                os.unlink(os.path.join(root, f))
                                break
                        break
                    self.create_index_file(addon, version)
                    current_repo_zip_path = os.path.join(self.zips_path, addon,'{}-{}.zip'.format(addon, version))
                    copy_path = os.path.join(self.repo_path, '{}-{}.zip'.format(addon, version))
                    shutil.copyfile(current_repo_zip_path, copy_path)
            
            except Exception as e:
                print('Error creating addons xml file: ' + str(e))

        addons_xml = addons_xml.strip() + u'\n</addons>\n'
        with open(self.addons_file, 'w', encoding='utf-8') as f:
            f.write(addons_xml)

    #============================#

    def create_index_file(self, repo_name, version):
        repo_zip_name = '{0}-{1}.zip'.format(repo_name, version)
        with open(self.index_file, 'w') as f:
            f.write('<a href="{0}">{0}</a>'.format(repo_zip_name))

     #============================#
    
    def create_zips(self, addon_path, addon_name, xml_path, version):
        ignore_files = ('.git', '.github', '.gitignore', '.DS_Store', 'thumbs.db', '.idea', 'venv', '.vscode')
        copy_files = ['icon.png', 'fanart.jpg', 'addon.xml']
        addon_dir_path = os.path.join(self.zips_path, addon_name)
        addon_zip_path = os.path.join(addon_dir_path, '{0}-{1}.zip'.format(addon_name, version))
        
        if not os.path.exists(addon_dir_path):
            os.makedirs(addon_dir_path)
        
        if not os.path.exists(addon_zip_path):
            try:
                zip = zipfile.ZipFile(addon_zip_path, 'w', compression=zipfile.ZIP_DEFLATED)
                root_length = len(os.path.dirname(os.path.abspath(addon_path)))

                for root, dirs, files in os.walk(addon_path):
                    for i in ignore_files:
                        if i in dirs:
                            try: dirs.remove(i)
                            except: pass
                        for f in files:
                            if f.startswith(i):
                                try: files.remove(f)
                                except: pass

                    archive_root = os.path.abspath(root)[root_length:]
                    
                    for f in files:
                        if f in copy_files:
                            new_image_path = root.split(addon_name+'/')[-1]
                            if new_image_path.endswith(addon_name):
                                shutil.copy(os.path.join(root, f), addon_dir_path)
                            else:
                                new_image_path = os.path.join(addon_dir_path, new_image_path)
                                
                                if not os.path.exists(new_image_path):
                                    os.makedirs(new_image_path)

                                shutil.copy(os.path.join(root, f), new_image_path)

                        full_path = os.path.join(root, f)
                        archive_name = os.path.join(archive_root, f)
                        zip.write(full_path, archive_name, zipfile.ZIP_DEFLATED)
                
                zip.close()

            except Exception as e:
                print('Error creating zip file: ' + str(e))

    #============================#

    def create_md5_xml(self):
        try:
            with open(self.addons_file, 'r', encoding='utf-8') as f:
                hash = hashlib.md5(f.read().encode('utf-8')).hexdigest()
                open(self.md5_file, 'w').write(hash)
        except Exception as e: print('MD5 Creation Error: ' + str(e))

    #============================#

    def run(self):
        g = Generator()
        g.remove_binaries()
        g.create_addons_xml()
        g.create_md5_xml()

    #============================#


