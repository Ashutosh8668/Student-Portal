 const icon2=document.getElementById("icon2");
        icon2.onclick=function()
        {
            if(document.body.classList.contains("light-mode")){
            document.body.classList.remove("light-mode");
            document.body.classList.add("dracula-mode");
            localStorage.setItem("theme","dracula-mode");
            }
            else if(document.body.classList.contains("dark-mode")){
            document.body.classList.remove("dark-mode");
            document.body.classList.add("dracula-mode");
            localStorage.setItem("theme","dracula-mode");
            }
            else{
                document.body.classList.add("dracula-mode");
            localStorage.setItem("theme","dracula-mode");
            }
            document.getElementById("currenttheme").innerHTML = localStorage.theme;
        };
        document.body.classList.add(localStorage.getItem("theme"));
    document.getElementById("currenttheme").innerHTML = localStorage.theme;