"""
Copyright  2015, Fantain Sports Private Limited

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

"""
This module will take each model and update the data
"""
import logging
import string
import random
from django.db import transaction
from . import discover


def process_field_action(action, length):
    if action == "name":
        return "vivek"
    if action == "zero":
        return 0
    if action == "randomstring":
        return ''.join(random.choice(string.ascii_letters)
                       for _ in range(length))
    if action == "randomnumber":
        return random.randint(0, length)


def process_field(model_rec, field_action):
    # The field_action is a tuple with the following format.
    # (field_name, Action to perform)
    if field_action:
        metafield = getattr(model_rec, "_meta").get_field(field_action[0])
        if metafield:
            if metafield.auto_created | metafield.hidden | metafield.is_relation:
                return False
            else:
                field_data = metafield.deconstruct()
                logging.debug(
                    u"metadata for field {0} is {1}".format(
                        field_action[0],
                        field_data))
                if 'max_length' in field_data:
                    setattr(
                        model_rec,
                        field_action[1],
                        process_field_action(
                            field_action[1],
                            field_data['max_length']))
                    return True
                else:
                    logging.error(
                        "This field {0} has no length attribute".format(
                            field_action[0]))


def process_model(model_obj, fields_collection):
    processed = 0
    for anobj in model_obj.objects.all():
        transaction.set_autocommit(False)
        while processed % 1000:
            record_success = True
            for field_action in fields_collection:
                record_success &= process_field(anobj, field_action)
            if record_success:
                anobj.save()
                processed += 1
        logging.info(
            u"processed {0} records for {1}".format(
                processed,
                model_obj))
        transaction.set_autocommit(True)
    # to catch the stragglers
    transaction.set_autocommit(True)
    logging.info(
        u"processed {0} records for {1}".format(
            processed,
            model_obj))


def process_file(filedata):
    for modelinfo, fieldinfo in filedata.iteritems():
        model = discover.get_model(modelinfo[0], modelinfo[1])
        if model:
            process_model(model, fieldinfo)
