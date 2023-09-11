string serverurl = "http://www.yoursever.tld";
string port = "85";
key server;
default
{
    touch_start(integer total_number)
    {
        llMessageLinked(LINK_SET,255,"Hello MQTT!","/test/topic");
    }
    link_message(integer link,integer chan,string message,key id)
    {
        if(chan == 255)
        {
            string topic = (string)id;
            server = llHTTPRequest(serverurl+":"+port+"/send_message?topic="+topic+"/&message="+message
            ,[HTTP_METHOD, "GET",HTTP_VERBOSE_THROTTLE, FALSE,HTTP_MIMETYPE,"text/plain;charset=utf-8",HTTP_BODY_MAXLENGTH, 16384],"");
        }
    }
    http_response(key id, integer status, list metaData, string body)
    {
        if(status != 200)
        llOwnerSay((string)status +" : "+body); 
    }
}
