def generate_score_breakdown(sementic_score, skill_match,sections):
  total_sections = len(sections) if section else 1
  present_sections = sum(1 for v in sections.values() if v == "present")
  missing_sec=[k for k, v in (sections or {}).items( ) if v!="present"]
  completeness_score = round(present_sections / total_sections * 100, 1)
  sec_score= (
        semantic_score      * 0.40 +
        skill_match_percent * 0.35 +
        completeness_score  * 0.25
    )

    if final_score >= 80:
        grade = "Excellent"
    elif final_score >= 65:
        grade = "Good"
    elif final_score >= 50:
        grade = "Average"
    else:
        grade = "Needs Work"
  

 sem_msg="strong content match" if sementic_score>=75 else("moderate match" if sementic_score >=50 else "below moderate")
 skill_msg=f"missing skills:{','.join(missing_skills[:5])}" if missing_skills else "full skill matched"
 sec_msg=f"missing sections :{','.join(missing_sec)}" if missing_sec else "all sections are present"
 return{
  "final_score" : final_score,
  "singals":{
    "skill_match":{"score": round(skill_match_data.get("match_percent",0.0),1),"weight":35%}  ,
    "sementic_match":{"score":round(sementic_score,1),"weight":40%}
    "completeness":{"score":sec_score,"weight":25%}
    },
    "rationable_panel":[sem_msg,skill_msg,sec_msg]
 }