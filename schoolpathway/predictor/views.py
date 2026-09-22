from django.shortcuts import render, redirect
# Create your views here.

import os
from .models import Prediction
import joblib
import numpy as np

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#model = joblib.load('randomforest_model.pkl')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(
    os.path.join(BASE_DIR,'randomforest_model.pkl')
)
def home(request):
    return render(request, 'predictor/home.html')



def get_mark(request, field_name):
    value = request.POST.get(field_name,'').strip()

    if value == '':
        return None
    
    try:
        value = float(value)

        if value <0 or value >100:
            return None
        
        return value
    
    except(ValueError, TypeError):
        return None

@login_required
def predict(request):
    if request.method == 'POST':

        math = get_mark(request,'MATH')
        eng = get_mark(request,'ENG')
        kis = get_mark(request,'KISW')
        science = get_mark(request,'INT. SCI')
        pretech = get_mark(request,'PRE.TECH')
        agriculture = get_mark(request,'AGRI')
        cre = get_mark(request,'CRE')
        carts = get_mark(request,'C/A')
        sst = get_mark(request,'SST')

        scienceproj = get_mark(request,'SCI_PROJ')
        cartsproj = get_mark(request,'CREA_PROJ')
        agrproj = get_mark(request,'AGR_PROJ')

        marks = [
            math,
            eng,
            kis,
            science,
            pretech,
            agriculture,
            cre,
            carts,
            sst,
            scienceproj,
            cartsproj,
            agrproj
        ]


        if any(mark is None for mark in marks):
            messages.error(
                request,'Please fill in  numbers between 0 to 100 only'
            )

            return redirect('predict')


        prefect = int(request.POST['PRE&SCOUT'])
        musicdrama = int(request.POST['MUSIC&DRAMA'])
        sports = int(request.POST['SPORTS'])
        school = int(request.POST['SCH. TYPE'])
        student_name=request.POST['student_name']
        gender = int(request.POST['GENDER'])
        
     



#def predict(request):

 #   prediction = None

  #  if request.method == 'POST':
   #     student_name=request.POST['student_name']
    #    gender = int(request.POST['GENDER'])
        
     #
     #    math = float(request.POST['MATH'])
        #eng = float(request.POST['ENG'])
        #kis = float(request.POST['KISW'])
        #science = float(request.POST['INT. SCI'])
       # pretech = float(request.POST['PRE.TECH'])
        #agriculture = float(request.POST['AGRI'])
        #cre = float(request.POST['CRE'])
        #carts = float(request.POST['C/A'])
        #sst = float(request.POST['SST'])

        #scienceproj = float(request.POST['SCI_PROJ'])
        #cartsproj = float(request.POST['CREA_PROJ'])
        #agrproj = float(request.POST['AGR_PROJ'])

        #prefect = int(request.POST['PRE&SCOUT'])
        #musicdrama = int(request.POST['MUSIC&DRAMA'])
        #sports = int(request.POST['SPORTS'])
        #school = int(request.POST['SCH. TYPE'])

        data = np.array([[
            gender,
            math,
            eng,
            kis,
            science,
            pretech,
            agriculture,
            cre,
            carts,
            sst,
            scienceproj,
            cartsproj,
            agrproj,
            prefect,
            musicdrama,
            sports,
            school
]])
        
       # result = model.predict(data)
        #pathway = result[0]
        #prediction=pathway

        result = int(model.predict(data)[0])
        pathway_map = {
                        0:'ARTS & SPORTS SCIENCE',
                        1:'SOCIAL SCIENCE',
                        2:'STEM'
                    }

        prediction = pathway_map[result]


        subjects = {
            'Mathematics': math, 
            'English': eng,
            'Kiswahili': kis,
            'Integrated Science':science,
            'Pre-Technical Studies': pretech,
            'Agriculture': agriculture,
            'C.R.E': cre,
            'Creative Arts':carts,
            'SST':sst

        }

        top_subjects = sorted(
            subjects.items(),
            key=lambda x:x[1],
            reverse=True

        )[:3]

        strengths = []

        for subject, score in top_subjects:

            if subject == "Mathematics":
                strengths.append("Analytical Thinking")

            elif subject == "Integrated Science":
                strengths.append("Scientific Reasoning")

            elif subject == "Pre-Technical Studies":
                strengths.append("Technical Skills")

            elif subject == "English":
                strengths.append("Communication Skills")

            elif subject == "Kiswahili":
                strengths.append("Language Proficiency")

            elif subject == "Creative Arts":
                strengths.append("Creative Expression")

            elif subject == "SST":
                strengths.append("Social Awareness")

            elif subject == "Agriculture":
                strengths.append("Practical Problem Solving")

            elif subject == "C.R.E":
                strengths.append("Ethical Reasoning")


        strengths_text = ", ".join(strengths)


        strength_factors = []

        

        if musicdrama == 1:
            strength_factors.append(
                "Participation in Music and Drama"
            )

        if sports == 1:
            strength_factors.append(
                "Active Participation in Sports and Games"
            )

        if prefect == 1:
            strength_factors.append(
                "Leadership Experience"
            )

        if strength_factors:
            strength_factors_text = ", ".join(
                strength_factors
            )
        else:
            strength_factors_text = "No major co-curricular factors identified"


        if prediction == 'STEM':

            explanation = (
                f"The recommendation is based on the student's "
                f"demonstrated strengths in {strengths_text}. "
                f"These abilities indicate strong analytical, "
                f"scientific and problem-solving capabilities "
                f"that align well with STEM careers."
            )
            careers = [

                            "Doctor",
                            "Engineer",
                            "Software Developer",
                            "Data Scientist",
                            "Architect",
                            "Statistician",
                            "Actuary",
                            "Pilot",
                            "Research Scientist",
                            "Cybersecurity Analyst"

                    ]
            

            prospects = (
                            "The STEM pathway is associated with growing demand "
                            "in technology, healthcare, engineering, artificial "
                            "intelligence, renewable energy and scientific research."
                        )


        elif prediction == 'ARTS & SPORTS SCIENCE':
            


            explanation = (
                f"The recommendation is based on the student's "
                f"strengths in {strengths_text} together with "
                f"{strength_factors_text}. These qualities "
                f"suggest strong creative, expressive and "
                f"communication abilities that are valuable "
                f"in Arts-related careers."
            )

            careers = [

                            "Teacher",
                            "Musician",
                            "Journalist",
                            "Graphic Designer",
                            "Photographer",
                            "Actor",
                            "Film Producer",
                            "Writer",
                            "Content Creator",
                            "Media Specialist"

                        ]
            
            prospects = (
                        "The Arts pathway offers opportunities in creative "
                        "industries, digital media, communication, performing "
                        "arts and content creation."
                    )


        else:


            explanation = (
                f"The recommendation is influenced by the student's "
                f"strengths in {strengths_text}. These strengths "
                f"indicate potential for leadership, communication, "
                f"social understanding and decision-making, which "
                f"are important in Social Science careers."
            )



            careers = [

                            "Lawyer",
                            "Accountant",
                            "Economist",
                            "Psychologist",
                            "Human Resource Officer",
                            "Business Manager",
                            "Diplomat",
                            "Political Scientist",
                            "Public Administrator",
                            "Project Manager"

                        ]



            prospects = (
                            "The Social Science pathway prepares students for "
                            "careers in business, governance, economics, law, "
                            "leadership and public service."
                        )
        Prediction.objects.create(
            student_name = student_name,
            gender=gender,
            math=math,
            eng=eng,
            kis=kis,
            science=science,
            pretech=pretech,
            agriculture=agriculture,
            cre=cre,
            carts=carts,
            sst = sst,
            scienceproj=scienceproj,
            cartsproj=cartsproj,
            agrproj= agrproj,
            prefect= prefect,
            musicdrama=musicdrama,
            sports=sports,
            school=school

    )


        return render(
            request,
        'predictor/result.html',
        {
            'prediction': prediction,
            'top_subjects': top_subjects,
            'strengths': strengths,
            'strength_factors': strength_factors,
            'explanation': explanation,
            'careers': careers,
            'prospects': prospects
        }
    )




    return render(
    request,
    'predictor/predict.html'
    )


   









     

    #Prediction.objects.create(
      #      student_name = student_name,
       #     gender=gender,
        #    math=math,
         #   eng=eng,
          #  kis=kis,
           # science=science,
            #pretech=pretech,
    #        agriculture=agriculture,
     #       cre=cre,
      #      carts=carts,
       #     sst = sst,
        #    scienceproj=scienceproj,
         #   cartsproj=cartsproj,
          #  agrproj= agrproj,
           # prefect= prefect,
    #        musicdrama=musicdrama,
     #       sports=sports,
      #      school=school

    #)
    
    #return render(
     #   request, 
    #'predictor/result.html',
    #{'prediction':prediction,
     #'top_subjects':top
     #'explanation': explanation,
     #'careers': careers
     #}
#)



