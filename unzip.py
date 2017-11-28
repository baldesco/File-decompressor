import zipfile,subprocess, glob, os

# directorio = sys.argv[1]

def descomprimir(directorio_in,directorio_out):
    os.chdir(directorio_in)
    flag = 0
    lista_archivos = glob.glob("*.zip") + glob.glob("*.Z")
    if len(lista_archivos) > 0:
        for file in glob.glob("*.zip"):
          zip_ref = zipfile.ZipFile(file, 'r')
          zip_ref.extractall(directorio_out)
          zip_ref.close()

        for file in glob.glob("*.Z"):
          comando = r' "C:/Program Files/7-Zip/7z.exe" e "' + directorio_in+"/"+file+'" -o"'+directorio_out+'" -aoa'
          print(comando)
          subprocess.call(comando,shell=True)
    else:
        flag = 1
    return flag


# a=r' "C:/Program Files/7-Zip/7z.exe" e a.Z -o"C:/Archivos Eduardo/Investigacion y miscelaneo/Descomprimidor Python/test/1" -y'
# subprocess.call(a,shell=True)
