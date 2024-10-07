enum 
class checklist:
    itemtype   = "undefined"
    itemaction = "undefined"

    def load_checklist_item(rawdata,index):
        try:
            itemtype = rawdata[index]["type"]
            itemdata = rawdata[index]["type"]
        except Exception as e:
            throw e
            
            
    
