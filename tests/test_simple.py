# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import gxsimcom


if __name__ == "__main__":
    gxsim = GXSim2Com()
    gxsim.Connect()
    bitValues =gxsim.BlockReadBit("M0",64)
    print(bitValues)
    wordValues = gxsim.BlockReadWord("D0",960)
    print(wordValues)
    dwrodValues = gxsim.BlockReadDWord("D1030",1)
    print(dwrodValues)
    bitValues =gxsim.BlockReadFloat("D1000",480)
    print(bitValues)

    b = gxsim.WriteBit("M0",1)
    print(b)
    b = gxsim.WriteWord("D1030",100)
    print(b)
    b = gxsim.WriteDWord("D1030",999999)
    print(b)
    b = gxsim.WriteFloat("D1030",1.23)
    print(b)
    gxsim.Close()