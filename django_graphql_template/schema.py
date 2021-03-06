import graphene
import django_graphql_template.template_app.schema as template_app_schema

# Combine GraphQL Schema from different apps

class Query(
    template_app_schema.Query,
    # Add more app-level queries here
    
    graphene.ObjectType
):
    pass

class Mutation(
    template_app_schema.Mutation,
    #add more app-level mutations here

    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
