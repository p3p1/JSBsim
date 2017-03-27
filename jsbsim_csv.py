import os
import csv

input_terminal = input("Output: cvs, fgfs, google?")

for case in switch(input_terminal)
	if case('csv'):
		x = './src/JSBSim --script="scripts/c3106_csv_output.xml" --outputlogfile="c3106_csv.log'
		breake;
	if case('google'):
		x = './src/JSBSim --script="scripts/c3106_csv_output.xml" --outputlogfile="c3106_csv.log'
		breake;
	if case('fgfs'):
		x = './src/JSBSim --script="scripts/c3106_csv_output.xml" --outputlogfile="c3106_csv.log'
		breake;


os.system(x)

if input_terminal == "csv"
	if os.path.isdir('csv_data_output') == False
		os.mkdir('csv_data_output',mode=0o777,*,dir_fd=None)
	os.system('mv c310_*.csv csv_data_output')
	with open('csv_data_output/c310_acceleration.csv') as f: 
		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
		for row in reader 
			print row
	
	
