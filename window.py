'''main module for guiding parser with CTk'''
#import PIL
from typing import Tuple
import customtkinter,tkinter
from PIL import Image
from linkbuilder import build_a_link
from avito_parser import Parser

class Window(customtkinter.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry('700x400')
        self.title('bby_parser')
        self.iconbitmap("icon.ico")
        self.data={}
        self.logo= customtkinter.CTkImage(light_image=Image.open("logo.png"),size=(550,200))

        self.main_frame = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.main_frame.grid(row=0, column=0,padx=(20,20),pady=(20,20),sticky="nsew")  
 
        self.link_entry = customtkinter.CTkEntry(master=self.main_frame, width=300, corner_radius=100,placeholder_text='Вы можете вставить ссылку')
        self.link_entry.grid(row=0, column=0,padx=(10,10),pady=(2,2))
        self.button_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=10)
        self.button_frame.grid(row=0, column=1,padx=(10,10),pady=(2,2),sticky="nsew")
        self.button_generate=customtkinter.CTkButton(master=self.button_frame,text='Сгенерировать ссылку', width=100,command=self.generate_link, corner_radius=100)
        self.button_generate.grid(row=0,column=0,padx=(0,0))
        self.button_parse=customtkinter.CTkButton(master=self.button_frame,text='Включить парсер', width=100,command=self.parser_starter, corner_radius=100)
        self.button_parse.grid(row=0,column=1,padx=(0,0))

        self.Choises_city = customtkinter.CTkComboBox(master=self.main_frame, corner_radius=100, values=['Выберите город','Все регионы','Москва','СПб и ЛО','Севастополь','Ростов','Краснодар'], command=self.choise_city_event,width=300)
        self.Choises_city.grid(row=1, column=0,padx=(10,10),pady=(2,2),sticky="w")
        self.Choises_product_group = customtkinter.CTkComboBox(master=self.main_frame, corner_radius=100, values=["Выберите группу товаров",'Транспорт','Недвижимость','Для дома и дачи','Электроника','Ноутбуки'],command=self.choise_base_event,width=300)
        self.Choises_product_group.grid(row=2, column=0,padx=(10,10),pady=(2,2),sticky="w")
        self.Choises_sortBy = customtkinter.CTkComboBox(master=self.main_frame, corner_radius=100, values=["Выберите параметр сортировки",'По умолчанию','Дешевле','По дате'],command=self.choise_sort_event,width=300)
        self.Choises_sortBy.grid(row=3, column=0,padx=(10,10),pady=(2,2),sticky="w")

        self.kwoards_entry = customtkinter.CTkEntry(master=self.main_frame, width=300, corner_radius=100,placeholder_text='Введите ключевые слова')
        self.kwoards_entry.grid(row=1, column=1,padx=(10,10),pady=(2,2))
        self.max_price = customtkinter.CTkEntry(master=self.main_frame, width=300, corner_radius=100,placeholder_text='Введите максимальную цену')
        self.max_price.grid(row=2, column=1,padx=(10,10),pady=(2,2))
        self.min_price = customtkinter.CTkEntry(master=self.main_frame, width=300, corner_radius=100,placeholder_text='Введите минимальную цену')
        self.min_price.grid(row=3, column=1,padx=(10,10),pady=(2,2))

        
        self.logo_lable= customtkinter.CTkLabel(master=self.main_frame,text='',image=self.logo)
        self.logo_lable.grid(row=4,columnspan=2,rowspan=2,padx=(10,10),pady=(2,2),sticky="nsew")

  
    def generate_link(self):
        self.link_entry.delete(0, 'end')
        if str(self.kwoards_entry.get()) != '':
            self.data['keywoards'] = str(self.kwoards_entry.get())
        link=build_a_link(self.data)
        self.link_entry.insert(index=tkinter.END,string=link)
        return print(link)

    def choise_city_event(self,values):
        location = {'Все регионы':'all', #локация
                    'Москва': 'moskva',
                    'СПб и ЛО':'sankt_peterburg_i_lo',
                    'Севастополь': 'sevastopol',
                    'Ростов': 'rostovskaya_oblast',
                    'Краснодар': 'krasnodar'}
        if values in location:
            self.data['location'] = location[values]
    def choise_base_event(self,values):
        base = {'Транспорт': 'transport', #группа товаров   
                'Недвижимость': 'nedvizhimost',
                'Для дома и дачи': 'dlya_doma_i_dachi',
                'Электроника': 'bytovaya_elektronika',
                'Ноутбуки': 'noutbuki'}
        if values in base:
            self.data['base'] = base[values]
    def choise_sort_event(self,values):
        range_by = {'По умолчанию': 'default',   #способ отображения
                    'Дешевле': 'cheep',
                    'По дате': 'date'}
        if values in range_by:
            self.data['range_by'] = range_by[values]

    def parser_starter(self):
        parser = Parser(link=str(self.link_entry.get()),
                max_price=int(self.max_price.get()) if str(self.max_price.get()) != '' else 50000,
                min_price=int(self.min_price.get()) if str(self.min_price.get()) != '' and str(self.min_price.get()).isdigit()  else 20000,
                search_items=9999,
                search_pages=1000,
                title_file=str(self.kwoards_entry.get()) if str(self.kwoards_entry.get()) != '' else 'parsed_data')
        try:
            parser.parse_avito()
        except Exception as ex:
            print(ex)
        finally:
            parser.close_parser()
        
    
if __name__=='__main__':
    app=Window()
    app.mainloop()
    data=app.data
