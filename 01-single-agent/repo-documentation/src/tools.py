import os
import ast
from typing import List, Dict
from datetime import datetime
from langchain.tools import tool

from src.config import EXCLUDE_DIRS

@tool
def list_tree(path: str, depth: int = 3) -> List[str]:
    """List all the files and directories in a path.

    Args:
        path (str): Path of the directory to list
        depth (int): How much it is going into subdirectories

    Returns:
        List[str]: Every path with every directory and file
    """    
    elements_in_path = []
    for root, dirs, files in os.walk(path, topdown=True):

        if depth is not None and root.count(os.sep) - path.count(os.sep) >= depth:
            dirs[:] = [] 

        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in files:
            elements_in_path.append(os.path.join(root, name))
        for name in dirs:
            elements_in_path.append(os.path.join(root, name))

    return elements_in_path

@tool
def read_file(path: str, max_lines: int = 100) -> List[str]:
    """Reads lines inside a file.

    Args:
        path (str): Path of the file to read
        max_lines (int, optional): Maximum number of lines to read. Defaults to 100.

    Returns:
        List[str]: The lines inside the file
    """    
    file_list = []
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i > max_lines:
                break
            file_list.append(line)

    return file_list

@tool
def find_undocumented(path:str, depth: int = 2) -> Dict[str, List[Dict[str, str]]]:
    """Uses the function "list_tree" to find all documents in path and cath all the
    docstrings in every function.

    Args:
        path (str): Path of the directory to search the docstrings
        depth (int): How much it is going into subdirectories

    Returns:
        Dict[str:List[Dict[str:str]]]: All the information of both documented 
                                        and undocumented funtions
    """    
    undocumented = []
    documented = []

    all_files = list_tree.invoke({"path": path, "depth": depth})
    py_files = [f for f in all_files if f.endswith(".py")]

    for file in py_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

            tree = ast.parse(content, filename=file)
            functions = [f for f in ast.walk(tree) if isinstance(f, ast.FunctionDef)] 

            for f in functions:
                doc = ast.get_docstring(f)

                if doc is None:
                    undocumented.append({
                        "file": file,
                        "name": f.name,
                        "line": str(f.lineno),
                        "type": "function"
                    })
                else:
                    documented.append({
                        "file": file,
                        "name": f.name,
                        "line": str(f.lineno),
                        "type": "function"
                    })

        except SyntaxError as e:
            print(f"The file thrown an error: \n{e}")

    return {"undocumented": undocumented, "documented": documented}

@tool
def write_proposal(path: str, content: str, index: int = 1):
    """Write in a file all the proposals.

    Args:
        path (str): Path of the directory for the proposals to be saved
        content (str): Content of the proposal
        index (int, optional): If necessary, the function can create different files with different indexes. 
                                Defaults to 1.
    """    
    with open(f"{path}/changes_{index}.md", 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now()}\n\n{content}\n\”{'-'*50}")