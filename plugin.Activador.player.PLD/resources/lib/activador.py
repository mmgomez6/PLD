import urllib, os, xbmc, xbmcgui
import base64
addon_id = 'plugin.video.live.pld'
data_folder = 'special://home/addons/plugin.video.live.pld/'
Url = base64.b64decode('aHR0cDovL3Byb3llY3RvbHV6ZGlnaXRhbC5pbmZvL3R2Z3VpYS9kb3dubG9hZC9hY3RpcGxheWVyLzMzLw==')
File = ['source_file']

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("ACTIVANDO PLAYER.PROYECTOLUZDIGITAL","Introduciendo Codigo",' ', ' ')
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
	
addon_id = 'plugin.video.live.pld'
data_folder = 'special://userdata/addon_data/plugin.video.live.pld/'
Url = base64.b64decode('aHR0cDovL3Byb3llY3RvbHV6ZGlnaXRhbC5pbmZvL3R2Z3VpYS9kb3dubG9hZC9hY3RpcGxheWVyLw==')
File = ['settings.xml']

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("ACTIVANDO PLAYER.PROYECTOLUZDIGITA","Introduciendo Codigo",' ', ' ')
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
addon = xbmcaddon.Addon('plugin.Activador.player.PLD')	
	
util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), 
               'special://home/addons/plugin.Activador.player.PLD/intro.mp4')	
	
	
