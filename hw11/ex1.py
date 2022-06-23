import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
import requests

pd.options.mode.chained_assignment = None

df = pd.read_csv("https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv", sep=",")

f = df.columns.get_loc
ACGT = df.iloc[:, np.r_[f("reads_all"), f("A"):f("A_fraction")]]


def get_el_pd_df(pd_df, ind_ls):
    """
    Gets the cell value, element, from a list with 2 indices (1st - row, 2nd - column)
    @param pd_df: pandas DataFrame
    @param ind_ls: list of 2 elements, 1st - row, 2nd - column
    @return: object, cell value of the pandas DataFrame at the ind_ls
    """
    return pd_df.iloc[[ind_ls[0]], [ind_ls[1]]].iloc[0, 0]


def sum_of_el_pd_df(pd_df, ind_ls):
    """
    Calculates sum of the cell values, elements indicated by the list of indices (list of sublists)
    @param pd_df: pandas DataFrame
    @param ind_ls: list, list of sublists, each sublist a list of 2 elements, 1st - row, 2nd - column
    @return: int, sum of the cell values
    """
    elements = []
    for i in ind_ls:
        elements.append(get_el_pd_df(pd_df, i))
    return sum(elements)


nans = np.array(np.where(ACGT.isnull())).T  # Indices of NaNs (each row 2-element list)
not_nans = np.array(np.where(ACGT.notnull())).T  # Indices of Not NaNs
for i in range(len(ACGT)):
    ind_nan = nans[i]  # Getting the list of nan indices
    ind_not_nan = not_nans[4 * i:4 * i + 4]  # Getting the list of not nan indices
    # Getting the number of reads
    num_reads = get_el_pd_df(ACGT, ind_not_nan[0])
    # Getting the sum of the other not-nan nucleotides
    sum_nuc = sum_of_el_pd_df(ACGT, ind_not_nan[1:4])
    # Substituting the nan-elements
    ACGT.at[ind_nan[0], ACGT.columns[ind_nan[1]]] = num_reads - sum_nuc

nucleotides = ["A", "C", "T", "G"]
for nuc in nucleotides:
    ACGT[nuc + "_frequency"] = ACGT[nuc] / ACGT["reads_all"]


ACGT["pos"] = df["pos"]

ACGT[['pos'] + [x + "_frequency" for x in nucleotides]].plot(x='pos', stacked=True,
                                                             figsize=(15, 10), subplots=True)
plt.savefig("ACGT_frequency_plt.jpg")
for ax in plt.gcf().axes:
    ax.legend(loc=1)
plt.savefig("ACGT_frequency_plt.jpg")
plt.show()

ACGT[['pos'] + nucleotides].plot(x='pos', kind='bar', stacked=True,
                                 figsize=(15, 10))
plt.savefig("ACGT_count_hist.jpg")
plt.legend(loc='upper right')
plt.show()

ACGT[['pos'] + [x + "_frequency" for x in nucleotides]].plot(x='pos', kind='bar', stacked=True,
                                                             figsize=(15, 10))
plt.legend(loc='upper right')
plt.savefig("ACGT_freq_hist.jpg")
plt.show()
