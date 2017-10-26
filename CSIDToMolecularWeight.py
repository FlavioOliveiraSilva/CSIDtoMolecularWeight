# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:45:30 2017

@author: FlavioSilva
"""

import lxml.html
import requests



CSIDList = ['7219','6967','388322','71358','96840','23107144','93564','15634','70104','13835351','11043','13837988','5830','46336','7658']

for CSID in CSIDList:   

    UrlCompleted = ('http://www.chemspider.com/Chemical-Structure.%s.html?rid' %CSID)
    ChemSpiderPage = requests.get(UrlCompleted)
    html = lxml.html.fromstring(ChemSpiderPage.content)
    MolecularWeight = html.xpath('//*[@id="ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_structureHead"]/ul[1]/li[2]/text()')
   
    try:
        print (CSID, MolecularWeight)
        print (MolecularWeight)

        
    except:
        print 'ERROR - Too long string'

