from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    content_url = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date publication')

    def __str__(self) :
        return self.post_title +' ('+ self.pub_date.strftime("%d/%m/%Y")+')'
    
class Tag(models.Model):
    tag_title = models.CharField(max_length=50)
    
    def __str__(self) :
        return self.tag_title

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self) :
        return self.post.post_title + ' - ' + self.tag.tag_title
