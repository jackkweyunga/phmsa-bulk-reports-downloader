<samp>

### USAGE

- Place csv files in the `sources` folder in the format:
    ```
    sources
    ├───csv1.csv
    ├───csv2.csv
    ├───csv3.csv
    └───csv4.csv
    ```
- Run `python main.py`
- The downloaded files will be in the `output`

### SCOPE

- The csv files must contain an index column with the link in the first column of format:
    ```
    "<A HREF = https://portal.phmsa.dot.gov/PDFGenerator/getPublicReport/OHMIR_5800-1?INCIDENTID=720164 target=""_blank"">I-2017090112</A> extract link
    ```

- Downloaded files are pdfs
  </samp>