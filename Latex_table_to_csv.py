import re
import csv

def latex_table_to_csv(latex_code, csv_filename):
    # Extract the table body
    table_body = re.search(r'\\begin\{tabular\}\{.*?\}(.*?)\\end\{tabular\}', latex_code, re.S).group(1)

    # Remove any LaTeX formatting commands
    table_body = re.sub(r'\\textbf\{(.*?)\}', r'\1', table_body)
    table_body = re.sub(r'\\midrule', '', table_body)

    # Split rows and columns
    rows = table_body.strip().split('\\\\')

    # Extract header row
    header = rows[0].strip().split('&')
    header = [cell.strip() for cell in header]

    # Extract data rows
    data_rows = []
    for row in rows[1:]:
        if row.strip():
            cells = row.strip().split('&')
            cells = [cell.strip() for cell in cells]
            data_rows.append(cells)

    # Write to CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data_rows)

# LaTeX table string
latex_code = r"""
\begin{table*}[t]
\centering
\setlength{\tabcolsep}{1mm}{
\small
\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Dataset} & \textbf{LOF} & \textbf{Iforest} & \textbf{AutoEncoders} & \textbf{DAGMM} & \textbf{Elliptic Envelope} & \textbf{DevNet} & \textbf{GAN} & \textbf{MGBTAI} & \textbf{d-BTAI} & \textbf{NN}\\
\hline
ALOI & 0.63 & 0.51 & 0.51 & 0.51 & 0.49 & 0.49 & 0.52 & 0.52 & 0.53 & \textbf{0.68}\\
annthyroid & 0.63 & 0.66 & 0.55 & 0.62 & 0.73 & 0.54 & 0.51 & 0.5 & 0.6 & \textbf{0.99}\\
backdoor & 0.68 & 0.52 & 0.53 & 0.89 & 0.88 & 0.91 & 0.89 & 0.49 & 0.76 & \textbf{0.99}\\
breastw & 0.57 & 0.7 & 0.63 & 0.64 & 0.66 & 0.95 & 0.41 & 0.65 & 0.91 & \textbf{0.99}\\
campaign & 0.48 & 0.63 & 0.55 & 0.59 & 0.62 & 0.72 & 0.55 & 0.53 & 0.61 & \textbf{0.93}\\
cardio & 0.55 & 0.77 & 0.64 & 0.52 & 0.68 & 0.85 & 0.4 & 0.64 & 0.72 & \textbf{0.99}\\
Cardiotocography & 0.53 & 0.59 & 0.55 & 0.54 & 0.57 & 0.67 & 0.5 & 0.59 & 0.61 & \textbf{0.93}\\
celeba & 0.47 & 0.63 & 0.5 & 0.6 & 0.64 & 0.9 & 0.52 & 0.75 & 0.55 & \textbf{0.98}\\
cover & 0.56 & 0.73 & 0.91 & 0.57 & 0.52 & 0.94 & 0.5 & 0.5 & 0.68 & \textbf{0.99}\\
donors & 0.63 & 0.54 & 0.6 & 0.9 & 0.62 & 0.96 & 0.47 & 0.5 & 0.63 & \textbf{1}\\
fault & 0.5 & 0.54 & \textbf{0.68} & 0.5 & 0.48 & 0.5 & 0.53 & 0.51 & 0.63 & 0.61\\
fraud & 0.51 & 0.88 & 0.89 & 0.77 & 0.88 & 0.91 & NA & 0.75 & 0.78 & \textbf{0.99}\\
glass & 0.68 & 0.6 & 0.56 & 0.5 & 0.61 & 0.5 & 0.52 & 0.53 & \textbf{0.89} & 0.85\\
Hepatitis & 0.53 & 0.51 & 0.49 & 0.53 & 0.59 & 0.53 & 0.51 & 0.44 & 0.48 & \textbf{0.66}\\
http & 0.47 & 0.94 & 0.95 & 0.95 & 0.95 & 0.95 & NA & 0.95 & 0.94 & \textbf{0.99}\\
InternetAds & 0.6 & 0.68 & 0.61 & 0.5 & 0.66 & 0.54 & 0.47 & 0.62 & 0.63 & \textbf{0.79}\\
Ionosphere & 0.63 & 0.67 & 0.53 & 0.57 & 0.62 & 0.57 & 0.55 & 0.5 & 0.87 & \textbf{0.90}\\
landsat & 0.53 & 0.48 & 0.5 & 0.49 & 0.45 & 0.51 & 0.55 & 0.44 & 0.56 & \textbf{0.85}\\
letter & 0.75 & 0.52 & 0.49 & 0.49 & 0.6 & 0.51 & 0.5 & 0.54 & 0.72 & \textbf{0.84}\\
Lymphography & 0.88 & 0.97 & 0.62 & 0.53 & 0.89 & 0.61 & 0.62 & \textbf{0.97} & 0.88 & 0.88\\
magic.gamma & 0.56 & 0.61 & 0.54 & 0.55 & 0.62 & 0.74 & 0.59 & 0.59 & 0.65 & \textbf{0.89}\\
mammography & 0.64 & 0.77 & 0.58 & 0.78 & 0.52 & 0.86 & 0.47 & 0.5 & 0.8 & \textbf{0.96}\\
mnist & 0.58 & 0.67 & 0.56 & 0.54 & 0.54 & 0.82 & 0.5 & 0.46 & 0.71 & \textbf{0.95}\\
musk & 0.47 & 0.95 & 0.72 & 0.96 & 0.96 & 0.96 & 0.5 & 0.85 & 0.82 & \textbf{1}\\
optdigits & 0.58 & 0.55 & 0.52 & 0.53 & 0.45 & 0.96 & 0.51 & 0.88 & 0.42 & \textbf{1}\\
PageBlocks & 0.67 & 0.72 & 0.61 & 0.6 & 0.78 & 0.55 & 0.62 & 0.53 & 0.55 & \textbf{0.92}\\
pendigits & 0.53 & 0.89 & 0.74 & 0.46 & 0.59 & 0.95 & 0.58 & 0.41 & 0.67 & \textbf{0.99}\\
Pima & 0.49 & 0.57 & 0.5 & 0.52 & 0.54 & 0.64 & 0.46 & 0.49 & 0.57 & \textbf{0.70}\\
satellite & 0.54 & 0.66 & 0.52 & 0.6 & 0.64 & 0.61 & 0.5 & 0.65 & 0.68 & \textbf{0.92}\\
satimage-2 & 0.59 & 0.94 & 0.46 & 0.78 & 0.95 & 0.94 & 0.5 & 0.92 & 0.83 & \textbf{1}\\
shuttle & 0.43 & 0.7 & 0.8 & 0.83 & 0.66 & 0.95 & 0.5 & 0.5 & 0.9 & \textbf{0.99}\\
skin & 0.51 & 0.45 & 0.46 & 0.61 & 0.53 & 0.96 & 0.47 & 0.56 & 0.53 & \textbf{0.99}\\
smtp & 0.8 & 0.82 & 0.8 & 0.88 & 0.83 & 0.8 & 0.5 & 0.64 & 0.81 & \textbf{0.97}\\
SpamBase & 0.48 & 0.5 & 0.5 & 0.55 & 0.48 & 0.68 & 0.43 & 0.57 & 0.58 & \textbf{0.95}\\
speech & 0.52 & 0.51 & 0.54 & 0.47 & 0.51 & 0.84 & 0.51 & 0.49 & 0.48 & \textbf{0.96}\\
Stamps & 0.53 & 0.61 & 0.53 & 0.46 & 0.51 & 0.53 & 0.72 & 0.51 & \textbf{0.63} & 0.62\\
thyroid & 0.65 & 0.93 & 0.76 & 0.81 & 0.94 & 0.82 & 0.81 & 0.6 & 0.84 & \textbf{0.99}\\
vertebral & 0.46 & 0.44 & 0.44 & 0.48 & 0.44 & 0.49 & 0.31 & 0.49 & 0.39 & \textbf{0.62}\\
vowels & 0.84 & 0.6 & 0.62 & 0.46 & 0.52 & 0.76 & 0.49 & 0.58 & 0.79 & \textbf{0.99}\\
Waveform & 0.61 & 0.56 & 0.64 & 0.61 & 0.53 & 0.57 & 0.82 & 0.5 & 0.64 & \textbf{0.95}\\
WBC & 0.55 & 0.95 & 0.91 & 0.86 & 0.96 & 0.95 & 0.52 & 0.97 & 0.9 & \textbf{0.99}\\
WDBC & 0.96 & 0.95 & 0.96 & 0.91 & 0.91 & 0.96 & 0.46 & 0.95 & 0.94 & \textbf{1}\\
Wilt & 0.55 & 0.44 & 0.5 & 0.54 & 0.55 & 0.45 & 0.5 & 0.48 & 0.48 & \textbf{0.99}\\
wine & 0.99 & 0.59 & 0.82 & 0.66 & 0.67 & 0.95 & 0.81 & 0.96 & 0.88 & \textbf{0.99}\\
WPBC & 0.46 & 0.46 & 0.5 & 0.48 & 0.48 & 0.49 & 0.49 & 0.47 & \textbf{0.51} & 0.47\\
yeast & 0.48 & 0.49 & 0.5 & 0.5 & 0.48 & 0.5 & 0.53 & 0.49 & 0.47 & \textbf{0.66}\\
CIFAR10 & 0.59 & 0.6 & 0.52 & 0.5 & 0.59 & 0.68 & 0.64 & 0.49 & 0.64 & \textbf{0.87}\\
FashionMNIST & 0.6 & 0.68 & 0.58 & 0.56 & 0.64 & 0.81 & 0.67 & 0.51 & 0.76 & \textbf{0.96}\\
MNIST-C & 0.59 & 0.53 & 0.49 & 0.53 & 0.53 & 0.94 & 0.54 & 0.5 & 0.71 & \textbf{0.99}\\
MVTec-AD & 0.7 & 0.75 & 0.59 & 0.56 & 0.39 & 0.51 & 0.73 & 0.61 & 0.92 & \textbf{0.96}\\
SVHN & 0.56 & 0.51 & 0.49 & 0.5 & 0.55 & 0.94 & 0.58 & 0.51 & 0.73 & \textbf{0.92}\\
Agnews & 0.56 & 0.51 & 0.5 & 0.51 & 0.52 & 0.51 & 0.56 & 0.5 & 0.55 & \textbf{0.96}\\
Amazon & 0.51 & 0.51 & 0.5 & 0.5 & 0.51 & 0.51 & 0.51 & 0.5 & 0.5 & \textbf{0.89}\\
Imdb & 0.49 & 0.48 & 0.5 & 0.5 & 0.48 & 0.52 & 0.5 & 0.48 & 0.5 & \textbf{0.92}\\
Yelp & 0.55 & 0.55 & 0.48 & 0.51 & 0.52 & 0.51 & 0.49 & 0.5 & 0.56 & \textbf{0.95}\\
20newsgroups & 0.64 & 0.53 & 0.51 & 0.52 & 0.55 & 0.5 & 0.49 & 0.5 & 0.47 & \textbf{0.93}\\
BATADAL\_04 & 0.65 & 0.52 & 0.54 & 0.64 & \textbf{0.71} & 0.5 & 0.55 & 0.52 & 0.68 & 0.57\\
SWaT 1 & 0.5 & 0.57 & 0.53 & \textbf{0.76} & 0.56 & 0.57 & 0.5 & 0.57 & 0.74 & 0.54\\
SWaT 2 & 0.51 & 0.54 & 0.55 & 0.57 & 0.59 & 0.58 & 0.5 & 0.54 & \textbf{0.61} & 0.56\\
SWaT 3 & 0.51 & 0.48 & 0.64 & 0.79 & 0.57 & 0.66 & 0.5 & 0.48 & 0.68 & \textbf{0.81}\\
SWaT 4 & 0.5 & 0.47 & 0.43 & \textbf{0.61} & 0.47 & 0.9 & 0.5 & 0.47 & 0.31 & 0.07\\
SWaT 5 & 0.49 & 0.6 & 0.63 & 0.65 & 0.71 & 0.7 & 0.5 & 0.6 & \textbf{0.75} & 0.64\\
SWaT 6 & 0.51 & 0.7 & 0.78 & 0.68 & 0.68 & 0.6 & 0.5 & 0.7 & 0.74 & \textbf{0.82}\\
ecoli & 0.85 & 0.84 & 0.83 & 0.85 & 0.85 & 0.57 & 0.5 & 0.82 & 0.71 & \textbf{0.99}\\
cmc & 0.48 & 0.44 & 0.59 & 0.48 & 0.51 & 0.45 & 0.69 & 0.46 & 0.57 & \textbf{0.97}\\
lympho h & 0.88 & \textbf{0.95} & 0.62 & 0.45 & 0.78 & 0.53 & 0.5 & 0.44 & 0.83 & 0.87\\
wbc h & 0.8 & 0.82 & 0.71 & 0.75 & 0.8 & 0.96 & 0.49 & 0.75 & 0.86 & \textbf{0.99}\\
\hline
\end{tabular}
}
\caption{AUC-ROC values of the 10 algorithms on the 67 multivariate datasets. The highest value(s) is marked in bold.}
\label{table:9}
\end{table*}

"""

# Convert the LaTeX table to CSV
latex_table_to_csv(latex_code, 'multi_output_4.csv')
