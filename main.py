import tkinter as tk
from tkinter.ttk import *
import threading
import wget
import os
from functools import partial
from Animations import Header_Menu_Animation
from Backend import Feature_Set_Backend, Download_Backend, Device_Download_Backend, Build_Download_Backend

app = tk.Tk()
app.geometry('600x400')
app.resizable(0,0)
app.title('PA')

BASE_BACKGROUND = '#292929'
HEADER_BASE_COLOR = '#F5F5F5'
HEADER_COLOR_PRIMARY = '#1c1c1c'
HEADER_COLOR_SECONDARY = '#8ec63e'

Home_Background_Image = tk.PhotoImage(file = "src/home_background.png")
Header_Menu_Image = tk.PhotoImage(file = "src/menu.png")
Menu_Back_Image = tk.PhotoImage(file = "src/back.png")

ICON = tk.PhotoImage(file = 'src/pa-icon.png')
app.iconphoto(False, ICON)

app.configure(background=BASE_BACKGROUND)

def Home_Page():

	def Threading_Button_Menu(Frame_,target_def):
		
		Label_ = tk.Label(Frame_, text = 'Loading...', font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
		Label_.place(relx=0.04 , rely= 0.88 )
		b_ = tk.Button(Frame_, text='Download', bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_COLOR_SECONDARY, font=('Helvetica', 14,'bold'), highlightthickness=0)
		b_.place(relx=0.54 , rely= 0.6 )
		b_["state"] = "disabled"
		_ = threading.Thread(target=target_def,)
		_.start()

	def Threading_Button_Model(Frame_,target_def):
		
		Label_ = tk.Label(Frame_, text = 'Retrieving Build...', font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
		Label_.place(relx=0.64 , rely= 0.36 )
		b_ = tk.Button(Frame_,text='Next', bd = 0, bg = BASE_BACKGROUND, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), highlightthickness=0,)
		b_.place(relx=0.72 , rely= 0.238, relheight= 0.08 ,relwidth= 0.2  )
		b_["state"] = "disabled"
		_ = threading.Thread(target=target_def,)
		_.start()
		

	def Threading_Button_Build(Frame_,target_def):
		Label_ = tk.Label(Frame_, text = 'Retrieving Build info...', font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
		Label_.place(relx=0.64 , rely= 0.84 )
		b_ = tk.Button(Frame_,text='Next', bd = 0, bg = BASE_BACKGROUND, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), highlightthickness=0,)
		b_.place(relx=0.72 , rely= 0.718, relheight= 0.08 ,relwidth= 0.2  )
		b_["state"] = "disabled"
		_ = threading.Thread(target=target_def,)
		_.start()
		

	############################# HEADER ###########################################################################################
	def Menu_Page():

		def Download_Page():

			def Feature_Back_Home():
				Header_Frame = Header_Menu_Animation(app)
				Menu_Page()

			def Device_Model_Selected():


				def Device_Model_Final():

					def Device_Build_Download(Build_Link):

						Build_Name = Build_Link[0].split('/')[-1]

						if os.path.exists('Downloads') == False:
							os.mkdir('Downloads')

						Download_Dir_Final = f'{os.getcwd()}/Downloads/'

						Device_Build_Download_Frame = Header_Menu_Animation(app)
						Downloading_Label = tk.Label(Device_Build_Download_Frame, text = 'Downloading ...', font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
						Downloading_Label.place(relx=0.04 , rely= 0.08 )
						progress_ = Progressbar(Device_Build_Download_Frame, orient = tk.HORIZONTAL,length = 100, mode = 'determinate')
						progress_.place(relx=0.2 , rely= 0.48, relheight= 0.08 ,relwidth= 0.6)

						perc = tk.StringVar()
						perc.set('0')

						Downloaded_Percentage_Label = tk.Label(Device_Build_Download_Frame, text = f'{perc}% Completed', font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
						Downloaded_Percentage_Label.place(relx=0.2 , rely= 0.6 )

						def Download_Indicator(current, total, width=80):

							Download_Completed_Percentage = round((current / total * 100),2)
							progress_['value'] = Download_Completed_Percentage
							perc.set(Download_Completed_Percentage)
							Downloaded_Percentage_Label.config(text=f'{Download_Completed_Percentage}% Completed')
							Device_Build_Download_Frame.update_idletasks()
							if int(Download_Completed_Percentage) == 100:
								Downloaded_Percentage_Label.config(text=f'Done Downloading')
								Build_Downloaded_Name_Label = tk.Label(Device_Build_Download_Frame, text = Build_Name, font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
								Build_Downloaded_Name_Label.place(relx=0.2 , rely= 0.66)
								Build_Downloaded_Dir_Label = tk.Label(Device_Build_Download_Frame, text = 'Check inside Downloads Folder', font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
								Build_Downloaded_Dir_Label.place(relx=0.2 , rely= 0.76)

						wget.download(Build_Link[0], bar=Download_Indicator, out=Download_Dir_Final)

					
					Device_Build_Selected = Build_Selected.get()
					Device_Selected_Codename = Device_Selected.get()
					Device_Selected_Codename = Device_Selected_Codename.split('(')[1].split(')')[0]
					Build_Title, Build_Date, Build_Link_Info, Build_Link_Download = Build_Download_Backend(Device_Selected_Codename, Device_Build_Selected)
					Device_Model_Frame = Header_Menu_Animation(app)

					Build_Label = tk.Label(Device_Model_Frame, text = Build_Title[0], font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
					Build_Label.place(relx=0.04 , rely= 0.08 )
					tk.Label(Device_Model_Frame, text = 'Date : ', font=('calibre', 12,'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY).place(relx=0.1 , rely= 0.24 )
					Build_Content_Date = tk.Label(Device_Model_Frame, text = Build_Date[0], font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
					Build_Content_Date.place(relx=0.14 , rely= 0.3 )
					tk.Label(Device_Model_Frame, text = 'Info : ', font=('calibre', 12,'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY).place(relx=0.1 , rely= 0.4 )
					Build_Content_Link_Info = tk.Label(Device_Model_Frame, text = Build_Link_Info[0], font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
					Build_Content_Link_Info.place(relx=0.14 , rely= 0.46)
					tk.Label(Device_Model_Frame, text = 'Download Link : ', font=('calibre', 12,'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY).place(relx=0.1 , rely= 0.56 )
					Build_Content_Link_Download = tk.Entry(Device_Model_Frame, font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
					Build_Content_Link_Download.place(relx=0.14 , rely= 0.62, relheight= 0.08 ,relwidth= 0.62)
					Build_Content_Link_Download.insert(-1, Build_Link_Download[0])
					Build_Download_Button = tk.Button(Device_Model_Frame,text='Download', bd = 0, bg = BASE_BACKGROUND, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), highlightthickness=0, command = partial(Device_Build_Download, Build_Link_Download))
					Build_Download_Button.place(relx=0.72 , rely= 0.82, relheight= 0.08 ,relwidth= 0.2  )

				Device_Selected_Codename = Device_Selected.get()
				Device_Selected_Codename = Device_Selected_Codename.split('(')[1].split(')')[0]
				Version_Available = Device_Download_Backend(Device_Selected_Codename)

				Build_Label_Select = tk.Label(Download_Frame, text = 'Select Build', font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
				Build_Label_Select.place(relx=0.04 , rely= 0.56 )

				Build_Selected = tk.StringVar()
				Build_Selected.set( Version_Available[0] )
				  
				Build_Dropdown = tk.OptionMenu( Download_Frame , Build_Selected , *Version_Available )
				Build_Dropdown.place(relx=0.08 , rely= 0.72 )

				Next_Button = tk.Button(Download_Frame,text='Next', bd = 0, bg = BASE_BACKGROUND, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), highlightthickness=0, command = partial(Threading_Button_Build,Download_Frame, Device_Model_Final))
				Next_Button.place(relx=0.72 , rely= 0.718, relheight= 0.08 ,relwidth= 0.2  )


			Device_Name_List, Device_Codename_List = Download_Backend()
			Download_Frame = Header_Menu_Animation(app)
			Device_Final_List = []
			for i in range(len(Device_Name_List)):
				Device_Final_List.append(f'{Device_Name_List[i]} ({Device_Codename_List[i]})')

			Download_Label_Select = tk.Label(Download_Frame, text = 'Select Your Device', font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
			Download_Label_Select.place(relx=0.04 , rely= 0.08 )

			Device_Selected = tk.StringVar()
			Device_Selected.set( Device_Final_List[0] )
			  
			Device_Dropdown = tk.OptionMenu( Download_Frame , Device_Selected , *Device_Final_List )
			Device_Dropdown.place(relx=0.08 , rely= 0.24 )
			Back_Button = tk.Button(Download_Frame, bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), image = Menu_Back_Image, highlightthickness=0, command = Feature_Back_Home)
			Back_Button.place(relx=0.88 , rely= 0.06 )
			Next_Button = tk.Button(Download_Frame,text='Next', bd = 0, bg = BASE_BACKGROUND, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), highlightthickness=0, command = partial(Threading_Button_Model, Download_Frame, Device_Model_Selected))
			Next_Button.place(relx=0.72 , rely= 0.238, relheight= 0.08 ,relwidth= 0.2  )


		Header_Frame = Header_Menu_Animation(app)
		Header_Label_1 = tk.Label(Header_Frame, text = 'paranoid', font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
		Header_Label_1.place(relx=0.06 , rely= 0.268 )
		Header_Label_2 = tk.Label(Header_Frame, text = 'android', font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_SECONDARY)
		Header_Label_2.place(relx=0.26 , rely= 0.268 )
		Team_Button = tk.Button(Header_Frame, text='Team (Coming Soon...)', bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_COLOR_SECONDARY, font=('Helvetica', 14,'bold'), highlightthickness=0)
		Team_Button.place(relx=0.54 , rely= 0.4 )
		Wallpapper_Button = tk.Button(Header_Frame, text='Wallpaper (Coming Soon...)', bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_COLOR_SECONDARY, font=('Helvetica', 14,'bold'), highlightthickness=0)
		Wallpapper_Button.place(relx=0.54 , rely= 0.5 )
		Download_Button = tk.Button(Header_Frame, text='Download', command =partial(Threading_Button_Menu,Header_Frame, Download_Page), bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_COLOR_SECONDARY, font=('Helvetica', 14,'bold'), highlightthickness=0)
		Download_Button.place(relx=0.54 , rely= 0.6 )
		Blog_Button = tk.Button(Header_Frame, text='Blog (Coming Soon...)', bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_COLOR_SECONDARY, font=('Helvetica', 14,'bold'), highlightthickness=0)
		Blog_Button.place(relx=0.54 , rely= 0.7 )

		def Menu_Back_Home():
			Header_Frame = Header_Menu_Animation(app)
			Home_Page()

		Back_Button = tk.Button(Header_Frame, bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), image = Menu_Back_Image, highlightthickness=0, command = Menu_Back_Home)
		Back_Button.place(relx=0.88 , rely= 0.06 )

	Header_Frame = tk.Frame(app, background = HEADER_BASE_COLOR)
	Header_Frame.place(relx=0.0 , rely= 0.0 , relheight= 0.2 ,relwidth= 1 )
	Header_Label_1 = tk.Label(Header_Frame, text = 'paranoid', font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
	Header_Label_1.place(relx=0.06 , rely= 0.268 )
	Header_Label_2 = tk.Label(Header_Frame, text = 'android', font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_SECONDARY)
	Header_Label_2.place(relx=0.26 , rely= 0.268 )
	Menu_Button = tk.Button(Header_Frame, bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), image = Header_Menu_Image, highlightthickness=0, command = Menu_Page)
	Menu_Button.place(relx=0.88 , rely= 0.3 )


	############################## HOME #############################################################################################
	def Feature_Back_Home():
			Header_Frame = Header_Menu_Animation(app)
			Home_Page()
	def Threading_Button(target_def):
		Frame_ = Header_Menu_Animation(app)
		Label_ = tk.Label(Frame_, text = 'Loading...', font=('calibre', 20, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
		Label_.place(relx=0.06 , rely= 0.26 )
		_ = threading.Thread(target=target_def,)
		_.start()

	def Feature_Page():
		
		Feature_Heading,Feature_p, Feature_li1, Feature_li2 = Feature_Set_Backend()
		Feature_Frame = Header_Menu_Animation(app)
		Back_Button = tk.Button(Feature_Frame, bd = 0, bg = HEADER_BASE_COLOR, fg=HEADER_BASE_COLOR, font=('Helvetica', 14,), image = Menu_Back_Image, highlightthickness=0, command = Feature_Back_Home)
		Back_Button.place(relx=0.88 , rely= 0.84 )

		Feature_Label_1 = tk.Label(Feature_Frame, text = Feature_p[0], font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
		Feature_Label_1.place(relx=0.04 , rely= 0.04 )
		n = 0.1
		for item in Feature_li1:
			n += 0.044
			Feature_Label_1 = tk.Label(Feature_Frame, text = item, font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
			Feature_Label_1.place(relx=0.08 , rely= n )

		Feature_Label_2 = tk.Label(Feature_Frame, text = Feature_p[1], font=('calibre', 18, 'bold'), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
		Feature_Label_2.place(relx=0.58 , rely= 0.04 )
		n = 0.1
		for item in Feature_li2:
			n += 0.048
			Feature_Label_1 = tk.Label(Feature_Frame, text = item, font=('calibre', 12,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
			Feature_Label_1.place(relx=0.62 , rely= n )

	Home_Frame = tk.Frame(app, background = HEADER_BASE_COLOR)
	Home_Frame.place(relx=0.0 , rely= 0.2 , relheight= 0.8 ,relwidth= 1 )
	Home_Background = tk.Label(Home_Frame, image = Home_Background_Image)
	Home_Background.place(relx=0.0 , rely= 0.0, relheight= 1 ,relwidth= 1 )
	Home_Secondary_Frame = tk.Frame(Home_Frame, background = HEADER_BASE_COLOR)
	Home_Secondary_Frame.place(relx=0.0 , rely= 0.88 , relheight= 0.12 ,relwidth= 1 )
	Header_Label_2 = tk.Label(Home_Secondary_Frame, text = 'PA 10 Quartz has been released', font=('calibre', 14,), bd=0, bg=HEADER_BASE_COLOR, fg=HEADER_COLOR_PRIMARY)
	Header_Label_2.place(relx=0.02 , rely= 0.18 )
	Home_Feature_Button = tk.Button(Home_Secondary_Frame,text='Feature Set  > ', bd = 0, bg = HEADER_BASE_COLOR, fg='#536DFE', font=('Helvetica', 16,'bold'), highlightthickness=0, command = partial(Threading_Button, Feature_Page))
	Home_Feature_Button.place(relx=0.64 , rely= 0.0 , relwidth=0.4, relheight=1)

Home_Page()
app.mainloop()