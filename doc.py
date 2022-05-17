from docx import Document
import copy
from num2words import num2words

def create_documents(sheet, document):
    def foreach(keys, sheet, index, doc):
        for key in keys:
            for p in doc.paragraphs:
                if key in p.text:
                    inline = p.runs
                    for i in range(len(inline)):
                        if key in inline[i].text:
                            if key == 'COUNT':
                                text = inline[i].text.replace(key, str(sheet[key][index]) + " " + num2words(int(sheet[key][index]), lang='ru'))
                            else:
                                text = inline[i].text.replace(key, str(sheet[key][index]))
                            inline[i].text = text
                #p. text = p.text.replace(key, str(sheet[key][index]))

    sheet = sheet
    keys = list(sheet.keys())
    document = document

    for i,_ in enumerate(sheet[keys[0]]):
        newDoc = copy.deepcopy(document)
        foreach(keys, sheet, i, newDoc)
        newDoc.save("docs/" + str(i) + "_demo.docx")
