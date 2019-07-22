'''
ECG records reader related classes
'''

import csv


class ECGReader:
    '''
    Reads a csv ECG record and select data from it.
    '''

    def __init__(self, path):
        '''
        Arguments:
            path: path to ecg record csv file
        
        Opens Csv file and fill entity list
        '''

        self.entities = []
        with open(path, 'r') as csv_file:
            row_reader = csv.reader(csv_file)
            for row in row_reader:
                entity_type = row[0]
                start = row[1]
                end = row[2]
                tags = [tag for tag in row[3:]]
                self.entities.append(Entity(entity_type, start, end, tags=tags))

    def premature_p_count(self):
        '''
        Returns: number of P waves tagged premature

        Counts the number of P waves tagged premature in the entity list
        '''
        return sum(entity.type == 'p' and 'premature' in entity.tags for entity in self.entities)
    
    def premature_qrs_count(self):
        '''
        Returns: number of QRS waves tagged premature

        Counts the number of QRS waves tagged premature in the entity list
        '''
        return sum(entity.type == 'qrs' and 'premature' in entity.tags for entity in self.entities)
        return 
    
    def get_heart_rate(self):
        '''
        Returns: (minimum heart rate, timestamp), (maximum heart rate, timestamp), mean heart rate 

        Compute mean heart rate from entity list and returns it along with the maximum and minimum heart rate
        and when they happened. If there is less than 2 QRS complexes, the heart rate can't be computed and
        (None, None, None) is returned instead.
        '''
        qrs_count = 0
        rates = []
        previous_qrs_time = None

        # (min/max, timestamp)
        min_rate = float('inf'), 0
        max_rate = 0, 0
        
        for entity in self.entities:
            if entity.type == 'qrs':
                qrs_count += 1
                if previous_qrs_time is not None: 
                    rate = 60000 / (entity.start - previous_qrs_time)
                    rates.append(rate)
                    if rate < min_rate[0]:
                        min_rate = rate, entity.start
                    elif rate > max_rate[0]:
                        max_rate = rate, entity.start
                previous_qrs_time = entity.start
    
        if qrs_count < 2:
            return None, None, None
        else:
            return min_rate, max_rate, sum(rates) / (qrs_count - 1)


class Entity:
    '''
    Basic ECG entity class. An entity can be of the following types

    P wave, T wave, QRS complex, invalid
    '''
    def __init__(self, entity_type, start, end, tags=None):
        '''
        Arguments:
            entity_type: p, t, qrs, inv according to the type of the entity (see above)
            start: starting time of the entity in ms since the start of the recording
            end: ending time of the entity in ms since the start of the recording
            tags: list of tags related to the entity

        Initialize an entity
        '''
        self.type = entity_type.lower()
        self.start = int(start)
        self.end = int(end)
        self.tags = tags
