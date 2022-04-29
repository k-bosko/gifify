function populateLinks(elementSelector, links) {
    const uploadLinksEl = $(elementSelector)
    uploadLinksEl.html('')
    for ( const link of links ) {
        const linkEl = document.createElement('a')
        linkEl.href = link.url
        linkEl.innerText = link.name

        uploadLinksEl.append(linkEl)
    }
}

function requestToPull() {
    $.ajax({
        url: "/pull_links",
        success: function( result ) {
          populateLinks("#upload-links", result.uploads)
          populateLinks("#download-links", result.downloads)
        }
      });
}

setInterval(() => requestToPull(), 10000)
requestToPull()
