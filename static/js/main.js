function populateLinks(elementSelector, links) {
    const downloadLinksEl = $(elementSelector)
    downloadLinksEl.html('')
    for ( const [filename, url] of Object.entries(links) ) {
        const liEl = document.createElement('li')
        const linkEl = document.createElement('a')
        liEl.appendChild(linkEl)
        downloadLinksEl.append(liEl)

        linkEl.href = url
        linkEl.innerText = filename
    }
}

function requestToPull() {
    $.ajax({
        url: "/pull_links",
        success: function( result ) {
        //   populateLinks("#upload-links", result.uploads)
          populateLinks("#download-links", result)
        }
      });
}

setInterval(() => requestToPull(), 10000)
requestToPull()
