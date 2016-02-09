# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 16:44:33 2016

@author: thomas.douenne
"""

from __future__ import division

import os
import pandas as pd
import pkg_resources

assets_directory = os.path.join(
    pkg_resources.get_distribution('openfisca_france_indirect_taxation').location
    )

nomenclature_by_postes = pd.DataFrame.from_csv(os.path.join(assets_directory,
            'openfisca_france_indirect_taxation', 'assets', 'legislation',
            'nomenclature_coicop_source_by_postes.csv'), sep = ';', header = -1)
nomenclature_by_postes.reset_index(inplace = True)
nomenclature_by_postes.rename(columns = {0: 'code_coicop', 1: 'label_poste'}, inplace = True)
nomenclature_by_postes = nomenclature_by_postes.ix[2:].copy()
niveau_nomenclature = ['divisions', 'groupes', 'classes', 'sous_classes', 'postes']
for niveau in niveau_nomenclature:
    nomenclature_by_postes[niveau] = 0

nomenclature_by_postes['divisions'] = nomenclature_by_postes['code_coicop'].str[1:3].copy()
nomenclature_by_postes['groupes'] = nomenclature_by_postes['code_coicop'].str[4:5].copy()
nomenclature_by_postes['classes'] = nomenclature_by_postes['code_coicop'].str[6:7].copy()
nomenclature_by_postes['sous_classes'] = nomenclature_by_postes['code_coicop'].str[8:9].copy()
nomenclature_by_postes['postes'] = nomenclature_by_postes['code_coicop'].str[10:11].copy()
for niveau in niveau_nomenclature:
    nomenclature_by_postes[niveau] = nomenclature_by_postes[niveau].astype(int)

nomenclature_by_postes['code_coicop'] = nomenclature_by_postes['code_coicop'].str[1:].copy()

nomenclature_by_sous_classes = pd.DataFrame.from_csv(os.path.join(assets_directory,
            'openfisca_france_indirect_taxation', 'assets', 'legislation',
            'nomenclature_coicop_source_by_sous_classes.csv'), sep = ';', header = -1)
nomenclature_by_sous_classes.reset_index(inplace = True)
nomenclature_by_sous_classes.rename(columns = {0: 'code_coicop', 1: 'label_sous_classe'}, inplace = True)
nomenclature_by_sous_classes = nomenclature_by_sous_classes.ix[2:].copy()
niveau_nomenclature = ['divisions', 'groupes', 'classes', 'sous_classes']
for niveau in niveau_nomenclature:
    nomenclature_by_sous_classes[niveau] = 0

# Problème dû au fichier Excel, nous devons changer le contenu d'une case:
nomenclature_by_sous_classes.loc[nomenclature_by_sous_classes['code_coicop'] == '01.1.4.4', 'code_coicop'] = "'01.1.4.4"

nomenclature_by_sous_classes['divisions'] = nomenclature_by_sous_classes['code_coicop'].str[1:3].copy()
nomenclature_by_sous_classes['groupes'] = nomenclature_by_sous_classes['code_coicop'].str[4:5].copy()
nomenclature_by_sous_classes['classes'] = nomenclature_by_sous_classes['code_coicop'].str[6:7].copy()
nomenclature_by_sous_classes['sous_classes'] = nomenclature_by_sous_classes['code_coicop'].str[8:9].copy()
for niveau in niveau_nomenclature:
    nomenclature_by_sous_classes[niveau] = nomenclature_by_sous_classes[niveau].astype(int)
del nomenclature_by_sous_classes['code_coicop']


nomenclature_by_classes = pd.DataFrame.from_csv(os.path.join(assets_directory,
            'openfisca_france_indirect_taxation', 'assets', 'legislation',
            'nomenclature_coicop_source_by_classes.csv'), sep = ';', header = -1)
nomenclature_by_classes.reset_index(inplace = True)
nomenclature_by_classes.rename(columns = {0: 'code_coicop', 1: 'label_classe'}, inplace = True)
nomenclature_by_classes = nomenclature_by_classes.ix[2:].copy()
niveau_nomenclature = ['divisions', 'groupes', 'classes']
for niveau in niveau_nomenclature:
    nomenclature_by_classes[niveau] = 0

nomenclature_by_classes['divisions'] = nomenclature_by_classes['code_coicop'].str[1:3].copy()
nomenclature_by_classes['groupes'] = nomenclature_by_classes['code_coicop'].str[4:5].copy()
nomenclature_by_classes['classes'] = nomenclature_by_classes['code_coicop'].str[6:7].copy()
for niveau in niveau_nomenclature:
    nomenclature_by_classes[niveau] = nomenclature_by_classes[niveau].astype(int)
del nomenclature_by_classes['code_coicop']

nomenclature_by_groupes = pd.DataFrame.from_csv(os.path.join(assets_directory,
            'openfisca_france_indirect_taxation', 'assets', 'legislation',
            'nomenclature_coicop_source_by_groupes.csv'), sep = ';', header = -1)
nomenclature_by_groupes.reset_index(inplace = True)
nomenclature_by_groupes.rename(columns = {0: 'code_coicop', 1: 'label_groupe'}, inplace = True)
nomenclature_by_groupes = nomenclature_by_groupes.ix[2:].copy()
niveau_nomenclature = ['divisions', 'groupes']
for niveau in niveau_nomenclature:
    nomenclature_by_groupes[niveau] = 0

nomenclature_by_groupes['divisions'] = nomenclature_by_groupes['code_coicop'].str[1:3].copy()
nomenclature_by_groupes['groupes'] = nomenclature_by_groupes['code_coicop'].str[4:5].copy()
for niveau in niveau_nomenclature:
    nomenclature_by_groupes[niveau] = nomenclature_by_groupes[niveau].astype(int)
del nomenclature_by_groupes['code_coicop']

nomenclature_by_divisions = pd.DataFrame.from_csv(os.path.join(assets_directory,
            'openfisca_france_indirect_taxation', 'assets', 'legislation',
            'nomenclature_coicop_source_by_divisions.csv'), sep = ';', header = -1)
nomenclature_by_divisions.reset_index(inplace = True)
nomenclature_by_divisions.rename(columns = {0: 'code_coicop', 1: 'label_division'}, inplace = True)
nomenclature_by_divisions = nomenclature_by_divisions.ix[2:].copy()

nomenclature_by_divisions['divisions'] = 0
nomenclature_by_divisions['divisions'] = nomenclature_by_divisions['code_coicop'].str[1:3].copy()
nomenclature_by_divisions['divisions'] = nomenclature_by_divisions['divisions'].astype(int)
del nomenclature_by_divisions['code_coicop']

nomenclature_divisions_groupes = pd.merge(nomenclature_by_divisions, nomenclature_by_groupes, on = 'divisions')
del nomenclature_by_divisions, nomenclature_by_groupes
nomenclature_divisions_classes = \
    pd.merge(nomenclature_divisions_groupes, nomenclature_by_classes, on = ['divisions', 'groupes'])
del nomenclature_by_classes, nomenclature_divisions_groupes
nomenclature_divisions_sous_classes = \
    pd.merge(nomenclature_divisions_classes, nomenclature_by_sous_classes, on = ['divisions', 'groupes', 'classes'])
del nomenclature_by_sous_classes, nomenclature_divisions_classes
nomenclature_coicop = pd.merge(
    nomenclature_divisions_sous_classes, nomenclature_by_postes,
    on = ['divisions', 'groupes', 'classes', 'sous_classes'])
del nomenclature_by_postes, nomenclature_divisions_sous_classes

nomenclature_coicop = nomenclature_coicop[['code_coicop'] + ['label_division'] + ['label_groupe'] +
    ['label_classe'] + ['label_sous_classe'] + ['label_poste'] + ['divisions'] + ['groupes'] + ['classes'] +
    ['sous_classes'] + ['postes']].copy()

nomenclature_coicop.to_csv(os.path.join(assets_directory, 'openfisca_france_indirect_taxation', 'assets',
    'legislation', 'nomenclature_coicop.csv'), sep = ';')

# On fait correspondre à chaque bien sa catégorie fiscale
nomenclature_coicop['categorie_fiscale'] = 0
nomenclature_coicop.loc[nomenclature_coicop['divisions'] == 1, 'categorie_fiscale'] = 2 # see exceptions
nomenclature_coicop.loc[nomenclature_coicop['divisions'] == 3, 'categorie_fiscale'] = 3
nomenclature_coicop.loc[nomenclature_coicop['divisions'] == 5, 'categorie_fiscale'] = 3 # see exceptions...

parametres_fiscalite_file_path = os.path.join(
    assets_directory,
    'openfisca_france_indirect_taxation',
    'assets',
    'legislation',
    'coicop_to_categorie_fiscale.csv',
    )
parametres_fiscalite_data_frame = pd.read_csv(
    parametres_fiscalite_file_path, sep = ';', converters={'posteCOICOP': str}
    )
parametres_fiscalite_data_frame['posteCOICOP'] = parametres_fiscalite_data_frame['posteCOICOP'].astype(str)
parametres_fiscalite_data_frame['divisions'] = parametres_fiscalite_data_frame['posteCOICOP'].str[:2].copy().astype(int)
parametres_fiscalite_data_frame['groupes'] = parametres_fiscalite_data_frame['posteCOICOP'].str[2:3].copy().astype(int)
parametres_fiscalite_data_frame['classes'] = parametres_fiscalite_data_frame['posteCOICOP'].str[3:4].copy().astype(int)
parametres_fiscalite_data_frame['sous_classes'] = \
    parametres_fiscalite_data_frame['posteCOICOP'].str[4:5].copy()

check_coicop = parametres_fiscalite_data_frame.copy()
check_coicop = check_coicop.drop_duplicates(cols = ['posteCOICOP', 'categoriefiscale'])

check_coicop_class = check_coicop[check_coicop['sous_classes'] == ''].copy()
del check_coicop_class['sous_classes'], check_coicop_class['supplementaire'], check_coicop_class['posteCOICOP']

nomenclature_categ_fiscale = pd.merge(nomenclature_coicop, check_coicop_class, on = ['divisions', 'groupes', 'classes'])
nomenclature_categ_fiscale['year_start'] = nomenclature_categ_fiscale['annee']
nomenclature_categ_fiscale['year_stop'] = nomenclature_categ_fiscale['annee'].shift(-1)
nomenclature_categ_fiscale['year_stop'] = nomenclature_categ_fiscale['year_stop'].fillna(2014)
nomenclature_categ_fiscale['year_stop'] = nomenclature_categ_fiscale['year_stop'].astype(int)
nomenclature_categ_fiscale['year_stop'] = nomenclature_categ_fiscale['year_stop'] - 1
nomenclature_categ_fiscale.loc[nomenclature_categ_fiscale['year_stop'] == 1993, 'year_stop'] = 2014

check_coicop_sous_class = check_coicop[check_coicop['sous_classes'] != ''].copy()

# To do : on peut maintenant traiter les cas particuliers, et notamment les biens qui ont disparus dans le merge
# tabac, énergie,

nomenclature_categ_fiscale.loc[nomenclature_categ_fiscale['code_coicop'] == '01.1.5.2.2', 'categoriefiscale'] = 3
nomenclature_categ_fiscale.loc[nomenclature_categ_fiscale['code_coicop'] == '01.1.8.1.3', 'categoriefiscale'] = 3


