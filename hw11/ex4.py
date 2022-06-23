import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_gff(path_to_GFF_file):
    """
    Returns the GFF file as pandas DataFrame
    @param path_to_GFF_file: str, path to GFF file
    @return: pandas DataFrame
    """
    gff_col = ["chromosome",
               "source",
               "type",
               "start",
               "end",
               "score",
               "strand",
               "phase",
               "attribute"]
    return pd.read_csv("rrna_annotation.gff",
                       sep="\t",
                       names=gff_col,
                       comment="#")


gff = read_gff("rrna_annotation.gff")


def read_bed6(path_to_BED_file):
    """
    Reads the 6-column BED file and returns it as a pandas DataFrame
    @param path_to_BED_file:
    @return:
    """
    bed_col = ["chromosome",
               "start",
               "end",
               "name",
               "score",
               "strand"]
    return pd.read_csv(path_to_BED_file,
                       sep="\t",
                       names=bed_col)


bed = read_bed6("alignment.bed")

gff["attribute"] = gff["attribute"].str.split("=").str[2].str.split(" ").str[0]

gff.loc[:, ["chromosome", "attribute"]].value_counts().reset_index(name='counts')
plt.figure(figsize=(10, 10), dpi=80)
sns.countplot(x=gff.chromosome, data=gff, hue=gff.attribute, palette='pastel')
plt.xticks(rotation=90)
plt.show()


def gff2bed(gff):
    """
    Converts GFF pandas DataFrame coordinates to BED coordinates
    @param gff: pandas DataFrame, gff
    @return: pandas DataFrame with BED coordinates
    """
    gff_2_bed = gff.copy()
    gff_2_bed.start -= 1
    return gff_2_bed


gff_2_bed = gff2bed(gff)
mrg = gff_2_bed.merge(bed, how='inner', on='chromosome')
filt_mrg = mrg[(mrg["start_y"] <= mrg["start_x"]) & (mrg["end_y"] >= mrg["end_x"])]
print(filt_mrg)
