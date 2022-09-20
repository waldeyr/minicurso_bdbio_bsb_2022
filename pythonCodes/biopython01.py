from Bio.KEGG import REST
from Bio.KEGG import Enzyme
request = REST.kegg_get("ec:2.7.7.9")
open("ec_2.7.7.9.txt", "w").write(request.read())
records = Enzyme.parse(open("ec_2.7.7.9.txt"))
record = list(records)[0]
record.classname
record.entry
