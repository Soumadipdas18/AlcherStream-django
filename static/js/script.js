const getdata = async(search) => {
    var response = await fetch(`https://api.themoviedb.org/3/search/movie?api_key=59464d534e81b292572cc80e723e531e&query=${search}&language=en-US`);
    if (response.status !== 200) {
        throw new error("Cannot fetch");
    }
    var data = await response.json();
    return data;
};

function searchquery(event) {
    event.preventDefault();
    var str = document.getElementById('inputMovie').value;
    str = str.trim().replace(/ /g, "+");
    if (str != '') {
        document.getElementById('blockbuster-1').innerHTML = "SEARCH RESULTS"
            // document.getElementById('blockbuster-2').style.display = "none";
    } else {
        document.getElementById('blockbuster-1').innerHTML = "BLOCKBUSTER HITS"
            // document.getElementById('blockbuster-2').style.display = "block";
    }
    getdata(str).then((value) => {
        const resultarray = value.results;
        var i = 1;
        resultarray.forEach(res => {
            if (res.poster_path !== null) {
                document.getElementById(`title-${i}`).innerHTML = res.title;
                document.getElementById(`desc-${i}`).innerHTML = res.overview;
                document.getElementById(`img-${i}`).src = `https://image.tmdb.org/t/p/w500/${res.poster_path}`

                i += 1;
            }
        });

    }).catch((err) => {
        console.log(`Failed ${e.message}`);
    });
}

function change(i) {
    console.log(document.getElementById(`title-${i}`).innerHTML);
    console.log(document.getElementById(`desc-${i}`).innerHTML);
    console.log(document.getElementById(`img-${i}`).src);

    $.ajax({
        url: 'favorites/',
        data: {
            'name': document.getElementById(`title-${i}`).innerHTML,
            'desc': document.getElementById(`desc-${i}`).innerHTML,
            'imgsrc': document.getElementById(`img-${i}`).src
        },
        success: function() {
            alert('Added to favorites');
        },
        error: function() {
            alert('Already there in favorites. How many times will you add?');
        }
    });
}

function review(i) {
    console.log(document.getElementById(`title-${i}`).innerHTML);
    console.log(document.getElementById(`desc-${i}`).innerHTML);
    console.log(document.getElementById(`img-${i}`).src);

    $.ajax({
        url: 'reviews/',
        data: {
            'name': document.getElementById(`title-${i}`).innerHTML,
            'desc': document.getElementById(`desc-${i}`).innerHTML,
            'imgsrc': document.getElementById(`img-${i}`).src
        },
        success: function() {
            var a = document.getElementById(`img-${i}`).src.split("/");
            var path = a[a.length - 1];
            var a1 = path.split('.')
            path = a1[0];
            window.location.href = `/reviews/all/${path}`;
        }
    });
}

function deletefavorite(i) {
    console.log(document.getElementById(`title-${i}`).innerHTML);
    console.log(document.getElementById(`desc-${i}`).innerHTML);
    console.log(document.getElementById(`img-${i}`).src);

    $.ajax({
        url: '../delete/',
        data: {
            'name': document.getElementById(`title-${i}`).innerHTML,
            'desc': document.getElementById(`desc-${i}`).innerHTML,
            'imgsrc': document.getElementById(`img-${i}`).src
        },
        success: function() {
            location.reload();
        }
    });
}


document.getElementById('inputMovie').addEventListener('input', searchquery);

window.addEventListener('scroll', () => {
    if (scrollY > document.querySelector(".navbar").offsetHeight * 6) {
        document.querySelector(".navbar").style.background = "#333";
    } else if (scrollY < document.querySelector(".navbar").offsetHeight * 6) {
        document.querySelector(".navbar").style.background = "transparent";
    }
});