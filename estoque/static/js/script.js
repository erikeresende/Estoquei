document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search-input");
    const productList = document.getElementById("product-list");
    const viewAllButton = document.getElementById("view-all");

    // Função para atualizar a lista de produtos
    function updateProductList(url) {
        fetch(url, {
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(response => response.json())
        .then(data => {
            // Atualiza o conteúdo da lista de produtos com o HTML recebido
            productList.innerHTML = data.html;

            // Ajusta os botões de descrição após atualizar a lista
            adjustDescriptionButtons();
        })
        .catch(error => console.error("Erro na busca AJAX:", error));
    }

    // Evento de envio do formulário de busca
    if (searchInput) {
        searchInput.addEventListener("input", function() {
            const query = searchInput.value;
            updateProductList(`?query=${encodeURIComponent(query)}`);
        });
    }

    // Evento de clique no botão "Ver Todos"
    if (viewAllButton) {
        viewAllButton.addEventListener("click", function(event) {
            event.preventDefault(); // Impede a ação padrão
            updateProductList(`?query=`); // Exibe todos os produtos
        });
    }

    // Ajusta a exibição dos botões "Ver Mais" e "Ver Menos"
    function adjustDescriptionButtons() {
        const descriptionTexts = document.querySelectorAll('.description-text');
        
        descriptionTexts.forEach(text => {
            if (text.scrollHeight > text.clientHeight) {
                const button = text.nextElementSibling; // Obtém o botão associado

                if (button && button.classList.contains('btn-link')) {
                    button.style.display = 'inline-block'; // Exibe o botão
                    button.addEventListener('click', function() {
                        text.classList.toggle('expanded');
                        button.textContent = text.classList.contains('expanded') ? 'Ver Menos' : 'Ver Mais';
                    });
                }
            }
        });
    }

    // Ajusta os botões de descrição ao carregar a página
    adjustDescriptionButtons();
});

// Função para alternar a descrição (adicionada no final para maior clareza)
// script.js
// Função para alternar a descrição
function toggleDescription(id) {
    const descElement = document.getElementById(`desc-${id}`);
    const button = document.querySelector(`button[data-id="${id}"]`);
    
    if (descElement && button) {
        if (descElement.classList.contains('expanded')) {
            descElement.classList.remove('expanded');
            descElement.style.maxHeight = "90px"; // Recolhe a descrição
            button.innerText = 'Ver Mais'; // Atualiza o texto do botão para "Ver Mais"
        } else {
            descElement.classList.add('expanded');
            descElement.style.maxHeight = "none"; // Expande a descrição
            button.innerText = 'Ver Menos'; // Atualiza o texto do botão para "Ver Menos"
        }
    } else {
        console.error('Elemento da descrição ou botão não encontrado.');
    }
}




