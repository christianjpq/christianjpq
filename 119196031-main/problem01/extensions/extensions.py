arquivo = input("File name: ")
arquivo = arquivo.strip().lower()


if arquivo.endswith("gif") or arquivo.endswith("png"):
    print("image/" + arquivo.split(".")[-1])
elif arquivo.endswith("jpg") or arquivo.endswith("jpeg"):
    print("image/jpeg")
elif arquivo.endswith("txt"):
    print("text/plain")
elif arquivo.endswith("zip") or arquivo.endswith("pdf"):
    print("application/" + arquivo.split(".")[-1])
else:
    print("application/octet-stream")