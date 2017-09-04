import json

AOR = "addressOfRecord"

class Registers:
    """ 
    Collection of register json objects. Currently stored in a dictionnary
    with the aor as the key. Each aor can have multiple registers so each
    value in the dict are lists of register objects.
    """



    def __init__(self):
        self.registers = {}

    
    def store_register(self, new_register):
        """
        adds a register object to this collection
        """
        
        if new_register[AOR] in self.registers:
            # aor was already exists so we append to list
            self.registers[new_register[AOR]].append(new_register)
        else:
            # aor was not there so we create a new aor/list pair in the dict
            self.registers[new_register[AOR]] = [new_register]


    def from_file(self, register_filepath):
        """
        adds all the register objects from the file to the collection
        """

        with open(register_filepath,'r') as reg_file:
            for line in reg_file:
                self.store_register(json.loads(line.strip()))


    def lookup(self, aor):
        """
        looks up aor in the collection, will raise a key error if aor not found 
        Returns json object containing 1 or more registers for the given aor
        """

        aor_registers = self.registers[aor]
        if len(aor_registers) == 1:
            return json.dumps(aor_registers[0])
        return json.dumps(aor_registers)

    def __str__(self):

        ret = ""
        for aor,register_list in self.registers.iteritems():
            ret += aor + "\n"
            for r in register_list:
                ret += r['contact'] + ", "
        return ret



    
