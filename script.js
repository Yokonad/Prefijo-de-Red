function calcular() {
    const prefijo = parseInt(document.getElementById('cidr').value);
    const resultadosDiv = document.getElementById('resultados');
    resultadosDiv.innerHTML = '';

    if (isNaN(prefijo) || prefijo <= 0 || prefijo > 32) {
        resultadosDiv.innerHTML = '<p style="color:white;">Por favor ingresa un prefijo válido entre 1 y 32.</p>';
        return;
    }

    const totalIps = Math.pow(2, 32 - prefijo);
    const utilizables = totalIps > 2 ? totalIps - 2 : 0;
    const reservadas = totalIps - utilizables;
    const mascaraDecimal = convertirMascaraDecimal(prefijo);
    const mascaraBinaria = convertirMascaraBinaria(prefijo);

    const resultadosHtml = `
        <p><strong>Prefijo CIDR:</strong> /${prefijo}</p>
        <p><strong>Máscara (Decimal):</strong> ${mascaraDecimal}</p>
        <p><strong>Máscara (Binario):</strong> ${mascaraBinaria}</p>
        <p><strong>Total de IPs:</strong> ${totalIps}</p>
        <p><strong>IPs Utilizables:</strong> ${utilizables}</p>
        <p><strong>Reservadas (Red + Broadcast):</strong> ${reservadas}</p>
    `;

    resultadosDiv.innerHTML = resultadosHtml;
}

function convertirMascaraDecimal(prefijo) {
    const bitsEncendidos = Array(prefijo).fill('1');
    const bitsApagados = Array(32 - prefijo).fill('0');
    const mascaraBinaria = bitsEncendidos.concat(bitsApagados).join('');
    const octetos = mascaraBinaria.match(/.{1,8}/g).map(bin => parseInt(bin, 2));
    return octetos.join('.');
}

function convertirMascaraBinaria(prefijo) {
    const bitsEncendidos = Array(prefijo).fill('1');
    const bitsApagados = Array(32 - prefijo).fill('0');
    const mascaraBinaria = bitsEncendidos.concat(bitsApagados).join('');
    return mascaraBinaria.match(/.{1,8}/g).join('.');
}
