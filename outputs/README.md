# Output Format

All the emails in the `inputs/emails` folder will be parsed and the output (a .csv file) will be saved in the `outputs/` folder.

>**NOTE**: The `outputs/` folder will be created if it does not exist. You can change the path of the output folder by providing `-o` or `--output_dir` argument.

## Format of the output csv file
```
emails
sample1@gmail.com
sample2.@gmail.com
...
samplen.@gmail.com
```

>**NOTE**: The default output file name is `emails.csv`. You can change the name of the output file by providing `--output_filename` argument.