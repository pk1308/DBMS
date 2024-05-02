echo [$(date)]: "START"
export _VERSION_=3.11
read _project_name 
conda deacivate 
echo [$(date)]: "creating environment with python ${_VERSION_}"
conda create -n ${_project_name} python=${_VERSION_} -y
echo [$(date)]: "activate environment"
conda activate ${_project_name}
echo [$(date)]: "install requirements"
pip3 install -r requirements.txt
echo [$(date)]: "END"

# to remove everything -
# rm -rf env/ .gitignore conda.yaml README.md .git/