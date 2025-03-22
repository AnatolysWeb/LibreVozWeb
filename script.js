document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("post-form")?.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const contenido = document.getElementById("content").value;
        const autor = "Anónimo";  // En el futuro, podrías obtener el alias del usuario autenticado

        const response = await fetch("http://127.0.0.1:5000/posts", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ autor, contenido })
        });

        if (response.ok) {
            alert("Publicación enviada");
        }
    });
});

