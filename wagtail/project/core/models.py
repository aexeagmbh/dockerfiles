from django.db import models
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('description',)

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    block1_title = models.CharField(max_length=512, blank=True)
    block1_subtitle = RichTextField(blank=True)
    block1_content1 = RichTextField(blank=True)
    block1_content2 = RichTextField(blank=True)
    block1_content3 = RichTextField(blank=True)
    block1_content4 = RichTextField(blank=True)
    block1_footer = RichTextField(blank=True)

    block2_title = models.CharField(max_length=512, blank=True)
    block2_content1 = RichTextField(blank=True)
    block2_content2 = RichTextField(blank=True)
    block2_content3 = RichTextField(blank=True)
    block2_content4 = RichTextField(blank=True)

    block3_content1 = RichTextField(blank=True)
    block3_thumbnail1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    block3_content2 = RichTextField(blank=True)
    block3_thumbnail2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    block3_content3 = RichTextField(blank=True)
    block3_thumbnail3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    block3_content4 = RichTextField(blank=True)
    block3_thumbnail4 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    block_signup_title = models.CharField(max_length=512, blank=True)
    block_signup_button_label = models.CharField(max_length=128, blank=True)

    block4_content1 = RichTextField(blank=True)
    block4_content2 = RichTextField(blank=True)

    class Meta:
        description = "The top level homepage for your site"
        verbose_name = "Homepage"


HOME_BLOCK1_FIELDS = [
    FieldPanel('block1_title'),
    FieldPanel('block1_subtitle'),
    FieldPanel('block1_content1'),
    FieldPanel('block1_content2'),
    FieldPanel('block1_content3'),
    FieldPanel('block1_content4'),
    FieldPanel('block1_footer'),
]

HOME_BLOCK2_FIELDS = [
    FieldPanel('block2_title'),
    FieldPanel('block2_content1'),
    FieldPanel('block2_content2'),
    FieldPanel('block2_content3'),
    FieldPanel('block2_content4'),
]

HOME_BLOCK3_FIELDS = [
    FieldPanel('block3_content1'),
    FieldPanel('block3_thumbnail1'),
    FieldPanel('block3_content2'),
    FieldPanel('block3_thumbnail2'),
    FieldPanel('block3_content3'),
    FieldPanel('block3_thumbnail3'),
    FieldPanel('block3_content4'),
    FieldPanel('block3_thumbnail4'),
]

HOME_BLOCK_SIGNUP_FIELDS = [
    FieldPanel('block_signup_title'),
    FieldPanel('block_signup_button_label'),
]

HOME_BLOCK4_FIELDS = [
    FieldPanel('block4_content1'),
    FieldPanel('block4_content2'),
]

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    MultiFieldPanel(HOME_BLOCK1_FIELDS, heading='Block 1 elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK2_FIELDS, heading='Block 2 elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK3_FIELDS, heading='Block 3 elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK_SIGNUP_FIELDS, heading='Block Sign Up elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK4_FIELDS, heading='Block 4 elements', classname="collapsible collapsed"),
]


class OneColumnMainPage(Page):
    subtitle = RichTextField()
    row1_teaser1 = RichTextField(blank=True)
    row1_teaser2 = RichTextField(blank=True)
    row1_teaser3 = RichTextField(blank=True)
    main_content = RichTextField()
    conversion_title = models.CharField(max_length=256, blank=True)
    conversion_url = models.URLField(blank=True)
    conversion_button_label = models.CharField(max_length=256, blank=True)
    foot_row = RichTextField(blank=True)


OneColumnMainPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('subtitle', classname="full"),
    FieldPanel('row1_teaser1', classname="full"),
    FieldPanel('row1_teaser2', classname="full"),
    FieldPanel('row1_teaser3', classname="full"),
    FieldPanel('main_content', classname="full"),
    FieldPanel('conversion_title', classname="full"),
    FieldPanel('conversion_url', classname="full"),
    FieldPanel('conversion_button_label', classname="full"),
    FieldPanel('foot_row', classname="full"),
]
