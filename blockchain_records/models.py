from django.db import models
from hashlib import sha256
from student_records.models import StudentRecord

# Create your models here.

class Block(models.Model):
    previous_block = models.ForeignKey('Block',null=True,on_delete=models.DO_NOTHING,related_name='previous')
    data = models.ForeignKey(StudentRecord,on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    nonce = models.IntegerField()

    def block_hash(self):
        data = ','.join([str(self.timestamp), str(self.data), self.previous_block.block_hash()])
        data += '0' * self.nonce
        return sha256(bytes(data,encoding='utf-8')).hexdigest()



        


    

    

    
