#######################################
###   DATE        : 2021-12-06      ###
###   AUTHOR      : Dmitry Ivanov   ###
###   DESCRIPTION : Todo-list app   ###
#######################################

from packages.todo import todo

# plug and play :)

app = todo.Todo() # todo app initialization
app.run()
