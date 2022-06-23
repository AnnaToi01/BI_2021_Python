from bs4 import BeautifulSoup
import requests
import numpy as np
import sqlite3
import pandas as pd


def pd_to_sql(pd_df, path_to_db):
    """
    Gets a pandas DataFrame and saves it as a database
    @param pd_df: pandas DataFrame
    @param path_to_db: str, path to output databases
    @return: None
    """
    # Creating connection and database
    con = sqlite3.connect(path_to_db)

    with con:
        # Converting pd dataframe to SQL
        pd_df.to_sql(name=path_to_db, con=con, if_exists='replace', index=False)  # one could also append here


def get_countries_table():
    """
    Enters the Worldometers Coronavirus database and returns bs4 table corresponding to countries table
    @return: table, bs4.element.Tag corresponding to coronavirus table
    """
    # Getting the website HTML and finding the table with the countries:
    source = requests.get("https://www.worldometers.info/coronavirus/").text
    soup = BeautifulSoup(source, 'lxml')
    # Table with all the countries
    table = soup.find("table", id="main_table_countries_today")
    return table


def get_headers(table):
    """
    Returns the names of the columns for the coronavirus database
    @param table, bs4.element.Tag corresponding to coronavirus table
    @return: col_names, list of column names
    """
    # Getting the headers
    col_names = []
    for i in table.find_all("th"):
        col_names.append("_".join(i.get_text(strip=True, separator="\n").replace(" ", "_").splitlines()))

    # Correcting some reading error
    col_names[col_names.index('Tot\xa0Cases/_1M_pop')] = 'Tot._Cases/_1M_pop'
    # There are some remnant column names in the end...
    col_names = col_names[:-6]
    return col_names


def continent_table(table, col_names, path_to_output_db):
    """
    Creates a COVID statistic table for continents
    @param table, bs4.element.Tag corresponding to coronavirus table
    @param col_names: , list of column names
    @return: cont, pd.DataFrame with the continent data
    """
    # Index
    ind = 0

    # List of dictionaries corresponding to the continents
    data_cont = []
    for i in table.find_all("tr", class_="total_row_world"):
        # Numerating from 1
        ind += 1
        # Separating the text in the row
        dt = i.text.strip().split("\n")
        # Continent name
        continent = dt[0]
        # Creating a dictionary from the rest of the values
        dic_inf = dict(zip(col_names[2:], dt[2:]))
        # Trying to convert all the numbers to integers
        for key, value in dic_inf.items():
            try:
                dic_inf[key] = int(value.replace(",", ""))
            except ValueError:
                pass
        # Encompassing dictionary for each row
        dic = {
            "#": ind,
            "Continent,Other": continent,
            **dic_inf
        }
        data_cont.append(dic)

    # Dropping one random weird row (7)
    cont = pd.DataFrame(data_cont).set_index("#").drop(7)

    # Reindexing as on the website
    cont.index = np.arange(1, len(cont) + 1)
    cont.index.name = "#"

    # Creating databases
    pd_to_sql(cont, path_to_output_db)
    return cont


def country_table(table, col_names, path_to_output_db):
    """
    Creates a COVID statistic table for continents
    @param table, bs4.element.Tag corresponding to coronavirus table
    @param col_names: , list of column names
    @return: cont, pd.DataFrame with the continent data
    """
    # Index
    ind = 0

    # List of dictionaries corresponding to the continents
    country_data = []
    for i in table.find_all("tr", class_="total_row_world"):
        # Numerating from 1
        ind += 1
        # Separating the text in the row
        dt = i.text.strip().split("\n")
        # Continent name
        continent = dt[1]
        # Creating a dictionary from the rest of the values
        dic_inf = dict(zip(col_names[2:], dt[2:]))
        # Trying to convert all the numbers to integers
        for key, value in dic_inf.items():
            try:
                dic_inf[key] = int(value.replace(",", ""))
            except ValueError:
                pass
        # Encompassing dictionary for each row
        dic = {
            "#": ind,
            "Country,Other": continent,
            **dic_inf
        }
        country_data.append(dic)

    # Dropping one random weird row (7)
    country = pd.DataFrame(country_data).set_index("#")
    # Creating databases
    pd_to_sql(country, path_to_output_db)
    return country


class COVID_Country:
    """A Sample COVID_Country Class for COVID statistics
    It can be used to create a new object, country, and add it to the table
    """

    def __init__(self, country, total_cases, new_cases, total_deaths, new_deaths, total_recovered, new_recovered,
                 active_cases, ser_cr, cas_p_mil, death_p_mil, tot_test, test_p_mil, pop, continent):
        """
        Initiating the class
        @param country: str, country
        @param total_cases: int, total cases
        @param new_cases: int, new cases
        @param total_deaths: int, total deaths
        @param new_deaths: int, new deaths
        @param total_recovered: int, total recovered
        @param new_recovered: int, new, recovered
        @param active_cases: int, active cases
        @param ser_cr: int, serious or critical cases
        @param cas_p_mil: int, cases per million
        @param death_p_mil: int, deaths per million
        @param tot_test: int, total tests
        @param test_p_mil: int, tests per million
        @param pop: int, population size
        @param continent: str, continent of the country
        """
        self.country = country
        self.total_cases = total_cases
        self.new_cases = new_cases
        self.total_deaths = total_deaths
        self.new_deaths = new_deaths
        self.total_recovered = total_recovered
        self.new_recovered = new_recovered
        self.active_cases = active_cases
        self.ser_cr = ser_cr
        self.cas_p_mil = cas_p_mil
        self.death_p_mil = death_p_mil
        self.tot_test = tot_test
        self.test_p_mil = test_p_mil
        self.pop = pop
        self.continent = continent

    def __repr__(self):
        """
        Class representation when printed
        @return: None
        """
        return f"Country {self.country} with total cases of {self.total_cases} and population of {self.pop}"


def insert_country(country):
    """
    Inserts a new COVID_Country object into the database
    @param country: COVID_Country object
    @return: None
    """
    con = sqlite3.connect("country.db")
    cur = con.cursor()
    with con:
        query = "INSERT INTO `country.db` VALUES (" + ("?," * 15)[:-1] + ")"
        cur.execute(query, tuple(country.__dict__.values()))


def get_stat_by_country(country_name, col_names):
    """
    Gets statistics (row) about the country of the choice
    @param country_name: str, name of the country
    @param col_names: , list of column names
    @return: list, statistics about the country
    """
    con = sqlite3.connect("country.db")
    cur = con.cursor()
    with con:
        query = "SELECT * FROM `country.db` WHERE `Country,Other`=:country"
        cur.execute(query, {'country': country_name})
        stat_dic = dict(zip(col_names, *cur.fetchall()))
        return stat_dic


def update_continent(country_name, continent):
    """
    Changing the continent of a country
    @param country_name: str, name of the country
    @param continent: str, name of the continent
    @return: None
    """
    con = sqlite3.connect("country.db")
    cur = con.cursor()
    with con:
        query = """
        UPDATE `country.db` SET Continent = :continent
        WHERE `Country,Other`=:country
        """
        cur.execute(query, {'country': country_name, 'continent': continent})


def update_total_count(country_name, new_cases):
    """
    Updates total count of cases and new cases
    @param country_name: str, name of the country
    @param new_cases: int, number of the new cases
    @return: None
    """
    con = sqlite3.connect("country.db")
    cur = con.cursor()
    with con:
        query = """
        UPDATE `country.db`
        SET
            Total_Cases = Total_Cases + :new_cases,
            New_Cases = :new_cases
        WHERE
            `Country,Other` = :country
        """  # New cases are obviously equal to the new cases that were added that day
        cur.execute(query, {'country': country_name, 'new_cases': new_cases})


def remove_country(country_name):
    """
    Removes a country
    @param country_name: str, name of the country
    @return: None
    """
    con = sqlite3.connect("country.db")
    cur = con.cursor()
    with con:
        query = """
        DELETE from `country.db`
        WHERE
            `Country,Other` = :country
        """
        cur.execute(query, {"country": country_name})


def max_tot_count_country_on_cont():
    """
    Returns a list of countries with maximal total count on a continent/undefined
    @return: list
    """
    con = sqlite3.connect("country.db")
    cur = con.cursor()
    with con:
        query = """
        SELECT Continent, `Country,Other`, Total_Cases, New_Cases, `Tot._Cases/_1M_pop`, Population
        FROM `country.db`
        GROUP BY Continent
        ORDER BY Total_Cases DESC
        """
        cur.execute(query)
        return cur.fetchall()


def count_country_per_continent():
    """
    Returns a list of tuples with count of countries on each continent
     - (count_of_countries, continent)
    @return: list, list of (count_of_countries, continent)
    """
    con = sqlite3.connect("country.db")
    cur = con.cursor()
    with con:
        query = """
        SELECT COUNT(`Country,Other`), Continent
        FROM `country.db`
        GROUP BY Continent
        """
        cur.execute(query)
        return cur.fetchall()


def main():
    """
    Main function that executes everything above and showcases the order of the code
    @return: tuple, tuple of two pandas DataFrames with coronavirus statistics about continents and countries
    """
    # Getting the table for the countries
    table = get_countries_table()
    # Column names
    col_names = get_headers(table)
    # Saving the continent table
    cont = continent_table(table, col_names, "cont.db")
    # Saving the countries table
    country = country_table(table, col_names, "countries.db")

    # Object of class COVID_Country
    utopia = COVID_Country("utopia", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3500000, "dreams")

    # Inserting utopia into the database
    insert_country(utopia)

    # Get statistics
    print(get_stat_by_country("Georgia", col_names))

    # Update continent
    update_continent("Georgia", "Europe")

    # Update the total and new count
    update_total_count('utopia', 1)

    # Return countries with maximal total count on each continent
    print(max_tot_count_country_on_cont())

    # Count of countries per continent
    print(count_country_per_continent())

    # Removes a country
    remove_country("utopia")

    return cont, country


if __name__ == "__main__":
    cont, country = main()
