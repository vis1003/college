var hm = require("http");
hm.createServer(function(req,resp){
    resp.write("Welcome to the world of Node JS");
    resp.end();
}).listen(8084);
