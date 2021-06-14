
from django.db import models as md
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ManyToManyField
# Create your models here.

# for Accessories, easier to select supperlier
class Supplier(md.Model):
    brandName = md.CharField('Brand Name', max_length=20, null=True)

    def __str__(self) -> str:
        return self.brandName

class Accessories(md.Model):
    supplier = md.ForeignKey(Supplier, on_delete=md.CASCADE, blank=True, null=True)
    img = md.ImageField("Accessories photo", null=True, blank=True, upload_to="proImgForBrands")
    fullName = md.CharField('Full name', max_length=50, null=True)
    intro = md.TextField('Introduction', max_length=200, null=True)

    def __str__(self) -> str:
        return str(self.supplier) + ' ' + self.fullName


class Brands(md.Model):
    brand = md.CharField('Brand', max_length=50, null=True)
    title = md.CharField('Title', max_length=50, null=True)
    subTitle = md.CharField('Subtitle', max_length=50, null=True)
    slogan = md.CharField('Slogan', max_length=50, null=True)
    des = md.TextField('Brand description', max_length=500, null=True)
    brandImg = md.ImageField('brand image', null=True, blank=True, upload_to="iamges")

    def __str__(self) -> str:
        return self.brand

class TrailCamPro(md.Model):
    brand = md.ForeignKey(Brands, on_delete=md.CASCADE, blank=True, null=True)
    ab = md.CharField('Abbreviation', max_length=10, null=True)
    # for brand page
    proImg = md.ImageField('Photo of product', null=True, blank=True, upload_to="proImgForBrands") # also can be used in product page
    modelName = md.CharField('Model full name', max_length=50, null=True)
    des1 = md.CharField(max_length=10, null=True)
    des2 = md.CharField(max_length=10, null=True)
    des3 = md.CharField(max_length=10, null=True)

    # for the first section of product page
    briefIntro = md.CharField('brief introduciton', max_length=20, null=True)
    intro = md.TextField('Detailed introduction', max_length=800, null=True)
    proImgBack = md.ImageField("Back photo of product", null=True, blank=True, upload_to="proImgForBrands")
    proImgOpen = md.ImageField("Openned photo of product", null=True, blank=True, upload_to="proImgForBrands")

    # for the specification
    imgRes = md.CharField('Imgae resolution', max_length=100, null=True)
    vedRes = md.CharField('Vedio resolution', max_length=100, null=True)
    vedLen = md.CharField('Vedio Length', max_length=50, null=True)
    hybridMode = md.CharField('Hybrid Mode', max_length=50, null=True)
    screen = md.CharField('Screen', max_length=50, null=True)
    detRan = md.CharField('Detection Range', max_length=50, null=True)
    illumination = md.CharField('Illumination', max_length=50, null=True)
    illRan = md.CharField('Illumination Range', max_length=50, null=True)
    triSpe = md.CharField('Trigger speed', max_length=50, null=True)
    SmartIR = md.CharField('Smart IR', max_length=50, null=True)
    imaCol = md.CharField('Image color', max_length=100, null=True)
    mulShoPerTri = md.CharField('Multi shop per trigger', max_length=50, null=True)
    mulShoRat = md.CharField('Multi shot rate', max_length=50, null=True)
    infoBar = md.CharField('Information bar', max_length=100, null=True)
    deley = md.CharField('Delay', max_length=50, null=True)
    opeTim = md.CharField('Operation time', max_length=50, null=True)
    shuSet = md.CharField('Shutter setting', max_length=50,null=True)
    isoSet = md.CharField('Iso setting', max_length=50, null=True)
    timLapSet = md.CharField('Time-Lapse setting', max_length=50, null=True)
    timLapInt = md.CharField('Time-Lapse interval', max_length=50, null=True)
    cardType = md.CharField('Memory card type', max_length=50, null=True)
    carCap = md.CharField('Memory card capacity', max_length=50, null=True)
    memCon = md.CharField('Memory card configuration', max_length=50, null=True)
    batLif = md.CharField('Battery life', max_length=50, null=True)
    batTypQua = md.CharField('Battery type and Quantity', max_length=50, null=True)
    opeTem = md.CharField('Operation temperature', max_length=50, null=True)
    focAdj = md.CharField('Customization focus range', max_length=50, null=True)
    demoVedioDay = md.URLField('Youtube link of demo vedio in daytime', null=True)
    demoVedioNight = md.URLField('Youtube link of demo vedio at night', null=True)
    acc = md.ManyToManyField(Accessories, blank=True)
    dayIframeTag = md.TextField(max_length=2000, null=True)
    nightIframeTag = md.TextField(max_length=2000, null=True)


    def __str__(self) -> str:
        return str(self.brand) + " " + self.ab

