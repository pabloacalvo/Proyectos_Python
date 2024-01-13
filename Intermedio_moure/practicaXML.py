from xml.etree.ElementTree import parse, Element

name_file = 'C:\\ncr\caja\\testing-cencosud-argentina-jumbo-selfscan\P_REGCONF.hierarchy.99991.ScanAndPay.XML'
doc_xml = parse(name_file)
raiz = doc_xml.getroot()
print(raiz.tag)
print(len(list(raiz)))
print(raiz[0][0])



