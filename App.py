import customtkinter as ctk
from Prediction import Predict

class ToolTip:


    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tooltip_window is not None:
            return  
        x = self.widget.winfo_rootx() + 25
        y = self.widget.winfo_rooty() + 25
        self.tooltip_window = ctk.CTkToplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        self.tooltip_window.configure(fg_color="#2A3441")
        label = ctk.CTkLabel(
            self.tooltip_window, 
            text=self.text, 
            fg_color="#2A3441",
            text_color="#E0E5EB",
            corner_radius=6,
            font=("Inter", 14)
        )
        label.pack(padx=10, pady=8)

    def hide_tooltip(self, event=None):
        if self.tooltip_window is not None:
            self.tooltip_window.destroy()
            self.tooltip_window = None
def create_app():
    # Theme and appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    # Window setup
    root = ctk.CTk()
    root.title("Diabetes Prediction")

    # Screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width * 0.8)
    window_height = int(screen_height * 0.5)
    
    # Window configuration
    root.geometry(f"{window_width}x{window_height}")
    root.minsize(window_width, window_height)
    root.configure(fg_color="#1A1F25")

    # Main container
    main_container = ctk.CTkFrame(root, fg_color="#1A1F25")
    main_container.pack(expand=True, fill="both", padx=40, pady=30)

    # Title Section
    title_frame = ctk.CTkFrame(main_container, fg_color="#212832", corner_radius=15)
    title_frame.pack(pady=(0, 25), padx=20, fill='x')
    
    title_label = ctk.CTkLabel(
        title_frame, 
        text="Diabetes Risk Prediction", 
        font=("Inter", 36, "bold"),
        text_color="#E0E5EB"
    )
    title_label.pack(pady=(20, 15))

    description_label = ctk.CTkLabel(
        title_frame,
        text="Advanced ML-powered tool for predicting diabetes risk based on health metrics.\n"
             "Input your health data below to receive an instant risk assessment.",
        font=("Inter", 16),
        text_color="#B0B9C6",
        wraplength=window_width - 100
    )
    description_label.pack(pady=(0, 20), padx=40)

    # Input Frame
    input_frame = ctk.CTkFrame(main_container, fg_color="#212832", corner_radius=15)
    input_frame.pack(pady=(0, 25), padx=20, fill='x')

    # Configure grid
    input_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    # Common styles
    label_font = ("Inter", 16)
    entry_font = ("Inter", 16)
    input_height = 40
    label_style = {
        "font": label_font,
        "text_color": "#B0B9C6"
    }
    entry_style = {
        "font": entry_font,
        "fg_color": "#2A3441",
        "border_color": "#3D4755",
        "text_color": "#E0E5EB",
        "height": input_height,
        "corner_radius": 8
    }

    pregnancies_label = ctk.CTkLabel(input_frame, text="Pregnancies", **label_style)
    pregnancies_label.grid(row=0, column=0, sticky='e', padx=(20, 10), pady=15)
    pregnancies_entry = ctk.CTkEntry(input_frame, **entry_style)
    pregnancies_entry.grid(row=0, column=1, sticky='w', padx=(0, 20), pady=15)
    ToolTip(pregnancies_entry, " Number of pregnancies. ")

    # Glucose
    glucose_label = ctk.CTkLabel(input_frame, text="Glucose", **label_style)
    glucose_label.grid(row=1, column=0, sticky='e', padx=(20, 10), pady=15)
    glucose_entry = ctk.CTkEntry(input_frame, **entry_style)
    glucose_entry.grid(row=1, column=1, sticky='w', padx=(0, 20), pady=15)
    ToolTip(glucose_entry, " Plasma glucose concentration (mg/dL). ")

    # Skin Thickness
    skin_label = ctk.CTkLabel(input_frame, text="Skin Thickness", **label_style)
    skin_label.grid(row=0, column=2, sticky='e', padx=(20, 10), pady=15)
    skin_entry = ctk.CTkEntry(input_frame, **entry_style)
    skin_entry.grid(row=0, column=3, sticky='w', padx=(0, 20), pady=15)
    ToolTip(skin_entry, " Triceps skinfold thickness (mm). ")

    # Insulin
    insulin_label = ctk.CTkLabel(input_frame, text="Insulin", **label_style)
    insulin_label.grid(row=1, column=2, sticky='e', padx=(20, 10), pady=15)
    insulin_entry = ctk.CTkEntry(input_frame, **entry_style)
    insulin_entry.grid(row=1, column=3, sticky='w', padx=(0, 20), pady=15)
    ToolTip(insulin_entry, " 2-hour serum insulin (μU/mL). ")

    # BMI
    bmi_label = ctk.CTkLabel(input_frame, text="BMI", **label_style)
    bmi_label.grid(row=0, column=4, sticky='e', padx=(20, 10), pady=15)
    bmi_entry = ctk.CTkEntry(input_frame, **entry_style)
    bmi_entry.grid(row=0, column=5, sticky='w', padx=(0, 20), pady=15)
    ToolTip(bmi_entry, " Body Mass Index (kg/m²). ")

    # Diabetes Pedigree
    pedigree_label = ctk.CTkLabel(input_frame, text="Diabetes Pedigree", **label_style)
    pedigree_label.grid(row=1, column=4, sticky='e', padx=(20, 10), pady=15)
    pedigree_entry = ctk.CTkEntry(input_frame, **entry_style)
    pedigree_entry.grid(row=1, column=5, sticky='w', padx=(0, 20), pady=15)
    ToolTip(pedigree_entry, " Diabetes hereditary factor. ")

    # Age
    age_label = ctk.CTkLabel(input_frame, text="Age", **label_style)
    age_label.grid(row=2, column=0, sticky='e', padx=(20, 10), pady=15)
    age_entry = ctk.CTkEntry(input_frame, **entry_style)
    age_entry.grid(row=2, column=1, sticky='w', padx=(0, 20), pady=15)
    ToolTip(age_entry, " Patient's age in years. ")

    BloodPressure_label = ctk.CTkLabel(input_frame, text="Bloodpressure", **label_style)
    BloodPressure_label.grid(row=2, column=2, sticky='e', padx=(20, 10), pady=15)
    BloodPressure_entry = ctk.CTkEntry(input_frame, **entry_style)
    BloodPressure_entry.grid(row=2, column=3, sticky='w', padx=(0, 20), pady=15)
    ToolTip(BloodPressure_entry, " Diastolic blood pressure (mm Hg). ")


    def show_message(message):
        popup = ctk.CTkToplevel(root)
        popup.title("Message")
        popup.geometry("300x150")
        popup.configure(fg_color="#1A1F25")

        label = ctk.CTkLabel(popup, text=message, font=("Inter", 14), text_color="#E0E5EB")
        label.pack(pady=20)

        button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        button.pack(pady=(0, 20))

        #PREDICTION MODEL
    def on_predict():
        try:
            # Get and validate inputs
            pregnancies = int(pregnancies_entry.get())  # Should be int
            glucose = int(glucose_entry.get())          # Should be int
            blood_pressure = int(BloodPressure_entry.get())  # Should be int
            skin_thickness = int(skin_entry.get())      # Should be int
            insulin = int(insulin_entry.get())          # Should be int
            bmi = float(bmi_entry.get())                 # Should be float
            diabetes_pedigree = float(pedigree_entry.get())  # Should be float
            age = int(age_entry.get())                   # Should be int

            # Create inputs array
            inputs = [pregnancies, glucose, blood_pressure, skin_thickness,
                    insulin, bmi, diabetes_pedigree, age]

            # Call the prediction function
            predicted_class, probabilities = Predict(inputs)

            # Determine the prediction result
            result_message = (
                f"Prediction: {'Diabetic' if predicted_class == 1 else 'Not Diabetic'}\n"
                f"Probabilities:\n"
                f"- Diabetic: {probabilities}\n"
                f"- Not Diabetic: {probabilities}"
            )
            
            # Show result in a message box
            show_message(result_message)

        except ValueError:
            show_message("Input Error", "Please enter valid numeric values.")



    # Button Frame
    button_frame = ctk.CTkFrame(main_container, fg_color="#212832", corner_radius=15)
    button_frame.pack(pady=(0, 20), padx=20, fill='x')

    # Predict Button
    predict_button = ctk.CTkButton(
        button_frame,
        text="Predict Risk",
        command=on_predict,
        font=("Inter", 22, "bold"),
        corner_radius=10,
        height=50,
        width=400,
        fg_color="#3D7BF6",
        hover_color="#2D5CBD",
        text_color="#FFFFFF"
    )
    predict_button.pack(pady=20, padx=40)

    # Status bar
    status_label = ctk.CTkLabel(
        main_container,
        text="Ready for prediction",
        font=("Inter", 14),
        text_color="#8F96A3"
    )
    status_label.pack(pady=(10, 0))
    





    root.mainloop()

if __name__ == "__main__":
    create_app()