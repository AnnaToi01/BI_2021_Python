import requests
from bs4 import BeautifulSoup


class Github:
    "Provides information about Github account"

    github_website = "https://github.com/"

    def __init__(self, username):
        self.username = username

    def get_user_info(self):
        """
        Returns a dictionary containing user information
        @return: user_information, dictionary
        """
        user_information = {}

        source = requests.get(Github.github_website + self.username).text
        soup = BeautifulSoup(source, 'lxml')

        # Left side profile
        profile = soup.find('div', class_="js-profile-editable-replace")

        # User name
        name = profile.h1.span.text.strip()
        user_information["name"] = name
        # print(name)

        # Followers
        for i in profile.find_all('a', class_='Link--secondary no-underline no-wrap'):
            foll = i.text.strip().replace("\n", "").split()
            user_information[foll[1]] = int(foll[0])
            # print(" ".join(i.text.strip().replace("\n", "").split()))

        # Information (organization, place, website)
        for i in profile.ul.find_all("li"):
            user_information[i["itemprop"]] = i.text.strip()

        # Number of public repositories
        num_rep = soup.find("a", class_="UnderlineNav-item js-responsive-underlinenav-item").span.text
        # print(num_rep)

        user_information["Number of repositories"] = num_rep

        return user_information

    def get_user_repositories(self):
        """
        Returns a list of repositories in the form of a list of dictionaries
        @return: list, list of dictionaries,
                 each dictionary with keys username, name of repository, description, language
        """

        params = {
            'tab': 'repositories'
        }

        rep = requests.get(Github.github_website + self.username, params=params).text
        soup = BeautifulSoup(rep, 'lxml')

        rep_list_of_dict = []
        for i in soup.find('div', id='user-repositories-list').find_all("li"):
            rep_dict = {"Username": self.username}

            # Names of repositories
            name_rep = i.h3.a.text.strip()
            rep_dict["Name of repository"] = name_rep

            # Descriptions

            try:
                rep_dict["Description"] = i.p.text.strip()
            except AttributeError:
                pass

            # Programming language
            try:
                rep_dict["Programming Language"] = i.find("span", itemprop="programmingLanguage").text
            except AttributeError:
                pass

            rep_list_of_dict.append(rep_dict)

        return rep_list_of_dict

    def list_repository_contents(self, repository, repository_path):
        """
        Returns a list of files and directories in the repository of the user with path repository_path
        @param repository: str, repository name
        @param repository_path: str, path to repository
        @return: ls: list, list of files/directories in the repository
        """
        rep = requests.get("/".join([Github.github_website, self.username, repository, repository_path])).text
        soup = BeautifulSoup(rep, 'lxml')
        ls = []
        # Accessing all the rows in the repository
        for i in soup.find_all('div', role='rowheader'):
            ls.append(i.text.strip())
        return ls

    def download_file(self, repository, remote_file_path, local_file_path):
        """
        Downloads a file which has remote path in a repository and saves it locally
        @param repository: str, repository name
        @param remote_file_path: str, path to file in the repository
        @param local_file_path: str, path to file locally
        @return: None, saved file
        """
        raw_github_website = "https://raw.githubusercontent.com"
        if remote_file_path.startswith("blob"):
            remote_file_path = remote_file_path[5:]

        rep = requests.get("/".join([raw_github_website, username, repository, remote_file_path]))
        if not rep.ok:
            print("File does not exist or it is a directory")

        with open(local_file_path, "w") as f:
            f.write(rep.text)

        return


if __name__ == "__main__":
    # Defining username
    username = "annatoi01"

    # Creating an instance
    inst = Github(username)

    # Getting user info
    print(inst.get_user_info())

    # Getting the list of user repositories
    print(inst.get_user_repositories())

    # Getting the content of the repository
    repository = 'BI_2021_Python'
    repository_path = 'tree/hw11/'
    print(inst.list_repository_contents(repository, repository_path))

    # Downloading file
    repository = 'BI_ML_2021'
    remote_file_path = "main/hw1_intro_knn/code/knn.py"
    local_file_path = "knn.py"
    inst.download_file(repository, remote_file_path, local_file_path)
