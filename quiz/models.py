from django.db import models

class Test(models.Model):
  
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="제목")
    description = models.TextField(null=True, blank=True, verbose_name="설명")
    thumbnail = models.ImageField(null=True, blank=True, upload_to='thumbnail/', verbose_name="썸네일")
    engagement = models.IntegerField(default=0, verbose_name="참여수")
    likes = models.IntegerField(default=0, verbose_name="좋아요")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    
    class Meta:
        db_table = "tests"
        verbose_name = "테스트"
        verbose_name_plural = "01. 테스트"
        
    def __str__(self):
        return f'{self.title} - {self.description}'
       
        
class Question(models.Model):

    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, blank=True, related_name='question', verbose_name="테스트")
    content = models.TextField(null=False, blank=False, verbose_name="내용")
    image = models.ImageField(null=True, blank=True, upload_to='question/', verbose_name="이미지")
    index = models.IntegerField(default=0, verbose_name="인덱스")
    seconds = models.IntegerField(default=20, verbose_name="소요시간(초)")
    score = models.IntegerField(null=False, blank=False, default=1, verbose_name="점수")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    
    
    class Meta:
        db_table = "questions"
        verbose_name = "질문"
        verbose_name_plural = "02. 질문"
        ordering = ['index']

    def __str__(self):
        return f'Q{self.index}. {self.content}'
    
    
class Selection(models.Model):

    content = models.TextField(null=True, blank=True, verbose_name="내용")
    image = models.ImageField(null=True, blank=True, upload_to='selection/', verbose_name="이미지")
    is_correct = models.BooleanField(default=False, verbose_name="정답")
    index = models.IntegerField(default=0, verbose_name="인덱스")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='selection', verbose_name="질문")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    
    
    class Meta:
        db_table = "selections"
        verbose_name = "선택지"
        verbose_name_plural = "03. 선택지"
        ordering = ['content']
    
    def __str__(self):
        return f'{self.index}. {self.content}'