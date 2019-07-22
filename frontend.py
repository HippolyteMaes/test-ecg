'''
Fronten module
'''

from ecgreader import ECGReader
from utils import add_ms_to_datetime, datetime_to_print


class CLI:
    '''
    Command Line Interface frontend
    '''

    @classmethod
    def run(cls, recording_time, path):
        '''
        Arguments:
            recording_time: datetime of the start of the record
            path: path of the record

        Run command line interface and prints it
        '''
        header = cls.get_header(recording_time)
        body = cls.get_body(recording_time, path)
        print(header)
        print(body)


    @classmethod
    def get_header(cls, recording_time):
        '''
        Arguments:
            recording_time: datetime of the start of the record

        Returns: Header to print
        '''
        return '\n'.join([
            '=======================================================',
            'Record started on the {} at {}'.format(*datetime_to_print(recording_time)),
            '======================================================='
        ])
    
    @classmethod
    def get_body(cls, recording_time, path):
        '''
        Arguments:
            recording_time: datetime of the start of the record
            path: path of the record

        Returns: Body to print containing all relevant informations
        '''
        reader = ECGReader(path)
        premature_p = reader.premature_p_count()
        premature_qrs = reader.premature_qrs_count()
        min_heart_rate, max_heart_rate, mean_heart_rate = reader.get_heart_rate()

        prematures = '\n'.join([
            'Number of premature P waves : {}'.format(premature_p),
            'Number of premature QRS complexes : {}'.format(premature_qrs)
        ])

        if mean_heart_rate is not None:
            heart = '\n'.join([
                'Mean heart rate: {:.3f} bpm'.format(mean_heart_rate),
                'Minimum heart rate: {:.3f} bpm, happened on the {} at {}'.format(
                    min_heart_rate[0],
                    *datetime_to_print(add_ms_to_datetime(recording_time, min_heart_rate[1])),
                ),
                'Maximum heart rate: {:.3f} bpm, happened on the {} at {}'.format(
                    max_heart_rate[0],
                    *datetime_to_print(add_ms_to_datetime(recording_time, max_heart_rate[1]))
                )
            ])
        else:
            heart = "Can't compute heart rate as the recording does not contain enought QRS complexes"

        return prematures + '\n\n' + heart
