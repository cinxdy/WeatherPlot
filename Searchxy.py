from openpyxl import load_workbook

def searchxy(search_target):
    wb = load_workbook("./OpenAPIGuide/Location.xlsx", data_only=True)
    print("well done")
    #첫 시트
    ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])
    
    for row in ws.rows:
        if row[1].value==str(search_target):
            return row[5].value, row[6].value
    
    print("No Data!")
    wb.close()
    return None


#x,y = searchxy('1111054000')
#print("x>")
#print(x)
#print("y")
#print(y)