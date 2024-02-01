var enabledark=false;
    const icon=document.getElementById("icon");
        icon.onclick=function()
        {
            if(document.body.classList.contains("light-mode")){
            document.body.classList.remove("light-mode");
            document.body.classList.add("dark-mode");
            localStorage.setItem("theme","dark-mode");
            enabledark=true;
            }
            else if(document.body.classList.contains("dracula-mode")){
             document.body.classList.remove("dracula-mode");
            document.body.classList.add("dark-mode");
            localStorage.setItem("theme","dark-mode");
            enabledark=true;
            }
            else{
                document.body.classList.add("dark-mode");
            localStorage.setItem("theme","dark-mode");
            enabledark=true;
        }
            document.getElementById("currenttheme").innerHTML = localStorage.theme;
        };
        document.body.classList.add(localStorage.getItem("theme"));
    document.getElementById("currenttheme").innerHTML = localStorage.theme;