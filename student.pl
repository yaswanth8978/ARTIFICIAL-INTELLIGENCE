studies(charlie,csc135).
studies(olivia,csc135).
studies(jack,csc131).
studies(arthur,csc134).

teaches(krike,csc135).
teaches(collins,csc131).
teaches(collins,csc171).
teaches(juniper,csc134).
professor(x,y):- teaches(x,c),studies(y,c).
