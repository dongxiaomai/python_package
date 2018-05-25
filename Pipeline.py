import os
import sys
import Dict
import re
import xlrd

def Chr_fixed(Chr):		#if "chr" not in Chr, chr+Chr
	if re.search("chr",str(Chr)):
		pass
	else:
		try:
			Chr = "chr"+str(int(Chr))
		except:
			Chr= "chr"+Chr
	return Chr
def Pos_fixed(Pos):
	Pos = str(int(float(Pos)))
	return Pos
def check_string(List,string=""):
	for key in List:
		if key==string:
			return False
	else:
		return True
def get_excel_dict(File,titleIDs,null_string="-"):
	if len(titleIDs)>5:
		print["title个数太多"]
		os._exit(1)
	else:
		pass
	i = 0
	File_dict = {}
	head_dict = {}
	index_dict = {}
	workbook = xlrd.open_workbook(File)
	for sheet in workbook.sheets():
		for row in range(sheet.nrows):
			if i==0:
				lines = []
				for col in range(sheet.ncols):
					lines.append(sheet.cell(i,col).value)
				if set(titleIDs)&set(lines)==set(titleIDs):
					pass
				else:
					print("titles not in file head line,game over\ntitles:\t")
					print(lines)
					os._exit(1)
				chr_in_bool=False
				start_in_bool=False
				end_in_bool=False
				for index in range(len(lines)):
					index_dict[index] = lines[index]
					head_dict[lines[index]] = index
					if chr_in_bool:
						pass
					else:
						if "Chr" in lines[index] or "chr" in lines[index]:
							chr_in_bool = True
							chr_in_index= index
						else:
							pass
					if start_in_bool:
						pass
					else:
						if "Start" in lines[index] or "start" in lines[index]:
							start_in_bool = True
							start_in_index = index
						else:
							pass
					if end_in_bool:
						pass
					else:
						if "End" in lines[index] or "end" in lines[index]:
							end_in_bool = True
							end_in_index = index
						else:
							pass
				if "Chr" in titleIDs or "chr" in titleIDs:
					pass
				else:
					chr_in_bool = False
				if "Start" in titleIDs or "start" in titleIDs:
					pass
				else:
					start_in_bool = False
				if "End" in titleIDs or "end" in titleIDs:
					pass
				else:
					end_in_bool = False
				i+=1
				continue
			else:
				pass
			lines = []
			for col in range(sheet.ncols):
				lines.append(sheet.cell(row,col).value)
			if chr_in_bool:
				lines[chr_in_index] = Chr_fixed(lines[chr_in_index])
			else:
				pass
			if end_in_bool:
				lines[end_in_index] = Pos_fixed(lines[end_in_index])
			else:
				pass
			if start_in_bool:
				lines[start_in_index]= Pos_fixed(lines[start_in_index])
			else:
				pass
			for index in range(len(lines)):
				if lines[index]=="":
					lines[index]=null_string
				else:
					pass
			if len(titleIDs)==1:
				for index in range(len(lines)):
					if not check_string([lines[head_dict[titleIDs[0]]]]):
						continue
					else:
						pass
					Dict.addtodict2(File_dict,lines[head_dict[titleIDs[0]]],index_dict[index],lines[index])
			elif len(titleIDs)==2:
				for index in range(len(lines)):
					if not check_string([lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]]]):
						continue
					else:
						pass
					Dict.addtodict3(File_dict,lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],index_dict[index],lines[index])
			elif len(titleIDs)==3:
				for index in range(len(lines)):
					if not check_string([lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]]]):
						continue
					else:
						pass
					Dict.addtodict4(File_dict,lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],index_dict[index],lines[index])
			elif len(titleIDs)==4:
				for index in range(len(lines)):
					if not check_string([lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],lines[head_dict[titleIDs[3]]]]):
						continue
					else:
						pass
					Dict.addtodict5(File_dict,lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],lines[head_dict[titleIDs[3]]],index_dict[index],lines[index])
			elif len(titleIDs)==5:
				for index in range(len(lines)):
					if not check_string([lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],lines[head_dict[titleIDs[3]]],lines[head_dict[titleIDs[4]]]]):
						continue
					else:
						pass
					Dict.addtodict6(File_dict,lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],lines[head_dict[titleIDs[3]]],lines[head_dict[titleIDs[4]]],index_dict[index],lines[index])
			else:
				pass
			i+=1
	return File_dict

def get_file_dict(File,titleIDs,null_string="-"):
	if len(titleIDs)>5:
		print["title个数太多"]
		os._exit(1)
	else:
		pass
	i = 0
	File_dict = {}
	head_dict = {}
	index_dict = {}
	for line in open(File,"r"):
		if i==0:
			lines=line.strip("\n").split("\t")
			if set(titleIDs)&set(lines)==set(titleIDs):
				pass
			else:
				print("titles not in file head line,game over")
				os._exit(1)
			chr_in_bool=False
			for index in range(len(lines)):
				index_dict[index] = lines[index]
				head_dict[lines[index]] = index
				if chr_in_bool:
					pass
				else:
					if "Chr" in lines[index] or "chr" in lines[index]:
						chr_in_bool = True
						chr_in_index= index
					else:
						pass
			i+=1
			continue
		else:
			pass
		lines = line.strip("\n").split("\t")
		if chr_in_bool:
			lines[chr_in_index] = Chr_fixed(lines[chr_in_index])
		else:
			pass
		for index in range(len(lines)):
			if lines[index]=="":
				lines[index]=null_string
		if len(titleIDs)==1:
			for index in range(len(lines)):
				if not check_string([lines[head_dict[titleIDs[0]]]]):
					continue
				else:
					pass
				Dict.addtodict2(File_dict,lines[head_dict[titleIDs[0]]],index_dict[index],lines[index])
		elif len(titleIDs)==2:
			for index in range(len(lines)):
				if not check_string([lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]]]):
					continue
				else:
					pass
				Dict.addtodict3(File_dict,lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],index_dict[index],lines[index])
		elif len(titleIDs)==3:
			for index in range(len(lines)):
				if not check_string([lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]]]):
					continue
				else:
					pass
				Dict.addtodict4(File_dict,lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],index_dict[index],lines[index])
		elif len(titleIDs)==4:
			for index in range(len(lines)):
				if not check_string([lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],lines[head_dict[titleIDs[3]]]]):
					continue
				else:
					pass
				Dict.addtodict5(File_dict,lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],lines[head_dict[titleIDs[3]]],index_dict[index],lines[index])
		elif len(titleIDs)==5:
			for index in range(len(lines)):
				if not check_string([lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],lines[head_dict[titleIDs[3]]],lines[head_dict[titleIDs[4]]]]):
					continue
				else:
					pass
				Dict.addtodict6(File_dict,lines[head_dict[titleIDs[0]]],lines[head_dict[titleIDs[1]]],lines[head_dict[titleIDs[2]]],lines[head_dict[titleIDs[3]]],lines[head_dict[titleIDs[4]]],index_dict[index],lines[index])
		else:
			pass
		i+=1
	return File_dict
		
def check_bin(binlist):
	for Bin in binlist:
		if os.path.exists(Bin):
			pass
		else:
			print("not exists"+Bin)
			sys.stderr.write("not existing "+Bin)
			os._exit(1)


def BaseQualityRecalibration(inbam,out,reference,thread,knownsites,javabin,javatmp,gatkjar):
	check_bin([reference,javabin,gatkjar])
	cmds = javabin+" -Djava.io.tmpdir="+javatmp+" -XX:+UseParallelGC -XX:ParallelGCThreads=8 -Xmx6g -jar "+gatkjar+" -T BaseRecalibrator -nct "+thread+" --disable_auto_index_creation_and_locking_when_reading_rods -R "+reference+" -I "+inbam+" -rf BadCigar"
	for knowsite in knownsites:
		cmds +=" -knownSites "+knowsite
	cmds +=" -o "+out
	return cmds

def Printreads(inbam,BQSR,out,reference,thread,javabin,javatmp,gatkjar):
	check_bin([reference,javabin,gatkjar])
	cmds = javabin+" -Djava.io.tmpdir="+javatmp+" -XX:+UseParallelGC -XX:ParallelGCThreads=8 -Xmx6g -jar "+gatkjar+" -T PrintReads -nct "+thread+" --disable_auto_index_creation_and_locking_when_reading_rods -R "+reference+" -I "+inbam+" -BQSR "+BQSR+" -o "+out
	return cmds


def Bwa_sort_bam(R1fq,R2fq,outbam,reference,bampath,thread,SampleID,SM,LB,LA,PU,bwabin,samtoolsbin):
	check_bin([reference,bampath,bwabin,samtoolsbin])
	cmds = bwabin+" mem -t "+thread+" -M "+' -R \"@RG\\tID:'+SampleID+'\\tSM:'+SM+'\\tLB:'+LB+'\\tLA:'+LA+'\\tPU:'+	PU+'\tPL:Illumina\\tCN:Acorndx\" '+reference+" "+R1fq+" "+R2fq+" | "+samtoolsbin+" sort -T "+bampath+" -@ "+thread+" -m 4g -o "+outbam+" -"
	return cmds
def Markdup(inbam,outbam,dupStat,bampath,javabin,javatmp,parcardjar,samtoolsbin):
	ID = os.path.basename(inbam).split(".")[0]
	binlist = [javabin,javatmp,parcardjar,bampath]
	for Bin in binlist:
		if os.path.exists(Bin):
			pass
		else:
			print("not exists"+Bin)
			sys.stderr.write("not existing "+Bin)
			os._exit(1)
	cmds = javabin + " -Djava.io.tmpdir="+javatmp+" -XX:+UseParallelGC -XX:ParallelGCThreads=8 -Xmx1g -jar "+parcardjar+" MarkDuplicates I="+inbam+" O="+outbam+" M="+dupStat+" VALIDATION_STRINGENCY=SILENT ASSUME_SORTED=true REMOVE_DUPLICATES=false MAX_RECORDS_IN_RAM=1750000 TMP_DIR="+ bampath
	cmds +=";\n\t\t"+samtoolsbin+" index "+outbam
	return cmds
def Mutect2(tbam,javabin,javatmp,gatkjar,ref,Dbsnp,Cosmic,Bed,outdir,nbam="null"):
	ID = os.path.basename(tbam).split(".")[0]
	binlist = [javabin,javatmp,gatkjar,ref,Dbsnp,Cosmic,Bed,outdir]
	for Bin in binlist:
		if os.path.exists(Bin):
			pass
		else:
			print("not exists"+Bin)
			sys.stderr.write("not existing "+Bin)
			os._exit(1)
	if nbam=="null":
		cmds = javabin + " -Djava.io.tmpdir="+javatmp+" -Xmx6g -XX:+UseParallelGC -XX:ParallelGCThreads=8 -jar "+gatkjar+" -T MuTect2 --dontUseSoftClippedBases --maxReadsInRegionPerSample 7000 -R "+ref+" --dbsnp "+Dbsnp+" --cosmic "+Cosmic+" -L "+Bed+" -I:tumor "+tbam+" -o "+outdir+"/"+ID+".vcf\n"
	else:
		cmds = javabin + " -Djava.io.tmpdir="+javatmp+" -Xmx6g -XX:+UseParallelGC -XX:ParallelGCThreads=8 -jar "+gatkjar+" -T MuTect2 --dontUseSoftClippedBases --maxReadsInRegionPerSample 7000 -R "+ref+" --dbsnp "+Dbsnp+" --cosmic "+Cosmic+" -L "+Bed+" -I:tumor "+tbam+" -I:Normal "+nbam+" -o "+outdir+"/"+ID+".vcf\n"	
	cmds += javabin + " -Djava.io.tmpdir="+javatmp+" -Xmx6g -XX:+UseParallelGC -XX:ParallelGCThreads=8 -jar "+gatkjar+" -T SelectVariants --disable_auto_index_creation_and_locking_when_reading_rods -R "+ref+" --variant "+outdir+"/"+ID+".vcf"+" -o "+outdir+"/"+ID+".snv.vcf -selectType SNP\n"
	cmds += javabin + " -Djava.io.tmpdir="+javatmp+" -Xmx6g -XX:+UseParallelGC -XX:ParallelGCThreads=8 -jar "+gatkjar+" -T SelectVariants --disable_auto_index_creation_and_locking_when_reading_rods -R "+ref+" --variant "+outdir+"/"+ID+".vcf"+" -o "+outdir+"/"+ID+".indel.vcf -selectType INDEL\n"
	return cmds
def HaplotypeCaller(tbam,javabin,javatmp,gatkjar,ref,Bed,outdir,nbam="null"):
	ID = os.path.basename(tbam).split(".")[0]
	binlist = [javabin,javatmp,gatkjar,ref,Bed,outdir]
	for Bin in binlist:
		if os.path.exists(Bin):
			pass
		else:
			print("test not exists"+Bin)
	#		sys.stderr.write("not existing "+Bin)
			os._exit(1)
	if nbam=="null":
		cmds = javabin + " -Djava.io.tmpdir="+javatmp+" -Xmx6g -XX:+UseParallelGC -XX:ParallelGCThreads=8 -jar "+gatkjar+" -T HaplotypeCaller --disable_auto_index_creation_and_locking_when_reading_rods --dontUseSoftClippedBases -R "+ref+" -I "+tbam+" -L "+Bed+" --genotyping_mode DISCOVERY -stand_call_conf 10 "+"-o "+outdir+"/"+ID+".GATK.var.vcf\n"
	else:
		cmds = javabin + " -Djava.io.tmpdir="+javatmp+" -Xmx6g -XX:+UseParallelGC -XX:ParallelGCThreads=8 -jar "+gatkjar+" -T HaplotypeCaller --disable_auto_index_creation_and_locking_when_reading_rods --dontUseSoftClippedBases -R "+ref+" -I "+tbam+" -I "+nbam+" -L "+Bed+" --genotyping_mode DISCOVERY -stand_call_conf 10 "+"-o "+outdir+"/"+ID+".GATK.var.vcf\n"
	cmds += javabin +" -Djava.io.tmpdir="+javatmp+" -Xmx6g -XX:+UseParallelGC -XX:ParallelGCThreads=8 -jar "+gatkjar+" -T SelectVariants --disable_auto_index_creation_and_locking_when_reading_rods -R "+ref+" --variant "+outdir+"/"+ID+".GATK.var.vcf"+" -o "+ outdir+"/"+ID+"_snp.GATK.var.vcf -selectType SNP\n"
	cmds +=javabin +" -Djava.io.tmpdir="+javatmp+" -Xmx6g -XX:+UseParallelGC -XX:ParallelGCThreads=8 -jar "+gatkjar+" -T SelectVariants --disable_auto_index_creation_and_locking_when_reading_rods -R "+ref+" --variant "+outdir+"/"+ID+".GATK.var.vcf"+" -o "+ outdir+"/"+ID+"_indel.GATK.var.vcf -selectType INDEL\n"
	return cmds

def Mut_Annotation(annovcfbin,vcfF,outdir,mode):
	if os.path.exists(annovcfbin):
		pass
	else:
		print(annovcfbin+" not existing")
		os._exit(1)
	cmds = "perl "+annovcfbin+" -invcf "+vcfF+" -mode "+mode +" -outdir "+outdir+" -debug on\n"
	return cmds

def SearchDB_SomaticMut(schCTDBbin,snv,indel,rootdir,outdir):
	cmds = "perl "+schCTDBbin+" -snv "+snv +" -sindel "+indel+" -rootdir "+rootdir+" -outdir "+outdir+" -dom off"
	return cmds
def Error_Email(errormsg,Emailbin="/home/cancer/cancerAGM_vDS/pipeline/Email_Send_error.py",receivers="null"):
	if receivers=="null":
		cmds = "python "+Emailbin+" --error '"+errormsg+"' --receivers bioinfo@acorndx.com"
	else:
		cmds = "python "+Emailbin+" --error '"+errormsg+"' --receivers "+str(receivers)
	return cmds
