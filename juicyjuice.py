import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

np.set_printoptions(suppress=True)      # Turn off scientific notation format for data output

# Concentration Data
concentrations = np.array([ 1.49,
                    3.05,
                    2.53,
                    2.37,
                    3.49,
                    2.62,
                    2.8,
                    3.69,
                    3.04,
                    1.62,
                    2.11,
                    0.05,
                    3.31,
                    3.51,
                    2.66,
                    4.05,
                    1.36,
                    1.96,
                    1.12,
                    1.76,
                    1.62,
                    2.06,
                    1.17,
                    2.14,
                    0.46,
                    -0.49,
                    1.01,
                    1.66,
                    1.85,
                    2.3,
                    3.59,
                    1.56,
                    1.82,
                    1.34,
                    1.97,
                    2.46,
                    3.08,
                    2.87,
                    4.27,
                    2.52,
                    1.09,
                    0.33,
                    1.88,
                    2.52,
                    2.96,
                    1.35,
                    2.94,
                    2.6,
                    2.01,
                    1.58,
                    1.77,
                    3.25,
                    0.82,
                    3.65,
                    2.34,
                    1.67,
                    1.99,
                    0.7,
                    2.12,
                    2.36,
                    2.33,
                    1.46,
                    3.18,
                    2.92,
                    6,
                    8 ])
years = np.array([ 2019,
            2022,
            2020,
            2021,
            2019,
            2019,
            2023,
            2023,
            2020,
            2022,
            2021,
            2019,
            2023,
            2023,
            2019,
            2023,
            2023,
            2019,
            2019,
            2020,
            2019,
            2023,
            2019,
            2023,
            2021,
            2019,
            2023,
            2022,
            2021,
            2020,
            2021,
            2020,
            2020,
            2019,
            2019,
            2023,
            2019,
            2019,
            2022,
            2022,
            2021,
            2019,
            2021,
            2021,
            2023,
            2022,
            2021,
            2022,
            2021,
            2019,
            2022,
            2022,
            2022,
            2022,
            2022,
            2021,
            2021,
            2020,
            2022,
            2021,
            2023,
            2023,
            2019,
            2021,
            2023,
            2023 ])

# Generate histogram of concentrations
plt.hist(concentrations, bins=20, edgecolor='k', alpha=0.7)
plt.xlabel('Arsenic Concentration (ppb)')
plt.ylabel('Count')
plt.title('Arsenic Concentrations in Apple Juice')
plt.grid(True)
plt.show()

sorted_data = {
    2019: [ 1.49,
            3.05,
            2.53,
            2.37,
            3.49,
            2.62,
            2.8,
            3.69,
            3.04,
            1.62,
            2.11,
            0.05,
            3.31,
            3.51,
            2.66,
            4.05,
            1.36 ],
    2020: [ 1.96,
            1.12,
            1.76,
            1.62,
            2.06,
            1.17,
            2.14 ],
    2021: [ 0.46,
            -0.49,
            1.01,
            1.66,
            1.85,
            2.3,
            3.59,
            1.56,
            1.82,
            1.34,
            1.97,
            2.46,
            3.08,
            2.87 ],
    2022: [ 4.27,
            2.52,
            1.09,
            0.33,
            1.88,
            2.52,
            2.96,
            1.35,
            2.94,
            2.6,
            2.01,
            1.58,
            1.77 ],
    2023: [ 3.25,
            0.82,
            3.65,
            2.34,
            1.67,
            1.99,
            0.7,
            2.12,
            2.36,
            2.33,
            1.46,
            3.18,
            2.92,
            6,
            8 ]
}

confidence_level = 0.95

print('mean: ', np.mean(concentrations), ' - std: ', np.std(concentrations, ddof=1))

for year, data in sorted_data.items():
    n = len(data)
    mean = np.mean(data)
    standard_dev = np.std(data, ddof=1)
    t_critical = stats.t.ppf(1 - (1 - confidence_level) / 2, df=(n - 1))
    m_o_e = t_critical * (standard_dev / np.sqrt(n))    # Margin of Error
    confidence_interval = (mean - m_o_e, mean + m_o_e)

    print(f"Year {year} - Confidence Interval: {confidence_interval} ........... Mean: {mean} ........... Std: {standard_dev} ............ n: {n}")



