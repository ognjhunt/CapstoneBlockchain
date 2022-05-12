# Start
import \
    datetime as d  # import the datetime library for our block timestamp and rename it as d for simplicity while typing
import hashlib as h  # import the library for hashing our block data and rename it as h for simplicity while typing
import pandas as pd


class Block:  # create a Block class
    def __init__(self, index, timestamp, data,
                 prevhash):  # declare an initial method that defines a block, a block contains the following information
        self.index = index  # a block contains an ID
        self.timestamp = timestamp  # a block contains a timestamp
        self.data = data  # a block contains some transactions
        self.prevhash = prevhash  # a block contains a hash of the previous block
        self.hash = self.hashblock()  # a block contains a hash, the hash is obtained by hashing all the data contained in the block

    def hashblock(self):  # define a method for data encryption, this method will retain a hash of the block
        block_encryption = h.sha256()  # We need a sha256 function to hash the content of the block, so let's declare it here
        block_encryption.update(str(self.index).encode() + str(self.timestamp).encode() + str(self.data).encode() + str(
            self.prevhash).encode())  # to encrypt the data in the block, We need just to sum everything and apply the hash function on it
        return block_encryption.hexdigest()  # let's return that hash result

    @staticmethod  # declaring a static method for the genesis block
    def genesisblock():  # delcare a function for generating the first block named genesis
        return Block(0, d.datetime.now(), "genesis block transaction", " ")  # return the genesis block

    @staticmethod  # let's declare another static method to get the next block
    def newblock(lastblock):  # get the next block, the block that comes after the previous block (prevblock+1)
        index = lastblock.index + 1  # the id of this block will be equals to the previous block + 1, which is logic
        timestamp = d.datetime.now()  # The timestamp of the next block
        hashblock = lastblock.hash  # the hash of this block
        data = excelData  # ADD DATA FROM EXCEL IN HERE +str("")
        return Block(index, timestamp, data, hashblock)  # return the entire block


blockchain = [Block.genesisblock()]  # now it's time to initialize our blockchain with a genesis block in it
prevblock = blockchain[
    0]  # the previous block is the genesis block itself since there is no block that comes before it at the indice 0


# let's print the genesis block information
def get_filehandle(file_name, mode):
    return open(file_name, mode)


test = get_filehandle("test.txt", "w")

test.write(f"Block ID: {prevblock.index}\n")
test.write(f"Timestamp: {prevblock.timestamp}\n")
test.write(f"Hash of the block: {prevblock.hash}\n")
test.write(f"Previous Block Hash: {prevblock.prevhash}\n")
test.write(f"data: {prevblock.data}\n\n\n")


index = 0
excelData = ""
blockDataArray = []

for i in range(0,5):  # the loop starts from here, we will need only 5 blocks in our ledger for now, this number can be increased
    addblock = Block.newblock(prevblock)  # the block to be added to our chain
    blockchain.append(addblock)  # we add that block to our chain of blocks
    prevblock = addblock  # now the previous block becomes the last block so we can add another one if needed
    fileLocation = "/Users/nijelhunt/Documents/SupplyChainData.xlsx"
    workBook = pd.read_excel(fileLocation)
    workBook.head()

    str1 = str('ID: ') + str(workBook['ID'].iloc[index]) + str('; ')
    str2 = str('Project Code: ') + str(workBook['Project Code'].iloc[index]) + str('; ')
    str3 = str('PQ #: ') + str(workBook['PQ #'].iloc[index]) + str('; ')
    str4 = str('PO / SO #: ') + str(workBook['PO / SO #'].iloc[index]) + str('; ')
    str5 = str('ASN/DN #: ') + str(workBook['ASN/DN #'].iloc[index]) + str('; ')
    str6 = str('Country: ') + str(workBook['Country'].iloc[index]) + str('; ')
    str7 = str('Managed By: ') + str(workBook['Managed By'].iloc[index]) + str('; ')
    str8 = str('Fulfill Via: ') + str(workBook['Fulfill Via'].iloc[index]) + str('; ')
    str9 = str('Vendor INCO Term: ') + str(workBook['Vendor INCO Term'].iloc[index]) + str('; ')
    str10 = str('Shipment Mode: ') + str(workBook['Shipment Mode'].iloc[index]) + str('; ')
    str11 = str('PQ First Sent to Client Date: ') + str(workBook['PQ First Sent to Client Date'].iloc[index]) + str(
        '; ')

    str12 = str('PO Sent to Vendor Date: ') + str(workBook['PO Sent to Vendor Date'].iloc[index]) + str('; ')
    str13 = str('Scheduled Delivery Date: ') + str(workBook['Scheduled Delivery Date'].iloc[index]) + str('; ')
    str14 = str('Delivered to Client Date: ') + str(workBook['Delivered to Client Date'].iloc[index]) + str('; ')
    str15 = str('Delivery Recorded Date: ') + str(workBook['Delivery Recorded Date'].iloc[index]) + str('; ')
    str16 = str('Product Group: ') + str(workBook['Product Group'].iloc[index]) + str('; ')
    str17 = str('Sub Classification: ') + str(workBook['Sub Classification'].iloc[index]) + str('; ')
    str18 = str('Vendor: ') + str(workBook['Vendor'].iloc[index]) + str('; ')
    str19 = str('Item Description: ') + str(workBook['Item Description'].iloc[index]) + str('; ')
    str20 = str('Molecule/Test Type: ') + str(workBook['Molecule/Test Type'].iloc[index]) + str('; ')
    str21 = str('Brand: ') + str(workBook['Brand'].iloc[index]) + str('; ')
    str22 = str('Dosage: ') + str(workBook['Dosage'].iloc[index]) + str('; ')

    str23 = str('Dosage Form: ') + str(workBook['Dosage Form'].iloc[index]) + str('; ')
    str24 = str('Unit of Measure (Per Pack): ') + str(workBook['Unit of Measure (Per Pack)'].iloc[index]) + str('; ')
    str25 = str('Line Item Quantity: ') + str(workBook['Line Item Quantity'].iloc[index]) + str('; ')
    str26 = str('Line Item Value: ') + str(workBook['Line Item Value'].iloc[index]) + str('; ')
    str27 = str('Pack Price: ') + str(workBook['Pack Price'].iloc[index]) + str('; ')
    str28 = str('Unit Price: ') + str(workBook['Unit Price'].iloc[index]) + str('; ')
    str29 = str('Manufacturing Site: ') + str(workBook['Manufacturing Site'].iloc[index]) + str('; ')
    str30 = str('First Line Designation: ') + str(workBook['First Line Designation'].iloc[index]) + str('; ')
    str31 = str('Weight (Kilograms): ') + str(workBook['Weight (Kilograms)'].iloc[index]) + str('; ')
    str32 = str('Freight Cost (USD): ') + str(workBook['Freight Cost (USD)'].iloc[index]) + str('; ')
    str33 = str('Line Item Insurance (USD): ') + str(workBook['Line Item Insurance (USD)'].iloc[index])
    # print(str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10 + str11)
    excelData = (
            str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10 + str11 + str12 + str13 + str14 + str15 + str16 + str17 + str18 + str19 + str20 + str21 + str22 + str23 + str24 + str25 + str26 + str27 + str28 + str29 + str30 + str31 + str32 + str33)
    blockDataArray.append(excelData)

    # print(addblock.index)
    # print(blockchain)
    # print(blockDataArray)
    # print(index)
    #  if index == 0 :
    #     index += 2
    # else :
    index += 1

    test.write(f"Block ID #{addblock.index}\n")  # show the block id
    test.write(f"Timestamp:{addblock.timestamp}\n")  # show the block timestamp
    test.write(f"Hash of the block:{addblock.hash}\n")  # show the hash of the added block
    test.write(f"Previous Block Hash:{addblock.prevhash}\n")  # show the previous block hash
    test.write(f"data:{addblock.data}\n\n\n")  # show the transactions or data contained in that block

    # end
test.close()