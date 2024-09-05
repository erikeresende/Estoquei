document.addEventListener('DOMContentLoaded', function() {
    // Certifique-se de que todos os elementos existem antes de adicionar event listeners
    const viewAllButton = document.getElementById('view-all');

    // Ajusta a exibição dos botões "Ver Mais" e "Ver Menos"
    function adjustDescriptionButtons() {
        const descriptionTexts = document.querySelectorAll('.description-text');
        
        descriptionTexts.forEach(text => {
            if (text.scrollHeight > text.clientHeight) {
                const button = document.createElement('button');
                button.classList.add('btn-link');
                button.textContent = 'Ver mais';
                button.addEventListener('click', function() {
                    text.classList.toggle('expanded');
                    button.textContent = text.classList.contains('expanded') ? 'Ver menos' : 'Ver mais';
                });
                text.parentNode.appendChild(button);
            }
        });
    }

    // Ajusta os botões de descrição ao carregar a página
    adjustDescriptionButtons();

    // Atualiza a lista de produtos ao clicar no botão "Ver Todos"
    if (viewAllButton) {
        viewAllButton.addEventListener('click', function() {
            // Adicione a lógica para exibir todos os produtos aqui, se necessário
        });
    }
});

// script.js
function toggleDescription(id) {
    const descElement = document.getElementById(`desc-${id}`);
    if (descElement.classList.contains('expanded')) {
        descElement.classList.remove('expanded');
        descElement.querySelector('.btn-link').innerText = 'Ver Mais';
    } else {
        descElement.classList.add('expanded');
        descElement.querySelector('.btn-link').innerText = 'Ver Menos';
    }
}
