"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def loadBooks(filename):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = cf.data_dir + filename
    return model.addBooks(booksfile)


def loadTags(filename):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + filename
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    tags = model.createTagList()
    for tag in input_file:
        model.addTag(tags, tag)
    return tags


def loadBooksTags(catalog):
    """
    Hace lo mismo que "loadTags". Puse el mismo codigo porque los datos de tags y
    de booktags son muy parecidos así que me parecio mas apropiado :)
    """
    bookstagsfile = cf.data_dir + catalog
    input_file = csv.DictReader(open(bookstagsfile, encoding='utf-8'))
    bookstags = model.createBookTagList()
    for book_tag in input_file:
        model.addBookTag(bookstags, book_tag)
    return bookstags
    
    
def loadSaludo(name):
    '''
    Carga el saludo :)
    '''
    saludo = model.saludo(name)
    return saludo
