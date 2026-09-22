from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.


from django.contrib.auth.decorators import login_required
import joblib
import csv
import pandas as pd
from django.http import HttpResponse
from reportlab.pdfgen import canvas

model = joblib.load('randomforest_model.pkl')
print(model.feature_names_in_)


@login_required
def teacher_dashboard(request):

    #if not request.user.groups.filter(
     #   name='Teacher'
    #).exists():
   #     return redirect ('home')
    return render(
        request, 'teacher/teacher_dashboard.html'
    )



@login_required
def upload_csv(request):

    if request.method == "POST":
        
        if 'csv_file' not in request.FILES:
            messages.error(request, 'Please Upload a CSV or'
            ' Excel File Before Clicking Predict ')
            return redirect ('upload_csv')
        #csv_file = request.FILES('csv_file')

        csv_file = request.FILES['csv_file']

        #df = pd.read_csv(csv_file)
        filename = csv_file.name

        if filename.endswith('.csv'):

            df = pd.read_csv(csv_file, encoding='latin1')

        elif filename.endswith('.xlsx'):
            df = pd.read_excel(csv_file)

        #elif filename not in request.FILES:
         #   messages.error(request, 'Please Upload A File Before Clicking Predict')
            #return redirect('upload_csv')


        else:
            messages.error(request,'Invalid File!' \
            ' Only CSV or Excel Files Allowed'
            )
            return redirect('upload_csv')

        required_columns = [  
                
                'GENDER',
                'NAME',
                'MATH',
                'ENG',
                'KISW',
                'INT. SCI',
                'PRE.TECH',
                'AGRI',
                'CRE',
                'C/A',
                'SST',
                'SCI_PROJ',
                'CREA_PROJ',
                'AGR_PROJ',
                'PRE&SCOUT',
                'MUSIC&DRAMA',
                'SPORTS',
                'SCH. TYPE'

            ]

        uploaded_columns = list(df.columns)

        if uploaded_columns!= required_columns:
            messages.error (
                request, 
                'Incorrect Excel Input Format! '
                'The Columns must be Labelled and Ordered Exactly as Follows:' +
                '|'.join(required_columns)

            )

            return redirect('upload_csv')
            
        
        #return HttpResponse(str(df.columns.tolist()))
        #df.rename(columns={
         #   'INTER': 'INT. SCI',
          #  'PRE TEC':'PRE.TECH',
           # 'SCHOOL':'SCH. TYPE',
            #'MUSICDRAMA':'MUSIC&DRAMA',
        #}, inplace=True)
        df['GENDER'] = df['GENDER'].astype(str).str.upper().replace({
            'M':1,
            'MALE':1,
            'F':0,
            'FEMALE':0
        }
            
        )

        df['SCH. TYPE'] = df['SCH. TYPE'].astype(str).str.upper().replace({
            'PUBLIC':1,
            'PRIVATE':0

        })

        df['SPORTS'] = df['SPORTS'].astype(str).str.upper().replace({
            'NO':0,
            'N':0,
            'YES':1,
            'Y':1
        })

        df['MUSIC&DRAMA'] = df['MUSIC&DRAMA'].astype(str).str.upper().replace({
            'NO':0,
            'N':0,
            'YES':1,
            'Y':1
        })

        df['PRE&SCOUT'] = df['PRE&SCOUT'].astype(str).str.upper().replace({

            'NO':0,
            'N':0,
            'YES':1,
            'Y':1
        })
        
        
        #print(df.columns.tolist())
        
        X = df[[
            #'NAME',
            'GENDER',
            'MATH',
            'ENG',
            'KISW',
            'INT. SCI',
            'PRE.TECH',
            'AGRI',
            'CRE',
            'C/A',
            'SST',
            'SCI_PROJ',
            'CREA_PROJ',
            'AGR_PROJ',
            'PRE&SCOUT',
            'MUSIC&DRAMA',
            'SPORTS',
            'SCH. TYPE'
        ]]
        model = joblib.load('randomforest_model.pkl')
        predictions = model.predict(X)

        pathway_map = {
            0: 'Arts',
            
            1: 'Social Science',

             2: 'STEM',
        }

        df['RECOMMENDED_PATHWAY'] = [
            pathway_map[p]
            for p in predictions
        ]

        results = df.to_dict('records')

        request.session['results'] = results

        return render(
            request,
            'teacher/batch_results.html',
            {'results': results}
        )

    return render(
        request,
        'teacher/upload_csv.html'
    )


def download_pdf(request):
    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] =('attachment; filename=results.pdf')

    p = canvas.Canvas(response)

    y = 800

    p.drawString(
        200,
        y,

        'Career Pathway Report'
    )

    y -=50

    

    results = request.session.get(
        'results',
        []

    
    )
    #return HttpResponse(str(results[0]))
    for row in results:
        p.drawString(
            50,
            y,
            f"{row['NAME']} - "
            f"{row['RECOMMENDED_PATHWAY']}"
        )

        y -=20

    p.save()

    return response
    #else:
     #   return HttpResponse('File not Found!', status=404)
    

    