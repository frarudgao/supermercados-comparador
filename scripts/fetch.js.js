
fetch('productos.json')
  .then(res => res.json())
  .then(data => {
    const tbody = document.querySelector('#tabla-precios tbody');
    data.forEach(prod => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${prod.nombre}</td>
        <td>${prod.mercadona} €</td>
        <td>${prod.carrefour} €</td>
      `;
      tbody.appendChild(row);
    });
  });
