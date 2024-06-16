import os
import sys

from shared.app_log import logger
from shared.functions import (create_ipynb, create_md, deploy_mkdocs,
                              get_git_status_files, git_add_and_commit,
                              update_my_docs)

if __name__ == "__main__":

    repo_path = os.getcwd()
    print(sys.argv[1])
    logger.info("converting files to PDF to MD ")
    status = create_md(files_to_create=[sys.argv[1]])
    logger.info(f"converted files to pdf to md  status ; {status} ")

    commit_message = input("please enter the commit message : ")
    git_add_and_commit(commit_message)
