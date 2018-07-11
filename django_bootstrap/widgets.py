from django.forms.widgets import Input, RadioSelect, TextInput
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


class OptionsRadioInput(RadioSelect):
    def __unicode__(self):
        if 'id' in self.attrs:
            label_for = ' for="%s_%s"' % (self.attrs['id'], self.index)
        else:
            label_for = ''
        choice_label = conditional_escape(force_unicode(self.choice_label))
        return mark_safe('<label%s>%s <span>%s</span></label>' %
                         (label_for, self.tag(), choice_label))


class AppendedText(TextInput):
    def render(self, name, value, attrs=None):
        append_text = self.attrs.get('text', '')
        return mark_safe('%s<span class="add-on">%s</span>' % (
            super(AppendedText, self).render(name, value, attrs),
            append_text))


class PrependedText(TextInput):
    def render(self, name, value, attrs=None):
        prepend_text = self.attrs.get('text', '')
        return mark_safe(
            '<span class="add-on">%s</span>%s' % (prepend_text, super(
                PrependedText, self).render(name, value, attrs)))


class AppendPrependText(TextInput):
    def render(self, name, value, attrs=None):
        append_text, prepend_text = self.attrs.get(
            'append_text', ''), self.attrs.get('prepend_text', '')
        return mark_safe(
            '<span class="add-on">%s</span>%s<span class="add-on">%s</span>' % (
            prepend_text, super(AppendPrependText, self).render(
                name, value, attrs), append_text))


class EmailInput(Input):
    input_type = 'email'

    def render(self, name, value, attrs=None):
        append_text = self.attrs.get('text', '@')
        return mark_safe('%s<span class="add-on">%s</span>' % (super(
            EmailInput, self).render(name, value, attrs), append_text))
