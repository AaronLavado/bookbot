def main():
    fatdictionary = {}

    spacecounter = {}
    
    acharacter = "a"
    bcharacter = "b"  
    ccharacter = "c"
    dcharacter = "d"
    echaracter = "e"
    fcharacter = "f"
    gcharacter = "g"
    hcharacter = "h"
    icharacter = "i"
    jcharacter = "j"
    kcharacter = "k"
    lcharacter = "l"
    mcharacter = "m"
    ncharacter = "n"
    ocharacter = "o"
    pcharacter = "p"
    qcharacter = "q"
    rcharacter = "r"
    scharacter = "s"
    tcharacter = "t"
    ucharacter = "u"
    vcharacter = "v"
    wcharacter = "w"
    xcharacter = "x"
    ycharacter = "y"
    zcharacter = "z"
    
    spacechar = " "
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        lowercase = file_contents.lower()
        acount = lowercase.count(acharacter)
        bcount = lowercase.count(bcharacter)
        ccount = lowercase.count(ccharacter)
        ecount = lowercase.count(echaracter)
        ncount = lowercase.count(ncharacter)
        pcount = lowercase.count(pcharacter)
        ccount = lowercase.count(ccharacter)
        spacecount = lowercase.count(spacechar)
    fatdictionary = {
        echaracter: ecount,
        ncharacter: ncount,
        pcharacter: pcount,
        ccharacter: ccount,
        
    }


    print(fatdictionary)
main()