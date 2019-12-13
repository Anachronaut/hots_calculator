let ally_draft = document.querySelector('#id_ally_draft_pick')
let opp_draft = document.querySelector('#id_opp_draft_pick')
ally_draft.addEventListener('change', selectChoice)
opp_draft.addEventListener('change', selectChoice)

let ally_ban = document.querySelector('#id_ally_ban')
let opp_ban = document.querySelector('#id_opp_ban')
ally_ban.addEventListener('change', selectChoice)
opp_ban.addEventListener('change', selectChoice)

loadForms()


function loadForms() {
    fetch(loadSelectUrl)
        .then( response => 
            response.json() )
        .then( data => {
            loadSelect(data)
        })
        .catch( err => console.error(err) )
}


function selectChoice(event) {
    let select = event.srcElement
    let update_text = select.dataset.update_text
    console.log(select, select.dataset)
    let data = { update_text: update_text}
    userAction(data)
}

function userAction(data) {
    let token = Cookies.get('csrftoken')
    console.log(data)
    fetch(updateURL, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        }
    })
    .then( response => response.json() )
        .then ( data => {
            loadSelect(data)
        })
        .catch( err => console.error(err) )
}

function loadSelect(data){
    console.log('Data loaded from server: ', data)
}