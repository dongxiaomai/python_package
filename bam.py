#!/bin/python
import sys
import pysam
import sys
import os
import threading
import tempfile
import gzip
import Dict
import time
base=[str(x) for x in range(10)]+[chr(x) for x in range(ord('A'), ord('A')+6)]

def addtodict(thedict,key_a,val):
	if key_a in thedict:
		thedict[key_a].append(val)
	else:
		thedict[key_a]=[val]

def addtodict2(thedict,key_a,key_b,val):
	if key_a in thedict:
	#	addtodict(thedict[key_a],key_b,val)
		 thedict[key_a].update({key_b:val})
	else:
		thedict.update({key_a:{key_b:val}})
def addtodict3(thedict,key_a,key_b,key_c,val):
	if thedict.has_key(key_a):
		addtodict2(thedict[key_a],key_b,key_c,val)
	else:
		thedict.update({key_a:{key_b:{key_c:val}}})
def addtodict4(thedict,key_a,key_b,key_c,key_d,val):
	if key_a in thedict:
		addtodict3(thedict[key_a],key_b,key_c,key_d,val)
	else:
		thedict.update({key_a:{key_b:{key_c:{key_d:val}}}})

def get_bed_dict(bedfile):
	bed_dict = {}
	i = 0
	init_chr = "chr1"
	for line in open(bedfile,"r"):
		lines = line.strip("\n").split("\t")
		ID  = lines[0]+":"+lines[1]+"_"+lines[2]
		range_list = list(range(int(lines[1]),int(lines[2])+1))
#		if lines[0] not in bed_dict.keys():
#			bed_dict[lines[0]]=range_list
#		else:
#			bed_dict[lines[0]][0:0] = range_list
		if len(lines[1])==5:
			ID = lines[1][0]
		else:
			ID = lines[1][:len(lines[1])-5]
		if lines[0] not in bed_dict.keys():
			bed_dict[lines[0]]={}
			bed_dict[lines[0]][ID]=range_list
		else:
			if ID not in bed_dict[lines[0]].keys():
				bed_dict[lines[0]][ID]=range_list
			else:
				bed_dict[lines[0]][ID][0:0]=range_list
		if init_chr==lines[0]:
			pass
		else:
			init_chr=lines[0]
		i+=1
#		Dict.addtodict3(bed_dict,lines[0],ID,"Start",int(lines[1]))
#		Dict.addtodict3(bed_dict,lines[0],ID,"End",int(lines[2]))
	return bed_dict
def filter_bed_dict(beddict,Chr,pos):
	if Chr not in beddict.keys():
		return True
	else:
		pos_in = False
		if len(str(pos))==5:
			ID = str(pos)[0]
		else:
			ID = str(pos)[:len(str(pos))-5]
		if ID not in beddict[Chr].keys():
			return False
		else:
			if int(pos) not in beddict[Chr][ID]:
				return False
			else:	
				return True	


def split_bed(bed,outdir,num):
	i=0
	bed_list=[]
	for line in open(bed):
		bed_list.append(line)
		i+=1
	Temp=int(i/num)
	bedF=[]
	for j in range(1,num):
		Out=open(outdir+"/"+bed.split("/")[-1].replace("bed","sub_"+str(j)+".bed"),"w")
		bedF.append(outdir+"/"+bed.split("/")[-1].replace("bed","sub_"+str(j)+".bed"))
		for k in bed_list[(j-1)*Temp:j*Temp]:
			Out.write(k)
		Out.close()
	Out=open(outdir+"/"+bed.split("/")[-1].replace("bed","sub_"+str(num)+".bed"),"w")
	bedF.append(outdir+"/"+bed.split("/")[-1].replace("bed","sub_"+str(num)+".bed"))
	for k in bed_list[(num-1)*Temp:]:
	#	bedF.append(outdir+"/"+bed.split("/")[-1].replace("bed",str(num)+".bed"))
		Out.write(k)
	Out.close()
	return bedF	

def read_gz_file(File):
	if os.path.exists(File):
		with gzip.open(File,"rb") as pf:
			for line in pf:
				yield line
	else:
		print ("not file")



class MyThread(threading.Thread):
	def __init__(self,bam,chrom,outbam):
		threading.Thread.__init__(self)
		self.bam=bam
		self.chrom=chrom
		self.outbam=outbam
	def run(self):
		split_chr(self.bam,self.chrom,self.outbam)
def test(bam,chrom,outbam):
	Thd=[]
	for i in range(len(chrom)):
		my_thread=MyThread(bam,chrom[i],outbam[i])
		Thd.append(my_thread)
	for i in range(len(chrom)):
		Thd[i].start()
	for i in range(len(chrom)):
		Thd[i].join()
	return outbam
chr=['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX']
def match_lens(cigar):
	m_len=0
	if cigar !=None:
		for tupple in cigar:
			if tupple[0]==0:
				m_len+=int(tupple[1])
			else:
				pass
	else:
		pass
	return m_len

def cut_fasta(chr,start,end,fasta):
	temp=tempfile.NamedTemporaryFile()
	os.system("samtools faidx "+fasta+" "+chr+":"+start+"-"+end+">"+temp.name)
	Seqline=""
	for seqline in open(temp.name,"r"):
		if ">" in seqline:
			continue
		else:
			Seqline+=seqline.strip("\n")
	return Seqline

def dec2bin(string_num,binnum=12):
	base_init='0'*int(binnum)
	num=int(string_num)
	mid=[]
	if num==0:
		return base_init
	while True:
		if num==0:
			break
		else:
			pass
		num,rem=divmod(num,2)
		mid.append(base[rem])
		base_real=''.join([str(x) for x in mid[::-1]])
	return base_init[0:int(binnum)-len(base_real)]+base_real
def zhuanhuan_seq(seq):
	seq_rev=[]
	array=range(len(seq))
	array_rev=array[::-1]
	for i in array_rev:
		if seq[i]=='A':
			seq_rev.append('T')
		elif seq[i]=='T':
			seq_rev.append('A')
		elif seq[i]=='G':
			seq_rev.append('C')
		elif seq[i]=='C':
			seq_rev.append('G')
		else:
			seq_rev.append('N')
	return "".join(seq_rev)
def zhuanhuan_seq_v2(seq):
	seq_rev=[]
	for base in seq:
		if base=="A":
			seq_rev.append('T')
		elif base=="T":
			seq_rev.append('A')
		elif base=="G":
			seq_rev.append('C')
		elif base=="C":
			seq_rev.append('C')
		else:
			seq_rev.append('N')
	return "".join(seq_rev)
def fasta_cut(fasta,fasta_new,chr,pos_start,pos_end):
	os.system("samtools faidx "+fasta+" "+chr+":"+pos_start+"-"+pos_end+">>"+fasta_new)
def fasta_merge_bed(fasta,fasta_new,bedfile):
	bed=open(bedfile,"r")
	CHR=[]
	for line in bed.readlines():
		lines=line.strip("\n").split("\t")
		chr=lines[0]
		pos_start=lines[1]
		pos_end=lines[2]
		fasta_cut(fasta,fasta_new,chr,pos_start,pos_end)
	os.system("bwa index "+fasta_new)
	os.system("samtools faidx "+fasta_new)
def Soft_Type_judge(cigar):
	SC=False
	if len(cigar)==1:
		SC_TYPE="MM"
	else:
		for tupple in cigar:
			if tupple[0]==4:
				if cigar[0][0]==4:
					SC_TYPE="SM"	
				else:
					SC_TYPE="MS"
				SC=True
	if len(cigar)>4:
		return "null"
	if SC:
		pass
	else:
		SC_TYPE="MM"
	return SC_TYPE
def cigar2string(cigar):
	line=[]
	for tupple in cigar:
		if tupple[0]==0:
			line.append(str(tupple[1])+"-M")
		elif tupple[0]==1:
			line.append(str(tupple[1])+"-I")
		elif tupple[0]==2:
			line.append(str(tupple[1])+"-D")
		elif tupple[0]==4:
			line.append(str(tupple[1])+"-S")
		else:
			line.append(str(tupple[1])+"-N")
	return ":".join(line)
def zhuanhuan_qual(qual):
	qual_rev=[]
	array=range(len(qual))
	array_rev=array[::-1]
	for i in array_rev:
		qual_rev.append(qual[i])
	return "".join(qual_rev)
def capture_ratio(bam,bed,outBAM):
	inbam=pysam.Samfile(bam, "rb")
	bedfile=open(bed,"r")
	bamEntry=inbam.fetch(until_eof=True)
	total_num=0
	for line in bamEntry:
		total_num+=1
	seqlen=len(line.seq)
	total_capture=0
	inbam.close()
	inbam=pysam.Samfile(bam, "rb")
	#outBAM=bam.replace(".bam",".capture.bam")
	outbam=pysam.Samfile(outBAM,"wb", template=inbam)
	for line in bedfile.readlines():
		lines=line.strip("\n").split("\t")
		bamEntry=inbam.fetch(lines[0],(int(lines[1])-seqlen), (int(lines[2])))
		for bam_line in bamEntry:
			total_capture+=1
			outbam.write(bam_line)
	outbam.close()
	cap_ratio=float(total_capture)/float(total_num)
	return [outBAM,cap_ratio]
def split(bam):
	inbam=pysam.Samfile(bam, "rb")
	outBAM=[]
	for line in chr:
		bamEntry=inbam.fetch(line)
		outBam=bam.replace(".bam","."+line+".bam")
		outBAM.append(outBam)
		outbam=pysam.Samfile(outBam,"wb", template=inbam)
		for bam_line in bamEntry:
			outbam.write(bam_line)
		outbam.close()
	inbam.close()
	return outBAM
def split_chr(bam,chrom,outBAM):
	inbam=pysam.Samfile(bam, "rb")
	outbam=pysam.Samfile(outBAM,"wb",template=inbam)
	for line in chrom:
		bamEntry=inbam.fetch(line)
		for bam_line in bamEntry:
			outbam.write(bam_line)
	outbam.close()
	inbam.close()
	return outBAM
def split_thread(bam,thread):
	out=[]
	i=0
	outtxt=[]
	outBAM=[]
	for i in range(int(thread)):
		OUTbam=bam.replace(".bam","."+str(i)+".bam")
		outBAM.append(OUTbam)
		out=[]
		outtxt.append(out)
	i=0
	for line in chr:
		if i< int(thread):
			pass
		else:
			i=0
		outtxt[i].append(line)
		i+=1
	print(outtxt)
	outBAM=test(bam,outtxt,outBAM)
	return outBAM
def merge(bamdata,bam):
	inBAM=[]
	for line in bamdata:
		inbam=pysam.Samfile(line,"rb")
		inBAM.append(inbam)
	outbam=pysam.Samfile(bam,"wb",template=inBAM[0])
	for line in inBAM:
		bamEntry=line.fetch(until_eof=True)
		for bam_line in bamEntry:
			outbam.write(bam_line)
	outbam.close()
	for line in inBAM:
		line.close()
	return bam
def read_num(bam):
	inbam=pysam.Samfile(bam,"rb")
	bamEntry=inbam.fetch(until_eof=True)
	total_num=0
	for line in bamEntry:
		total_num+=1
	return total_num
def rm_dup(bam,rm_bam):
	#rm_bam=bam.replace("bam","rm_dup.bam")
	inbam=pysam.Samfile(bam,"rb")
	bamEntry=inbam.fetch(until_eof=True)
	outbam=pysam.Samfile(rm_bam,"wb",template=inbam)
	total_num=0
	dup_num=0
	for line in bamEntry:
		total_num +=1
		if (int(line.flag) >1024 and int(line.flag)<2048) or (int(line.flag)>3072 and int(line.flag)<4096):
			dup_num+=1
			continue
		else:
			outbam.write(line)
	outbam.close()
	inbam.close()
	dup_ratio=float(dup_num)/float(total_num)
	return [rm_bam,dup_ratio]


