function populateLinks(elementSelector, links) {
    const downloadLinksEl = $(elementSelector)
    downloadLinksEl.html('')
    for ( const [filename, data] of Object.entries(links) ) {
        const liEl = document.createElement('li')
        downloadLinksEl.append(liEl)
        if ( data.expected ) {
          const spinnerEl = document.createElement('div')
          spinnerEl.innerHTML =
            `${filename} <img src='/static/images/spinner.gif' style='width: 1.5em; height: 1.5em;'></img>`
          liEl.appendChild(spinnerEl)
        } else {
          const linkEl = document.createElement('a')
          liEl.appendChild(linkEl)
          linkEl.href = data.url
          linkEl.innerText = filename
        }
    }
}

function requestToPull() {
    $.ajax({
        url: "/pull_links",
        success: function( result ) {
          populateLinks("#download-links", result)
        }
      });
}

setInterval(() => requestToPull(), 10000)
requestToPull()
