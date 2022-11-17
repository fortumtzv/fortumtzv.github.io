import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
df = pd.read_csv('internacional.csv')
df3 = pd.read_csv('GPA.csv')
df = df.dropna()
df.loc[df['Programa'].str.contains('AMC19'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('ARQ'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('ARQ07'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('ARQ11'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('ARQ19'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('BA 11'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('ADI17'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('LUB19'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('MDU21'),'Escuela']='Arquitectura, Arte y Diseño'
df.loc[df['Programa'].str.contains('CIS17'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('CIS19'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('DCS11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('DPP11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('BPS11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LPL04'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LPL07'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LPL11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('BL 11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LED06'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LED11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LED19'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LDP11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('BLF11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LDF09'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LDF11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('BE'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('BE 11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('BE11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LEC'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LEC07'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LEC11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LEC19'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LEP11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LEF09'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LEF11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LTP19'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('BIA07'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('BIA11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LRI'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LRI04'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LRI07'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LRI11'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('LRI19'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MAP17'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MAP20'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MDP21'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MEK20'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MGP09V'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MGP18V'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MPJ14'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MPE17'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('MPE20'),'Escuela']='Ciencias Sociales y Gobierno'
df.loc[df['Programa'].str.contains('COM17'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('DEH11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('DEH18'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('DEE15'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('EGE19V'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('ESC19'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('IMI'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('IMI11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BAA08'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BAA11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BAA17'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LAD07'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LAD11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LAD17'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LAD19'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LCC07'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LC 19'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BCD10'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BCD11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BCD17'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LCD'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LCD10'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LCD11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LCD17'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LEI19'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LLE11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LLE19'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LPE19'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BJM11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LMI07'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LMI11'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BAM13'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LPM12'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LTM19'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('LTS17'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('MPM09'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('MEE13V'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('MTO20V'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('MEH09'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('MEH09V'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('MHD19V'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('MTE13V'),'Escuela']='Humanidades y Educación'
df.loc[df['Programa'].str.contains('BIO17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('DBT11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('DBC17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('DCC16'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('DCI11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('DCI18'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('DNT16'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('EPY11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('EAE15'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ELS11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IBQ19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ICI19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ICT19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIT19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ING17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IA 08'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IA 11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BBM11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMD05'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMD11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMD19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BC 11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IC'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IC 07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IC 11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IC 19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IAB11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IAL19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BBS12'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IBN11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IAG19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BBE07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BBE11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BBE17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IBT'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IBT07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IBT11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IBT17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IBT19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IDM19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BSD11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IDS'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IDS10'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IDS11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IDS19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BAU11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IDA11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IE 19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IFI11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IFI19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BFE11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIA'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIA07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIA11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BDE16'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BDE17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IID12'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IID17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IID19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BME11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMT'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMT07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMT11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMT19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('INA19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BCN13'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BSI11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('INT09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('INT11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IRS19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ISC00'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ISC09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ISC11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BSR'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BSR11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ISD'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ISD08'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ISD11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BCT11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITC'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITC09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITC11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITC19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITI08'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITI11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITI17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BNT11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BNT17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITE08'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITE11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITM08'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITM11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITS08'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITS11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('ITD19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BEP11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BIE07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BIE11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIS'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIS03'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIS07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIS11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IIS19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IM 19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BMI11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMA00'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMA07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IMA11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BML07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BML11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IME07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IME11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IQ 19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BCI07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BCI11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IQA'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IQA07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IQA11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BCP11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IQP11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BCE07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('IQS00'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LTI08'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LTI11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LBC11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LBC17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LBC19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BCH11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LCQ09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LCQ11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('BIN11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LDI07'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LDI11'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LDI17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('LDI19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MER11V'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MTI12'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MTI12I'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MTI12V'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MTI21V'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MCY19'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MBC17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MBI09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MSE09E'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MIE09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MCP09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MSM09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MIT12'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MCC09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MCC16I'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MCI17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MEM16'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MIR09'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MIP13V'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MOI13'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MAC12'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MID09V'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MID21V'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('MNT16'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('TIE17'),'Escuela']='Ingeniería y Ciencias'
df.loc[df['Programa'].str.contains('DCA11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('DCF11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BBA06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BBA11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BBA16'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAE'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAE06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAE11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BFI06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BFI11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAF03'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAF06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAF11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAF19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAE16'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BFA11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('CPF03'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('CPF06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('CPF11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('CPF19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LDO19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LDE09'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LDE11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LDE19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LCS11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LAE19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LDN11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LIT19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BIL16'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LLN'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LLN05'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LLN11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BM 06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BM 11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LEM06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LEM11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LEM19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BMC13'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LMC'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LMC10'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LMC11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BGB19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BIB06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BIB11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LIN'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LIN06'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LIN11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LIN19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('BPO16'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LPO07'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('LPO11'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MA 09'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBM09'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBM20'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MGN10V'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MGN17V'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBA09'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBA09G'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBA15'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBA17G'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBA17I'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBA20'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MBD21'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MAF09'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MAF09V'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MAF15'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MAF20'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MAF20V'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MMT09'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('MIB05'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('NEG17'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('NEG19'),'Escuela']='Negocios'
df.loc[df['Programa'].str.contains('AEP07'),'Escuela']='No Aplica'
df.loc[df['Programa'].str.contains('INQ13'),'Escuela']='No Aplica'
df.loc[df['Programa'].str.contains('PBU07'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PBB07'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PBB12'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PBB14'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PTB07'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PTI14'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PBI07'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PBI14'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PHS12'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PTM10'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PTM11'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PTM14'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('PRT19D'),'Escuela']='Prepa Tec'
df.loc[df['Programa'].str.contains('IPU05'),'Escuela']='Internacionalización'
df.loc[df['Programa'].str.contains('RAP13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('REC13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('RGE13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('REG13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('REM13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('REO13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('REN13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('RPS13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('RUR13'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('LNB11'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('LNB19'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('LP 12'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('LPS12'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('LPS19'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('MC 05'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('MC 11'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('MC 19'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('MO 11'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('MO 19'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('SLD17'),'Escuela']='Salud'
df.loc[df['Programa'].str.contains('SLD19'),'Escuela']='Salud'
df = df.dropna()
df = df.replace('EUA', 'USA')
df = df.replace('ALE', 'DEU')
df = df.replace('ING', 'GBR')
df = df.replace('COR', 'KOR')
df = df.replace('SUI', 'CHE')
df = df.replace('HOL', 'NLD')
df = df.replace('SUE', 'SWE')
df = df.replace('JAP', 'JPN')
df = df.replace('DIN', 'DNK')
df = df.replace('CRO', 'HRV')
df = df.replace('TAI', 'TWN')
df = df.replace('POR', 'PRT')
df = df.replace('SIN', 'SGP')
df = df.replace('URU', 'URY')
df = df.replace('EAU', 'ARE')
df = df.replace('SER', 'SRB')
df = df.replace('EUA', 'USA')
df = df.replace('CHI', 'CZE')
df = df.replace('CRC', 'CRI')
df = df.replace('PRC', 'PRI')
df['Estatuslimpio'] = df['Estatus'].str[:1]
#Limpiar 'Estatus'
df = df.replace(['A', 'P'], 'Asignado')
df = df.replace(['E', 'I', 'C', 'T', 'R', 'N'], 'Rechazado')
df['Estatuslimpio'].value_counts()
#Limpiar 'Programas'
df['Programa'] = df['Programa'].str[:3]
#Limpiar 'OportunidadesSeleccionadas'
df['OportunidadesSeleccionadas'] = df['OportunidadesSeleccionadas'].str[3:17]
df['OportunidadesSeleccionadas'] = df['OportunidadesSeleccionadas'].map(lambda x: x.rstrip(',').lstrip(' '))
# Intercambio Internacional Tradicional y Study Abroad 
df.loc[df['OportunidadAsignada'].str.contains('INT'), 'Intercambio Internacional'] = 'INT'
df['Intercambio Internacional'].fillna('SA', inplace=True)
df.loc[(df['OportunidadAsignada'] == df['OportunidadesSeleccionadas']) & (df['Estatuslimpio'] == 'Asignado'), 'PrimeraOpcion'] = 'Si'
df['PrimeraOpcion'].fillna('No', inplace=True)
df = df.replace(['A', 'P'], 'Asignado')
df = df.replace(['E', 'I', 'C', 'T', 'R', 'N'], 'Rechazado')
df['Estatuslimpio'].value_counts()
df['PaisSeleccionado'] = df['OportunidadesSeleccionadas'].str[:3]
df['PaisAsignado'] = df['OportunidadAsignada'].str[:3]
df['Promedio'] = df.Promedio.apply(np.round)
GPA = []
for row in df['Promedio']:
    if row >=      97.0:    GPA.append('A+')
    elif 97 > row >= 93.0:    GPA.append('A')
    elif 93 > row >= 90.0:    GPA.append('A-')
    elif 90 > row >= 87.0:    GPA.append('B+')
    elif 87 > row >= 83.0:    GPA.append('B')
    elif 83 > row >= 80.0:    GPA.append('B-')
    elif 80 > row >= 77.0:    GPA.append('C+')
    elif 77 > row >= 73.0:    GPA.append('C')
    elif 73 > row >= 70.0:    GPA.append('C-')
    elif row > 70.0:        GPA.append('F')
    else:                   GPA.append('NA')
df['GPA']= GPA
df = df[df.Promedio >= 70]
df.sort_values(by=['Promedio'], ascending=False, inplace=True)
df1 = df
st.title('Dahsboard Base de Datos Internalización ITESM')
st.subheader('Este mapa representa el tipo de intercambio al que se han ido los alumnos de Tecnológico de Monterrey alrededor de los años y si fueron seleccionados en su primera elección de intercambio. Esta grafica permite que se diferencien entre el promedio total para ver cómo influye el promedio en el tipo de intercambio al que se van los estudiantes y en si fueron elegios en su primera elección. Tambein esta dividido por tipo de escuela')
Escuela = df1['Escuela'].unique().tolist()
esc = st.selectbox('Nombre de Escuela', Escuela,0)
df1 = df1[df1['Escuela'] == esc]
fig1 = px.parallel_categories(df1, 
                            dimensions= ['Promedio','Intercambio Internacional','PrimeraOpcion'],
                            color="Promedio", color_continuous_scale=px.colors.colorbrewer.RdYlGn,
                            labels={'Promedio':'Promedio', 'Escuela':'Escuela', 'Intercambio Internacional':'Tipo de Intercambio'},
                            )
fig1.update_layout(
    title={
        'text': "Mapa Aluvial de Tipo de Intercambio y Selección agrupada por Promedio",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig1, use_container_width=True)
st.table(df3)
col1, col2 = st.columns(2)
with col1:
    fig2 = px.sunburst(df, path=['Intercambio Internacional', 'GPA', 'PaisAsignado'], values='Promedio',
                    color='Promedio', color_continuous_scale=px.colors.colorbrewer.RdYlGn)
    fig2.update_layout(
        title={
            'text': "Análisis de Tipo de Programa por Promedio y País Asignado",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.subheader('Esta es una gráfica solar que representa el tipo de Intercambio al que se van los estudinates del Tecnológico de Monterrey. La grafica está agrupado por niveles de promedio y por países seleccionados para el intercambio.')
    st.plotly_chart(fig2, use_container_width=True)
with col2:
    fig3 = px.sunburst(df, path=['PrimeraOpcion', 'GPA', 'PaisAsignado'], values='Promedio',
                    color='Promedio', color_continuous_scale=px.colors.colorbrewer.RdYlGn)
    fig3.update_layout(
        title={
            'text': "Análisis de Selección de primera opción por Promedio y País Asignado",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.subheader('Esta es una gráfica solar que representa si los estudiantes del Tecnológico de Monterrey fueron seleccionados en su primera elección de intercambio. La grafica está agrupado por niveles de promedio y por países seleccionados para el intercambio.')
    st.plotly_chart(fig3, use_container_width=True)
df2 = df['PaisAsignado'].value_counts().rename_axis('unique_values').reset_index(name='counts')
fig4 = px.choropleth(df2, locations="unique_values",
                    color="counts", # lifeExp is a column of gapminder
                    hover_name="unique_values", # column to add to hover information
                    color_continuous_scale=px.colors.colorbrewer.RdYlGn,
                    projection= 'orthographic')
fig4.update_layout(
    title={
        'text': "Mapa Mundial de Países Asignados a Estudiantes a través de los años",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.subheader('Este es un mapa del mundo que representa a donde se va los estudiantes del Tecnológico de Monterrey de Intercambio. Este mapa se diferencia por colores dependiendo del número de personas que se van de intercambio a dicho país.')
st.plotly_chart(fig4, use_container_width=True)
