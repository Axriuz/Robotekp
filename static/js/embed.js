function embed(){
    var input1, input2, input3;
    input1 = document.getElementById("id_URL_Video").value;
    input2 = ("https://www.youtube.com/embed/");
    
    for (i=32; i <input1.length; i++){
        if(input1.charAt(i) != "&")
            input2 = input2 + input1.charAt(i)
        else
            break;
    }
    document.getElementById("id_URL_Video").value = input2;
}
function embed2(){
    var input1, input2, input3;
    input1 = document.getElementById("id_URL_Video").value;
    input2 = ("https://www.youtube.com/embed/");
    if(input1.charAt(31) == "="){
        for (i=32; i <input1.length; i++){
            if(input1.charAt(i) != "&")
                input2 = input2 + input1.charAt(i)
            else
                break;
        }
        document.getElementById("id_URL_Video").value = input2;
    }
}