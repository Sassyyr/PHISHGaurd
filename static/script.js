async function scanURL(){

    const url = document.getElementById("urlInput").value

    const response = await fetch("/scan",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({url:url})
    })

    const data = await response.json()

    console.log(data)   // helps debugging

    if(data.error){
        document.getElementById("result").innerText = data.error
        return
    }

    document.getElementById("result").innerText = data.result
    document.getElementById("intel").innerText = data.intel
    document.getElementById("action").innerText = data.action

}