str = "With ♥!"
print("My String's encoding: ", str.encoding.name) # UTF-8
print("\nMy String's size: ", str.size) # 7
print("\nMy String's bytesize: ", str.bytesize) # 9

def transcode str 
  # transcode from UTF-8859-1 to UTF-8
  str.force_encoding(Encoding::UTF_8)
end