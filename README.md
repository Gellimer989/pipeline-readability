## Pipeline readability

- `data`: contains the csv and yml files used to create the dataset
    - `dataset`: contains the list of a repositories where find a pipeline, the parents of a commit, and the result dataset
    - `pipeline.zip`: contains all the yml files used to calculate the metrics
- `script`: contains the python scripts for calculate the metrics and get the data
    - `pipeline_script`: script to get the pipeline
    - `postprocessing`: scripts to calculate deltas of metrics between versions 
    - `readability_script `: scripts to calcultae all the maetrics and create the final dataset
