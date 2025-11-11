#!/usr/bin/env python3
import logging
import os
import subprocess
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_analyzer.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Fonction pour compter les admins
def count_admins(csv_file):
    try:
        logger.info(f"Starting count_admins on file: {csv_file}")

        # Verifier le fichier existe
        if not os.path.exists(csv_file):
            logger.error(f"CSV file does not exist: {csv_file}")
            sys.exit(1)

        logger.info(f"File found, starting parsing")
        result = subprocess.run(['grep', 'admin', csv_file], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')
        admin_count = len([line for line in lines if line])
        logger.info(f"Admin count completed successfully: {admin_count} admins found")
        return admin_count
    
    except Exception as e:
        logger.error(f"Error counting admins: {e}")
        sys.exit(1)


# Fonction pour extraire les salaires des admins
def extract_admin_salaries(csv_file):
    try:
        logger.info(f"Starting extract_admin_salaries on file: {csv_file}")

        if not os.path.exists(csv_file):
            logger.error(f"CSV file does not exist: {csv_file}")
            sys.exit(1)

        logger.info(f"File found, parsing admin salaries")
        result = subprocess.run(['grep', 'admin', csv_file], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')

        admin_salaries = []
        for line in lines:
            if line:
                parts = line.split(',')
                if len(parts) >= 3:
                    try:
                        salary = float(parts[2])
                        admin_salaries.append(salary)
                    except ValueError:
                        logger.warning(f"Could not parse salary from line: {line}")

        logger.info(f"Extracted salaries completed successfully: {len(admin_salaries)} salaries found")
        return admin_salaries
    
    except Exception as e:
        logger.error(f"Error extracting admin salaries: {e}")
        sys.exit(1)

def employees_above_salary(csv_file, min_salary):
    try:
        logger.info(f"Starting to find employees above {min_salary}")

        if not os.path.exists(csv_file):
            logger.error(f"CSV file does not exist: {csv_file}")
            sys.exit(1)


        logger.info(f"File found, parsing data")
        cmd = f"awk -F, '$3 > {min_salary} {{print $1, $3}}' {csv_file}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        lines = [line for line in result.stdout.strip().split('\n') if line]

        employees_found = len(lines)

        logger.info(f"Search completed successfully: {employees_found} employees above {min_salary} found")
        return employees_found

    except Exception as e:
        logger.error(f"Error finding employees above {min_salary}: {e}")
        sys.exit(1) 

print(f"Nombre d'admins : {count_admins('employees.csv')}")
print(f"Salaires des admins : {extract_admin_salaries('employees.csv')}")
print(f"Salaire moyen admin : {sum(extract_admin_salaries('employees.csv')) / len(extract_admin_salaries('employees.csv'))}")
print(f"Employes gagnant > 6000 : {employees_above_salary('employees.csv', 6000)}")
