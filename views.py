from django.shortcuts import render

# Create your views here.
from .forms import CompareForm, WordForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .models import filecompare
from django.contrib import messages
from docx2pdf import convert
import random
import logging
logger = logging.getLogger('django')




def index(request):
       
    return render(request, 'index.html')

def fileupload(request):
    if request.method == 'POST':
        form = CompareForm(request.POST, request.FILES)
        logger.debug("##############Displaying Original File###########")
        print(request.FILES)  
        
        Originalfile = request.FILES['Originalfile']  
        Comparedfile = request.FILES['Comparedfile']          
        if form.is_valid():
            form.save()
            file1 = open('./media/generic/'+ str(Originalfile), 'r')
            Line1 = file1.readlines()
            logger.info("Selecting and Opening file1##############")
            file2 = open('./media/compared/'+ str(Comparedfile), 'r')
            Line2 = file2.readlines()
            logger.info("Selecting and Opening file2##############")
            difference = open('./media/result/'+ str(Originalfile), 'a')
            place= '../media/result/'+ str(Originalfile)
            difference.write("Results")
            output = []
    
            file1_main = []
            for lines in Line1:
                file1_main.append(lines.replace("\n",''))

            #print(file1_main) 
            print("file1--->".format(file1_main))

            file2_main = []
            for lines in Line2:
                file2_main.append(lines.replace("\n",''))

            print(file2_main)

            len_of_file1 = len(file1_main)
            len_of_file2 = len(file2_main)

            max_len = 0

            if len_of_file1 > len_of_file2:
                max_len = len_of_file1
            else:
                max_len = len_of_file2
            print(max_len)
            n,i,j=0,0,0

        while(n<max_len):
            
            if i == len_of_file1:
                logger.info("##########Comparing File modification for First File###########")
                difference.write("Change occured in line no. {} -> {}".format(j+1,file2_main[j]))
                output.append("Change occured in line no. {} -> {}".format(j+1,file2_main[j]))
                j=j+1
                n=n+1
                
            elif j == len_of_file2:
                logger.info("##########Comparing File modification for Second File###########")
                print(file1_main[i])
                i=i+1
                n=n+1
                
            else:
                if file1_main[i] == file2_main[j]:
                    i=i+1
                    j=j+1
                    n=n+1
                else:
                    difference.write("Change occured in line no. {} -> {}".format(j+1,file2_main[j]))
                    output.append("Change occured in line no. {} -> {}".format(j+1,file2_main[j]))
                    j=j+1
                    n=n+1
        
        #messages.success(request, 'Please enter both fields')            
        return render(request, 'compared_info.html', {'output': output,'place': place})
        
    else:
        form = CompareForm()
        
    return render(request,"upload_file.html", {'form':form})        

def listfiles(request):
    
    display = filecompare.objects.all()
    logger.error("##########Error displaying changes in file###########")


    return render(request, 'compare_list.html', {'display': display})

def pdfconverter(request):
    if request.method == 'POST':
        form = WordForm(request.POST, request.FILES)
        Wordfile = request.FILES['Wordfile'] 
        if form.is_valid():
            form.save()
            num = random.randint(1,10000)
            output = 'output_file'+str(num)
            doc = "./media/doctopdf/"+str(Wordfile)
            print(doc)
            pdf = "./media/pdfoutput/"+output+".pdf"
            convert(doc,pdf)
             
        else:
            messages.error(request,'Please choose word file only')
            return render(request, 'pdfconverter.html', {'form': form}) 

        return render(request, 'pdffile.html', {'output': pdf})      
#return redirect('listofpdfs')    
    else: 
        form = WordForm()
    return render(request, 'pdfconverter.html', {'form': form})  

def listofpdfs(request):
    display = filecompare.objects.all()
    logger.error("##########Error in displaying converted pdf file###########")


    return render(request, 'pdffile.html', {'display': display})


