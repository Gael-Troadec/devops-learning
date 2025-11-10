import subprocess

# Fonction pour compter les admins
def count_admins():
    result = subprocess.run(['grep', 'admin', 'employees.csv'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    return len(lines)

# Fonction pour extraire les salaires des admins
def get_admin_salaries():
    result = subprocess.run(['grep', 'admin', 'employees.csv'], capture_output=True, text=True)
    salaries = []
    for line in result.stdout.strip().split('\n'):
        parts = line.split(':')
        salaries.append(int(parts[2]))
    return salaries

def employees_above_salary(min_salary):
    cmd = f"awk -F: '$3 > {min_salary} {{print $1, $3}}' employees.csv"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = [line for line in result.stdout.strip().split('\n') if line]
    return lines 

print(f"Nombre d'admins : {count_admins()}")
print(f"Salaires des admins : {get_admin_salaries()}")
print(f"Salaire moyen admin : {sum(get_admin_salaries()) / len(get_admin_salaries())}")
print(f"Employes gagnant > 6000 : {employees_above_salary(6000)}")
