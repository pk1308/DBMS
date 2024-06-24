import os

from shared.app_log import logger
from shared.functions import (create_ipynb,deploy_mkdocs,
                              get_git_status_files, git_add_and_commit,
                              update_my_docs)

if __name__ == "__main__":

    repo_path = os.getcwd()
    update_my_docs()
    logger.info("successful update")
    deploy_mkdocs()
    logger.info("deployed mk docs ")
    commit_message = input("please enter the commit message : ")
    git_add_and_commit(commit_message)
