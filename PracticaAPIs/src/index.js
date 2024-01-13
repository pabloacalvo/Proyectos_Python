let parameters = []
function removeElement(event, position) {
    event.target.parentElement.remove()
    delete parameters[position]
}


const addJsonElement = json => {
    parameters.push(json)
    return parameters.length - 1
}

(function load(){
    const $form = document.getElementById("frmUsers")
    const $divElements = document.getElementById("divElements")
    const $btnSave = document.getElementById("btnSave")
    const $btnAdd = document.getElementById("btnAdd")

    const templateElement = (data, position) => {
        return (`
            <button class="delete" onclick="removeElement(event, ${position})"></button>
            <strong>User - </strong> ${data}
        `)
    }
    $btnAdd.addEventListener("click", (event) => {
        if($form.nombre.value !== "" && $form.apellido.value !== ""){
            let index = addJsonElement({
                nombre: $form.nombre.value,
                apellido: $form.apellido.value
            })
            const $div = document.createElement("div")
            $div.classList.add("notification", "is-link", "is-light", "py-2", "my-1")
            $div.innerHTML = templateElement(`${$form.nombre.value} ${$form.apellido.value}`, index)

            $divElements.insertBefore($div, $divElements.firstChild)

            $form.reset()
        }else{
            alert("Complete los campos")
        }
    })

    $btnSave.addEventListener("click", async (event) =>{
        parameters = parameters.filter(el => el != null)
        const url = "https://localhost:7100/socios/crearSocio"
        const response = await fetchData(url,"POST")
        console.log(response)
        const $jsonDiv = document.getElementById("jsonDiv")
        $jsonDiv.innerHTML = `JSON: ${JSON.stringify()}`
        $divElements.innerHTML = ""
        parameters = []
    })
})()
const fetchData = async (url, method, data)=>{
    jsonFetch = {
        method : method,
        cache : 'no-cache',
        headers : {'Content-Type': 'application/json'
        },
        body : JSON.stringify(data)
    }
    //console.log(jsonFetch)
    const response = await fetch(url,jsonFetch)
    if(response.ok) {
        return await response.json()
    }

}