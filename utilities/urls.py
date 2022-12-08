from utilities.views import *
from utilities.seeder import *
from django.urls import path

urlpatterns = [
    path('party_list/', PartyList.as_view(), name= "party_list"),
    path('states/', states),
    path('states/<int:pk>', states_by_id),
    path('senatorial/', senatorial),
    path('senatorial/<int:state_id>', senatorial_by_state),
    path('lga/', lga),
    path('lga/<int:state_id>', lga_by_state),
    path('lga/senatorial/<int:senatorial_id>', lga_by_senatorial),
    
    path('contact/', CreateContact.as_view(), name="contact"),
    path('contact_list/', ListContact.as_view(), name="contacts_list"),

    path('subscriber/', subscriber),

    path('candidates/', candidates),
    path('retrieve_update_delete_candidate/<int:pk>', CandidateRetrieveUpdateDelete.as_view(), name="retrieve_update_delete_candidate"),

    #Seeders
    path('seed/lga', seed_lga),
    path('seed/states', seed_states),
    path('seed/senatorial', seed_senatorial),
    path('seed/resetState', clearStates),
    path('seed/resetLga', clearLga),
]
