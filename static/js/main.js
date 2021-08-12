const toggleControl = (name) => {
    const elements = document.getElementsByClassName(name);
    
    for (let i = 0; i < elements.length; i++) {
        const element = elements[i];
        if (element.style.display == "none" || element.style.display == "") {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    }
    
}

const handleInput = (id) => {
    const slider = document.getElementById(id);
    const output = document.getElementById(id + "-field");
    output.innerHTML = slider.value;
}

const submitForm = (id) => {
    const form = document.getElementById(id);
    form.submit();
}
