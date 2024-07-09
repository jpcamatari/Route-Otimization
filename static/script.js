function addDestination() {
    const container = document.getElementById('destinos-container');
    const newDestination = document.createElement('div');
    newDestination.className = 'form-group destino-group';
    newDestination.innerHTML = `
        <label for="destino">Destino</label>
        <div class="input-group">
            <input type="text" class="form-control" name="destino" required>
            <div class="input-group-append">
                <button type="button" class="btn btn-outline-danger btn-sm" onclick="removeDestination(this)">
                    <i class="fas fa-minus"></i>
                </button>
                <button type="button" class="btn btn-outline-primary btn-sm ml-1" onclick="addDestination()">
                    <i class="fas fa-plus"></i>
                </button>
            </div>
        </div>
    `;
    container.appendChild(newDestination);
    updateButtons();
}

function removeDestination(button) {
    const container = document.getElementById('destinos-container');
    const destinoGroup = button.closest('.destino-group');
    if (container.childElementCount > 2) {
        container.removeChild(destinoGroup);
    }
    updateButtons();
}

function updateButtons() {
    const container = document.getElementById('destinos-container');
    const destinationGroups = container.getElementsByClassName('destino-group');
    for (let i = 0; i < destinationGroups.length; i++) {
        const group = destinationGroups[i];
        const addButton = group.querySelector('.btn-outline-primary');
        const removeButton = group.querySelector('.btn-outline-danger');
        
        if (i === destinationGroups.length - 1) {
            addButton.classList.remove('d-none');
        } else {
            addButton.classList.add('d-none');
        }

        if (destinationGroups.length > 2) {
            removeButton.classList.remove('d-none');
        } else {
            removeButton.classList.add('d-none');
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateButtons();
});
