from csv2pdf import convert
convert("names.csv", "names1.pdf") #to convert it into pdf simply
convert("names.csv", "names2.pdf", font=r"Lato-BlackItalic.ttf", headerfont=r"Lato-BlackItalic.ttf") #for adding custom fonts in pdf
convert("names.csv", "names3.pdf", headersize=10 , size=10) # to add custom header size in pdf file
convert("names.csv", "names4.pdf", headersize=10 , size=10, align="R") # to add right alignment
convert("names.csv", "names5.pdf", headersize=10 , size=10, align="L") # to add left alignment
convert("names.csv", "names6.pdf", headersize=10 , size=10, delimiter="&") # to add delimeter
convert("names.csv", "names7.pdf", headersize=10 , size=10, orientation="L") # to add orientation in pdf file