document.addEventListener('DOMContentLoaded', function() {
            // Seleciona todos os elementos que abrem modais
            const modalTriggers = document.querySelectorAll('.modal-trigger');
            
            // Adiciona evento de clique a cada trigger
            modalTriggers.forEach(trigger => {
                trigger.addEventListener('click', function() {
                    const modalId = this.getAttribute('data-modal');
                    const modal = document.getElementById(modalId);
                    modal.style.display = "block";
                    // Impede a rolagem da página quando o modal está aberto
                    document.body.style.overflow = "hidden";
                });
            });
            
            // Seleciona todos os botões de fechar
            const closeButtons = document.querySelectorAll('.close');
            
            // Adiciona evento de clique a cada botão de fechar
            closeButtons.forEach(button => {
                button.addEventListener('click', function() {
                    this.closest('.modal').style.display = "none";
                    // Restaura a rolagem da página
                    document.body.style.overflow = "auto";
                });
            });
            
            // Fecha o modal quando clicar fora do conteúdo
            window.addEventListener('click', function(event) {
                if (event.target.classList.contains('modal')) {
                    event.target.style.display = "none";
                    // Restaura a rolagem da página
                    document.body.style.overflow = "auto";
                }
            });
            
            // Fecha o modal com a tecla ESC
            document.addEventListener('keydown', function(event) {
                if (event.key === "Escape") {
                    document.querySelectorAll('.modal').forEach(modal => {
                        modal.style.display = "none";
                    });
                    // Restaura a rolagem da página
                    document.body.style.overflow = "auto";
                }
            });
        });