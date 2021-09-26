from pybb.permissions import DefaultPermissionHandler


class MyPyBBPermissionHandler(DefaultPermissionHandler):

    def may_create_topic(self, user, forum):
        """ return True if `user` is allowed to create a new topic in `forum` """
        return True

    def may_create_post(self, user, topic):
        """ return True if `user` is allowed to create a new post in `topic` """
        return True
