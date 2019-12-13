let ally_draft = document.querySelector('#id_ally_draft_pick')
let opp_draft = document.querySelector('#id_opp_draft_pick')
let ally_ban = document.querySelector('#id_ally_ban')
let opp_ban = document.querySelector('#id_opp_ban')

ally_draft.addEventListener('change', draftChoice)
opp_draft.addEventListener('change', draftChoice)
ally_ban.addEventListener('change', banChoice)
opp_ban.addEventListener('change', banChoice)


function draftChoice() {
    let token = Cookies.get('csrftoken')  

}

function banChoice() {
    let token = Cookies.get('csrftoken')  

}