import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyArrowPatch
import ipywidgets as widgets  # import ipywidgets package for interactive widgets
from cryptography.fernet import Fernet
import math
import numpy as np
import csv
import sys
import matplotlib.image as mpimg
from PIL import Image

# Load emoji images
zero_img = Image.open("./resources/0.png")
two_img = Image.open("./resources/2.png")
three_img = Image.open("./resources/3.png")
four_img = Image.open("./resources/4.png")

def readfile(lec):
    #reading csv filter
    global data 
    data = False
    with open('./resources/data.csv', 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == lec-1:  # Fifth row (index starts from 0)
                data = row
                break
    if data == False:
        print("Select valid game number")
        return 0
    else:
        return data

# Define the function for the slider
def update(response):
    return

def wavelength(response, lec, answer=None):
    # Create a figure and axis only if the data is valid
    if type(data) != bool:
        fig, ax = plt.subplots(figsize=(3,2), dpi=300)
    
        # Set the background color to match the image (dark)
        fig.patch.set_facecolor('#0A0F1F')
        ax.set_facecolor('#0A0F1F')
        
        circle_c = '#5FB6BB' if answer is None else '#F1E9DA'
    
        # Add the large semicircle
        large_semi = Wedge(center=(0, 0), r=10, theta1=0, theta2=180, color=circle_c, zorder=1)
        ax.add_patch(large_semi)
        
        if not (answer is None):
            graphical_answer = 180 - answer
            # Add the colored wedges (sectors)
            if (graphical_answer+25 > 180) & (graphical_answer+15 < 180):
                wedges = [
                    {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':180, 'label': '2'},  # Yellow-orange 
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':graphical_answer-15, 'theta2':graphical_answer-5, 'label': '3'},  # Orange
                    {'color': '#FFB64D', 'theta1':graphical_answer-25, 'theta2':graphical_answer-15, 'label': '2'},  # Yellow-orange
                ]
            elif (graphical_answer+15 == 180):
                wedges = [
                    # {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':180, 'label': '2'},  # Yellow-orange 
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':graphical_answer-15, 'theta2':graphical_answer-5, 'label': '3'},  # Orange
                    {'color': '#FFB64D', 'theta1':graphical_answer-25, 'theta2':graphical_answer-15, 'label': '2'},  # Yellow-orange
                ]
            elif (graphical_answer+15 > 180) & (graphical_answer+5 < 180):
                wedges = [
                    # {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':180, 'label': '2'},  # Yellow-orange 
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':180, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':graphical_answer-15, 'theta2':graphical_answer-5, 'label': '3'},  # Orange
                    {'color': '#FFB64D', 'theta1':graphical_answer-25, 'theta2':graphical_answer-15, 'label': '2'},  # Yellow-orange
                ]
            elif (graphical_answer+5 == 180):
                wedges = [
                    # {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':180, 'label': '2'},  # Yellow-orange 
                    # {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':graphical_answer-15, 'theta2':graphical_answer-5, 'label': '3'},  # Orange
                    {'color': '#FFB64D', 'theta1':graphical_answer-25, 'theta2':graphical_answer-15, 'label': '2'},  # Yellow-orange
                ]
            elif (graphical_answer+5 > 180):
                wedges = [
                    # {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':180, 'label': '2'},  # Yellow-orange 
                    # {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':180, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':graphical_answer-15, 'theta2':graphical_answer-5, 'label': '3'},  # Orange
                    {'color': '#FFB64D', 'theta1':graphical_answer-25, 'theta2':graphical_answer-15, 'label': '2'},  # Yellow-orange
                ]
            elif (graphical_answer-25 < 0) & (graphical_answer-15 > 0):
                wedges = [
                    {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':graphical_answer+25, 'label': '2'},  # Yellow-orange 
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':graphical_answer-15, 'theta2':graphical_answer-5, 'label': '3'},  # Orange
                    {'color': '#FFB64D', 'theta1':0, 'theta2':graphical_answer-15, 'label': '2'},  # Yellow-orange
                ] 
            elif (graphical_answer-15 == 0):
                wedges = [
                    {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':graphical_answer+25, 'label': '2'},  # Yellow-orange 
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':graphical_answer-15, 'theta2':graphical_answer-5, 'label': '3'}  # Orange
                ] 
            elif (graphical_answer-15 < 0) & (graphical_answer-5 > 0):
                wedges = [
                    {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':graphical_answer+25, 'label': '2'},  # Yellow-orange 
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':0, 'theta2':graphical_answer-5, 'label': '3'}  # Orange
                ]
            elif (graphical_answer-5 == 0):
                wedges = [
                    {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':graphical_answer+25, 'label': '2'},  # Yellow-orange 
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'}  # Blue
                ]
            elif (graphical_answer-5 < 0):
                wedges = [
                    {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':graphical_answer+25, 'label': '2'},  # Yellow-orange 
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':0, 'theta2':graphical_answer+5, 'label': '4'}  # Blue
                ]
            else:
                wedges = [
                    {'color': '#FFB64D', 'theta1':graphical_answer+15, 'theta2':graphical_answer+25, 'label': '2'},  # Yellow-orange
                    {'color': '#FF6324', 'theta1':graphical_answer+5, 'theta2':graphical_answer+15, 'label': '3'},  # Orange
                    {'color': '#4CAEDA', 'theta1':graphical_answer-5, 'theta2':graphical_answer+5, 'label': '4'},  # Blue
                    {'color': '#FF6324', 'theta1':graphical_answer-15, 'theta2':graphical_answer-5, 'label': '3'},  # Orange
                    {'color': '#FFB64D', 'theta1':graphical_answer-25, 'theta2':graphical_answer-15, 'label': '2'},  # Yellow-orange
                ]
            
            for wedge in wedges:
                w = Wedge(center=(0, 0), r=10, theta1=wedge['theta1'], theta2=wedge['theta2'], color=wedge['color'], zorder=1)
                ax.add_patch(w)
                # Add the number label to each wedge
                theta_mid = np.deg2rad((wedge['theta1'] + wedge['theta2']) / 2)
                x_label = 9 * np.cos(theta_mid)  # Radius at which the label is placed
                y_label = 9 * np.sin(theta_mid)
                ax.text(x_label, y_label, wedge['label'], color='black', fontsize=3, ha='center', va='center')
    
            if (answer + 5 > response >= answer - 5):
                ax.text(0, -5, "4 points!", color='white', fontsize=7, ha='center', va='center', fontweight='bold')
                ax.imshow(four_img, extent=[-1, 1, -4, -2])  # Adjust extent to set position and size
            elif (answer + 15 > response >= answer + 5) or (answer - 5 > response >= answer - 15):
                ax.text(0, -5, "3 points!", color='white', fontsize=7, ha='center', va='center', fontweight='bold')
                ax.imshow(three_img, extent=[-1, 1, -4, -2])  # Adjust extent to set position and size
            elif (answer + 25 > response >= answer + 15) or (answer - 15 > response >= answer - 25):
                ax.text(0, -5, "2 points", color='white', fontsize=7, ha='center', va='center', fontweight='bold')
                ax.imshow(two_img, extent=[-1, 1, -4, -2])  # Adjust extent to set position and size
            else:
                # Add the red circle
                ax.text(0, -5, "No points", color='white', fontsize=7, ha='center', va='center', fontweight='bold')
                ax.imshow(zero_img, extent=[-1, 1, -4, -2])  # Adjust extent to set position and size
    
    
        # Add the red circle
        red_circle = Circle((0, 0), radius=1, color='#DC203A', zorder=2)
        ax.add_patch(red_circle)
        
        # Add needle
        w = Wedge(center=(0, 0), r=8, theta1=180-response-.15, theta2=180-response+.15, color='#DC203A', zorder=1)
        ax.add_patch(w)
    
        # Add labels
        ax.text(-8.5, -1.5, data[1].replace(' ', '\n'), color='white', fontsize=6, ha='center', va='top')
        ax.text(8.5, -1.5, data[2].replace(' ', '\n'), color='white', fontsize=6, ha='center', va='top')
        
        # Add straight arrows with custom arrowheads
        # Arrow pointing left
        left_arrow = FancyArrowPatch(posA=(-7, -.65), posB=(-10, -.65), 
                                    arrowstyle='->', mutation_scale=10, color='white', lw=.5)
        ax.add_patch(left_arrow)
    
        # Arrow pointing right
        right_arrow = FancyArrowPatch(posA=(7, -.65), posB=(10, -.65), 
                                     arrowstyle='->', mutation_scale=10, color='white', lw=.5)
        ax.add_patch(right_arrow)
    
        # Remove axis lines and ticks
        ax.set_xlim([-12, 12])
        ax.set_ylim([-5, 11])
        ax.set_aspect('equal')
        ax.axis('off')
    
        # Show the plot
        plt.show()
    else:
        return 0

# Load the key (ensure you store this securely)
with open('./resources/enc.key', 'rb') as key_file:
    key = key_file.read()
cipher = Fernet(key)

def main(lec):
    #reading file
    data = readfile(lec)
    if data != 0:
        # Define a variable to store the response value
        response_value = [90]  # Initial value
        
        # Create an output widget to display print statements
        output = widgets.Output()
        
        # Function to be triggered by button click
        def on_button_click(b):
            with output:
                wavelength(response_value[0], lec, float(int(cipher.decrypt(data[3].encode('utf-8')).decode())))
                # Disable the button after it's clicked
                b.disabled = True
                b.description = "Answer Shown"
            
        # Use @widgets.interact with a slider and a custom label
        @widgets.interact(response=widgets.IntSlider(min=0, max=180, step=1, value=90, description='Your Response:',
                          layout=widgets.Layout(width='65%'), style={'description_width': 'initial'}))
        
        # define a function that takes the values from the sliders and plots the data
        def get_response(response):
            update(response)
            wavelength(response, lec) # Call the function to plot
            response_value[0] = response  # Update the list value
            return
        
        # Create a button widget
        button = widgets.Button(
            description="READY! Show me the answer!",
            layout=widgets.Layout(width='250px', height='50px'),
            style={'button_color': 'lightblue', 'font_weight': 'bold'}
        )
        
        # Define what happens when the button is clicked
        button.on_click(on_button_click)
        
        # Display the button and output widget
        display(button, output)
