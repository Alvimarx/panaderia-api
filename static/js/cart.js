// ==============================
// Utilidades
// ==============================

function getCart() {
    const raw = localStorage.getItem("pan_cart");
    return raw ? JSON.parse(raw) : [];
  }
  
  function saveCart(cart) {
    localStorage.setItem("pan_cart", JSON.stringify(cart));
    updateCartCount();
  }
  
  function updateCartCount() {
    const cart = getCart();
    const count = cart.reduce((sum, p) => sum + p.cantidad, 0);
    const countElement = document.getElementById("cart-count");
    if (countElement) countElement.textContent = count;
  }
  
  // ==============================
  // Agregar al carrito
  // ==============================
  
  function addToCart(id, nombre, precio) {
    let cart = getCart();
    const idx = cart.findIndex(p => p.id === id);
  
    if (idx >= 0) {
      cart[idx].cantidad += 1;
    } else {
      cart.push({ id, nombre, precio, cantidad: 1 });
    }
  
    saveCart(cart);
    alert(`${nombre} agregado al carrito`);
  }
  
  // ==============================
  // Render en checkout
  // ==============================
  
  function renderCheckout() {
    const resumen = document.getElementById("resumen-carrito");
    const form = document.getElementById("checkout-form");
    const cart = getCart();
  
    if (!resumen || !form) return;
  
    if (cart.length === 0) {
      resumen.innerHTML = "<p>El carrito está vacío.</p>";
      form.style.display = "none";
      return;
    }
  
    let html = "<ul>";
    let total = 0;
    for (const item of cart) {
      total += item.precio * item.cantidad;
      html += `<li>${item.nombre} x${item.cantidad} – $${item.precio * item.cantidad}</li>`;
    }
    html += `</ul><p><strong>Total: $${total}</strong></p>`;
    resumen.innerHTML = html;
  
    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      const cliente = document.getElementById("cliente").value;
  
      const payload = {
        cliente,
        productos: cart.map(p => ({
          producto_id: p.id,
          cantidad: p.cantidad
        }))
      };
  
      try {
        const res = await fetch("/api/pedido", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });
  
        if (!res.ok) throw new Error("Error en la orden");
        const data = await res.json();
        alert(`Pedido confirmado (#${data.id})`);
        localStorage.removeItem("pan_cart");
        window.location.href = "/";
      } catch (err) {
        alert("Error al enviar el pedido");
        console.error(err);
      }
    });
  }
  
  // ==============================
  // Al cargar la página
  // ==============================
  
  document.addEventListener("DOMContentLoaded", () => {
    updateCartCount();
  
    // Si existe el form, asumimos que estamos en checkout
    if (document.getElementById("checkout-form")) {
      renderCheckout();
    }
  });
  