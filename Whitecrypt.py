import hashlib

def Map(Method: int, Numbers: str):
	Mapping = Method == 1 and "          " or Method == 2 and "0945862731"
	Mapped = ""
	for Number in Numbers:
		Mapped += Mapping[int(Number)]
	return Mapped

def Unmap(Method: int, MappedNumbers: str):
	Mapping = Method == 1 and "          " or Method == 2 and "0945862731"
	Unmapped = ""
	for MappedNumber in MappedNumbers:
		Unmapped += str(Mapping.find(MappedNumber))
	return Unmapped

def ToUnicodeOrder(Separator: str, Text: str, Mapped: bool, MappingMethod: int):
	UnicodeOrder = ""
	Index = 0
	for Character in Text:
		Index += 1
		Unicode = str(ord(Character))
		UnicodeOrder += Mapped == True and Map(MappingMethod, Unicode) or Unicode
		if Index != len(Text):
			UnicodeOrder += Separator
	return UnicodeOrder

def FromUnicodeOrder(Separator: str, UnicodeOrder: str, Mapped: bool, MappingMethod: int):
	Text = ""
	for RawUnicode in UnicodeOrder.split(Separator):
		Unicode = Mapped == True and Unmap(MappingMethod, RawUnicode) or RawUnicode
		Text += chr(int(Unicode))
	return Text

def Encode(PlainText: str):
	return ToUnicodeOrder(" ", PlainText, True, 1)

def Decode(EncodedText: str):
	return FromUnicodeOrder(" ", EncodedText, True, 1)

def Encrypt(PlainText: str, Key: str):
	HashedKey = hashlib.sha512(Key.encode()).hexdigest()
	MappedKey = ToUnicodeOrder("1114112", HashedKey, True, 2) # separator is "1114112" because a unicode can be 0x10ffff at max in python
	MappedText = ToUnicodeOrder("1114112", PlainText, True, 2) # last parameter is 2 to map it with numbers instead of whitespaces
	EncryptedText = str(int(MappedText) + int(MappedKey))
	return ToUnicodeOrder(" ", EncryptedText, True, 1) # encrypted text but with whitespace mapping

def Decrypt(MappedEncryptedText: str, Key: str):
	UnmappedEncryptedText = FromUnicodeOrder(" ", MappedEncryptedText, True, 1)
	HashedKey = hashlib.sha512(Key.encode()).hexdigest()
	MappedKey = ToUnicodeOrder("1114112", HashedKey, True, 2)
	MappedText = str(int(UnmappedEncryptedText) - int(MappedKey))
	UnmappedText = FromUnicodeOrder("1114112", MappedText, True, 2)
	return UnmappedText
