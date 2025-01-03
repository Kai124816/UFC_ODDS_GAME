import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from User.profile import Person
from Fight_Card.card_constructor import Card
from Fight_Card.fight import Fight

def interface(user:Person,card:Card):
    # Initialize the main window
    window = tk.Tk()
    window.title('UFC Odds')
    window.geometry('800x600')
    window.configure(bg='#f0f0f0')  # Light gray background

    # Create the title label
    title_label = tk.Label(master=window, text='UFC Odds', font='Calibri 24 bold', bg='#f0f0f0', fg='#333333')
    title_label.pack(pady=(3, 3))

    # Create the units remaining label
    top_right_frame = tk.Frame(master=window, bg='#625e5e')
    top_right_frame.place(relx=1.0, rely=0.0, anchor='ne', x=-20, y=20)  # Adjust x and y for padding

    top_right_label_var = tk.StringVar()
    top_right_label_var.set(f'Units Remaining: {user.picks.remaining_budget}')
    top_right_label = ttk.Label(master=top_right_frame, textvariable=top_right_label_var, font='Calibri 18', anchor='center', background='#625e5e')
    top_right_label.pack()

    def update_label():
        top_right_label_var.set(f'Units Remaining: {user.picks.remaining_budget}')

    # Create placed bets button
    top_left_button = ttk.Button(window, text='Bets Placed', command=lambda: display_bets())
    top_left_button.pack(side='top', anchor='w', padx=20, pady=20)

    xy_frame = ctk.CTkScrollableFrame(window,width = 600, height = 800)

    xy_frame.pack()

    # Create main UI components
    for fight in card.fights:
        fight_frame = tk.Frame(xy_frame, bg='#ffffff', relief='ridge', borderwidth=2)
        fight_frame.pack(fill='x', pady=(10, 5), padx=20)

        # Display fight name
        label = ttk.Label(master=fight_frame, text=fight.name, font='Calibri 18', anchor='center')
        label.pack(pady=(10, 5))

        # Odds button
        style = ttk.Style()
        style.configure('OddsButton.TButton', font=('Calibri', 15))
        odds_button = ttk.Button(fight_frame, text="View Odds", style='OddsButton.TButton', 
                         command=lambda f=fight: display_odds_window(f))
        odds_button.pack(pady=(5, 10))

    def display_odds_window(fight:Fight):
        odds_window = tk.Toplevel()
        odds_window.title(f"{fight.fighter1} vs {fight.fighter2} Odds")
        odds_window.geometry('400x300')
        odds_window.configure(bg='#f0f0f0')

        tk.Label(odds_window, text=f"{fight.fighter1} Odds", font='Calibri 18 bold', bg='#f0f0f0').pack(pady=10)
        
        odds_frame = tk.Frame(odds_window, bg='#f0f0f0')
        odds_frame.pack(fill='x', padx=20)
        
        # Fighter 1 odds
        tk.Button(odds_frame, text=f"Moneyline: {fight.fighter1_ml}", font='Calibri 14', bg='#f0f0f0', command=lambda f=fight.fighter1: place_bets_window(f,"Moneyline")).pack()
        tk.Button(odds_frame, text=f"Decision: {fight.fighter1_props['Decision']}", font='Calibri 14', bg='#f0f0f0', command=lambda f=fight.fighter1: place_bets_window(f,"Decision")).pack()
        tk.Button(odds_frame, text=f"TKO: {fight.fighter1_props['TKO']}", font='Calibri 14', bg='#f0f0f0', command=lambda f=fight.fighter1: place_bets_window(f,"TKO")).pack()
        tk.Button(odds_frame, text=f"Submission: {fight.fighter1_props['Submission']}", font='Calibri 14', bg='#f0f0f0', command=lambda f=fight.fighter1: place_bets_window(f,"Submission")).pack()

        # Fighter 2 odds
        tk.Label(odds_window, text=f"{fight.fighter2} Odds", font='Calibri 18 bold', bg='#f0f0f0').pack(pady=10)
        
        odds_frame = tk.Frame(odds_window, bg='#f0f0f0')
        odds_frame.pack(fill='x', padx=20)

        tk.Button(odds_frame, text=f"Moneyline: {fight.fighter2_ml}", font='Calibri 14', bg='#f0f0f0', command=lambda f=fight.fighter2: place_bets_window(f,"Moneyline")).pack()
        tk.Button(odds_frame, text=f"Decision: {fight.fighter2_props['Decision']}", font='Calibri 14', bg='#f0f0f0', command=lambda f=fight.fighter2: place_bets_window(f,"Decision")).pack()
        tk.Button(odds_frame, text=f"TKO: {fight.fighter2_props['TKO']}", font='Calibri 14', bg='#f0f0f0', command=lambda f=fight.fighter2: place_bets_window(f,"TKO")).pack()
        tk.Button(odds_frame, text=f"Submission: {fight.fighter2_props['Submission']}", font='Calibri 14', bg='#f0f0f0', command=lambda f=fight.fighter2: place_bets_window(f,"Submission")).pack()

    # Placing bets
    def place_bets_window(fighter_name: str, method: str):
        w1 = tk.Toplevel()
        w1.title('Place Bets')
        w1.geometry('250x200')
        w1.configure(bg='#f0f0f0')
        
        ttk.Label(w1, text=f'Place bet on {fighter_name} by {method}', font='Calibri 15', wraplength=150, justify="center", background='#f0f0f0').pack(pady=(20, 10))
        
        input_box = tk.Text(w1, width=10, height=2, font='Calibri 14')
        input_box.pack(pady=(0, 10))
        
        btn = tk.Button(w1, text='Enter', font='Calibri 15', command=lambda: on_button_press(input_box, fighter_name,method))
        btn.pack()

    def is_integer(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
        
    def on_button_press(text_widget: tk.Text, fighter: str, method:str):
        txt = text_widget.get(1.0, tk.END).strip()  # Get the text and strip any trailing newlines
        if is_integer(txt):
            if int(txt) == 0:
                pick_error3()
            elif int(txt) > user.picks.remaining_budget:
                pick_error2()
            elif int(txt) < 0:
                pick_error4()
            else:
                try:
                    user.picks.make_pick(fighter,method,int(txt))
                    successful_pick()
                except Exception as e:
                    pick_error5(e)
        else:
            pick_error1()

    def successful_pick():
        message = f'Bet placed, {user.picks.remaining_budget} units remaining' 
        update_label()
        show_message("Pick Placed", message)

    def pick_error1():
        show_message("Error", "Your input is not an integer")

    def pick_error2():
        show_message("Error", "You placed more units than you have left")

    def pick_error3():
        show_message("Error", "Can't place 0 units")

    def pick_error4():
        show_message("Error", "Can't place negative units")

    def pick_error5(e:str):
        show_message("Error", e)
    
    def show_message(title: str, message: str):
        new_window = tk.Toplevel(window)
        new_window.title(title)
        new_window.geometry("250x100")
        new_window.configure(bg='#f0f0f0')
        ttk.Label(new_window, text=message, font='Calibri 15', wraplength=240, background='#f0f0f0').pack(pady=20, padx=20)

    # Display the bets
    def display_bets():
        # Create a new window
        w1 = tk.Toplevel()
        w1.title('Bets Placed')
        w1.geometry('400x400')
        w1.configure(bg='#f0f0f0')
        
        # Check if there are no bets
        if len(user.picks.picks) == 0:
            label = ttk.Label(w1, text='No Bets Placed Yet', font='Calibri 15', anchor='center', background='#f0f0f0')
            label.pack(pady=20)
        else:
            # Convert dictionary keys to a list
            for pick in user.picks.picks:
                bet_frame = tk.Frame(w1, bg='#ffffff', relief='ridge', borderwidth=2)
                bet_frame.pack(fill='x', pady=(10, 5), padx=20)
                
                label = ttk.Label(master=bet_frame, text=f'{pick[3]} units placed on {pick[0]} by {pick[1]}', font='Calibri 15', anchor='center', wraplength=300, justify='center', background='#ffffff')
                label.pack(pady=(10, 5))
                
                button_frame = tk.Frame(bet_frame, bg='#ffffff')
                button_frame.pack(fill='x', pady=(0, 10))
                
                button1 = tk.Button(button_frame, text='Remove Bet', font='Calibri 15', command=lambda f=pick: remove_bets(f, w1))
                button1.pack(pady=5)

    def remove_bets(pick: list, window: tk.Toplevel):
        window.destroy()
        user.picks.remove_pick(pick)
        update_label()
        display_bets()

    # Start the Tkinter event loop
    # window.mainloop()
    window.mainloop()



