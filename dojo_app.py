from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class DojoForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        scroll = ScrollView(size_hint=(1, 1), bar_width=10)
        container = BoxLayout(orientation='vertical', size_hint_y=None, padding=20, spacing=20)
        container.bind(minimum_height=container.setter('height'))

        label_style = {"color": (0, 0, 0, 1), "font_size": 18}
        input_style = {
            "background_color": (1, 1, 1, 1),
            "foreground_color": (0, 0, 0, 1),
            "cursor_color": (0, 0, 0, 1),
            "padding": [10, 10],
            "font_size": 16,
            "size_hint_y": None,
            "height": 44
        }

        # Title
        container.add_widget(Label(text="Dojo Training Planner", font_size=26, color=(0, 0, 0, 1), size_hint_y=None, height=40))

        # Name
        container.add_widget(Label(text="Name:", **label_style))
        self.name_input = TextInput(hint_text="Enter your name", **input_style)
        container.add_widget(self.name_input)

        # Mileage
        container.add_widget(Label(text="Current Weekly Mileage:", **label_style))
        self.mileage_input = TextInput(hint_text="Weekly mileage", input_filter="float", **input_style)
        container.add_widget(self.mileage_input)

        # Race date
        container.add_widget(Label(text="Target Race Date (YYYY-MM-DD):", **label_style))
        self.race_date_input = TextInput(hint_text="YYYY-MM-DD", **input_style)
        container.add_widget(self.race_date_input)

        # Shin splints
        container.add_widget(Label(text="Do you currently have shin splints?", **label_style))
        self.injury_checkbox = CheckBox(size_hint=(None, None), size=(40, 40))
        container.add_widget(self.injury_checkbox)

        # Energy level
        container.add_widget(Label(text="Energy level this week:", **label_style))
        self.energy_spinner = Spinner(
            text="normal",
            values=["low", "normal", "high"],
            size_hint_y=None,
            height=44,
            background_color=(1, 1, 1, 1),
            color=(0, 0, 0, 1),
            font_size=16
        )
        container.add_widget(self.energy_spinner)

        # Preferred days
        container.add_widget(Label(text="Preferred Run Days:", **label_style))
        self.days_input = TextInput(hint_text="e.g. Mon, Wed, Fri", **input_style)
        container.add_widget(self.days_input)

        # Submit
        self.submit_button = Button(
            text="Generate Plan",
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1),
            font_size=16
        )
        self.submit_button.bind(on_press=self.show_result)
        container.add_widget(self.submit_button)

        # Result
        self.result_label = Label(text="", color=(0, 0, 0, 1), font_size=16, size_hint_y=None)
        container.add_widget(self.result_label)

        # Set a minimum height to keep layout vertically centered
        container.height = 900

        scroll.add_widget(container)
        self.add_widget(scroll)

    def show_result(self, instance):
        name = self.name_input.text
        mileage = self.mileage_input.text
        race_date = self.race_date_input.text
        has_injury = self.injury_checkbox.active
        energy = self.energy_spinner.text
        preferred_days = self.days_input.text

        result = (
            f"Training Profile for {name}:\n"
            f"- Mileage: {mileage} mi/week\n"
            f"- Race Date: {race_date}\n"
            f"- Shin Splints: {'Yes' if has_injury else 'No'}\n"
            f"- Energy Level: {energy.capitalize()}\n"
            f"- Preferred Days: {preferred_days}"
        )

        self.result_label.text = result

class DojoApp(App):
    def build(self):
        return DojoForm()

DojoApp().run()
