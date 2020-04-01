import sys,getopt,os,re,shutil
def main(argv):
    inputdirpath="",
    configurefilepath=""
    outputdirpath=""
    try:
      opts, args = getopt.getopt(argv,"i:c:o:")
      for opt, arg in opts:
        if opt in ("-i"):
            inputdirpath = arg
        elif opt in ("-c"):
            configurefilepath = arg
        elif opt in ("-o"):
            outputdirpath = arg
    except getopt.GetoptError:
        inputdirpath="K:/Workspaces/python/namelistfilter/testing/input"
        configurefilepath="K:\\Workspaces\\python\\namelistfilter\\testing\\configure.txt"
        outputdirpath="K:/Workspaces/python/namelistfilter/testing/output"
    
    

    #获取目标目录
    targetAbsPath=os.path.abspath(outputdirpath)
    if os.path.exists(targetAbsPath+"\\existed")!=True:

        os.mkdir(targetAbsPath+"\\existed")
    if os.path.exists(targetAbsPath+"\\donotexisted")!=True:
        os.mkdir(targetAbsPath+"\\donotexisted")
    

    existingFileRecorder=open(configurefilepath,"r")

    linesall=existingFileRecorder.read()
    lines=linesall.split('\n')

    existingFileRecorder.close()
    existingFileRecorder=open(configurefilepath,"a")
    # existingFileRecorder.close()
    pattern="([a-zA-Z0-9-]+-[0-9]+)"
    for dirpaths,dirnames,filenames in os.walk(inputdirpath):
        for filename in filenames:
            # print(filename)
            prefilx=os.path.splitext(filename)[0]
            matchres=re.match(pattern,prefilx)
            if matchres:
                print(matchres.group(1))
                if matchres.group(1) in lines:
                    #如果文件重复
                    continue
                    # shutil.move(dirpaths+"\\"+filename,targetAbsPath+"\\existed\\"+filename)
                else:
                    # If file donnot existed
                    shutil.move(dirpaths+"\\"+filename,targetAbsPath+"\\donotexisted\\"+filename)
                    existingFileRecorder.write(matchres.group(1)+"\n")
                    lines.append(matchres.group(1))
            else:
                shutil.move(dirpaths+"\\"+filename,targetAbsPath+"\\donotexisted\\"+filename)
        
    existingFileRecorder.close()

if __name__ == "__main__":
    main(sys.argv[1:])




