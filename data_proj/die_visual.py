import pygal

fre = [155, 167, 168, 170, 159, 181]
hist = pygal.Bar()

hist.title = "result"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', fre)
hist.render_to_file('die_visual.svg')