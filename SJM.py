import os
import sys

def getJobCfg(jobid,cmds,preJobId,qmem="1g",ncpu="1",quene="all.q"):
	sjm_string = "job_begin\n"
	sjm_string = sjm_string + "\tname " + jobid + "\n"
	sjm_string = sjm_string + "\tmemory " + qmem + "\n"
	sjm_string = sjm_string + "\tqueue " + quene + "\n"
	sjm_string = sjm_string + "\tslots " + ncpu + "\n"
	sjm_string += "cmd_begin\n"
	for cmd in cmds[:-1]:
		sjm_string += "\t\t" + cmd + ";\n"
	sjm_string += "\t\t" + cmds[-1] + "\n"
	sjm_string += "cmd_end\n"
	sjm_string += "job_end\n"
	if preJobId == "null":
		return sjm_string
	else:
		for prevjobid in preJobId:
			sjm_string += "order " + prevjobid +" before " + jobid+"\n"
	return sjm_string

	
	
