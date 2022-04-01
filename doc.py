from docx import Document
import copy

def create_documents(sheet, document):
    def foreach(keys, sheet, index, doc):
        for key in keys:
            print(key)
            for p in doc.paragraphs:
                print(sheet[key][index])
                p. text = p.text.replace(key, str(sheet[key][index]))

    sheet = sheet
    keys = list(sheet.keys())
    document = document

    for i,_ in enumerate(sheet[keys[0]]):
        newDoc = copy.deepcopy(document)
        foreach(keys, sheet, i, newDoc)
        newDoc.save("docs/" + str(i) + "_demo.docx")
