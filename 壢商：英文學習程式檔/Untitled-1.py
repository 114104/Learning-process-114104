
import sqlite3
import os
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random
from tkinter import filedialog
import chardet
#pip install pillow
#pip install chardet
class user:
    def __init__(self,username="",password=""):
        self.username=username
        self.password=password
       
        #畫面
        self.root=tk.Tk()
        self.root.title("有bear而來")
        self.root.geometry("700x500")
        root_bg_image = Image.open("image/bg.jpg")
        root_bg_photo = ImageTk.PhotoImage(root_bg_image)

        root_bg = tk.Label(self.root, image=root_bg_photo)
        root_bg.place(x=0, y=0, relwidth=1, relheight=1) 



        # 個人框架

        self.user_frame=tk.Frame(self.root)
        # self.user_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        user_bg_image = Image.open("image/bg.jpg")
        user_bg_photo = ImageTk.PhotoImage(user_bg_image)
        self.user_bg = tk.Label(self.user_frame, image=user_bg_photo)

        # self.user_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.user_bg.lower()
        #帳號名稱
        self.username_label = tk.Label(self.user_frame,text=f"歡迎 {self.username}",font=("微軟正黑體",40),bg="moccasin")
        #單字庫
        self.search_btn = tk.Button(self.user_frame,text="     單字庫     ",font=("微軟正黑體",20),bg="moccasin",command=self.show_single_word_screen)
        #匯入
        self.import_btn = tk.Button(self.user_frame,text="       匯入       ",font=("微軟正黑體",20),bg="moccasin",command=self.show_import_screen)
        #測驗
        self.test_btn=tk.Button(self.user_frame,text="       測驗       ",font=("微軟正黑體",20),bg="moccasin",command=self.show_test_screen)
        #登出
        self.sign_out_btn=tk.Button(self.user_frame,text="       登出       ",font=("微軟正黑體",20),bg="moccasin",command=self.sign_out)
        
        #顯示
        self.show_user_screen()
 



        



        #單字庫
        self.single_word_frame=tk.Frame(self.root)
        single_word_bg_image = Image.open("image/bg.jpg")
        single_word_bg_photo = ImageTk.PhotoImage(single_word_bg_image)
        self.single_word_bg = tk.Label(self.single_word_frame, image=single_word_bg_photo)


        self.single_word_bg.lower()
        ###標題
        self.single_word_label=tk.Label(self.single_word_frame,text="   單字庫   ",font=("微軟正黑體",30),bg="moccasin")
        ###新增
        self.add_btn=tk.Button(self.single_word_frame,text="   新增單字   ",font=("微軟正黑體",20),bg="moccasin",command=self.show_add_screen)
        self.add_frame=tk.Frame(self.root)
        add_bg_image = Image.open("image/bg.jpg")
        add_bg_photo = ImageTk.PhotoImage(add_bg_image)
        self.add_bg = tk.Label(self.add_frame, image=add_bg_photo)
        self.add_bg.lower()
        self.english_entry=tk.Entry(self.add_frame,text="",font=("微軟正黑體",20))#英文
        self.chinese_entry=tk.Entry(self.add_frame,text="",font=("微軟正黑體",20))#中文
        self.mark_entry=tk.Entry(self.add_frame,text="",font=("微軟正黑體",20))#備註
        hard_options = ["普通", "難", "簡單"]
        self.var = tk.StringVar(self.add_frame)
        self.var.set(hard_options[0])
        self.hard_option= tk.OptionMenu(self.add_frame, self.var, *hard_options)#難度



        english_default_text="請輸入英文"
        chinese_default_text="請輸入中文"
        mark_default_text="備註"
        self.english_entry.insert(0, english_default_text)
        self.chinese_entry.insert(0, chinese_default_text)
        self.mark_entry.insert(0, mark_default_text)

        def clear_english_default_text(event):
            if self.english_entry.get() == english_default_text:
                self.english_entry.delete(0, tk.END)

        def restore_english_default_text(event):
            if not self.english_entry.get():
                self.english_entry.insert(0, english_default_text)

        self.english_entry.bind("<FocusIn>", clear_english_default_text)
        self.english_entry.bind("<FocusOut>", restore_english_default_text)


        def clear_chinese_default_text(event):
            if self.chinese_entry.get() == chinese_default_text:
                self.chinese_entry.delete(0, tk.END)
                
        def restore_chinese_default_text(event):
            if not self.chinese_entry.get():
                self.chinese_entry.insert(0, chinese_default_text)
                

        self.chinese_entry.bind("<FocusIn>", clear_chinese_default_text)
        self.chinese_entry.bind("<FocusOut>", restore_chinese_default_text)

        def clear_mark_default_text(event):
            if self.mark_entry.get() == mark_default_text:
                self.mark_entry.delete(0, tk.END)

        def restore_mark_default_text(event):
            if not self.mark_entry.get():
                self.mark_entry.insert(0, mark_default_text)

        self.mark_entry.bind("<FocusIn>", clear_mark_default_text)
        self.mark_entry.bind("<FocusOut>", restore_mark_default_text)
        self.add_confirm_btn=tk.Button(self.add_frame,text="   新增   ",font=("微軟正黑體",20),bg="moccasin",command=self.add_word)
        self.add_back_btn=tk.Button(self.add_frame,text="   返回   ",font=("微軟正黑體",20),bg="moccasin",command=lambda :self.back_single(self.add_frame))
        self.add_state_label=tk.Label(self.add_frame,text="    新增單字    ",font=("微軟正黑體",30),bg="moccasin")
        #刪除
        self.delete_word_btn=tk.Button(self.single_word_frame,text="   刪除單字   ",font=("微軟正黑體",20),bg="moccasin",command=self.show_delete_screen)
        self.delete_frame=tk.Frame(self.root)
        delete_bg_image = Image.open("image/bg.jpg")
        delete_bg_photo = ImageTk.PhotoImage(delete_bg_image)
        self.delete_bg = tk.Label(self.delete_frame, image=delete_bg_photo)
        self.delete_bg.lower()  
        self.delete_search_ent=tk.Entry(self.delete_frame,text="",font=("微軟正黑體",20))    
        self.delete_search_btn=tk.Button(self.delete_frame,text="  搜尋  ",font=("微軟正黑體",20),bg="moccasin",command=self.delete_search)
        self.delete_label=tk.Label(self.delete_frame,text="  刪除單字  ",font=("微軟正黑體",30),bg="moccasin")
        self.delete_back=tk.Button(self.delete_frame,text="  返回  ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.back_single(self.delete_frame))
        delete_default="請輸入英文"
        self.delete_search_ent.insert(0,delete_default)
        def clear_delete_default_text(event):
            if self.delete_search_ent.get() == delete_default:
                self.delete_search_ent.delete(0, tk.END)


        def restore_delete_default_text(event):
            if not self.delete_search_ent.get():
                self.delete_search_ent.insert(0, delete_default)
        
        self.delete_search_ent.bind("<FocusIn>", clear_delete_default_text)
        self.delete_search_ent.bind("<FocusOut>", restore_delete_default_text)
        self.delete_btn=tk.Button(self.delete_frame,text="    刪除    ",font=("微軟正黑體",20),bg="moccasin",command=self.delete)
        self.delete_all_btn=tk.Button(self.delete_frame,text="  全部刪除  ",font=("微軟正黑體",20),bg="moccasin",command=self.delete_all)
        self.del_opt = tk.StringVar(self.delete_frame)
        self.delete_options=["1"]
        self.delete_option= tk.OptionMenu(self.delete_frame, self.del_opt, *self.delete_options)

        ###查詢
        self.search_word_btn=tk.Button(self.single_word_frame,text="   查詢單字   ",font=("微軟正黑體",20),bg="moccasin",command=self.show_search_screen)
        self.search_frame=tk.Frame(self.root)
        search_bg_image = Image.open("image/bg.jpg")
        search_bg_photo = ImageTk.PhotoImage(search_bg_image)
        self.search_bg = tk.Label(self.search_frame, image=search_bg_photo)
        self.search_bg.lower()
        
        self.search_eng=tk.Entry(self.search_frame,text="",font=("微軟正黑體",20))
        self.show_chn=tk.Label(self.search_frame,text="  英文  ",font=("微軟正黑體",30),bg="moccasin")

        search_default="English"
        self.search_eng.insert(0,search_default)
        def clear_search_default_text(event):
            if self.search_eng.get() == search_default:
                self.search_eng.delete(0, tk.END)


        def restore_search_default_text(event):
            if not self.search_eng.get():
                self.search_eng.insert(0, search_default)

        self.search_eng.bind("<FocusIn>", clear_search_default_text)
        self.search_eng.bind("<FocusOut>", restore_search_default_text)


        self.search_btn=tk.Button(self.search_frame,text="  查詢  ",font=("微軟正黑體",20),bg="moccasin",command=self.search)
        self.search_back_btn=tk.Button(self.search_frame,text="  返回  ",font=("微軟正黑體",20),bg="moccasin",command=lambda :self.back_single(self.search_frame))



        ###查看
        self.see_btn=tk.Button(self.single_word_frame,text="   查看單字   ",font=("微軟正黑體",20),bg="moccasin",command=self.show_word_screen)
        self.word_frame=tk.Frame(self.root)

        word_bg_image = Image.open("image/bg.jpg")
        word_bg_photo = ImageTk.PhotoImage(word_bg_image)
        self.word_bg = tk.Label(self.word_frame, image=word_bg_photo)
        self.word_bg.lower()
        self.table = ttk.Treeview(self.word_frame, show="headings")
        columns = ("英文","中文","正確數","錯誤數","難易度","備註")
        self.table["columns"] = columns
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col,width=60)
        self.vsb = tk.Scrollbar(self.word_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.vsb.set)
        self.see_back_btn=tk.Button(self.word_frame,text="  ⬅  ",fg="white",font=("微軟正黑體",10),bg="black",command=lambda:self.back_single(self.word_frame))
        

        ###隨機查看
        self.random_see_btn=tk.Button(self.single_word_frame,text="   隨機查看   ",font=("微軟正黑體",20),bg="moccasin",command=self.show_random_screen)
        self.random_see_frame=tk.Frame(self.root)
        random_bg_image = Image.open("image/bg.jpg")
        random_bg_photo = ImageTk.PhotoImage(random_bg_image)
        self.random_bg = tk.Label(self.random_see_frame, image=random_bg_photo)
        self.random_bg.lower()
        self.chn_label=tk.Label(self.random_see_frame,text="  中文  ",font=("微軟正黑體",30),bg="moccasin")
        self.eng_label=tk.Label(self.random_see_frame,text="  英文  ",font=("微軟正黑體",30),bg="moccasin")
        self.hard_label=tk.Label(self.random_see_frame,text="  難度  ",font=("微軟正黑體",30),bg="moccasin")
        self.next_btn=tk.Button(self.random_see_frame,text=" 下一個 ",font=("微軟正黑體",20),bg="moccasin",command=self.random_next)
        self.random_back=tk.Button(self.random_see_frame,text="  返回  ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.back_single(self.random_see_frame))

        ###返回
        self.back_btn=tk.Button(self.single_word_frame,text="       返回       ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.back_root(self.single_word_frame))




        

#################################################################################################################################
        #匯入
        self.import_frame=tk.Frame(self.root)
        import_bg_image = Image.open("image/bg.jpg")
        import_bg_photo = ImageTk.PhotoImage(import_bg_image)
        self.import_bg = tk.Label(self.import_frame, image=import_bg_photo)
        self.import_bg.lower()

        self.import_label=tk.Label(self.import_frame,text="  檔案須為.txt \n 格式：(英文),(中文1,中文2,中文3,......)  ",font=("微軟正黑體",30),bg="moccasin")
        self.import_get=tk.Button(self.import_frame,text= "  匯入檔案  ",font=("微軟正黑體",20),bg="moccasin",command=self.get_file)
        self.basic_import=tk.Button(self.import_frame,text="  匯入內建單字  ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.import_data("1000.txt"))
        self.import_back=tk.Button(self.import_frame,text="    返回    ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.back_root(self.import_frame))
        

#################################################################################################################################
        #測驗

        self.test_frame=tk.Frame(self.root)
        test_bg_image = Image.open("image/bg.jpg")
        test_bg_photo = ImageTk.PhotoImage(test_bg_image)
        self.test_bg = tk.Label(self.test_frame, image=test_bg_photo)
        self.test_bg.lower()




        #中翻英0
        self.CTE_btn=tk.Button(self.test_frame,text="  中翻英  ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.show_test_root_screen(0))

###
        self.test_root_frame=tk.Frame(self.root)
        test_root_bg_image = Image.open("image/bg.jpg")
        test_root_bg_photo = ImageTk.PhotoImage(test_root_bg_image)
        self.test_root_bg = tk.Label(self.test_root_frame, image=test_root_bg_photo)
        self.test_root_bg.lower()

        self.spell_btn=tk.Button(self.test_root_frame,text="   拼字   ",font=("微軟正黑體",20),bg="moccasin",command=self.show_spell_screen)
        self.choice_btn=tk.Button(self.test_root_frame,text="   選擇   ",font=("微軟正黑體",20),bg="moccasin",command=self.show_choice_screen)
        self.test_root_back=tk.Button(self.test_root_frame,text="   返回   ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.back_test(self.test_root_frame))
###

        ###拼字
        self.spell_frame=tk.Frame(self.root)
        spell_bg_image = Image.open("image/bg.jpg")
        spell_bg_photo = ImageTk.PhotoImage(spell_bg_image)
        self.spell_bg = tk.Label(self.spell_frame, image=spell_bg_photo)
        self.spell_bg.lower()
            #題目
        self.spell_topic=tk.Label(self.spell_frame,text="請點下一題開始測驗",font=("微軟正黑體",30),bg="moccasin") 
            #輸入框
        self.spell_entry=tk.Entry(self.spell_frame,text="",font=("微軟正黑體",20))
        spell_default="請在此輸入"
        self.spell_entry.insert(0,spell_default)
        def clear_spell_default_text(event):
            if self.spell_entry.get() == spell_default:
                self.spell_entry.delete(0, tk.END)


        def restore_spell_default_text(event):
            if not self.spell_entry.get():
                self.spell_entry.insert(0, spell_default)

        self.spell_entry.bind("<FocusIn>", clear_spell_default_text)
        self.spell_entry.bind("<FocusOut>", restore_spell_default_text)
            #繳交
        self.submit_btn=tk.Button(self.spell_frame,text="確認",font=("微軟正黑體",20),bg="moccasin",command=self.Submit)
            #下一題
        self.spell_next_btn=tk.Button(self.spell_frame,text="下一題",font=("微軟正黑體",20),bg="moccasin",command=self.spell_next)
            #結束
        self.spell_end_btn=tk.Button(self.spell_frame,text="結束",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.test_end(self.spell_frame))



        ###選擇
        self.choice_frame=tk.Frame(self.root)
        choice_bg_image = Image.open("image/bg.jpg")
        choice_bg_photo = ImageTk.PhotoImage(choice_bg_image)
        self.choice_bg = tk.Label(self.choice_frame, image=choice_bg_photo)
        self.choice_bg.lower()
        #題目
        self.choice_topic=tk.Label(self.choice_frame,text="  請點選下一題開始測驗  ",font=("微軟正黑體",30),bg="moccasin")
        ###選項*4
        self.choice_1=tk.Button(self.choice_frame,text=" 1 ",font=("微軟正黑體",20),bg="moccasin",command=self.right_choice)
        self.choice_2=tk.Button(self.choice_frame,text=" 1 ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.wrong_choice(self.choice_2))
        self.choice_3=tk.Button(self.choice_frame,text=" 1 ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.wrong_choice(self.choice_3))
        self.choice_4=tk.Button(self.choice_frame,text=" 1 ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.wrong_choice(self.choice_4))
        ###下一題
        self.choice_next_btn=tk.Button(self.choice_frame,text="  下一題  ",font=("微軟正黑體",20),bg="moccasin",command=self.choice_next)
        ###結束
        self.choice_end=tk.Button(self.choice_frame,text=     "   結束   ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.test_end(self.choice_frame))

        #英翻中1
        self.ETC_btn=tk.Button(self.test_frame,text="  英翻中  ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.show_test_root_screen(1))

        self.test_back_btn=tk.Button(self.test_frame,text="  返回  ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.back_root(self.test_frame))

        #測驗結果

        self.test_end_frame=tk.Frame(self.root)
        test_end_bg_image = Image.open("image/bg.jpg")
        test_end_bg_photo = ImageTk.PhotoImage(test_end_bg_image)
        self.test_end_bg = tk.Label(self.test_end_frame, image=test_end_bg_photo)
        self.test_end_bg.lower()

        self.end_total=tk.Label(self.test_end_frame,text="  總題數  ",font=("微軟正黑體",20),bg="moccasin")
        self.end_right=tk.Label(self.test_end_frame,text="  正確數  ",font=("微軟正黑體",20),bg="moccasin")
        self.end_wrong=tk.Label(self.test_end_frame,text="  錯誤數  ",font=("微軟正黑體",20),bg="moccasin")
        self.end_back=tk.Button(self.test_end_frame,text="  返回  ",font=("微軟正黑體",20),bg="moccasin",command=lambda:self.back_test_root(self.test_end_frame))




#################################################################################################################################

        



        self.root.mainloop()

    #登入成功顯示使用者畫面
    def show_user_screen(self):
        self.user_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.user_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.username_label.place(relx=0.5,rely=0.1,anchor="center")
        self.search_btn.place(relx=0.5,rely=0.3,anchor="center")
        self.import_btn.place(relx=0.5,rely=0.45,anchor="center")
        self.test_btn.place(relx=0.5,rely=0.6,anchor="center")
        self.sign_out_btn.place(relx=0.5,rely=0.75,anchor="center")
    #顯示單字庫主畫面
    def show_single_screen(self):
        self.single_word_frame.place(relwidth=1,relheight=1)
        self.single_word_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.single_word_label.place(relx=0.5,rely=0.1,anchor="center")
        self.add_btn.place(relx=0.35,rely=0.25,anchor="center")
        self.delete_word_btn.place(relx=0.65,rely=0.4,anchor="center")
        self.search_word_btn.place(relx=0.35,rely=0.4,anchor="center") 

        self.see_btn.place(relx=0.35,rely=0.55,anchor="center")
        self.random_see_btn.place(relx=0.65,rely=0.25,anchor="center")        
        self.back_btn.place(relx=0.65,rely=0.55,anchor="center")  
    def show_single_word_screen(self):
        self.user_frame.place_forget()
        self.show_single_screen()
  
    def back_root(self,screen):
        screen.place_forget()
        self.user_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.user_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.username_label.place(relx=0.5,rely=0.1,anchor="center")
        self.search_btn.place(relx=0.5,rely=0.3,anchor="center")
        self.import_btn.place(relx=0.5,rely=0.45,anchor="center")
        self.test_btn.place(relx=0.5,rely=0.6,anchor="center")
        self.sign_out_btn.place(relx=0.5,rely=0.75,anchor="center")  
    
    #顯示新增畫面(單字庫內)
    def show_add_screen(self):
        self.single_word_frame.place_forget()
        self.add_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.add_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.chinese_entry.place(relx=0.5,rely=0.3,anchor="center")
        self.english_entry.place(relx=0.5,rely=0.45,anchor="center")
        self.mark_entry.place(relx=0.5,rely=0.6,anchor="center")
        self.add_confirm_btn.place(relx=0.6,rely=0.8,anchor="center")
        self.add_back_btn.place(relx=0.4,rely=0.8,anchor="center")
        self.add_state_label.place(relx=0.5,rely=0.1,anchor="center")
        self.hard_option.place(relx=0.5,rely=0.2,anchor="center")
    def show_delete_screen(self):
        self.single_word_frame.place_forget()
        self.delete_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.delete_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.delete_search_ent.place(relx=0.35,rely=0.3,anchor='center')
        self.delete_search_btn.place(relx=0.7,rely=0.3,anchor="center")
        self.delete_label.place(relx=0.5,rely=0.1,anchor="center")
        self.delete_back.place(relx=0.5,rely=0.7,anchor="center")
    #顯示查詢畫面
    def show_search_screen(self):
        self.single_word_frame.place_forget()
        self.search_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.search_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.search_eng.place(relx=0.5,rely=0.2,anchor="center")
        self.show_chn.place(relx=0.5,rely=0.4,anchor="n")
        self.search_btn.place(relx=0.3,rely=0.7,anchor="center")
        self.search_back_btn.place(relx=0.7,rely=0.7,anchor="center")

    #顯示查看畫面(單字庫內)
    def show_word_screen(self):
        self.single_word_frame.place_forget()
        self.word_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.word_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.vsb.place(relx=0.95, rely=0.05, relheight=0.9, anchor= "nw")
        self.table.place(relx=0.5,rely=0.5,anchor="center",relheight=0.9,relwidth=0.9)
        self.see_back_btn.place(relx=0,rely=0,anchor="nw")

        self.table.delete(*self.table.get_children())
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        cursor.execute(f"select * from {self.username}")
        information=cursor.fetchall()
        for i in information:
            self.table.insert("","end",values=i)
    #顯示隨機查看畫面
    def show_random_screen(self):
        self.single_word_frame.place_forget()
        self.random_see_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.random_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.chn_label.place(relx=0.5,rely=0.15,anchor="center")
        self.eng_label.place(relx=0.5,rely=0.3,anchor="center")
        self.hard_label.place(relx=0.5,rely=0.45,anchor="center")
        self.next_btn.place(relx=0.5,rely=0.6,anchor="center")    
        self.random_back.place(relx=0.5,rely=0.8,anchor="center")
        self.random_search()
    #返回
    def back_single(self,screen):
        screen.place_forget()
        self.show_single_screen()    


    def show_import_screen(self):
        self.user_frame.place_forget()
        self.import_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.import_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.import_label.place(relx=0.5,rely=0.15,anchor="center")
        self.import_get.place(relx=0.5,rely=0.35,anchor="center")
        self.basic_import.place(relx=0.5,rely=0.5,anchor="center")
        self.import_back.place(relx=0.5,rely=0.65,anchor="center")
        

    def show_test_screen(self):
        self.test_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.test_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.ETC_btn.place(relx=0.3,rely=0.4,anchor="center")
        self.CTE_btn.place(relx=0.7,rely=0.4,anchor="center")
        self.test_back_btn.place(relx=0.5,rely=0.6,anchor="center")
    def show_test_root_screen(self,mode):
        self.mode=mode
        self.test_frame.place_forget()
        self.test_root_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.test_root_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.spell_btn.place(relx=0.5,rely=0.3,anchor="center")
        self.choice_btn.place(relx=0.5,rely=0.45,anchor="center")
        self.test_root_back.place(relx=0.5,rely=0.6,anchor="center")

    def show_spell_screen(self):
        self.test_root_frame.place_forget()
        self.spell_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.spell_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.spell_topic.place(relx=0.5,rely=0.2,anchor="center")
        self.spell_entry.place(relx=0.5,rely=0.35,anchor="center")
        self.submit_btn.place(relx=0.5,rely=0.5,anchor="center")
        self.spell_end_btn.place(relx=0.7,rely=0.7,anchor="center")
        self.spell_next_btn.place(relx=0.3,rely=0.7,anchor="center")
        self.get_question()

    def back_test(self,screen):
        screen.place_forget()
        self.show_test_screen()

    def back_test_root(self,screen):
        screen.place_forget()
        self.show_test_root_screen(self.mode)
    

    def show_choice_screen(self):
        self.test_root_frame.place_forget()
        self.choice_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.choice_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.choice_topic.place(relx=0.5,rely=0.1,anchor="center")
        self.choice_1.place(relx=0.5,rely=0.25,anchor="center")
        self.choice_2.place(relx=0.5,rely=0.4,anchor="center")
        self.choice_3.place(relx=0.5,rely=0.55,anchor="center")
        self.choice_4.place(relx=0.5,rely=0.7,anchor="center")
        self.choice_end.place(relx=0.65,rely=0.85,anchor="center")
        self.choice_next_btn.place(relx=0.35,rely=0.85,anchor="center")
        self.get_question()








    def add_word(self):
        #擷取輸入值
        english=self.english_entry.get()
        chinese=self.chinese_entry.get()
        hard=self.var.get()
        mark=self.mark_entry.get()
        if (english=="請輸入英文" or chinese=="請輸入中文") or english[0].isdigit() or chinese[0].isdigit() :
            self.add_state_label.config(text="請輸入中文和英文")
            return
        if mark=="備註":
            mark='(無)'
        table_name=self.username
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()

        cursor.execute(f'''
        Select 中文 from {table_name} where 英文=?
        ''',(english,))
        cn=cursor.fetchone()
        
        if cn:
            cn=cn[0].split(";")
            if chinese not in cn:
                cn.append(chinese)
            cn=";".join(cn)

            cursor.execute(f'''
            update {table_name} set 中文 = ?,難易度 =?
            where 英文=?
            ''',(cn,hard,english))
        else:
            cursor.execute(f"INSERT INTO {table_name} (英文,中文,正確數,錯誤數,難易度,備註) values(?,?,0,0,?,?)",(english,chinese,hard,mark))
        self.add_state_label.config(text="  新增成功  ")
        conn.commit()
        conn.close()

    def delete_search(self):
        self.d_eng=self.delete_search_ent.get()
        if not self.d_eng:
            self.delete_label.config(text="  輸入欄不能為空  ")
            self.delete_all_btn.place_forget()
            self.delete_btn.place_forget()
            self.delete_option.place_forget()
        elif self.d_eng[0].isdigit():
            self.delete_label.config(text="請輸入英文")
            self.delete_all_btn.place_forget()
            self.delete_btn.place_forget()
            self.delete_option.place_forget()
        else:



            conn=sqlite3.connect("information.db")
            cursor=conn.cursor()
            cursor.execute(f"select 中文 from {self.username} where 英文=?",(self.d_eng,))
            d_chn=cursor.fetchall()
            if d_chn :
                self.delete_options = d_chn[0][0].split(";")
                self.del_opt.set(self.delete_options[0])
                self.delete_option= tk.OptionMenu(self.delete_frame, self.del_opt, *self.delete_options)


                self.delete_btn.place(relx=0.3,rely=0.7,anchor="center")
                self.delete_all_btn.place(relx=0.7,rely=0.7,anchor="center")
                self.delete_option.place(relx=0.5,rely=0.5,anchor="center") 
            else:
                self.delete_label.config(text="  未搜尋到此單字  ")
                self.delete_all_btn.place_forget()
                self.delete_btn.place_forget()
                self.delete_option.place_forget()

            conn.close()

    def delete(self):
        d_chn=self.del_opt.get()

        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        cursor.execute(f"select 中文 from {self.username} where 英文=?",(self.d_eng,))
        d_c=cursor.fetchall()
        if ";" in d_c[0][0]:
            chn = d_c[0][0].split(";")
            chn.remove(d_chn)
            cursor.execute(f"update {self.username} set 中文 =? where 英文=?",(";".join(chn),self.d_eng))
        else:
            cursor.execute(f"delete from {self.username} where 英文=?",(self.d_eng,))
        conn.commit()
        conn.close()
        self.delete_label.config(text="  刪除成功  ")
            
    def delete_all(self):
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        cursor.execute(f"delete from {self.username} where 英文=?",(self.d_eng,))
        conn.commit()
        conn.close()
        self.delete_label.config(text="  刪除成功  ")

    def search(self):
        eng=self.search_eng.get()
        if eng !="English" and eng and not eng[0].isdigit():
            conn=sqlite3.connect("information.db")
            cursor=conn.cursor()
            cursor.execute(f"select 中文 from {self.username} where 英文=?",(eng,))
            chn=cursor.fetchall()

            if chn:
                
                if ";" in chn[0][0]:
                    if len(chn[0][0])>10 and len(chn[0][0])<25:
                        self.show_chn.config(font=("微軟正黑體",15))
                    elif len(chn[0][0])>25 and len(chn[0][0])<50:
                        self.show_chn.config(font=("微軟正黑體",10))
                    elif len(chn[0][0])>50 :
                        chn[0][0]=chn[0][0][:len(chn[0][0])//2]+chn[0][0][len(chn[0][0])//2:]


                self.show_chn.config(text=chn[0][0].strip())
            else:
                self.show_chn.config(text="無此單字")
        else:
            self.show_chn.config(text="請輸入英文")
    
    def random_search(self):
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        cursor.execute(f"select 英文,中文,難易度 from {self.username}")
        self.random_word=cursor.fetchall()
        conn.close()
    
    def random_next(self):
        r=random.randint(0,len(self.random_word)-1)
        self.chn_label.config(text=f"  {self.random_word[r][1].strip()}  ")
        self.eng_label.config(text=f"  {self.random_word[r][0].strip()}  ")
        self.hard_label.config(text=f"  {self.random_word[r][2].strip()}  ")








    def convert_format(self,file_path):
        self.import_context=[]
        with open(file_path,"r" ,encoding=self.detect_encoding(file_path)) as f:
            rs=f.readlines()
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        cursor.execute(f"select 英文 from {self.username}")
        Eng=cursor.fetchall()
        
        for r in rs:
            I=r.split(",",maxsplit=1)
            C=""
            cs=I[1].split(",")
            
            if I[0].isdigit():
                continue
            if (I[0],) in Eng:
                cursor.execute(f"select 中文 from {self.username} where 英文=?",(I[0],))
                CS=cursor.fetchall()
                CS=CS[0][0].split(';')
                for c in cs:
                    # print("-"*20,CS,'*'*20,cs,"-"*20,c)
                    if c.strip() in CS:
                        C+=c.strip()
                
            else:

                C=";".join(cs)
            if C:
                self.import_context.append((I[0],C))
        conn.close()
    def import_add_word(self,english,chinese):
        #擷取輸入值

        


        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()

        cursor.execute(f'''
        Select 中文 from {self.username} where 英文=?
        ''',(english,))
        cn=cursor.fetchone()
        
        if cn:
            cn=cn[0].split(";")
            if chinese not in cn:
                cn.append(chinese)
            cn=";".join(cn)

            cursor.execute(f'''
            update {self.username} set 中文 = ?,難易度 =?
            where 英文=?
            ''',(cn,"普通",english))
        else:
            cursor.execute(f"INSERT INTO {self.username} (英文,中文,正確數,錯誤數,難易度,備註) values(?,?,0,0,?,?)",(english,chinese,"普通","(無)"))
        self.add_state_label.config(text="  新增成功  ")
        conn.commit()
        conn.close()
    def import_data(self,file_path):

        self.convert_format(file_path)
        if not self.import_context:
            self.import_label.config(text="  無新增資料  ")
            return
        for c in self.import_context:

            if ';' in c[1]:
                for c1 in c[1].split(';'):
                    self.import_add_word(c[0],c1)
            else:
                self.import_add_word(c[0],c[1])
        self.import_label.config(text="  匯入成功  ")
    def get_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.import_data(file_path)


            

    def detect_encoding(self,file_path):
        with open(file_path, 'rb') as f:
            rawdata = f.read()
        result = chardet.detect(rawdata)
        return result['encoding']




















































    def get_question(self):
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        cursor.execute(f"select 中文,英文,正確數,錯誤數 from {self.username}")
        self.questions=cursor.fetchall()
        conn.close()
        self.q_total=0
        self.q_right=0
        self.q_wrong=0
        
    def spell_next(self):
        self.spell_topic.config(bg="moccasin")
        if not self.questions:
            self.spell_topic.config(text=" 已經沒有題目囉!! ",bg="yellow")
            return
        self.bol=1
        self.q_total+=1
        r=random.randint(0,len(self.questions)-1)

        self.spell_topic.config(text=self.questions[r][self.mode].strip())
        if self.mode:
            self.answer=self.questions[r][0]
        else:
            self.answer=self.questions[r][1]

        self.question=self.questions.pop(r)
    def Submit(self):
        if not self.spell_entry.get() or self.spell_entry.get()=="請在此輸入":
            self.spell_topic.config(bg="white")
            self.spell_topic.config(bg="red")
            return
        if not self.bol:
            self.spell_topic.config(text="已通過")
            
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        print(self.answer)
        if self.spell_entry.get().lower() in self.answer.lower():
            self.spell_topic.config(bg="white")
            self.spell_topic.config(bg="green")
            self.bol=0
            self.q_right+=1
            cursor.execute(f"update {self.username} set 正確數 =? where 英文=?",(self.question[2]+1,self.question[1],))
        else:
            cursor.execute(f"update {self.username} set 錯誤數 =? where 英文=?",(self.question[3]+1,self.question[1],))
            self.spell_topic.config(bg="red")
            self.q_wrong+=1
        conn.commit()
        conn.close()
    
    def test_end(self,screen):
        self.end_total.config(text=f"  測驗總題數：{self.q_total}  ")
        self.end_right.config(text=f" 答對數：{self.q_right}  ")
        self.end_wrong.config(text=f" 錯誤數：{self.q_wrong}  ")
        screen.place_forget()
        self.test_end_frame.place(relwidth=1,relheight=1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.test_end_bg.place(x=0, y=0, relwidth=1, relheight=1) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.end_total.place(relx=0.5,rely=0.1,anchor="center")
        self.end_right.place(relx=0.3,rely=0.25,anchor="n")
        self.end_wrong.place(relx=0.3,rely=0.35,anchor="n")
        self.end_back.place(relx=0.7,rely=0.5,anchor="center")







    def choice_next(self):
        
        if len(self.questions)<4:
            self.choice_topic.config(text="  請多新增點單字再來  ",bg="red")
            return
        r=random.randint(0,len(self.questions)-1)
        w1=random.randint(0,len(self.questions)-1)
        w2=random.randint(0,len(self.questions)-1)
        w3=random.randint(0,len(self.questions)-1)
        if w1==r:
            w1-=1
        if w2==r:
            w2-=1
        if w3==r:
            w3-=1
        self.choice_topic.config(text=f"  {self.questions[r][self.mode].strip()}  ")
        if self.mode:
            self.choice_1.config(text=f"  {self.questions[r][0].strip()}  ",bg="moccasin")
            self.choice_2.config(text=f"  {self.questions[w1][0].strip()}  ",bg="moccasin")
            self.choice_3.config(text=f"  {self.questions[w2][0].strip()}  ",bg="moccasin")
            self.choice_4.config(text=f"  {self.questions[w3][0].strip()}  ",bg="moccasin")

        else:
            self.choice_1.config(text=f"  {self.questions[r][1].strip()}  ",bg="moccasin")
            self.choice_2.config(text=f"  {self.questions[w1][1].strip()}  ",bg="moccasin")
            self.choice_3.config(text=f"  {self.questions[w2][1].strip()}  ",bg="moccasin")
            self.choice_4.config(text=f"  {self.questions[w3][1].strip()}  ",bg="moccasin")
        
        p=[(0.5,0.25),(0.5,0.4),(0.5,0.55),(0.5,0.7)]
        random.shuffle(p)
        self.choice_1.place(relx=p[0][0],rely=p[0][1])
        self.choice_2.place(relx=p[1][0],rely=p[1][1])
        self.choice_3.place(relx=p[2][0],rely=p[2][1])
        self.choice_4.place(relx=p[3][0],rely=p[3][1])


    def wrong_choice(self,options):
        
        options.config(bg="red")
        self.q_wrong+=1
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        try:
            cursor.execute(f"update {self.username} set 錯誤數 =? where 英文 =?",(self.questions[3]+1,self.question[1]))
        except Exception as e:
            #print(e)
            pass
        conn.commit()
        conn.close()

    def right_choice(self):
        self.choice_1.config(bg="Green")
        self.q_right+=1
        conn=sqlite3.connect("information.db")
        cursor=conn.cursor()
        cursor.execute(f"update {self.username} set 正確數 =?",(self.questions[2]+1))
        conn.commit()
        conn.close()
























    def sign_out(self):
        self.root.destroy()
        initial()

        







class initial:

    def create_table(self):
        conn = sqlite3.connect('information.db')
        cursor = conn.cursor()
        # table_name =username  # 暫定使用者名稱
        cursor.execute(f'''
        CREATE TABLE {self.username} (
            英文 TEXT PRIMARY KEY,
            中文 TEXT,
            正確數 Integer,
            錯誤數 Integer,
            難易度 TEXT,
            備註 TEXT

        )
        ''')#["英文","中文","正確數","錯誤數","難易度","備註"]
        conn.commit()
        conn.close()
    #註冊
    def sign(self):
        #擷取資訊
        self.username=self.Username.get()
        self.password=self.Password.get()
        conn=sqlite3.connect("users.db")
        cursor=conn.cursor()
        cursor.execute('''
            select 帳號 from user where 帳號=?
        ''',(self.username,))
        if self.username[0].isdigit():
            self.state_label.config(text="帳號第一位不能為數字")
        elif not (self.username!="請輸入帳號" and self.password!="請輸入密碼"):
            self.state_label.config(text="請輸入帳號和密碼")

        elif not cursor.fetchone():
            cursor.execute('''INSERT INTO user (帳號,密碼) Values(?,?)''',(self.username,self.password))
            
            self.create_table()
            self.state_label.config(text="註冊成功")
        else:
            self.state_label.config(text="帳號已註冊")
        conn.commit()
        conn.close()
    #登入
    def login(self):
        #擷取資訊
        username=self.Username.get()
        password=self.Password.get()
        conn=sqlite3.connect("users.db")
        cursor=conn.cursor()
        cursor.execute('''
            select 密碼 from user where 帳號=?
        ''',(username,))
        if not(username!="請輸入帳號" and password!="請輸入密碼"):
            self.state_label.config(text="請輸入帳號和密碼")
            return
        pw=cursor.fetchone()
        if pw :
            pw=pw[0]
            if password==pw:
                global user1
                self.state_label.config(text="登入成功")
                self.root.destroy()
                user1=user(username,password)
            else:
                self.state_label.config(text="帳號或密碼錯誤")
        else:
            self.state_label.config(text="帳號或密碼錯誤")

    #畫面
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("有bear而來")
        self.root.geometry("700x500")
        self.root_bg_image = Image.open("image/bg.jpg")
        self.root_bg_photo = ImageTk.PhotoImage(self.root_bg_image)

        self.root_bg = tk.Label(self.root, image=self.root_bg_photo)
        self.root_bg.place(x=0, y=0, relwidth=1, relheight=1) 



        #登入 框架
        self.log_frame=tk.Frame(self.root)
        self.log_frame.place(relwidth=1,relheight=1)

        log_bg_image = Image.open("image/bg.jpg")
        log_bg_photo = ImageTk.PhotoImage(log_bg_image)
        self.log_bg = tk.Label(self.log_frame, image=log_bg_photo)
        self.log_bg.place(x=0, y=0, relwidth=1, relheight=1) 
        self.log_bg.lower()




        self.state_label=tk.Label(self.log_frame,text="請輸入帳號和密碼並點擊註冊或登入",font=("微軟正黑體",20),bg="moccasin")
        self.state_label.place(relx=0.5,rely=0.1,anchor="center")


        self.Username=tk.Entry(self.log_frame,width=20,font=("Arial", 16))
        self.Password=tk.Entry(self.log_frame,width=20,font=("Arial", 16))
        self.Username.place(relx=0.5, rely=0.2, anchor="center")
        self.Password.place(relx=0.5, rely=0.3, anchor="center")
        Username_default_text="請輸入帳號"
        Password_default_text="請輸入密碼"
        self.Username.insert(0, Username_default_text)
        self.Password.insert(0, Password_default_text)

        def clear_username_default_text(event):
            if self.Username.get() == Username_default_text:
                self.Username.delete(0, tk.END)

        def restore_username_default_text(event):
            if not self.Username.get():
                self.Username.insert(0, Username_default_text)

        self.Username.bind("<FocusIn>", clear_username_default_text)
        self.Username.bind("<FocusOut>", restore_username_default_text)


        def clear_password_default_text(event):
            if self.Password.get() == Password_default_text:
                self.Password.delete(0, tk.END)
                self.Password.config(show="*")
        def restore_password_default_text(event):
            if not self.Password.get():
                self.Password.insert(0, Password_default_text)
                self.Password.config(show="")

        self.Password.bind("<FocusIn>", clear_password_default_text)
        self.Password.bind("<FocusOut>", restore_password_default_text)



        self.log_button=tk.Button(self.log_frame,text="登入",font=("Arial",16),command=self.login)
        self.sign_button=tk.Button(self.log_frame,text="註冊",font=("Arial",16),command=self.sign)
        self.sign_button.place(relx=0.4,rely=0.6,anchor="center")
        self.log_button.place(relx=0.6,rely=0.6,anchor="center")

        self.root.mainloop()





#-------------------------------------------------------------------------------------------------------------------------
def create_user():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE Table user (
        帳號 text primary key,
        密碼 Text
    )''')
    conn.commit()
    conn.close()
#-------------------------------------------------------------------------------------------------------------------------
 #-------------------------------------------------------------------------------------------------------------------------
#檢查或創建user.db(紀錄帳密)是否存在
script_dir = os.path.dirname(__file__)#os.getcwd()

file_name = "users.db"
file_path = os.path.join(script_dir, file_name)

if not os.path.isfile(file_path):
    create_user()
initial()