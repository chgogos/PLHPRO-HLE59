import pandas as pd # Χρήση της βιβλιοθήκης pandas
import matplotlib.pyplot as plt # Χρήση της βιβλιοθήκης matplotlib.pyplot

def printMeteoData(file,city):
    '''Ανάγνωση μετεωρολογικών δεδομένων, για μια πόλη, και εκτύπωσή τους'''
    # Υποερώτημα α
    # Ανάγνωση με την pandas του φύλλου για την πόλη σε ένα dataframe
    city_df = pd.read_excel(file,sheet_name=city)
    # Εκτύπωση του dataframe με τα στοιχεία της πόλης
    print(city)
    print('-'*len(city))
    print(city_df)

def printMeteoStats(file,metric,city):
    '''Ανάγνωση μετεωρολογικών δεδομένων, για μια πόλη, και εκτύπωση βασικών στατιστικών στοιχείων μιας μετρικής'''
    # Υποερώτημα β
    # Ανάγνωση με την pandas του φύλλου για την πόλη σε ένα dataframe
    city_df = pd.read_excel(file,sheet_name=city)
    # Υπολογισμός και εκτύπωση μέσης τιμής και οριακών τιμών της μετρικής
    mean_value = city_df[metric].mean()
    min_value = city_df[metric].min()
    max_value = city_df[metric].max()
    print(city)
    print('-'*len(city))
    print(f'Μέση {metric}: {mean_value:.2f}')
    print(f'Ελάχιστη {metric}: {min_value}')
    print(f'Μέγιστη {metric}: {max_value}')

def plotMeteoData(file,x_axis,metric,*list_of_cities):
    '''Ανάγνωση μετεωρολογικών δεδομένων και εμφάνιση συγκριτικού γραφήματος μιας μετρικής'''
    # Υποερώτημα γ
    # Επανάληψη για όλες τις πόλεις
    for city in list_of_cities:
        # Ανάγνωση με την pandas του φύλλου για την πόλη σε ένα dataframe
        city_df = pd.read_excel(file,sheet_name=city)
        # Δημιουργία γραφήματος με τα δεδομένα της μετρικής για την πόλη
        plt.plot(city_df[x_axis],city_df[metric],label=city)
    # Προσθήκη τίτλου, ετικετών αξόνων και υπομνήματος
    plt.title(f'{metric} για {len(list_of_cities)} πόλεις')
    plt.xticks(fontsize=8,rotation=45,ha="right")
    plt.xlabel(x_axis)
    plt.ylabel(metric)
    plt.legend(fontsize=8)
    # Εμφάνιση του γραφήματος
    plt.show()

# Κυρίως πρόγραμμα

# Ορισμός του αρχείου με τα δεδομένα προς ανάγνωση
excel_file='weatherdata.xlsx'

# Υποερώτημα δ

# Εκτύπωση, με την printMeteoData, των στοιχείων για την Αθήνα
printMeteoData(excel_file,'Αθήνα')
# Εκτύπωση, με την  printMeteoStats, βασικών στατιστικών τιμών θερμοκρασίας
# για τη Θεσσαλονίκη
printMeteoStats(excel_file,'Θερμοκρασία','Θεσσαλονίκη')
# Δημιουργία συγκριτικού διαγράμματος για την υγρασία στις τρεις πόλεις
plotMeteoData(excel_file,'Μήνας','Υγρασία','Αθήνα','Θεσσαλονίκη','Πάτρα')
