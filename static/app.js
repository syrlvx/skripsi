function toggleSidebar(){
    document.getElementById("sidebar").classList.toggle("open");
}

function showFileName(input){
    const zone = input.closest(".dropzone");
    const target = zone.querySelector(".file-name");
    if(input.files && input.files.length){
        target.textContent = "✓ " + input.files[0].name;
    }else{
        target.textContent = "";
    }
}

function updateSelection(){
    const cards = document.querySelectorAll(".level-card");
    const selected = [];

    cards.forEach(card => {
        const input = card.querySelector('input[type="checkbox"]');
        const isSelected = input.checked;

        card.classList.toggle("selected", isSelected);
        card.setAttribute("aria-pressed", isSelected ? "true" : "false");

        if(isSelected) selected.push(input.value);
    });

    const target = document.getElementById("selectedJenjang");
    if(target){
        target.innerHTML = selected.length
            ? selected.map(x => `<b>${x}</b>`).join("")
            : "<em>Belum ada jenjang yang dipilih</em>";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    /*
     * PENTING:
     * Card sekarang adalah div, bukan label.
     * Jadi browser tidak melakukan toggle checkbox otomatis.
     * JS menjadi satu-satunya pengendali pilihan.
     */
    document.querySelectorAll(".level-card").forEach(card => {
        const input = card.querySelector('input[type="checkbox"]');

        const toggleCard = () => {
            input.checked = !input.checked;
            updateSelection();
        };

        card.addEventListener("click", toggleCard);

        card.addEventListener("keydown", (e) => {
            if(e.key === "Enter" || e.key === " "){
                e.preventDefault();
                toggleCard();
            }
        });
    });

    updateSelection();

    const sidebar = document.getElementById("sidebar");
    if(sidebar){
        document.querySelectorAll(".nav-item").forEach(link => {
            link.addEventListener("click", () => {
                if(window.innerWidth <= 760) sidebar.classList.remove("open");
            });
        });
    }

    const form = document.getElementById("jenjangForm");
    if(form){
        form.addEventListener("submit", (e) => {
            const selected = form.querySelectorAll('input[name="jenjang"]:checked');
            if(selected.length === 0){
                e.preventDefault();
                alert("Silakan pilih minimal satu jenjang pendidikan terlebih dahulu.");
            }
        });
    }
});
