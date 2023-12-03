
var clearButton = document.getElementById("clear")
var resultsContainer = document.getElementById("searchResults");

clearButton.addEventListener('click', clear)

function clear() {
    let search = document.getElementById("searchInput");

    search.value = '';
    location.reload();

}

function search() {
    var searchTerm = document.getElementById("searchInput").value.toLowerCase();
    var results = [];

    var subdirectories = [
        "nao_etiquetado",
        "educacao",
        "homossexualidades",
        "conjuracao_baiana",
        "mulheres_em_conflitos",
        "fim_da_guerra",
        "comida_e_modos_de_comer",
        "redemocratizacao",
        "feminismos",
        "antonio_vieira",
        "canudos",
        "drogas",
        "getulio_vargas",
        "trafico_de_escravos",
        "leopoldina",
        "primeira_guerra_mundial",
        "contestado",
        "descobrimentos",
        "o_golpe_de_1964",
        "o_golpe_de_1965",
        "o_golpe_de_1966",
        "o_golpe_de_1967",
        "revolucao_de_1932",
        "revolucao_de_1933",
        "revolucao_de_1934",
        "jesuitas",
        "princesa_isabel",
        "africa_brasil",
        "astrologia",
        "d_pedro_i",
        "italianos_do_brasil",
        "arqueologia",
        "batalhas",
        "sociedades_secretas",
        "fora_da_lei",
        "o_negocio_da_inconfidencia",
        "brasil_e_estados_unidos",
        "amantes",
        "profecias",
        "integralismo",
        "animais_de_estimacao",
        "atentados_politicos",
        "judeus",
        "cafe",
        "feiticaria",
        "napoleao",
        "escravidao",
        "republica",
        "franca",
        "independencia",
        "euclides_da_cunha",
        "arabes_no_brasil"
    ];
    function searchInDirectory(directory) {
        return fetch(`./pages/${directory}/index.html`)
            .then(response => response.text())
            .then(content => {
                var parser = new DOMParser();
                var htmlDoc = parser.parseFromString(content, 'text/html');
                var links = htmlDoc.querySelectorAll('a[href$=".html"]');
                var promises = [];

                links.forEach(function (link) {
                    var filePath = link.getAttribute("href");

                    var resultPath = `./pages/${directory}/${filePath}`;

                    var fetchPromise = fetch(resultPath)
                        .then(response => response.text())
                        .then(fileContent => {
                            if (fileContent.toLowerCase().includes(searchTerm)) {
                                results.push({ title: link.textContent, link: resultPath });
                            }
                        })
                        .catch(error => {
                            console.error("erro ao buscar arquivo " + resultPath, error);
                        });

                    promises.push(fetchPromise);
                });

                return Promise.all(promises);
            })
            .catch(error => {
                console.error("erro ao buscar diretório " + directory, error);
            });
    }

    results = [];

    Promise.all(subdirectories.map(searchInDirectory))
        .then(() => {
            displayResults(results);
        });
}

function displayResults(results) {

    resultsContainer.innerHTML = "";

    if (results.length === 0) {
        resultsContainer.innerHTML = "nenhum resultado encontrado.";
    } else {
        results.forEach(function (result) {
            var resultLink = document.createElement('a');
            resultLink.textContent = result.title;

            var resultPath = result.link;
            resultLink.href = resultPath;
            resultLink.target = "_blank";
            resultsContainer.appendChild(resultLink);
        });
    }
}