from django.db import models
import uuid
from hashlib import sha256
from student_records.models import StudentRecord
import os


class Block(models.Model):
    previous_block = models.ForeignKey('Block', 
                                        null=True,
                                        blank=True,
                                        on_delete=models.DO_NOTHING,
                                        related_name='previous'
                                       )
    action = models.CharField(max_length=50)
    data = models.ForeignKey(StudentRecord, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    nonce = models.IntegerField()

    def block_hash(self):
        if self.previous_block == None:
            previous_hash = os.getenv("GEN_HASH")
        else: previous_hash = self.previous_block.block_hash()

        data = ','.join(
            [str(self.timestamp), 
             str(self.data), 
             previous_hash
            ]
        )
        data += '0' * self.nonce
        return sha256(bytes(data,encoding='utf-8')).hexdigest()

    def __str__(self):
        return self.block_hash()



        


    

    

    
