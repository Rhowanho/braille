import glob

from PIL import Image
import PIL.ImageOps 
import os



def CalculateSize(files):

    size_x=[]

    size_y=[]

    

    for file in files:

        image =Image.open(file)

        size_x.append(image.size[0])

        size_y.append(image.size[1])

    #print (size_x)

    #print (size_y)

    

    x_min = min(size_x)

    y_min = min(size_y) 

     

    total_x_size = x_min * len(files)

    total_y_size = y_min * len(files)

    

    #print("x_min:", x_min)

    #print("y_min:", y_min)

    #print("total_x_size",total_x_size)

    #print("total_y_size",total_y_size)

    

    return x_min,y_min,total_x_size,total_y_size



def ResizeTomin(files,x_min,y_min,x_size,y_size):

    file_list=[]

    for file in files:

        image = Image.open(file)

        resized_file = image.resize((x_min,y_min))

        file_list.append(resized_file)

        #print(resized_file.size)

        #resized_file.show()

        #resized_file.close()

        

    return file_list, x_size, y_size,x_min, y_min

def ResizeTomax(files,x_min,y_min,x_size,y_size):

    file_list=[]

    for file in files:

        image = Image.open(file)

        resized_file = image.resize((x_min,y_min))

        file_list.append(resized_file)

        #print(resized_file.size)

        #resized_file.show()

        #resized_file.close()

        

    return file_list, x_size, y_size,x_min, y_min


def ImageMerge(file_list,x_size,y_size,x_min,y_min,Name):
    
    path = "./static/image/"
    FileName= Name
    TypeOf = ".PNG"

    saveImageFileName = path + FileName + TypeOf

    new_image = Image.new("L",(x_size,y_min))

    for index in range(len(file_list)):

        area=((index * x_min),0,(x_min*(index+1)), y_min)

        new_image.paste(file_list[index],area) 

    #new_image.show()    

    new_image.save(saveImageFileName,"PNG",quality=80, optimize=True, progressive=True)

    #new_image.save("result.png","PNG")

    #new_image.close()

    return new_image
     

def Paste_Image(files):

    x_min,y_min,x_size,y_size=CalculateSize(files)

    file_list,x_size,y_size,x_min,y_min = ResizeTomin(files,x_min,y_min,x_size,y_size)

    Name = MakeName(files)

    image=ImageMerge(file_list,x_size,y_size,x_min,y_min,Name)     
    return image



#############################################################################

### Main()

#############################################################################

if __name__ == '__main__':

    pass



def SaveImage(list):
    target_dir="./BR_image/test/"
    
    files = []
    
    for i in list:
        s = 0
        f = 6
        if len(i) == 6:
            files.append(target_dir+i+".png")
        else:
            for x in range(len(i)//6):
                files.append(target_dir+i[s:f]+".png")
                s = s + 6
                f = f + 6

    return files

def MakeName(list):
    numberlist = []
    for i in list:
        st = os.path.split(i)
        st1 = os.path.splitext(st[1])
        numberlist.append(st1[0])
    str_numberlist = ''.join(numberlist)
    abc = str_numberlist[0:89]
    return abc
