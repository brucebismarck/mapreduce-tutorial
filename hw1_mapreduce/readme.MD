Note:
1. Basic linux commands showed in TopsailIntroPt2MapRed.pdf
2. Other linux commands can be found commands.txt
3. Test .py fine in local system first and then use 'scp' to transfer it to hadoop remote 'local'
4. Open hadoop and use 
 /*hadoop jar /var/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /mindlink/VDL2011_Meds.txt  -output Q2results -mapper /shared/class19/Q2_mapper.py -reducer /shared/class19/Q2_reducer_1.py*/ to run it and use -cat fo find the file and see the result
 Note, please make at least d--x--x--x for each .py file to let them runable in hadoop system
 
