'''
A collection of core components.

Alias: nwcc
'''

# GLOBAL MODULES
import os
import requests
import seaborn as sns
from pandas import DataFrame

# LOCAL MODULES
# CLASSES

# FUNCTIONS
def create_file_path(folder_path : str, file_name : str) -> str:

    '''Creates a file path.'''

    return os.path.join(folder_path, file_name) 
def create_numbered_file_path(folder_path : str, number : int, extension : str) -> str:

    r'''Creates a numbered file path. Example: ("C:\\", 1, "html") => "C:\\1.html"'''

    file_name : str = f"{number}.{extension}"
    file_path : str = create_file_path(folder_path = folder_path, file_name = file_name)    

    return file_path
def create_numbered_file_paths(folder_path : str, range_start : int, range_end : int, extension : str) -> list[str]:

    '''Creates a collection of numbered file paths.'''

    file_paths : list[str] = []
    for i in range(range_start, range_end):
        file_path : str = create_numbered_file_path(folder_path = folder_path, number = i, extension = extension)
        file_paths.append(file_path)

    return file_paths

def remove_files(extensions : list[str], working_folder_path : str) -> None:

    '''Delete all the files of the provided extensions from the provided folder.'''    

    for file_name in os.listdir(path = working_folder_path):
        for extension in extensions:
            if file_name.endswith(extension):
                os.remove(os.path.join(working_folder_path, file_name))

def load_content(file_path : str) -> str:
    
    '''Reads the content of the provided text file and returns it as string.'''

    content = None
    with open(file_path, 'r') as file:
        content = file.read()

    return content
def load_contents(working_folder_path : str, extension : str) -> list[str]:

    '''Reads the contents of all the text files in the provided folder and returns them as a collection of strings.'''

    if not extension.startswith("."):
        extension = f".{extension}"

    file_paths : list[str] = []
    for file_name in os.listdir(path = working_folder_path):
        if file_name.endswith(extension):
            file_path : str = create_file_path(folder_path = working_folder_path, file_name = file_name)   
            file_paths.append(file_path)

    contents : list[str] = []
    for file_path in file_paths:
        content : str = load_content(file_path = file_path)
        contents.append(content)

    return contents

def save_content(content : str, file_path : str) -> None:    

    '''Writes the provided content to the provided file path.'''

    with open(file_path, 'w') as new_file:
        new_file.write(content)
def save_contents(contents : list[str], file_paths : list[str]) -> None: 

    '''Writes the provided contents to the provided file paths.'''

    for i in range(len(contents)):
        save_content(content = str(contents[i]), file_path = file_paths[i]) # without str() it returns 'bytes' (?)
def save_log(contents : list[str], working_folder_path : str, file_name : str) -> None:

    '''Writes the provided collection of strings as newline-separated lines into the provided file.'''

    file_path : str = create_file_path(folder_path = working_folder_path, file_name  = file_name)

    lines : list[str] = []
    for i in range(len(contents)):
        lines.append(contents[i])
        lines.append('\n')

    with open(file_path, 'w') as new_file:
        new_file.writelines(lines)

def get_page_content(page_url : str) -> str:

    '''Performs a GET request against the provided url and returns its content as string.'''

    page_response = requests.get(page_url)
    page_content = page_response.content

    return page_content
def get_page_contents(page_urls : list[str]) -> list[str]:

    '''Performs a GET request against the provided urls and returns their contents as a collection of strings.'''

    page_contents : list[str] = []
    for page_url in page_urls:
        page_content = get_page_content(page_url = page_url)
        page_contents.append(page_content)

    return page_contents

def decode_unicode_characters(string : str) -> str:
    
    r'''Example: "Antikt \u0026 Design" => "Antikt & Design"'''

    return string.encode('utf_8').decode('unicode_escape')

def show_box_plot(df : DataFrame, x_name : str) -> None:

    '''Shows a box plot.'''

    title = f"{x_name} ranges"
    df_plot = sns.boxplot(x = df[x_name]).set(title = title)
def show_bar_plot(df : DataFrame, x_name : str, y_name : str) -> None:

    '''Shows a bar plot.'''

    title = f"{y_name} by {x_name}"
    df_plot = df.plot(x = x_name, y = y_name, legend = True, kind = "bar", title = title)

def describe_dataframe(df : DataFrame, column_names : list[str]) -> DataFrame:
    
    '''Describes the provided dataframe according to the provided column names.'''

    describe_df = df[column_names].describe().apply(lambda s: s.apply(lambda x: format(x, 'g')))

    return describe_df
def remove_outliers(df : DataFrame, column_name : str) -> DataFrame:

    '''Removes all the values higher than "75%" metric from the provided dataframe's column.'''

    describe_df : DataFrame = df[column_name].describe()
    threshold : float = float(describe_df["75%"])

    condition = (df[column_name] <= threshold)   
    filtered_df : DataFrame = df[condition]

    return filtered_df

# MAIN
if __name__ == "__main__":
    pass