""" Number base, and to/from ASCII converter GUI. Now supporting Fractions
    Author: Marc Katzef
    Date: 20/4/2016
"""

from tkinter import *
#from tkinter.ttk import *

class Maingui:
    """Builds the gui in a given window or frame"""
    def __init__(self, window):
        """Places all of the GUI elements in the given window/frame, and
        initializes the variables that are needed for this GUI to do anything"""
        self.window = window
        
        self.top_rely = 0
        self.next_rely = 0.15
        top_height = 40

        self.w2 = StringVar()
        self.w2.set('20')
        self.h2 = StringVar()
        self.h2.set('14')

        self.top_bar = Frame(window)
        self.top_bar.place(x=0, y=0, relwidth=1, height=top_height)             
        
        self.entry1_label = Label(self.top_bar, text='Text A', font=('Arial', 12), anchor='center')
        self.entry1_label.place(relx=0.1, y=0, height=top_height, relwidth=0.3)
        
        self.entries = Frame(window)  
        
        self.string1_entry = Text(self.entries)
        self.string1_entry.place(relx=0, y=0, relwidth=0.5, relheight=1)
        
        self.entry2_label = Label(self.top_bar, text='Text B', font=('Arial', 12), anchor='center')
        self.entry2_label.place(relx=0.6, y=0, height=top_height, relwidth=0.3)       

        self.string2_entry = Text(self.entries)
        self.string2_entry.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
        
        self.entries.place(relx=0, y=top_height, relwidth=1, relheight=1, height=-(top_height))
        
        self.button1 = Button(self.top_bar, command=self.check, font=('Arial', 10, 'bold'))
        self.button1.place(relx=0.5, y=top_height/2, relwidth=0.2, anchor='center')
        
        self.displaying_results = False
        self.change_button('light gray', 'Check')
        

    def insert_result(self, result, summary, ratio, red_map=-1):
        self.result = Text(self.entries)
        self.result.place(relx=0, relwidth=1, relheight=1)#
        self.button1['command'] = self.remove_results
        
        self.result.delete('1.0', END)
        self.result.tag_configure("red", background="#ffC0C0")
        self.result.tag_configure("grey", background="#E0E0E0")
        
        grey_white = 0
        if red_map == -1:            
            self.result.insert(END, result)
        else:
            counter = 0
            for line in result:
                self.result.insert(END, line + '\n')
                is_red = red_map[counter]
                grey_white = 1 - grey_white
                if is_red:
                    self.result.tag_add("red", '%d.0' % (counter + 1), 'end-1c')
                elif grey_white:
                    self.result.tag_add("grey", '%d.0' % (counter + 1), 'end-1c')
                    
                counter += 1
        
        self.entry1_label['text'] = ''
        self.entry2_label['text'] = ''
        
        #red_component = int((1-ratio) * 255)
        #green_component = int((2 ** ratio - 1) * 255)
        #colour = "#%02x%02x00" % (red_component, green_component)
        if summary == 'Identical':
            self.change_button("light green", "100%")
        else:
            self.change_button("#FFC0C0", "%.0f%%" % (100 * ratio))            
        
        self.displaying_results = True
    
    
    def change_button(self, colour, text):
        self.button1['background'] = colour
        self.button1['text'] = text 
    
    
    def remove_results(self):
        self.result.destroy()        
        self.change_button('light gray', 'Check')
        
        self.button1['text'] = 'Check'
        self.button1['command'] = self.check
        
        self.entry1_label['text'] = 'Text A'
        self.entry2_label['text'] = 'Text B'
        
        self.displaying_results = False
        
        
    def check(self, *args):
        """Collects the appropriate information from the user input, then 
        retrieves the appropriate output, and places it in the appropriate text 
        field, appropriately"""

        file_a = input_string = self.string1_entry.get('1.0', 'end-1c')
        file_b = input_string = self.string2_entry.get('1.0', 'end-1c')
        
        list_a = [line.strip() for line in file_a.splitlines()]
        list_b = [line.strip() for line in file_b.splitlines()] 
        
        size_a = len(list_a)
        size_b = len(list_b)
        
        oh_oh = 'Empty:'
        problem = 0
        if size_a == 0:
            oh_oh += ' Text A'
            problem += 1
            
        if size_b == 0:
            oh_oh += ' Text B'
            problem += 1
        
        if problem == 1:
            self.insert_result(oh_oh, 'Problem', 0)
            return
        elif problem == 2: #Both empty
            self.insert_result(oh_oh, 'Identical', 1)
            return
        
        result = []
        
        identical = True   
        red_map = []
        correct_counter = 0
        space = max([len(line) for line in list_a])
        common_template = '%d:\t%' + str(space) + 's |=| %''s'
        difference_template = '%d:\t%' + str(space) + 's |X| %''s'
        #common_template = '%s |= %d =| %s\n'
        #difference_template = '%s |X %d X| %s\n'
        for index in range(min(size_a, size_b)):
            line_a = list_a.pop(0)
            line_b = list_b.pop(0)
            if line_a == line_b:
                correct_counter += 1
                result.append(common_template % (index+1, line_a, line_a))
                #result += common_template % (line_a, index+1, line_a)
                red_map.append(False)
            else:
                identical = False
                new_part = difference_template % (index+1, line_a, line_b)
                result.append(new_part)
                red_map.append(True)
                #result += difference_template % (line_a, index+1, line_b)
        
        if len(list_a) > 0:
            identical = False
            for line in list_a:
                index += 1
                new_part = difference_template % (index+1, line, '')
                result.append(new_part)
                red_map.append(True)
                #result += difference_template % (line, index+1, '')
        elif len(list_b) > 0:
            identical = False
            for line in list_b:
                index += 1
                new_part = difference_template % (index+1, '', line)
                result.append(new_part)
                red_map.append(True)
                #result += difference_template % ('', index+1, line)
        
        correct_ratio = correct_counter / max(size_a, size_b)
        
        if identical:
            summary = 'Identical'
        else:
            summary = 'Different'
            
        self.insert_result(result, summary, correct_ratio, red_map)


def main():
    """Sets everything in motion"""
    window = Tk()
    window.title('Difference Checker')
    window.minsize(220, 200)
    Maingui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
