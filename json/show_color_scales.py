from plotly import colors

#colors is dictionry of key=colorscale name
#value = colors themselves
#reversescale = go opposite way for data list (bright to dark)
    #dark to light
for key in colors.PLOTLY_SCALES.keys():
    print(key)