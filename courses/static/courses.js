function paginate_func(pg_num){
            url = window.location.href
            if(url.includes('page')){
                var mn = url.indexOf('page');
                mn+=5;
                if(url.indexOf('&', mn)==-1){
                    var pre = url.slice(0, mn);
                    url = pre+pg_num;
                }
                else{
                    var pre = url.slice(0, mn);
                    var post = url.slice(url.indexOf('&', mn),url.length);
                    url = pre+pg_num+post;
                }
            }
            else{
                if(url.indexOf('?')==-1){
                    url+=("?page="+pg_num);
                }
                else{
                    url+=("&page="+pg_num)
                }
            }
            window.location.href=url;
        }