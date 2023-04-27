
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member: member["id"] = self._generateId()
        self._members.append(member)
        return member

    def delete_member(self, id):
        new_list= list(filter(lambda dict: dict['id']!=id,self._members))
        self._members=new_list
        return new_list

    def get_member(self, id):
        for member in self._members:
            if member['id']==id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members