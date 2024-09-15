import json
import textwrap

colourmap = {
    "p":"",
    "h1":"\033[96;4;1m",
    "h2":"\033[96m"
}
    
def load_manual(dmmy):
    with open("manuals/main_manual.txt") as text:
        return text.read()
    

def load_manual_json(indents,wrap_width):
    json_parsed=[]
    with open("manuals/main.json") as text:
        json_parsed=json.load(text);
        
    parsed_text=""
    for i in json_parsed:
        if(i["type"] in colourmap):
            wrapped_text=i["text"]
            wrapped_text_arr=textwrap.wrap(
                wrapped_text, width=wrap_width,
                replace_whitespace=False
            )
            if (len(wrapped_text_arr)==1):
                parsed_text+="\n\n\n"+indents+colourmap[i["type"]]+wrapped_text_arr[0]+"\033[0m\n\n"
                continue
            else:
                wrapped_text=indents+("\n"+indents).join(wrapped_text_arr)

            #parsed_text+=colourmap[i["type"]]
            parsed_text+=wrapped_text
            #parsed_text+="\033[0m\n\n"
        else:
            parsed_text+=(indents+i["text"])
            
    parsed_text+="\n\n";
    
    return parsed_text
