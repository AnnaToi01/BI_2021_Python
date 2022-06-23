import sys
import requests
import re
from bs4 import BeautifulSoup
import time
from Bio import SeqIO
import argparse


def save_content(resp, path_to_output):
    """
    Saves the content of the requests model Response into a file
    @param resp: requests.models.Response
    @param path_to_output: str, path to ot
    @return: None
    """
    with open(path_to_output, "wb") as file:
        file.write(resp.content)
    return


def check_response(resp):
    """
    Prints the URL and the status code in case the request did not function
    @param resp: requests.models.Response
    @return: None
    """
    if not resp.ok:
        print(resp.url)
        print(resp.status_code)


class Taxonomy:
    """
    Class Taxonomy works with https://www.ncbi.nlm.nih.gov/Taxonomy/TaxIdentifier/tax_identifier.cgi from NCBI

    Its main purpose is to extract the tax_ids from the species names
    """

    def __init__(self):
        """
        Initializes the class Taxonomy
        """
        self.species_name = None

    def get_tax_id(self, species_name):
        """
        Returns the list of tax_ids of the species specified in species_name
        @param species_name: str, name/names of species, separated by "\n"
        @return: tax_ids, list of str
        """

        self.species_name = species_name

        # Creating payload to access the according results page
        tax_payload = {
            "tax": self.species_name,
            "button": "Show on screen"
        }

        # Request URL from taxonomy website
        tax_url = "https://www.ncbi.nlm.nih.gov/Taxonomy/TaxIdentifier/tax_identifier.cgi"

        # Saving the according results
        resp = requests.post(tax_url, data=tax_payload)

        # Check response
        check_response(resp)

        # Saves the results as html file
        save_content(resp, "tax.html")

        # Reading the content of the response (html) from the website with soup
        tax_soup = BeautifulSoup(resp.content, 'lxml')

        # Table of taxonomy
        tax_table = tax_soup.find("table", cellpadding="0", cellspacing="5", width="600").find_all("tr")

        # Getting headers
        headers = tax_table[0].text.split("\n")
        ind_taxid = headers.index("taxid")

        # Getting rows
        tax_ids = []

        # Here we parse through the table generated as a result
        for rows in tax_table[1:]:
            # We assign according variables to values in each of four columns
            tax_ids.append(rows.text.split("\n")[ind_taxid])

        if tax_ids.__contains__(" "):
            raise ValueError("One of the taxon names was invalid")

        return tax_ids


class Alignment:
    """
    Works with tblastn (https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=tblastn) alignment output and
    returns an object with all the alignment details
    """
    def __init__(self, subj_name, subj_id, subj_len, num_matches,
                 subj_range, metrics_dic, score, e_value, identity, query_seq, subj_seq):
        self.subj_name = subj_name
        self.subj_id = subj_id
        self.subj_len = subj_len
        self.num_matches = num_matches
        self.subj_range = subj_range
        self.metrics_dic = metrics_dic
        self.score = score
        self.e_value = e_value
        self.identity = identity
        self.query_seq = query_seq
        self.subj_seq = subj_seq


def query(fasta_seq, tax_id):
    """
    Saves first query input HTML file, and the HTML file after job was completed,
    returns the JobID (RID) and the accession numbers
    @param fasta_seq: str, FASTA sequence
    @param tax_id: str, taxon id
    @return: RID, str,
             acc_num_ls, list
    """

    # print(fasta_seq)
    # print(tax_id)
    # Request URL for BLAST
    blast_url = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"

    # Payload for initial query
    query_payload = {
        "QUERY": fasta_seq,
        "db": "protein",
        "GENETIC_CODE": 1,
        "ADV_VIEW": "true",
        "stype": "nucleotide",
        # "SUBJECTFILE": "(binary)",
        "DATABASE": "Whole_Genome_Shotgun_contigs",
        "DB_GROUP": "wgsOrg",
        "EQ_MENU": tax_id,
        "NUM_ORG": 1,
        "MAX_NUM_SEQ": 100,
        "EXPECT": 0.05,
        "WORD_SIZE": 6,
        "HSP_RANGE_MAX": 0,
        "MATRIX_NAME": "BLOSUM62",
        "MATCH_SCORES": "1,-2",
        "GAPCOSTS": "11 1",
        "COMPOSITION_BASED_STATISTICS": 2,
        "FILTER": "L",
        "REPEATS": 4829,
        "TEMPLATE_LENGTH": 0,
        "TEMPLATE_TYPE": 0,
        "PSSM": "(binary)",
        "SHOW_OVERVIEW": "true",
        "SHOW_LINKOUT": "true",
        "GET_SEQUENCE": "true",
        "FORMAT_OBJECT": "Alignment",
        "FORMAT_TYPE": "HTML",
        "ALIGNMENT_VIEW": "Pairwise",
        "MASK_CHAR": 2,
        "MASK_COLOR": 1,
        "DESCRIPTIONS": 100,
        "ALIGNMENTS": 100,
        "LINE_LENGTH": 60,
        "NEW_VIEW": "true",
        "NCBI_GI": "false",
        "SHOW_CDS_FEATURE": "false",
        "NUM_OVERVIEW": 100,
        "FORMAT_NUM_ORG": 1,
        "CONFIG_DESCR": "2,3,4,5,8,9,10,11,12,13,14",
        "CLIENT": "web",
        "SERVICE": "plain",
        "CMD": "request",
        "PAGE": "Translations",
        "PROGRAM": "tblastn",
        "UNGAPPED_ALIGNMENT": "no",
        "BLAST_PROGRAMS": "tblastn",
        "DB_DISPLAY_NAME": "wgs",
        "ORG_DBS": "orgDbsOnly_wgs",
        "SELECTED_PROG_TYPE": "tblastn"}

    # Getting query page
    query_resp = requests.post(blast_url, data=query_payload)

    # Check response
    check_response(query_resp)

    # Reading the query_resp
    query_soup = BeautifulSoup(query_resp.content, 'lxml')

    # Getting RID
    RID = query_soup.find("input", {"name": "RID"})["value"]

    # Save it as an HTML page
    save_content(query_resp, "_".join([RID, "query_page.html"]))

    # Making RID payload
    rid_payload = {
        "CMD": "Get",
        "RID": RID
    }

    # Saving the according results
    rid_resp = requests.post(blast_url, data=rid_payload)

    # Check response
    check_response(rid_resp)

    # Reading the content of the response
    rid_soup = BeautifulSoup(rid_resp.content, "lxml")

    # List for accession numbers
    acc_num_ls = []

    # Waiting for the results to load
    while True:
        try:
            # print(rid_soup.find("table", id="dscTable"))
            # Going over each row in the table under Description tab and getting the accession number
            for row in rid_soup.find("table", id="dscTable").tbody.find_all("tr"):
                acc_num_ls.append(row.find("td", class_="c12 l lim").text.strip().split(".")[0])
            break
        except AttributeError:
            print("Loading...")
            time.sleep(10)
            # Reloading the website
            rid_resp = requests.post(blast_url, data=rid_payload)
            # Check response
            check_response(rid_resp)
            # Reading the content of the response
            rid_soup = BeautifulSoup(rid_resp.content, "lxml")

    # Saving the first results page with Descriptions
    save_content(rid_resp, "_".join([RID, "rid.html"]))

    return RID, acc_num_ls


def get_alignment(RID, acc_num_ls):
    """
    Saves the alignment HTML file and gets all alignment details from Alignment tab of the BLAST results,
    generating an Alignment object and for each alignment match returning a list of Alignment objects
    @param RID: str, RID
    @param acc_num_ls: list, list of accession numbers
    @return: alignments, list of Alignment objects
    """
    # Take accession numbers, make them into format for ALIGN_SEQ_LIST
    acc_seq = ""
    for i in acc_num_ls:
        acc_seq += "gb|" + i + "|,"

    # Making alignment payload
    alig_payload = {
        "CMD": "Get",
        "RID": RID,
        "ALIGN_SEQ_LIST": acc_seq[:-1],
    }

    # Request URL for BLAST
    blast_url = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"

    # Saving the according results
    alig_resp = requests.post(blast_url, data=alig_payload)
    # print(resp.url)
    # print(rid_soup.text)

    # Check response
    check_response(alig_resp)

    # Save the alignment as HTML file
    save_content(alig_resp, "_".join([RID, "alignments.html"]))

    # Reading the HTML
    alig_soup = BeautifulSoup(alig_resp.content, "lxml")

    alig_list = []

    for i in alig_soup.find_all("div", class_="oneSeqAln"):
        # Title/headers of one alignment block
        title = i.find("div", class_="dlfRow").text.strip().split("\n")

        # Accessing subject names, id, len, matches...
        subj_name = title[0]
        subtitle = title[1].split(":")
        subj_id = subtitle[1][:-6]
        subj_len = subtitle[2][:-17]
        num_matches = subtitle[-1]
        #     print(subj_name, subj_id, subj_len, num_mathes)

        # Now accessing the alignment metrics bar
        alig_bar = i.find("div", class_="alnAll")
        #     stat_bar = alig_bar.find("div", id=re.compile(r"hd.*"))
        #     print(stat_bar.text.strip())

        # Accessing the subject range, score, and so on - generate a dictionary, as well as each value separately
        subj_range = alig_bar.find("span", class_="alnRn").label.text.split()
        subj_range = tuple(map(int, map(subj_range.__getitem__, [-3, -1])))
        score_table = alig_bar.table
        description = [i.text for i in score_table.find_all("tr")[0].find_all("th")]
        #     print(score_table.find_all("tr")[0].find_all("th"))
        #     print(description)
        scores = [i.text for i in score_table.find_all("tr")[1].find_all("td")]
        #     print(scores)
        metrics_dic = dict(zip(description, scores))
        #     print(metrics_dic)
        score = metrics_dic["Score"]
        e_value = metrics_dic["Expect"]
        identity = metrics_dic["Identities"]
        #     print(score, e_value, identity)

        # Getting the alignment sequences
        alig_seq = alig_bar.find("div", id=re.compile(r"ar.*"))
        # print(alig_seq.text)
        query_seq = ""
        subj_seq = ""
        spl_alig_seq = alig_seq.text.split()
        for i, entry in enumerate(spl_alig_seq):
            # Query sequence
            if entry == "Query":
                #         print(i)
                #         print(spl_alig_seq[i+2])
                query_seq += spl_alig_seq[i + 2]

            # Subject (input) sequence
            elif entry == "Sbjct":
                subj_seq += spl_alig_seq[i + 2]

        alig_list.append(Alignment(subj_name, subj_id, subj_len, num_matches, subj_range,
                         metrics_dic, score, e_value, identity, query_seq, subj_seq))
    return alig_list


def fasta_alig(path_to_file, tax_id):
    """
    Reads a FASTA file and returns a dictionary of Alignments for each FASTA sequence
    @param path_to_file: str, path to FASTA file
    @param tax_id: str, taxon id
    @return: alig_dict: dict, dictionary with FASTA ids as keys and list of Alignment objects as values
    """
    alig_dict = {}
    with open(path_to_file) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            fasta_seq = str(record.seq)
            RID, acc_num_ls = query(fasta_seq, tax_id)
            print("RID: ", RID)
            print("Accession numbers of alignments: ", *acc_num_ls)
            alig_obj = get_alignment(RID, acc_num_ls)
            # print(alig_obj)
            alig_dict[record.id] = alig_obj

    return alig_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provide Taxonomy IDs and/or BLAST alignments")

    # Taxonomy ID argument
    parser.add_argument("-id", "--taxid", help="Species name(s) or taxID(s)", nargs="+", default=sys.stdin)

    # Input file
    parser.add_argument("-i", "--input_file", help="Path to input FASTA file with protein sequences", nargs="?")

    # Parsing all the arguments
    args = parser.parse_args()

    # Accessing the taxonomy ID
    tax = Taxonomy()
    ls = tax.get_tax_id("\n".join(args.taxid))

    if args.input_file is None:
        question_alig = input("Do you want to continue with the alignment? [print yes if continue] ")
        if question_alig.lower() == "yes":
            fasta_seq = input("Enter protein FASTA sequence: ")
            RID, acc_num_ls = query(fasta_seq, ls[0])
            print("RID: ", RID)
            print("Accession numbers of alignments: ", *acc_num_ls)
            print(get_alignment(RID, acc_num_ls))
        else:
            print("TaxIDs:", *ls)
    else:
        # Getting the Alignment
        print(fasta_alig(args.input_file, ls[0]))
