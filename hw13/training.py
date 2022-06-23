import sqlite3
import pandas as pd
import sqlalchemy
from itertools import chain


def sqlite3_pd_to_sql(path_to_file, path_to_db):
    """
    Reads a file (csv file, with first column as index)
    and converts it to a pandas DataFrame
    Converts this pandas DataFrame to SQL using pandas and sqlite3
    @param path_to_file: str, path to the csv file
    @param path_to_db: str, path to the output SQL database
    @return: None
    """
    # Reading the csv through pandas
    df = pd.read_csv(path_to_file, index_col=0)

    # Creating connection and database
    con = sqlite3.connect(path_to_db)

    with con:
        # Converting pd dataframe to SQL
        df.to_sql(name=path_to_db, con=con, if_exists='replace', index=False)  # one could also append here


def sqlalchemy_pd_to_sql(path_to_file, absolute_path_to_db):
    """
    Reads a file (csv file, with first column as index)
    and converts it to a pandas DataFrame
    Converts this pandas DataFrame to SQL using pandas and sqlalchemy
    @param path_to_file: str, path to the csv file
    @param absolute_path_to_db: str, absolute path to the output SQL database
    @return: None
    """
    # Reading the csv through pandas
    df = pd.read_csv(path_to_file, index_col=0)

    # Create a reference for SQL library
    engine = sqlalchemy.create_engine("sqlite:////" + absolute_path_to_db)

    # Conversion to SQL
    df.to_sql(absolute_path_to_db, con=engine, if_exists='replace')


def scrub(name):
    """
    Tries to prevent SQL injection, needed for formatting of query strings
    @param name: str, column/table name
    @return: str, without characters other than digits, characters and _
    """
    # attributation: https://stackoverflow.com/a/3247553/7505395
    return ''.join(chr for chr in name if chr.isalnum() or chr == "_")


# Creating a database with pandas columns and types
def pd_to_cus_sql(path_to_file, path_to_db, table_name):
    """
    Reads a file (csv file, with first column as index)
    and converts it to a pandas DataFrame
    The pandas DataFrame is converted to SQL database,
    with specified table name as well as column names
    without characters other than digits, characters and _
    @param path_to_file: str, path to the csv file
    @param path_to_db: str, path to the output SQL database
    @return: None
    """
    # Type interconversion
    types_pd_to_sql = {
        "O": "text",
        "i": "int",
        "f": "float",
    }

    # Reading the csv through pandas
    df = pd.read_csv(path_to_file, index_col=0)

    # Creating connection and database
    con = sqlite3.connect(path_to_db)

    # Cursor
    cur = con.cursor()

    # Saving column names and types as in SQL
    cols = tuple(map(scrub, tuple(df.columns)))
    types = tuple(map(lambda x: types_pd_to_sql[x.kind], df.dtypes))

    # Tuple of cols and types (col0, type0, col1, type1...)
    ls = tuple(chain.from_iterable(tuple(zip(cols, types))))

    # Str for creation
    creation = f"CREATE TABLE IF NOT EXISTS {scrub(table_name)} (" + ("{} {}, " * (len(types))).format(*ls)[:-2] + ")"

    # Execution of creation
    with con:
        cur.execute(creation)

        # Str for insertion
        insertion = f"INSERT INTO {scrub(table_name)} (" + ("{}," * (len(cols))).format(*cols)[
                                                           :-1] + ") values(" + ("?," * len(cols))[:-1] + ")"

        # Insert Dataframe into SQL Server row by row - this takes a lot of time due to iteration
        for index, row in df.iterrows():
            cur.execute(insertion, tuple(row.values))


def empty_sql_col(path_to_db, col_names, types, table_name):
    """
    Create an empty SQL database with specified column names and types,
    @param path_to_db: str, path to the output SQL database
    @param col_names: list, column names
    @param types: list, list of types of SQL
    @param table_name: str, name of the table
    @return: None, creates an empty database
    """
    # Creating connection and database
    con = sqlite3.connect(path_to_db)

    # Cursor
    cur = con.cursor()

    # Tuple of cols and types (col0, type0, col1, type1...)
    ls = tuple(chain.from_iterable(tuple(zip(col_names, types))))

    # Str for creation
    creation = f"CREATE TABLE IF NOT EXISTS {scrub(table_name)} (" + ("{} {}, " * (len(types))).format(
        *map(scrub, ls))[:-2] + ")"

    # Execution of creation
    with con:
        cur.execute(creation)


if __name__ == "__main__":
    # sqlite3
    sqlite3_pd_to_sql("genotyping_data/metadata.csv", "sqlite3_metadata.db")
    sqlite3_pd_to_sql("genotyping_data/genstudio.csv", "sqlite3_genstudio.db")

    # sqlalchemy
    sqlalchemy_pd_to_sql("genotyping_data/metadata.csv",
                         "/home/annatoidze/Documents/BI_2021_Python/hw13/sqlalchemy_metadata.db")
    sqlalchemy_pd_to_sql("genotyping_data/genstudio.csv",
                         "/home/annatoidze/Documents/BI_2021_Python/hw13/sqlalchemy_genstudio.db")

    # row by row, corrected column names
    pd_to_cus_sql("genotyping_data/metadata.csv", "cus_metadata.db", "metadata")
    pd_to_cus_sql("genotyping_data/genstudio.csv", "cus_gen.db", "genstudio")

    # Making an empty database
    empty_sql_col("employee.db", ["first", "last", "pay"], ["text", "text", "float"], "employee")

    # Selection examples

    # Connecting to the database
    con = sqlite3.connect("sqlite3_genstudio.db")
    cur = con.cursor()

    # Taking a look at table name
    cur.execute("SELECT * FROM sqlite_master WHERE type='table'")
    print(cur.fetchall())

    # E.g. selecting all rows with 1st chromosome and where Allel1 is A
    # We have to refer to the databases with whitespaces in them with ``
    all_a_chr1 = cur.execute("SELECT * FROM 'sqlite3_genstudio.db' WHERE `Allele1 - Top`='A' AND Chr=1").fetchall()
    print(all_a_chr1)

    # Database without whitespaces
    con = sqlite3.connect("cus_gen.db")
    cur = con.cursor()
    all_a_chr1_gc = cur.execute(
        "SELECT SampleID, SNPName, SNP, Chr, Position FROM genstudio WHERE Allele1Top='A' AND Chr=2 AND GCScore>0.9")
    print(all_a_chr1_gc.fetchall())

    # I noticed that the dna_chip_id column in metadata.csv resembles the Sample ID in genstudio.csv
    # Let's merge them an create a merged database
    mt = pd.read_csv("genotyping_data/metadata.csv")
    gen = pd.read_csv("genotyping_data/genstudio.csv")

    # Merging
    mer = pd.merge(mt, gen, left_on='dna_chip_id', right_on='Sample ID')
    mer.to_csv("genotyping_data/merged.csv")

    # Converting to SQL and saving as a merged.db
    sqlite3_pd_to_sql("genotyping_data/merged.csv", "merged.db")
    con = sqlite3.connect("merged.db")

    # Selecting some columns
    cur = con.cursor()
    print(cur.execute("SELECT `Sample ID`, `SNP Name`, sex, breed FROM 'merged.db'").fetchall())
