var Links = {
    setColor:function (color){
//        var flaglist = document.querySelectorAll('a');
//        var i = 0;
//        while (i<flaglist.length){
//            flaglist[i].style.color = color;
//            i+=1;
//        }
    $('a').css('color', color)
    }
}

var Body = {
    setColor:function (color){
        //document.querySelector('body').style.color = color;
        $('body').css('color', color);
    },
    setBackgroundColor:function (color){
        //document.querySelector('body').style.backgroundColor = color;
        $('body').css('backgroundColor', color);
    }
}
        
    
function night_day_handler(self){
    var flag = document.querySelector('body');
    if (self.value==='change to night'){
        Body.setBackgroundColor('#555555');
        Body.setColor('white');
        self.value = 'change to day';
        Links.setColor('orange');
    }
    else {
        Body.setBackgroundColor('white');
        Body.setColor('#555555');
        self.value = 'change to night';
        Links.setColor('darkgreen');
    }
}

