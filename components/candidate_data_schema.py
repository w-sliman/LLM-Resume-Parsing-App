from pydantic import BaseModel, Field
from typing import List, Optional

class date(BaseModel):
    """Date"""
    day: Optional[int] = Field(default=1, description="Day of month, a integer from 1 and 31, if unkown the default is 1")
    month: Optional[int] = Field(description="Month of year, an integer from 1 to 12")
    year: Optional[int] = Field(description="Year in yyyy format")
    

class job(BaseModel):
    """Job details"""
    job_title: Optional[str] = Field(description="Job titile")
    job_description: Optional[str] = Field(description="Information about the job and what did the candidate do in it if available.")
    started_at: Optional[date] = Field(description="When did the candidate start this job? Retrun None if not available")
    ended_at: Optional[date] = Field(description="When did the candidate end this job? Retrun None if not available")
    current_job: Optional[bool] = Field(description="True if this the candidates current job, False if it's not the candidate's current job")


class degree(BaseModel):
    """degree details, which only includes Bachelor's, Master's or Phd degrees"""
    degree_type: Optional[str] = Field(description="Degree type, which is Bachelor's, Master's or Phd")
    major: Optional[str] = Field(description="Degree major")
    university: Optional[str] = Field(description="Degree university")
    graduation_date: Optional[date] = Field(description="When did the candidate graduate? Retrun None if not available")


class candidate(BaseModel):
    """personal information about the candidate"""
    first_name: Optional[str] = Field(description="First name")
    last_name: Optional[str] = Field(description="Last name")
    country__phone_code: Optional[str] = Field(description="Country phone code, examples: +1 or +39")
    phone_number: Optional[int] = Field(description="Phone number, without country phone code")
    email: Optional[str] = Field(description="Email address")
    country: Optional[str] = Field(description="country")
    degrees: Optional[List[degree]] = Field(description="list of all candidate's degrees")
    jobs: Optional[List[job]] = Field(description="Only include jobs the candidate listed in a work experience section. Return None if he hasn't listed any.")
    skills: Optional[list[str]] = Field(description="list of candidate's skills that are relevant to the job")