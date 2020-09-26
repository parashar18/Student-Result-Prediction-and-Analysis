import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd


def ek_func(DF_STU):		
	table =	html.Div(children=[
		html.H4('Your Data'),
		dt.DataTable(
			rows=DF_STU.to_dict('records'),
			columns=sorted(DF_STU.columns),
			row_selectable=True,
			filterable=True,
			sortable=True,
			selected_row_indices=[],
			id='datatable-simple'
		),
		html.Div(id='selected-indexes')
	])
	
	return table