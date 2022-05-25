    
fetch('./json')
  .then((response) => {
    return response.json();
  })
  .then((myJson) => {
    
    const cover = document.getElementById('cover');
    const author = document.getElementById('author');
    const review = document.getElementById('review');
    const tagsAuthor = document.getElementById('tags-author');
    

    let len = (myJson.length);
    const random = Math.floor(Math.random()*len);

    cover.innerHTML = `
        <a href="${myJson[random].link}" target="_blank" >
            <img src="${myJson[random].image}"/>
        </a>`;
    author.innerHTML = `<h2>${myJson[random].author}</h2>`;
    review.innerHTML = `<p>${myJson[random].text}</p>`;
    // tagsAuthor.innerHTML = `<p>${myJson[random].tags_author}</p>`;
    
    const arrayTagsAuthor = (myJson[random].tags_author).split('/');        
    arrayTagsAuthor.forEach(function(tag) {
        tagsAuthor.innerHTML += `${tag} `;
    });



  });


