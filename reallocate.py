import os,sys
import argparse
import datetime
import tqdm
from shutil import copy2




parser = argparse.ArgumentParser(description='Process for reallocating TOPICA Materials')
parser.add_argument('infile', help='the feed folder')
parser.add_argument('outfile', help='output folder')
parser.add_argument('week',type=int, help='Week # of the year: [1,52]')
parser.add_argument('-year', default=2019, help='yyyy')
args = parser.parse_args()

weekday = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

in_folder = args.infile 
import datetime

date_ = datetime.datetime.strptime(str(args.year) + '-'+str(args.week-1)  + '-1', "%Y-%W-%w")
#date_ = datetime.date(int(args.date[4:]), int(args.date[2:-4]), int(args.date[:2]))
day_ = [(date_ + datetime.timedelta(i)).date().isoformat() +'_'+ weekday[i] for i in range(7)]
#day_ = [date_(i+1).date().isoformat() +'_'+ weekday[i] for i in range(1, 7)]
out_folder = [os.path.join(args.outfile,day_[i]) for i in range(7)] 

os.makedirs(args.outfile, exist_ok=True)

for i in range(7):
	os.makedirs(out_folder[i], exist_ok=True)

for f_1 in tqdm.tqdm(os.listdir(in_folder)):
	s_1 = os.path.join(in_folder,f_1)
	for f_2 in os.listdir(s_1):
		s_2 = os.path.join(s_1, f_2)
		for i, f_3 in enumerate(os.listdir(s_2)):
			file = os.path.join(s_2, f_3)
			#assert f_3[:2] == day_[i][8:10],'There is an error btw date {0} and {1}:'.format(f_3, day_[i][8:10])
			for k in range(len(out_folder)):
				if f_3[:2] == day_[k][8:10]:
					copy2(file, out_folder[k])
print('Done!')
