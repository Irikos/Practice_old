<%@ Language=vbscript %>
<%Option explicit

Function getBinaryFile(strFilePath)
	Dim oStream
	Set oStream = Server.CreateObject("ADODB.Stream")
	oStream.Open
	oStream.Type = 1
	oStream.LoadFromFile strFilePath

	getBinaryFile = oStream.read
	Set oStream = Nothing
End Function 


Dim url
url = unescape(Request("URL"))


Dim idx
idx = InStr( url, "//" )
if(idx>0)then
	url = Mid( url, idx+2 )
	idx = InStr( url, "/" )
	url = Mid( url, idx+1 )
end if


if(len(url) = 0 Or Right( url, 1) = "/") then
	url = url + "_"
end if


if(Left( url, 1) = "/")then
	url = Mid( url, 2)
end if


idx = InStrRev( url, "/" )
url = Left( url, idx) + escape( Mid( url, idx+1 ) ) + ".jpg"
url = Server.MapPath( url )


Dim fs
set fs = Server.CreateObject("Scripting.FileSystemObject")
if (fs.FileExists(url))then
	Response.ContentType = "image/jpeg"
    Response.BinaryWrite( getBinaryFile(url) )
else
	Response.ContentType = "image/jpeg"
    Response.BinaryWrite( getBinaryFile(Server.MapPath("no.jpg")) )
end if
%>