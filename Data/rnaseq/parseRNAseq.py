
with open("bsubtillis_RPKM.txt") as fin, open("bsubtillis_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[0]+","+line_spt[1]+"\n")


with open("cperfringens.csv") as fin, open("cperfringens_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split(",")
		out.write(line_spt[0]+","+line_spt[1]+"\n")

with open("ctrachomatic.txt") as fin, open("ctrachomatic_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[0]+","+line_spt[3]+"\n")

with open("ecoli.txt") as fin, open("ecoli_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		if line_spt[1][0] == "[":
			out.write(line_spt[0]+","+line_spt[1][1]+"\n")
		else:
			out.write(line_spt[0]+","+line_spt[1]+"\n")

with open("fsucc.txt") as fin, open("fsucc_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[0]+","+line_spt[1]+"\n")


with open("mtuberculosis.txt") as fin, open("mtuberculosis_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[0]+","+line_spt[5]+"\n")

with open("paeruginosa.txt") as fin, open("paeruginosa_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[1]+","+line_spt[2]+"\n")

with open("scoelicolor.txt") as fin, open("scoelicolor_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[0]+","+line_spt[1]+"\n")

with open("scoelicolor.txt") as fin, open("scoelicolor_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[0]+","+line_spt[1]+"\n")

with open("senterica.txt") as fin, open("sentrica_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[0]+","+line_spt[2]+"\n")

with open("vcholerae.txt") as fin, open("vcholerae_filtered.csv",'w') as out:
	for line in fin:
		line_spt = line.split("\t")
		out.write(line_spt[0]+","+line_spt[14]+"\n")