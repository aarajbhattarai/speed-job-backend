import graphene

from .types import ApplicantGQLType, JobGQLType
from jobsapp.models import Applicant, Job
from .exceptions import GraphQLError


class JobQuery(graphene.ObjectType):
    jobs = graphene.List(JobGQLType)
    job = graphene.Field(JobGQLType, pk=graphene.Int())

    def resolve_jobs(self, info):
        return Job.objects.all()

    def resolve_job(self, info, pk, **kwargs):
        if pk:
            try:
                return Job.objects.get(pk=pk)
            except Job.DoesNotExist:
                return GraphQLError("Job doesn't exists")
        return None


class ApplicantQuery(graphene.ObjectType):
    applicants = graphene.List(ApplicantGQLType)
    applicant = graphene.Field(ApplicantGQLType, pk=graphene.Int())

    def resolve_applicants(self, info, **kwargs):
        return Applicant.objects.all()
    
    def resolve_applicant(self, info, pk, **kwargs):
        if pk:
            try:
                return Applicant.objects.get(pk=pk)
            except Applicant.DoesNotExist:
                return GraphQLError("Applicant doesn't exists")
        return None
