const icon3=document.getElementById("icon3");
        icon3.onclick=function()
        {
            if(document.body.classList.contains("dracula-mode")){
            document.body.classList.remove("dracula-mode");
            document.body.classList.add("light-mode");
            localStorage.setItem("theme","light-mode");
            }
            else if(document.body.classList.contains("dark-mode")){
            document.body.classList.remove("dark-mode");
            document.body.classList.add("light-mode");
            localStorage.setItem("theme","light-mode");
            }
            else{
                document.body.classList.toggle("light-mode");
            localStorage.setItem("theme","light-mode");
        }
            document.getElementById("currenttheme").innerHTML = localStorage.theme;
        };
        document.body.classList.add(localStorage.getItem("theme"));
    document.getElementById("currenttheme").innerHTML = localStorage.theme;