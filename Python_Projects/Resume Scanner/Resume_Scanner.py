


def scn_resume(resume):
    from resume_parser import resumeparse
    
    data = resumeparse.read_file(resume)
    for i ,j in data.items():
        print(f"{i} :>> {j}")
        

scn_resume("prashant_jadhav_cv.pdf")