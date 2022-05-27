from models import Note
import datetime


def savenewpost(text):
    das = Note.create(text=text)
    das.save()


def noteslist():
    return Note.select()
