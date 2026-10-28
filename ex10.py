import re
 
skills = [
    "python", "java", "c", "c++", "sql",
    "machine learning", "deep learning",
    "artificial intelligence", "data science",
    "html", "css", "javascript",
    "power bi", "excel", "tensorflow",
    "pandas", "numpy", "opencv"
]
 
def analyze_resume(resume, job_description):
    resume = resume.lower()
    job_description = job_description.lower()
 
    resume_skills = []
    for skill in skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', resume):
            resume_skills.append(skill)
 
    required_skills = []
    for skill in skills:
        if re.search(r'\b' + re.escape(skill) + r'\b',
                     job_description):
            required_skills.append(skill)
 
    matched_skills = list(set(resume_skills) &
                          set(required_skills))
    missing_skills = list(set(required_skills) -
                          set(resume_skills))
 
    if required_skills:
        score = len(matched_skills) / len(required_skills) * 100
    else:
        score = 0
 
    return (resume_skills, required_skills,
            matched_skills, missing_skills, score)
 
 
print("===== AI RESUME ANALYZER =====")
resume = input("\nEnter your Resume Text:\n")
job = input("\nEnter Job Description:\n")
 
resume_skills, required_skills, matched, missing, score = \
    analyze_resume(resume, job)
 
print("\n===== ANALYSIS RESULT =====")
print("\nDetected Resume Skills:")
print(", ".join(resume_skills) if resume_skills else "No skills detected")
 
print("\nRequired Job Skills:")
print(", ".join(required_skills) if required_skills else "No skills detected")
 
print("\nMatched Skills:")
print(", ".join(matched) if matched else "No matching skills")
 
print("\nMissing Skills:")
print(", ".join(missing) if missing else "No missing skills")
 
print(f"\nResume Match Score: {score:.2f}%")
 
if score >= 75:
    print("Recommendation: Strong Match")
elif score >= 50:
    print("Recommendation: Moderate Match")
else:
    print("Recommendation: Needs Improvement")
