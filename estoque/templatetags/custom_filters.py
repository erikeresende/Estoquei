from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    """Adiciona uma classe CSS ao campo de formulário.

    Args:
        field: O campo do formulário a ser estilizado.
        css: A classe CSS a ser adicionada ao campo.

    Returns:
        O campo do formulário com a classe CSS adicionada.
    """
    if hasattr(field, 'as_widget'):
        # Adiciona a classe CSS ao campo do formulário
        return field.as_widget(attrs={"class": css})
    return field
