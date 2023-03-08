import pandas as pd
from tkinter import *

#importing the data from a csv file and creating a dictionary with column headings as keys
data = pd.read_csv(r'dataset.csv')
dict1 = data.to_dict(orient='list')
#Creating empty lists to add the genre classified songs
ls_pop = []
ls_rnb = []
ls_rock = []
ls_rap = []
ls_emo = []
ls_dance = []
ls_hiphop = []
ls_edm = []

#loop to lookup and classify the song's genre
for i in range(len(dict1['top genre'])):
  if 'boy band' in dict1['top genre'][i]:
    dict1['top genre'][i] = 'pop rock'
  if 'latin' in dict1['top genre'][i]:
    dict1['top genre'][i] = 'pop'
  if 'neo soul' in dict1['top genre'][i]:
    dict1['top genre'][i] = 'r&b'
  if 'pop' in dict1['top genre'][i]:
    ls_pop.append(dict1['top genre'][i])
  if 'r&b' in dict1['top genre'][i]:
    ls_rnb.append(dict1['top genre'][i])
  if 'rock' in dict1['top genre'][i]:
    ls_rock.append(dict1['top genre'][i])
  if 'rap' in dict1['top genre'][i]:
    ls_rap.append(dict1['top genre'][i])
  if 'emo' in dict1['top genre'][i]:
    ls_emo.append(dict1['top genre'][i])
  if 'dance' in dict1['top genre'][i]:
    ls_dance.append(dict1['top genre'][i])
  if ' hip hop' in dict1['top genre'][i]:
    ls_hiphop.append(dict1['top genre'][i])
  if 'electro' in dict1['top genre'][i]:
    ls_edm.append(dict1['top genre'][i])


#defining a class for the buttons with methods to define behaviour and appearance of the buttons

class buttons(Button):
  def __init__(self, *args, **kwargs):
    Button.__init__(self, *args, **kwargs)
  
  def button_state(self, state='active'):
    self.config(state=state)

  def button_design(self, background='grey'):
    self.config(bg = background)

#defining a class for the appearance of the drop down lists
class dropdowns(OptionMenu):
  def __init__(self, *args, **kwargs):
    OptionMenu.__init__(self, *args, **kwargs)
    self.config(bg = 'pink')
    
#defining a class to specify behaviour of the generate playlist button
class main_info:
  def __init__(self, option):
    self.option = option

  def get_selection(self):
    selection = self.option
    print(selection)

  def genre_get_playlist(self):
    playlist = generate_playlist_genre(self.option)
    return playlist

  def year_get_playlist(self):
    playlist = generate_playlist_year(self.option)
    print(playlist)
    return playlist

  def length_get_playlist(self):
    playlist = generate_playlist_length(self.option)
    print(playlist)
    return playlist

  def popularity_get_playlist(self):
    playlist = generate_playlist_popularity(self.option)
    print(playlist)
    return playlist
#function to activate button after a field is selected first
def button_activate(*args):
  genre = clicked1.get()
  if genre == 'Filter':
    button_generate_playlist.button_state('disabled')
  else:
    button_generate_playlist.button_state('active')

#function to open new window when specific buttons are clicked
def onclick():
  root.withdraw()
  new_window(clicked1.get(), clicked2.get())

#function to display the currated playlist on the new window   
def get_playlist_for_display():
  if clicked1.get() == 'Genre':
    playlist = main_info(clicked2.get()).genre_get_playlist()
  elif clicked1.get() == 'Year':
    playlist =  main_info(clicked2.get()).year_get_playlist()
  elif clicked1.get() == 'Length':
    playlist =  main_info(clicked2.get()).length_get_playlist()
  elif clicked1.get() == 'Popularity':
    playlist = main_info(clicked2.get()).popularity_get_playlist()
  return playlist




'''Function to generate playlist on basis of genre'''


def generate_playlist_genre(clicked):

  playlist = {}
  lstitle = []
  lsartist = []
  #for i in range(len(options)):
  if clicked == 'Pop':
    ls = ls_pop
  elif clicked == 'Dance':
    ls = ls_dance
  elif clicked == 'Rap':
    ls = ls_rap
  elif clicked == 'Rock':
    ls = ls_rock
  elif clicked == 'R&B':
    ls = ls_rnb
  elif clicked == 'Emo':
    ls = ls_emo
  elif clicked == 'Edm':
    ls = ls_edm
  elif clicked == 'Hip Hop':
    ls = ls_hiphop

  for element in ls:
    #print(element)
    for i in range(len(dict1['top genre'])):
      if element == dict1['top genre'][i]:
        first = dict1['title'][i]
        second = dict1['artist'][i]
        #         # print(dict1['top genre'])
        #         # print('\n')
        #         # print(first)
        #         # print(second)
        lstitle.append(first)
        lsartist.append(second)
  playlist = dict(zip(lstitle, lsartist))
  return (playlist)

  # print(lstitle)
  # print('\n')
  # print(lsartist)


"""function to generate playlist on basis of year"""


def generate_playlist_year(clicked):
  playlist = {}
  lstitle = []
  lsartist = []
  ls_1900s = []
  ls_2010s = []
  ls_2015s = []
  ls_2020s = []

  for i in range(len(dict1['year'])):
    if 2000 > dict1['year'][i]:
      ls_1900s.append(dict1['year'][i])
    elif 2000 <= dict1['year'][i] < 2010:
      ls_2010s.append(dict1['year'][i])
    elif 2010 <= dict1['year'][i] < 2015:
      ls_2015s.append(dict1['year'][i])
    else:
      ls_2020s.append(dict1['year'][i])

  if clicked == "Before 2000s":
    ls = ls_1900s
  elif clicked == "2000 to 2010":
    ls = ls_2010s
  elif clicked == "2010 to 2015":
    ls = ls_2015s
  elif clicked == "2015 to 2021":
    ls = ls_2020s
  for element in ls:
    for i in range(len(dict1['year'])):
      if element == dict1['year'][i]:
        first = dict1['title'][i]
        second = dict1['artist'][i]
        lstitle.append(first)
        lsartist.append(second)
    
  playlist = dict(zip(lstitle, lsartist))
  return (playlist)

"""function to generate playlist on basis of length"""

def generate_playlist_length(clicked):
  playlist = {}
  lstitle = []
  lsartist = []
  ls_2min = []
  ls_3min = []
  ls_4min = []
  ls_5min = []

  for i in range(len(dict1['length'])):
    if 120 > dict1['length'][i]:
      ls_2min.append(dict1['length'][i])
    elif 120 <= dict1['length'][i] < 180:
      ls_3min.append(dict1['length'][i])
    elif 180 <= dict1['length'][i] < 240:
      ls_4min.append(dict1['length'][i])
    else:
      ls_5min.append(dict1['length'][i])

  if clicked == "1 to 2 min":
    ls = ls_2min
  elif clicked == "2 to 3 min":
    ls = ls_3min
  elif clicked == "3 to 4 min":
    ls = ls_4min
  elif clicked == "4 to 5 min":
    ls = ls_5min

  for element in ls:
    for i in range(len(dict1['length'])):
      if element == dict1['length'][i]:
        first = dict1['title'][i]
        second = dict1['artist'][i]
        lstitle.append(first)
        lsartist.append(second)
  playlist = dict(zip(lstitle, lsartist))
  return (playlist)

"""function to generate playlist on basis of popularity"""

def generate_playlist_popularity(clicked):
  playlist = {}
  lstitle = []
  lsartist = []
  ls_25=[]
  ls_50=[]
  ls_75 = []
  ls_100 = []
  
  for i in range(len(dict1['popularity'])):
    if 25 > dict1['popularity'][i]:
      ls_25.append(dict1['popularity'][i])
    elif 25 <= dict1['popularity'][i] < 50:
      ls_50.append(dict1['popularity'][i])
    if 50 <= dict1['popularity'][i] < 75:
      ls_75.append(dict1['popularity'][i])
    else:
      ls_100.append(dict1['popularity'][i])
  if clicked == "0 to 25 %":
    ls = ls_25
  elif clicked == "25 to 50 %":
    ls = ls_50
  if clicked == "50 to 75 %":
    ls = ls_75
  elif clicked == "75 to 100 %":
    ls = ls_100

  for element in ls:
    for i in range(len(dict1['popularity'])):
      if element == dict1['popularity'][i]:
        first = dict1['title'][i]
        second = dict1['artist'][i]
        lstitle.append(first)
        lsartist.append(second)
  playlist = dict(zip(lstitle, lsartist))
  return (playlist)

def appear(filter):
  global drop2, selected_filter
  clicked2.set('Select Option')

  if filter == 'Genre':
    drop2 = dropdowns(root, clicked2, *options_genre)
    drop2['menu'].config(bg='white')
    drop2.place(x = label_x, y = filter_y + 100, width = 120, height = 25)
  elif filter == 'Year':
    drop2 = dropdowns(root, clicked2, *options_year)
    drop2['menu'].config(bg='white')
    drop2.place(x = label_x, y = filter_y + 100, width = 120, height = 25)
  elif filter == 'Length':
    drop2 = dropdowns(root, clicked2, *options_length)
    drop2['menu'].config(bg='white')
    drop2.place(x = label_x, y = filter_y + 100, width = 120, height = 25)
  elif filter == 'Popularity':
    drop2 = dropdowns(root, clicked2, *options_popularity)
    drop2['menu'].config(bg='white')
    drop2.place(x = label_x, y = filter_y + 100, width = 120, height = 25)
  
  clicked2.trace('w', button_activate)
  selected_filter = my_canvas.create_text(250, filter_y + 10, text = F'Filter: {clicked1.get()}', font =('Times New Roman', 18), fill='dark blue')
  drop1.place_forget()


def reset():
  clicked1.set("Filter")
  clicked2.set("Select Option")
  drop1.place(x = label_x, y = filter_y, width = 120, height =30)
  drop2.place_forget()
  my_canvas.itemconfigure(selected_filter, state='hidden')
  button_generate_playlist.config(state='disabled')

def new_window(filter, type):
  new_window = Toplevel(root)
  new_window.title("Playlist Generator")
  window_width = 500 #ww
  window_height = 678 #wh

  new_window.resizable(False, False)
  new_window.geometry(F'{window_width}x{window_height}')

  frame=Frame(new_window,width=window_width, height=window_height)
  frame.pack(fill='both', expand = True)

  my_canvas = Canvas(frame, width=window_width, height=window_height)
  my_canvas.pack(fill="both", expand=True)

  scrollbar = Scrollbar(my_canvas, orient=VERTICAL, command=my_canvas.yview)
  scrollbar.pack(side=RIGHT, fill=Y)
  
  my_canvas.config(yscrollcommand=scrollbar.set)
  my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

  def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

  my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
  top_msg = Frame(my_canvas,width=window_width, height=100)
  top_msg.place(x=0,y=0)
  my_canvas.create_window((0,0), window=top_msg, anchor="nw")
  playlist_table = Frame(my_canvas,width=window_width,height=window_height-82)
  playlist_table.place(x=0,y=0)
  my_canvas.create_window((0,100), window=playlist_table, anchor="nw")

  altura = 0

  first_line = Label(top_msg, text="😊Enjoy your playlist😊", font=('Times New Roman', 20, 'underline'), anchor='n').place(x=112.5, y=10)
  filter_name = Label(top_msg, text=F"{filter}: {type}", anchor='n', font=('Times New Roman', 16)).place(x=0, y=60)
  resume = Button(top_msg, text='Go back', command=lambda: [root.deiconify(), new_window.destroy()])
  resume.place(x = 10, y = 10)
  playlist = get_playlist_for_display()
  artist_label = Label(playlist_table, text="Artist", anchor='w', width=20, font=('Arial', 12, 'underline'), fg='#9925be').grid(row=0, column=0,columnspan=2)
  blank=Label(playlist_table, text='  ').grid(row=0, column=1, columnspan=2)
  title_label = Label(playlist_table, text="Song Title", anchor='w', width=20, font=('Arial', 12, 'underline'), fg='#9925be').grid(row=0, column=2,columnspan=2)
  
  i = 1
  for title, artist in playlist.items():
      display_playlist_artist = Label(playlist_table,text=F"{artist}", anchor='w', width=20).grid(row=i,column=0,columnspan=2)
      display_playlist_title = Label(playlist_table, text=F"{title}",anchor='w', width=20).grid(row = i, column=2,columnspan=2)
      i+=1
      altura = altura + 30
      playlist_table.configure(height=altura)

def label_center(lw):
  x = window_width/2-lw/2
  return x

def label_width_canvas(canvas, object):
  boundary = canvas.bbox(object)
  width = boundary[2] - boundary[0]
  height = boundary[3] - boundary[1]
  return width, height
  
root = Tk()    

window_width = 500 #ww
window_height = 678 #wh
label_x = label_center(120)
filter_y = 250
root.resizable(False, False)
root.geometry(F'{window_width}x{window_height}')
root.title("Playlist Generator")

bg = PhotoImage(file=r'background.png')
my_canvas = Canvas(root, width=window_width, height=window_height)
my_canvas.pack(fill="both", expand=True)

#set bg as background
my_canvas.create_image(0, 0, image=bg, anchor='nw')

global step2

welcome_message = my_canvas.create_text(99, 135, text="Welcome to THE playlist generator!", font=('Times New Roman', 16, 'bold'), anchor='nw')
step1 = Label(text="Step True: Choose a filter", font=('Times New Roman', 13), anchor='nw', bg = 'white').place(x = 43.5, y = 200)
step2 = Label(text="Step 2: Select an option from the dropdown below", font=('Times New Roman', 13), anchor='nw', bg = 'white').place(x = 43.5, y = 300)

'''look for x-coordinate to place text in the center to be placed in line 383'''
# welcome_message_x = label_center(label_size_canvas(my_canvas, welcome_message)[0])
# print(welcome_message_x)
# x-coordinate is 43.5

option_1 = ['Genre', 'Year', 'Length', 'Popularity']

options_year = ['Before 2000s', '2000 to 2010', '2010 to 2015', '2015 to 2021']
options_genre = ['Pop', 'Dance', 'Rap', 'Rock', 'R&B', 'Emo', 'Edm', 'Hip Hop']
options_length = ['True to 2 min', '2 to 3 min', '3 to 4 min', '4 to 5 min']
options_popularity = ['0 to 25 %','25 to 50 %','50 to 75 %', '75 to 100 %']

clicked1 = StringVar(root)
clicked2 = StringVar(root)
clicked1.set("Filter")

drop1 = dropdowns(root, clicked1, *option_1, command=appear)
drop1.place(x = label_x, y = filter_y, width = 120, height =30)

button_generate_playlist = buttons(root, text='Generate Playlist', state='disabled', command=onclick)
# button1 = Button(root, text='Return to homepage')
# button1.place(x = 100, y = 200)
# root.update()
# print(button1.winfo_height())
button_generate_playlist.place(x = label_x - 70, y = filter_y + 185, width = 120, height = 25)

reset_button = buttons(root, text='Reset Selection', fg = "white", bg="#FF00D4",command=reset)
reset_button.place(x = label_x + 70, y = filter_y + 185, width = 120, height = 25)

root.mainloop()
