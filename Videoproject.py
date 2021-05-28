from tkinter import *
import tkinter.ttk
from tkinter import filedialog
from moviepy.editor import *
from tkinter import filedialog
from tkinter import font




#Interface
class The_Interface:
    ColorListe = TextClip.list("color")
    Seconds = []
    Durations = []
    FontListe = TextClip.list('font')
    Sizes = list(range(1,300))
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.grid_columnconfigure(0,weight=1)
        self.fenetre.grid_rowconfigure(0,weigh=1)
        self.xcan = Canvas(self.fenetre,bg = "dark grey",width = 900,height = 600)
        self.xcan.grid(row=0,column=0,sticky=N+S+W+E)
        self.xcan.create_window(10,10,anchor =NW, window=Label(self.fenetre,text="Header color",bg="grey",fg ="dark blue"))
        self.xcan.create_window(10,50,anchor=NW,window=Label(self.fenetre,text="Footer color", bg ="grey", fg ="dark red"))
        self.Hcolor = StringVar()
        self.HeaderColor = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Hcolor, width = 10)
        self.HeaderColor["value"] = self.ColorListe
        self.HeaderColor.current(10)
        self.xcan.create_window(90,10,anchor = NW, window = self.HeaderColor)
        self.Fcolor = StringVar()
        self.FooterColor = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Fcolor, width = 10)
        self.FooterColor["value"] = self.ColorListe
        self.FooterColor.current(17)
        self.xcan.create_window(90,50,anchor = NW, window = self.FooterColor)
        self.FooterBut = Button(self.fenetre, text = "Add footer", bg ="dark grey", command = self.Footer)
        self.xcan.create_window(180,50,anchor = NW,window=self.FooterBut)
        self.HeaderBut = Button(self.fenetre, text = "Add header", bg ="dark grey", command = self.Header)
        self.xcan.create_window(180,10,anchor=NW,window=self.HeaderBut)
        self.xcan.create_rectangle(5,5,260,80, fill = "grey")

        self.xcan.create_window(10,120, anchor =NW,window=Label(self.fenetre,text = "Add a message at the end of the video", bg="grey", fg = "dark red"))
        self.Last_Texte = Text(self.fenetre,width = 26, height = 5)
        self.xcan.create_window(10,150,anchor =NW,window=self.Last_Texte)
        self.xcan.create_window(10,240,anchor=NW,window=Label(self.fenetre, text = "Color", bg="grey", fg ="dark red"))
        self.Last_C = StringVar()
        self.Last_Color = tkinter.ttk.Combobox(self.fenetre,textvariable = self.Last_C, width = 24)
        self.xcan.create_window(55,240, anchor =NW, window = self.Last_Color)
        self.Last_Color["value"] = self.ColorListe
        self.Last_Color.current(3)

        self.xcan.create_window(10,270,anchor=NW,window=Label(self.fenetre, text = "Font", bg="grey", fg ="dark red"))
        self.Last_F = StringVar()
        self.Last_Font = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Last_F, width = 24)
        self.xcan.create_window(55, 270,anchor=NW, window=self.Last_Font)
        self.Last_Font["value"] = self.FontListe
        self.Last_Font.current(0)

        self.xcan.create_window(10,300,anchor=NW,window=Label(self.fenetre, text = "Size", bg="grey", fg ="dark red"))
        self.Last_Si = IntVar()
        self.Last_Size = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Last_Si, width = 24)
        self.xcan.create_window(55, 300,anchor=NW, window=self.Last_Size)
        self.Last_Size["value"] = self.Sizes
        self.Last_Size.current(45)

        self.xcan.create_window(10,330,anchor=NW,window=Label(self.fenetre, text = "Background", bg="grey", fg ="dark red"))
        self.Last_B = StringVar()
        self.Last_Background = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Last_B, width = 19)
        self.xcan.create_window(85, 330,anchor=NW, window=self.Last_Background)
        self.New_C_Liste = ["transparent"] + self.ColorListe 
        self.Last_Background["value"] = self.New_C_Liste
        self.Last_Background.current(0)

        self.xcan.create_window(10,360,anchor=NW,window=Label(self.fenetre, text = "Seconds before end", bg="grey", fg ="dark red"))
        self.Last_S = DoubleVar()
        self.Last_Seconds = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Last_S, width = 13)
        self.xcan.create_window(122, 360,anchor=NW, window=self.Last_Seconds)
        self.Last_Seconds["value"] = self.Seconds
        
        self.AddEnd = Button(self.fenetre, text = "Add End Message", bg ="dark red", fg="white", width = 29,command = self.AddEnd)
        self.xcan.create_window(10, 390,anchor=NW, window=self.AddEnd)
        self.xcan.create_rectangle(5,110,233,430,fill = "grey")

        self.xcan.create_window(208,500, anchor=NW, window=Label(self.fenetre,text ="Fps", bg = "dark grey",fg="dark red"))
        self.FPS = Entry(self.fenetre)
        self.xcan.create_window(238,500,anchor=NW,window=self.FPS)
        self.FPS.insert(0,"Default")

        self.xcan.create_window(445,500, anchor=NW, window=Label(self.fenetre,text ="Format", bg = "dark grey",fg="dark blue"))
        self.Format = Entry(self.fenetre)
        self.xcan.create_window(495,500,anchor=NW,window=self.Format)
        self.Format.insert(0,"mp4")

        self.xcan.create_window(325,470, anchor=NW, window=Label(self.fenetre,text ="Name", bg = "dark grey"))
        self.Name = Entry(self.fenetre)
        self.xcan.create_window(365,470,anchor=NW,window=self.Name)
        
        

        
        
        

        
        self.Upload = Button(self.fenetre, text = "Upload video", bg ="dark grey", width = 20, command = self.Upload)
        self.xcan.create_window(340,10,anchor=NW,window=self.Upload)
        self.LabelPath = Label(self.fenetre,text="Path : ",bg ="dark grey")
        self.xcan.create_window(340,90,anchor=NW,window=self.LabelPath)
        self.xcan.create_window(600,10, anchor=NW, window=Label(self.fenetre,text ="In Second", bg = "dark grey", fg = "dark blue"))
        self.xcan.create_window(600,50, anchor=NW, window=Label(self.fenetre,text ="Duration(s)", bg = "dark grey", fg = "dark blue"))
        self.Min = DoubleVar()
        self.MinCombo = tkinter.ttk.Combobox(self.fenetre,textvariable = self.Min, width = 10,state ="readonly")
        self.xcan.create_window(670,10,anchor=NW,window=self.MinCombo)
        self.Dur = DoubleVar()
        self.DurCombo = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Dur, width = 10)
        self.xcan.create_window(670,50,anchor=NW,window=self.DurCombo)
        self.xcan.create_window(600,90, anchor=NW, window=Label(self.fenetre,text ="In position", bg = "dark grey", fg = "dark blue"))
        #670 90
        self.InPos = StringVar()
        self.Position = tkinter.ttk.Combobox(self.fenetre, textvariable = self.InPos, width = 10)
        self.xcan.create_window(670,90, anchor = NW, window = self.Position)
        self.Position["value"] = ["header", "footer"]
        self.Position.current(0)
        self.MinCombo["value"] = self.Seconds
        self.DurCombo["value"] = self.Durations
        

        self.xcan.create_window(600,130, anchor=NW, window=Label(self.fenetre,text ="Size", bg = "dark grey", fg = "dark blue"))
        self.Size = IntVar()
        self.The_Size = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Size,width = 10)
        self.xcan.create_window(670,130, anchor=NW, window = self.The_Size)
        self.The_Size["value"] = self.Sizes
        self.The_Size.current(23)

        self.xcan.create_window(600,170, anchor=NW, window=Label(self.fenetre,text ="Color", fg = "dark blue",bg = "dark grey"))
        self.La_Couleur = StringVar()
        self.La_Coul = tkinter.ttk.Combobox(self.fenetre, textvariable = self.La_Couleur,width = 10)
        self.xcan.create_window(670,170, anchor=NW, window = self.La_Coul)
        self.La_Coul["value"] = self.ColorListe
        self.La_Coul.current(7)

        self.xcan.create_window(600,210, anchor=NW, window=Label(self.fenetre,text ="Font",fg = "dark blue", bg = "dark grey"))
        self.Font = StringVar()
        self.Fo = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Font,width = 10)
        self.xcan.create_window(670,210, anchor=NW, window = self.Fo)
        self.Fo["value"] = self.FontListe
        self.Fo.current(0)

        

        
        
        
        
       

        self.AddText = Button(self.fenetre, text = "Add text", bg ="dark grey",fg ="dark blue", width = 10, height = 13, command = self.AddText)
        self.xcan.create_window(760,15,anchor=NW,window=self.AddText)
        self.xcan.create_rectangle(580,5,795,332)
        self.ExportBut = Button(self.fenetre, text = "EXPORT", bg="dark grey", width = 110, command = self.Export)
        self.xcan.create_window(10,560,anchor=NW, window=self.ExportBut)
        self.PreviewBut = Button(self.fenetre, text = "Preview", bg ="dark grey", width = 110, command = self.Preview)
        self.xcan.create_window(10,530,anchor = NW, window = self.PreviewBut)
        self.Adder_texte = Text(self.fenetre, width = 24, height = 5)
        self.xcan.create_window(590,240,anchor =NW, window = self.Adder_texte)

        

    

        

        
        

        
        self.clip = ""

    def AddEnd(self):
        self.Last_Text_Message = TextClip(self.Last_Texte.get(0.0,END),font = self.Last_F.get(),color=self.Last_C.get(),fontsize = self.Last_Si.get(), bg_color = self.Last_B.get(),size=(self.clip.size[0],self.clip.size[1]))
        self.Last_Text_Message = self.Last_Text_Message.set_duration(abs(self.Last_S.get()))
        self.Last_Text_Message = self.Last_Text_Message.set_start(self.clip.duration + self.Last_S.get())
        self.clip = CompositeVideoClip([self.clip,self.Last_Text_Message])
    def Preview(self):
        self.clip.preview()
    def Export(self):
        
        self.clip.write_videofile(str(self.Name.get())+"Modified."+ str(self.Format.get()),fps = float(self.FPS.get()))
        
                                  
    def AddText(self):
        self.Text_Adding = self.Adder_texte.get(0.0,END)
        self.Texting = TextClip(self.Text_Adding,color=self.La_Couleur.get(),fontsize = self.Size.get(),font = self.Font.get())
        
        if self.InPos.get() == "header":
            self.Texting = self.Texting.set_pos(("center","top"))
        else:
            self.Texting = self.Texting.set_pos(("center","bottom"))
            

        self.Texting = self.Texting.set_duration(self.Dur.get())
        self.Texting = self.Texting.set_start(self.Min.get())
        
        
        self.clip = CompositeVideoClip([self.clip,self.Texting])
        
    def Upload(self):
        file = filedialog.askopenfilename()
        faa = file.split("/")
        
        faa2 = faa[len(faa)-1]
        faa2 = faa2.split(".")
        
        Le_NomX = faa2[0]
        Le_Extension = faa2[1]
        
        
        self.Name.delete(0,END)
        self.Name.insert(0, str(Le_NomX)+"Modified")
        
        self.LabelPath.configure(text = "Path : " + str(file),fg ="red")
        self.Upload.configure(text="Change video")
        self.clip = VideoFileClip(file)
        self.La_Duree = list()
        self.i = 0
        self.a = 0
        while self.i <= self.clip.duration:
            self.La_Duree.append(self.a)
            self.Une_D = float(self.a) + 0.5
            self.La_Duree.append(self.Une_D)
       
            self.a += 1
            self.i += 1

        self.Negative = [-x for x in self.La_Duree]
        self.Final_Duree = self.La_Duree + self.Negative
        self.MinCombo["value"] = self.Final_Duree
        self.DurCombo["value"] = self.Final_Duree
        self.Last_Seconds["value"] = self.Negative
        self.FPS.delete(0,END)
        try:
            type(self.clip.fps) == float
            self.FPS.insert(0, self.clip.fps)
        except:
            
            self.FPS.insert(0,30.0)
        
    def Footer(self):
        self.txt_clipF = TextClip(" ",size=(self.clip.size[0],self.clip.size[1]/7),bg_color=self.Fcolor.get(), color = self.Fcolor.get())
        self.txt_clipF = self.txt_clipF.set_pos((0,"bottom")).set_duration(self.clip.duration)
        self.clip = CompositeVideoClip([self.clip, self.txt_clipF])
        self.FooterBut.configure(bg = self.Fcolor.get())
    def Header(self):
        self.txt_clipH = TextClip(" ",size=(self.clip.size[0],self.clip.size[1]/7),bg_color=self.Hcolor.get(), color = self.Hcolor.get())
        self.txt_clipH = self.txt_clipH.set_pos((0,"top")).set_duration(self.clip.duration)
        self.clip = CompositeVideoClip([self.clip,self.txt_clipH])
        self.HeaderBut.configure(bg = self.Hcolor.get())
                                 
        
        


#Create d'un objet interface
My_Interface = The_Interface
My_Interface()


        
