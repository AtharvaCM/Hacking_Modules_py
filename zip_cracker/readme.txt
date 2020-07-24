You can find an executable of the same program in the dist folder
This executable is for Kali Linux and similar OS

To make an executable for windows Run pyinstaller on windows and create it.

NOTE:
    If the file's compression type is type 9: Deflate64/Enhanced Deflate (PKWare's proprietary 
format as opposed to the more common type 8) it wont work and a zipfile bug: it will not throw an exception for unsupported compression-types. It used to just silently return a bad file object [Section 4.4.5 compression method]. I filed that bug and now it raises NotImplementedError when the compression type is unknown.
