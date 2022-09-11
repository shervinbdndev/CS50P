try:
    import os
    import sv_ttk
    import tkinter
    import requests
    import ntkutils
    import webbrowser
    import subprocess
    import darkdetect
    import customtkinter
    from typing import Any
    from pytube import YouTube
    from typing import Literal
    from threading import Thread
    from tkinter import filedialog
    from tkinter import messagebox
    from typing_extensions import Self
    from tkinter.constants import BOTH
    from tkinter.font import (BOLD , NORMAL)
    from tkinter.ttk import (Notebook , Frame)
    from tkinter.__init__ import (StringVar, Label)
    from customtkinter.widgets.ctk_entry import CTkEntry
    from customtkinter.widgets.ctk_button import CTkButton
    from customtkinter.widgets.ctk_checkbox import CTkCheckBox

except ModuleNotFoundError.__doc__:
    raise RuntimeError(args='Cannot Run Application') from None

finally:
    ...





class LengthSize:
    def getSize(bytes , default = '') -> str:
        for unit in ['' , 'KB' , 'MB' , 'GB' , 'TB' , 'PB']:
            if (bytes < 1024):
                return f'{bytes:.2f}{unit}{default}'
            bytes /= 1024






class YoutubeDownloader:
    def __init__(self : Self) -> Literal[None]:
        super(YoutubeDownloader , self).__init__()
        self.root = tkinter.Tk()
        self.root.title(string='Youtube Downloader')
        self.root.geometry(newGeometry='555x320')
        self.root.resizable(width=False , height=False)
        self.rootTabControl = Notebook(master=self.root)
        self.root.wm_attributes('-alpha', 0.969)
        """self.root.wm_attributes('-alpha' , 0.95)"""
        self.tester = Label(master=self.root)
        self.svLink = StringVar(master=self.root)
        self.svPath = StringVar(master=self.root)
        self.svCombo = StringVar(master=self.root)
        self.tabDownload = Frame(master=self.rootTabControl)
        self.tabVidInfo = Frame(master=self.rootTabControl)
        self.tabLanguage = Frame(master=self.rootTabControl)
        """self.tabCustomize = Frame(master=self.rootTabControl)"""
        self.tabAbout = Frame(master=self.rootTabControl)
        self.rootTabControl.add(child=self.tabDownload , text='Download')
        self.rootTabControl.add(child=self.tabVidInfo , text='Video Information')
        self.rootTabControl.add(child=self.tabLanguage , text='Language')
        """self.rootTabControl.add(child=self.tabCustomize , text='Customize')"""
        self.rootTabControl.add(child=self.tabAbout , text='About')
        self.rootTabControl.pack(expand=1 , fill=BOTH)
        self.persian : bool = False
        self.english : bool = True
        self.fileSize : int = 0

        def getTheme(arg : str) -> Literal[None]:
            if (arg == 'light'):
                sv_ttk.set_theme(theme='light')
                customtkinter.set_appearance_mode(mode_string='light')
                self.root.configure(background='#FAFAFA')
                self.linkEntry.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.linkDestination.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.downloadStatus.configure(background='#FAFAFA')
                self.videoLinkLabel.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.videoLinkLabel.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.videoAuthorLabel.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.status.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.labelCheckBoxSelectInfo.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.svVideoAuthor.configure(background='#FAFAFA' , foreground='#000000')
                self.svViewsCount.configure(background='#FAFAFA' , foreground='#000000')
                self.viewsCount.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.highestQualityBtn.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.lowestQualityBtn.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.btn1080.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.btn720.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.btn480.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.btn360.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.btnPA.configure(bg_color='#FAFAFA')
                self.btnEN.configure(bg_color='#FAFAFA')
                self.audioOnlybtn.configure(bg_color='#FAFAFA' , fg_color='#1D94D0')
                self.browseSaveDialogLabel.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.labelVideoSecs.configure(background='#FAFAFA' , foreground='#000000')
                self.svVideoSecs.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.labelVideoID.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.svVideoID.configure(background='#FAFAFA' , foreground='#000000')
                self.labelChannelID.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.svChannelID.configure(background='#FAFAFA' , foreground='#000000')
                self.labelLiveContent.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.svLiveContent.configure(background='#FAFAFA' , foreground='#000000')
                self.labelLengthSize.configure(background='#FAFAFA' , foreground='#1D94D0')
                self.svVideoSize.configure(background='#FAFAFA' , foreground='#000000')
            elif (arg == 'dark'):
                sv_ttk.set_theme(theme='dark')
                customtkinter.set_appearance_mode(mode_string='dark')
                self.root.configure(background='#1C1C1C')
                self.linkEntry.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.linkDestination.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.downloadStatus.configure(background='#1C1C1C')
                self.videoLinkLabel.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.videoAuthorLabel.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.svVideoAuthor.configure(background='#1C1C1C' , foreground='#ffffff')
                self.svViewsCount.configure(background='#1C1C1C' , foreground='#ffffff')
                self.viewsCount.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.videoLinkLabel.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.status.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.labelCheckBoxSelectInfo.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.highestQualityBtn.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.btnEN.configure(bg_color='#1C1C1C')
                self.btnPA.configure(bg_color='#1C1C1C')
                self.lowestQualityBtn.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.btn1080.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.btn720.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.btn480.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.btn360.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.audioOnlybtn.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                self.browseSaveDialogLabel.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.labelVideoSecs.configure(background='#1C1C1C' , foreground='#ffffff')
                self.svVideoSecs.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.labelVideoID.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.svVideoID.configure(background='#1C1C1C' , foreground='#ffffff')
                self.labelChannelID.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.svChannelID.configure(background='#1C1C1C' , foreground='#ffffff')
                self.labelLiveContent.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.svLiveContent.configure(background='#1C1C1C' , foreground='#ffffff')
                self.labelLengthSize.configure(background='#1C1C1C' , foreground='#1D94D0')
                self.svVideoSize.configure(background='#1C1C1C' , foreground='#ffffff')
                self.btnME.configure(bg_color='#1C1C1C' , fg_color='#1D94D0')
                ntkutils.dark_title_bar(window=self.root)

        def setBySystemTheme() -> Literal[None]:
            if (darkdetect.isLight()):
                getTheme(arg='light')
            elif (darkdetect.isDark()):
                getTheme(arg='dark')

        def browseFile(arg : Any) -> Literal[None]:
            if (arg == 'browse'):
                downloadDirectory = filedialog.askdirectory(initialdir=os.path.join(os.path.abspath(path=os.path.dirname(p=__file__))) , title='Save Video')
                self.svPath.set(value=downloadDirectory)

        def openDownloadedVideoPath(arg : str) -> Literal[None]:
            if (arg == 'open'):
                path = os.path.normpath(path=self.svPath.get())
                subprocess.run(args=[os.path.join(os.getenv(key='WINDIR') , 'explorer.exe') , path])

        def changeAppLanguage(arg : Any) -> Literal[None]:
            if (arg == 'pa'):
                self.persian = True
                self.english = False
                self.root.title(string='یوتیوب دانلودر')
                self.rootTabControl.add(child=self.tabDownload , text='دانلود')
                self.rootTabControl.add(child=self.tabVidInfo , text='مشخصات ویدیو')
                self.rootTabControl.add(child=self.tabLanguage , text='زبان')
                self.rootTabControl.add(child=self.tabAbout , text='درباره')
                self.videoLinkLabel.configure(text='لینک ویدیو :')
                self.browseSaveDialogLabel.configure(text='محل ذخیره سازی :')
                if (darkdetect.isDark()):
                    self.btnDownload.configure(text='دانلود' , bg_color = '#1C1C1C')
                    self.btnPaste.configure(text='الصاق' , bg_color = '#1C1C1C')
                    self.btnBrowse.configure(text='انتخاب' , bg_color = '#1C1C1C')
                    self.btnPA.configure(text='پارسی' , bg_color = '#1C1C1C')
                    self.btnEN.configure(text='انگلیسی' , bg_color = '#1C1C1C')
                    self.btnME.configure(text='گیتهاب' , bg_color = '#1C1C1C')
                    self.btnOpenFile.configure(text='بازکردن' , bg_color = '#1C1C1C')
                elif (darkdetect.isLight()):
                    self.btnDownload.configure(text='دانلود' , bg_color = '#FAFAFA')
                    self.btnPaste.configure(text='الصاق' , bg_color = '#FAFAFA')
                    self.btnBrowse.configure(text='انتخاب' , bg_color = '#FAFAFA')
                    self.btnPA.configure(text='پارسی' , bg_color = '#FAFAFA')
                    self.btnEN.configure(text='انگلیسی' , bg_color = '#FAFAFA')
                    self.btnME.configure(text='گیتهاب' , bg_color = '#FAFAFA')
                    self.btnOpenFile.configure(text='بازکردن' , bg_color = '#FAFAFA')
                self.status.configure(text='وضعیت :')
                self.downloadStatus.configure(text='نامعلوم')
                self.highestQualityBtn.configure(text='کیفیت بالاترین')
                self.lowestQualityBtn.configure(text='کیفیت ترین پایین')
                self.audioOnlybtn.configure(text='صدا فقط')
                self.videoAuthorLabel.configure(text='منصف :')
                self.viewsCount.configure(text='بازدید :')
                self.svVideoSecs.configure(text='زمان :')
                self.labelVideoID.configure(text='آی دی ویدیو :')
                self.labelChannelID.configure(text='آی دی کانال :')
                self.labelLiveContent.configure(text='زنده :')
                self.labelLengthSize.configure(text='حجم ویدیو :')
            elif (arg == 'en'):
                self.english = True
                self.persian = False
                self.root.title(string='Youtube Downloader')
                self.rootTabControl.add(child=self.tabDownload , text='Download')
                self.rootTabControl.add(child=self.tabVidInfo , text='Video Information')
                self.rootTabControl.add(child=self.tabLanguage , text='Language')
                self.rootTabControl.add(child=self.tabAbout , text='About')
                self.videoLinkLabel.configure(text='Video Link :')
                self.browseSaveDialogLabel.configure(text='Destination :')
                if (darkdetect.isDark()):
                    self.btnDownload.configure(text='Download' , bg_color = '#1C1C1C')
                    self.btnPaste.configure(text='Paste' , bg_color = '#1C1C1C')
                    self.btnBrowse.configure(text='Browse' , bg_color = '#1C1C1C')
                    self.btnPA.configure(text='Persian' , bg_color = '#1C1C1C')
                    self.btnEN.configure(text='English' , bg_color = '#1C1C1C')
                    self.btnME.configure(text='Github' , bg_color = '#1C1C1C')
                    self.btnOpenFile.configure(text='Open' , bg_color = '#1C1C1C')
                elif (darkdetect.isLight()):
                    self.btnDownload.configure(text='Download' , bg_color = '#FAFAFA')
                    self.btnPaste.configure(text='Paste' , bg_color = '#FAFAFA')
                    self.btnBrowse.configure(text='Browse' , bg_color = '#FAFAFA')
                    self.btnPA.configure(text='Persian' , bg_color = '#FAFAFA')
                    self.btnEN.configure(text='English' , bg_color = '#FAFAFA')
                    self.btnME.configure(text='Github' , bg_color = '#FAFAFA')
                    self.btnOpenFile.configure(text='Open' , bg_color = '#FAFAFA')
                self.status.configure(text='Status :')
                self.downloadStatus.configure(text='Not Using')
                self.highestQualityBtn.configure(text='Highest Quality')
                self.lowestQualityBtn.configure(text='Lowest Quality')
                self.audioOnlybtn.configure(text='Audio Only')
                self.videoAuthorLabel.configure(text='Author :')
                self.viewsCount.configure(text='Views :')
                self.svVideoSecs.configure(text='Seconds :')
                self.labelVideoID.configure(text='Video ID :')
                self.labelChannelID.configure(text='Channel ID :')
                self.labelLiveContent.configure(text='Live Content :')
                self.labelLengthSize.configure(text='Video Size :')

        def startDownload() -> Literal[None]:
            startThread = Thread(target=downloadVideo)
            startThread.start()

        def pasteContent(arg : Any) -> Literal[None]:
            if (arg == 'paste'):
                pastedContent = self.root.clipboard_get()
                self.svLink.set(value=pastedContent)

        def aboutMe(arg : Any) -> Literal[None]:
            if (arg == 'me'):
                webbrowser.open(url='https://github.com/shervinbdndev')

        def getVideoInfo() -> Literal[None]:
            try:
                self.svVideoAuthor.configure(text=YouTube(url=self.svLink.get()).vid_info['videoDetails']['author'])
                self.svViewsCount.configure(text=f"{int(YouTube(url=self.svLink.get()).vid_info['videoDetails']['viewCount']):,}")
                self.labelVideoSecs.configure(text=YouTube(url=self.svLink.get()).vid_info['videoDetails']['lengthSeconds'])
                self.svVideoID.configure(text=YouTube(url=self.svLink.get()).vid_info['videoDetails']['videoId'])
                self.svChannelID.configure(text=YouTube(url=self.svLink.get()).vid_info['videoDetails']['channelId'])
                self.svLiveContent.configure(text=[True if str(YouTube(url=self.svLink.get()).vid_info['videoDetails']['isLiveContent']) == 1 else False])
            except requests.ConnectionError as e:
                self.svVideoAuthor.configure(text=e.__doc__)
                self.svViewsCount.configure(text=e.__doc__)
                self.labelVideoSecs.configure(text=e.__doc__)
                self.svVideoID.configure(text=e.__doc__)
                self.svChannelID.configure(text=e.__doc__)
                self.svLiveContent.configure(text=e.__doc__)
                self.svVideoSize.configure(text=e.__doc__)

        def downloadVideo() -> Literal[None]:
            if (self.svLink.get() is not None):
                if (self.highestQualityBtn.check_state == True):
                    try:
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='درحال دانلود' , fg='#b59b2a')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloading' , fg='#b59b2a')
                        self.root.update()
                        video = YouTube(url=self.svLink.get())
                        getVideoInfo()
                        videoStream = video.streams.get_highest_resolution()
                        self.svVideoSize.configure(text=LengthSize.getSize(videoStream.filesize))
                        videoStream.download(self.svPath.get())
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='دانلود شد' , fg='#28A745')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                    except Exception:
                        if ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                        elif ((self.english is False) and (self.persian is True)):
                            self.downloadStatus.configure(text='ناموفق' , fg='#CA3B47')
                            self.root.update()
                elif (self.lowestQualityBtn.check_state == True):
                    try:
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='درحال دانلود' , fg='#b59b2a')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloading' , fg='#b59b2a')
                        self.root.update()
                        video = YouTube(url=self.svLink.get())
                        getVideoInfo()
                        videoStream = video.streams.get_lowest_resolution()
                        self.svVideoSize.configure(text=LengthSize.getSize(videoStream.filesize))
                        videoStream.download(self.svPath.get())
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='دانلود شد' , fg='#28A745')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                    except Exception:
                        if ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                        elif ((self.english is False) and (self.persian is True)):
                            self.downloadStatus.configure(text='ناموفق' , fg='#CA3B47')
                            self.root.update()
                elif (self.audioOnlybtn.check_state == True):
                    try:
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='درحال دانلود' , fg='#b59b2a')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloading' , fg='#b59b2a')
                        self.root.update()
                        video = YouTube(url=self.svLink.get())
                        getVideoInfo()
                        videoStream = video.streams.get_audio_only(subtype='mp4')
                        self.svVideoSize.configure(text=LengthSize.getSize(videoStream.filesize))
                        videoStream.download(self.svPath.get())
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='دانلود شد' , fg='#28A745')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                    except Exception:
                        if ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                        elif ((self.english is False) and (self.persian is True)):
                            self.downloadStatus.configure(text='ناموفق' , fg='#CA3B47')
                            self.root.update()
                elif (self.btn1080.check_state == True):
                    try:
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='درحال دانلود' , fg='#b59b2a')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloading' , fg='#b59b2a')
                        self.root.update()
                        video = YouTube(url=self.svLink.get())
                        getVideoInfo()
                        videoStream = video.streams.get_by_resolution(resolution='1080p')
                        self.svVideoSize.configure(text=LengthSize.getSize(videoStream.filesize))
                        videoStream.download(self.svPath.get())
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='دانلود شد' , fg='#28A745')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                    except Exception:
                        if ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                        elif ((self.english is False) and (self.persian is True)):
                            self.downloadStatus.configure(text='ناموفق' , fg='#CA3B47')
                            self.root.update()
                elif (self.btn720.check_state == True):
                    try:
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='درحال دانلود' , fg='#b59b2a')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloading' , fg='#b59b2a')
                        self.root.update()
                        video = YouTube(url=self.svLink.get())
                        getVideoInfo()
                        videoStream = video.streams.get_by_resolution(resolution='720p')
                        self.svVideoSize.configure(text=LengthSize.getSize(videoStream.filesize))
                        videoStream.download(self.svPath.get())
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='دانلود شد' , fg='#28A745')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                    except Exception:
                        if ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                        elif ((self.english is False) and (self.persian is True)):
                            self.downloadStatus.configure(text='ناموفق' , fg='#CA3B47')
                            self.root.update()
                elif (self.btn480.check_state == True):
                    try:
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='درحال دانلود' , fg='#b59b2a')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloading' , fg='#b59b2a')
                        self.root.update()
                        video = YouTube(url=self.svLink.get())
                        getVideoInfo()
                        videoStream = video.streams.get_by_resolution(resolution='480p')
                        self.svVideoSize.configure(text=LengthSize.getSize(videoStream.filesize))
                        videoStream.download(self.svPath.get())
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='دانلود شد' , fg='#28A745')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                    except Exception:
                        if ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                        elif ((self.english is False) and (self.persian is True)):
                            self.downloadStatus.configure(text='ناموفق' , fg='#CA3B47')
                            self.root.update()
                elif (self.btn360.check_state == True):
                    try:
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='درحال دانلود' , fg='#b59b2a')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloading' , fg='#b59b2a')
                        self.root.update()
                        video = YouTube(url=self.svLink.get())
                        getVideoInfo()
                        videoStream = video.streams.get_by_resolution(resolution='360p')
                        self.svVideoSize.configure(text=LengthSize.getSize(videoStream.filesize))
                        videoStream.download(self.svPath.get())
                        if ((self.persian is True) and (self.english is False)):
                            self.downloadStatus.configure(text='دانلود شد' , fg='#28A745')
                        elif ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                    except Exception:
                        if ((self.english is True) and (self.persian is False)):
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                        elif ((self.english is False) and (self.persian is True)):
                            self.downloadStatus.configure(text='ناموفق' , fg='#CA3B47')
                            self.root.update()
            else:
                messagebox.askokcancel(title='Invalid Link' , message='Please Enter a Valid Link')

        def checkBoxesChecked() -> Literal[None]:
            if ((self.english is True) and (self.persian is False)):
                if (self.highestQualityBtn.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Only Select Highest')
                if (self.lowestQualityBtn.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Only Select Lowest')
                if ((self.highestQualityBtn.check_state is False) and (self.lowestQualityBtn.check_state is False)):
                    self.labelCheckBoxSelectInfo.configure(text='')
                if (self.btn1080.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Only Select 1080p')
                if (self.btn720.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Only Select 720p')
                if (self.btn480.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Only Select 480p')
                if (self.btn360.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Only Select 360p')
                if ((self.btn1080.check_state is True) and (self.btn720.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn1080.check_state is True) and (self.btn480.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn1080.check_state is True) and (self.btn360.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn720.check_state is True) and (self.btn1080.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn720.check_state is True) and (self.btn480.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn720.check_state is True) and (self.btn360.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn480.check_state is True) and (self.btn1080.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn480.check_state is True) and (self.btn720.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn480.check_state is True) and (self.btn360.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn360.check_state is True) and (self.btn1080.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn360.check_state is True) and (self.btn720.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
                if ((self.btn360.check_state is True) and (self.btn480.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='You Can Select One Quality')
            elif ((self.english is False) and (self.persian is True)):
                if (self.highestQualityBtn.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='فقط میتوانید بالاترین کیفیت را انتخاب کنید')
                if (self.lowestQualityBtn.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='فقط میتوانید پایین ترین کیفیت را انخاب کنید')
                if ((self.highestQualityBtn.check_state is False) and (self.lowestQualityBtn.check_state is False)):
                    self.labelCheckBoxSelectInfo.configure(text='')
                if (self.btn1080.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='فقط میتوانید 1080 انتخاب کنید')
                if (self.btn720.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='فقط میتوانید 720 انتخاب کنید')
                if (self.btn480.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='فقط میتوانید 480 انتخاب کنید')
                if (self.btn360.check_state is True):
                    self.labelCheckBoxSelectInfo.configure(text='فقط میتوانید 360 انتخاب کنید')
                if ((self.btn1080.check_state is True) and (self.btn720.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn1080.check_state is True) and (self.btn480.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn1080.check_state is True) and (self.btn360.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn720.check_state is True) and (self.btn1080.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn720.check_state is True) and (self.btn480.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn720.check_state is True) and (self.btn360.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn480.check_state is True) and (self.btn1080.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn480.check_state is True) and (self.btn720.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn480.check_state is True) and (self.btn360.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn360.check_state is True) and (self.btn1080.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn360.check_state is True) and (self.btn720.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')
                if ((self.btn360.check_state is True) and (self.btn480.check_state is True)):
                    self.labelCheckBoxSelectInfo.configure(text='نمیتوانید چند کیفیت را انتخاب کنید')

        self.labelCheckBoxSelectInfo = Label(
            master=self.tabDownload ,
            text= '',
            font=('normal' , 9 , BOLD)
        )

        self.labelCheckBoxSelectInfo.place(x=130 , y=150)

        self.status = Label(master=self.tabDownload , text='Status :' , font=('normal' , 12 , BOLD))

        self.status.place(x=290 , y=180)

        self.downloadStatus = Label(master=self.tabDownload , text='Not Using' , font=('normal' , 9 , BOLD) , foreground='#b59b2a')

        self.downloadStatus.place(x=390 , y=192 , anchor=tkinter.CENTER)

        self.videoLinkLabel = Label(master=self.tabDownload , text='Video Link :' , font=('normal' , 12 , BOLD))

        self.videoLinkLabel.place(x=20 , y=30)

        self.linkEntry = CTkEntry(
            master=self.tabDownload ,
            textvariable=self.svLink ,
            corner_radius=5 ,
            width=285 ,
            justify=tkinter.LEFT
        )

        self.linkEntry.place(x=128 , y=28)

        self.browseSaveDialogLabel = Label(master=self.tabDownload , text='Destination :' , font=('normal' , 12 , BOLD))

        self.browseSaveDialogLabel.place(x=12 , y=105)

        self.linkDestination = CTkEntry(
            master=self.tabDownload ,
            textvariable=self.svPath ,
            corner_radius=5 ,
            width=285 ,
            justify=tkinter.LEFT
        )

        self.linkDestination.place(x=128 , y = 102)

        self.btnPaste = CTkButton(
            master=self.tabDownload ,
            text='Paste' ,
            corner_radius=5 ,
            width=100 ,
            command=lambda:pasteContent(arg='paste') ,
            cursor='hand2'
        )

        self.btnPaste.place(x=428 , y = 28)

        self.btnBrowse = CTkButton(
            master=self.tabDownload ,
            text='Browse' ,
            corner_radius=5 ,
            width=100 ,
            command=lambda:browseFile(arg='browse') ,
            cursor='hand2'
        )

        self.btnBrowse.place(x=428 , y = 102)

        self.btnDownload = CTkButton(
            master=self.tabDownload ,
            text='Download' ,
            corner_radius=5 ,
            width=220 ,
            command= startDownload ,
            cursor='hand2'
        )

        self.btnDownload.place(x=295 , y=225)

        self.btnOpenFile = CTkButton(
            master=self.tabDownload ,
            text='Open' ,
            corner_radius=5 ,
            width=80 ,
            command=lambda:openDownloadedVideoPath(arg='open') ,
            cursor='hand2'
        )

        self.btnOpenFile.place(x=440 , y=177)

        self.highestQualityBtn = CTkCheckBox(
            master=self.tabDownload ,
            text='Highest Quality' ,
            state=NORMAL ,
            command=checkBoxesChecked
        )

        self.highestQualityBtn.place(x=130 , y = 180)

        self.lowestQualityBtn = CTkCheckBox(
            master=self.tabDownload ,
            text='Lowest Quality' ,
            state=NORMAL ,
            command=checkBoxesChecked
        )

        self.lowestQualityBtn.place(x=130 , y = 210)

        self.audioOnlybtn = CTkCheckBox(
            master=self.tabDownload ,
            text='Audio Only' ,
            state=NORMAL ,
            command=checkBoxesChecked
        )

        self.audioOnlybtn.place(x=130 , y = 240)

        self.btn1080 = CTkCheckBox(
            master=self.tabDownload ,
            text='1080p' ,
            state=NORMAL ,
            command=checkBoxesChecked
        )

        self.btn1080.place(x=15 , y=150)

        self.btn720 = CTkCheckBox(
            master=self.tabDownload ,
            text='720p' ,
            state=NORMAL ,
            command=checkBoxesChecked
        )

        self.btn720.place(x=15 , y=180)

        self.btn480 = CTkCheckBox(
            master=self.tabDownload ,
            text='480p' ,
            state=NORMAL ,
            command=checkBoxesChecked
        )

        self.btn480.place(x=15 , y=210)

        self.btn360 = CTkCheckBox(
            master=self.tabDownload ,
            text='360p' ,
            state=NORMAL ,
            command=checkBoxesChecked
        )

        self.btn360.place(x=15 , y=240)

        self.btnPA = CTkButton(
            master=self.tabLanguage ,
            text='Persian' ,
            corner_radius=5 ,
            width=150 ,
            command=lambda:changeAppLanguage(arg='pa') ,
            cursor='hand2'
        )

        self.btnPA.place(relx=0.2 , rely=0.5 , anchor=tkinter.W)

        self.btnEN = CTkButton(
            master=self.tabLanguage ,
            text='English' ,
            corner_radius=5 ,
            width=150 ,
            command=lambda:changeAppLanguage(arg='en') ,
            cursor='hand2'
        )

        self.btnEN.place(relx=0.5 , rely=0.5 , anchor=tkinter.W)

        self.btnME = CTkButton(
            master=self.tabAbout ,
            text='Github' ,
            corner_radius=5 ,
            width=150 ,
            command=lambda:aboutMe(arg='me') ,
            cursor='hand2'
        )

        self.btnME.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)

        self.videoAuthorLabel = Label(master=self.tabVidInfo , text='Author :' , font=('normal' , 12 , BOLD))

        self.videoAuthorLabel.place(x=2 , y=15 + 5)

        self.svVideoAuthor = Label(master=self.tabVidInfo , text=None , font=('normal' , 10 , BOLD))

        self.svVideoAuthor.place(x=90 , y=15 + 5)

        self.viewsCount = Label(master=self.tabVidInfo , text='Views :' , font=('normal' , 12 , BOLD))

        self.viewsCount.place(x=2 , y=50 + 5)

        self.svViewsCount = Label(master=self.tabVidInfo , text=None , font=('normal' , 10 , BOLD))

        self.svViewsCount.place(x=90 , y=50 + 5)

        self.svVideoSecs = Label(master=self.tabVidInfo , text='Seconds :' , font=('normal' , 12 , BOLD))

        self.svVideoSecs.place(x=2 , y=85 + 5)

        self.labelVideoSecs = Label(master=self.tabVidInfo , text=None , font=('normal' , 10 , BOLD))

        self.labelVideoSecs.place(x=111 , y=85 + 5)

        self.labelVideoID = Label(master=self.tabVidInfo , text='Video ID :' , font=('normal' , 12 , BOLD))

        self.labelVideoID.place(x=2 , y=120 + 5)

        self.svVideoID = Label(master=self.tabVidInfo , text=None , font=('normal' , 10 , BOLD))

        self.svVideoID.place(x=111 , y=120 + 5)

        self.labelChannelID = Label(master=self.tabVidInfo , text='Channel ID :' , font=('normal' , 12 , BOLD))

        self.labelChannelID.place(x=2 , y=155 + 5)

        self.svChannelID = Label(master=self.tabVidInfo , text=None , font=('normal' , 10 , BOLD))

        self.svChannelID.place(x=130 , y=155 + 5)

        self.labelLiveContent = Label(master=self.tabVidInfo , text='Live Content :' , font=('normal' , 12 , BOLD))

        self.labelLiveContent.place(x=2 , y=190 + 5)

        self.svLiveContent = Label(master=self.tabVidInfo , text=None , font=('normal' , 10 , BOLD))

        self.svLiveContent.place(x=140 , y=190 + 5)

        self.labelLengthSize = Label(master=self.tabVidInfo , text='Video Size :' , font=('normal' , 12 , BOLD))

        self.labelLengthSize.place(x=2 , y=225 + 5)

        self.svVideoSize = Label(master=self.tabVidInfo , text=None , font=('normal' , 10 , BOLD))

        self.svVideoSize.place(x=110 , y=225 + 5)

        setBySystemTheme()

        self.root.mainloop()


def main() -> Literal[None]:
    YoutubeDownloader()


if (__name__ == '__main__'):
    main()