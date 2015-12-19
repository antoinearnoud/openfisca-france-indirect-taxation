# -*- coding: utf-8 -*-


from __future__ import division

import pandas

from openfisca_france_indirect_taxation.example.utils_example import create_survey_scenario, graph_builder_bar


if __name__ == '__main__':

    # Liste des coicop agrégées en 12 postes
    simulated_variables = ['coicop12_{}'.format(coicop12_index) for coicop12_index in range(1, 13)]
    for year in [2000, 2005, 2011]:
        # Constition d'une base de données agrégée par décile (= collapse en stata)
        survey_scenario = create_survey_scenario(year)
        simulation = survey_scenario.new_simulation()
        pivot_table = pandas.DataFrame()
        for values in simulated_variables:
            pivot_table = pandas.concat([
                pivot_table,
                survey_scenario.compute_pivot_table(values = [values], columns = ['niveau_vie_decile'])
                ])
        df = pivot_table.T
        df['depenses_tot'] = 0
        df['depenses_tot'] = df[['coicop12_{}'.format(i) for i in range(1, 13)]].sum(axis = 1)

        for i in range(1, 13):
            df['part_coicop12_{}'.format(i)] = \
                df['coicop12_{}'.format(i)] / df['depenses_tot']

        graph_builder_bar(df[['part_coicop12_{}'.format(i) for i in range(1, 13)]])