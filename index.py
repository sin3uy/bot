<?php
ob_start();
error_reporting(0);
define("API_KEY",'7522312323:AAGfaInciphqFMhXLP1bk1hYDZMEO2Oy-Z8');//توكن البوت
$botname = bot('getme',['bot'])->result->username;
function bot($method,$datas=[]){
$url = "https://api.telegram.org/bot".API_KEY."/$method";
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
curl_setopt($ch,CURLOPT_POSTFIELDS,$datas); 
$res = curl_exec($ch);
if(curl_error($ch)){
var_dump(curl_error($ch));
}else{
return json_decode($res);
}
}
//𓏳𓏳𓏳𓏳⦅ معلوماتك ⦆𓏳𓏳𓏳𓏳𓏳
$nmbr = "076788" ; #رقمك اسيا
$admin = 7037026615; #ايديك تلي
$chnl = "@s_p_p1" ; // يوزر قناتك
$sudo = "$admin";// لا تلعب هنا بشي
$sudo = array("7037026615","7037026615","7037026615");//هنا تخلي ايديات الادمن اذا تريد تخلي ادمن لبوت هنا
$Api_Tok = "04ed9b84257860f2fc6c51b0f425df0c" ;#توكن لموقع
//𓏳𓏳𓏳𓏳⦅ معلوماتك ⦆𓏳𓏳𓏳𓏳𓏳
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$text = $update->message->text;
$chat_id = $update->message->chat->id;
$from_id = $update->message->from->id;
$message_id = $update->message->message_id;
$from_id = $message->from->id;
$name = $update->message->from->first_name;
$username = $update->message->from->username;
$title = $message->chat->title;
///
$saiko = json_decode(file_get_contents("saiko.json"),1);
if($saiko['gch'] == null){
$saiko['gch'] = "❎";
file_put_contents("saiko.json",json_encode($saiko));
}
$xch = $saiko['ch'];
///
$members = explode("\n",file_get_contents("members.txt"));
$count = count($members) -1;
if($tc == 'private' and !in_array($from_id,$members)){
file_put_contents('members.txt',$from_id."\n",FILE_APPEND);
}
///
$oop = $xch;
$join = file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$oop&user_id=".$from_id);
$zr = str_replace("@","",$oop);
if($saiko['ch'] != null){
if($saiko['gch'] == "✅"){
if($message && (strpos($join,'"status":"left"') or strpos($join,'"Bad Request: USER_ID_INVALID"') or strpos($join,'"status":"kicked"'))!== false){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"
المعذره عليك الاشتراك في قناة البوت 🌹
📢┇  $oop
",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'اضغط هنا ✅' ,'url'=>"t.me/$zr"]],
]])
]);return false;
}
}
}
///
$update = json_decode(file_get_contents('php://input'));
$message= $update->message;
$text = $message->text;
$chat_id= $message->chat->id;
$name = $message->from->first_name;
$user = $message->from->username;
$message_id = $update->message->message_id;
$from_id = $update->message->from->id;
$a = strtolower($text);
$message = $update->message;
$chat_id = $message->chat->id;
$text = $message->text;
$chat_id2 = $update->callback_query->message->chat->id;
$message_id = $update->callback_query->message->message_id;
$data = $update->callback_query->data;
$from_id = $message->from->id;

$msg = file_get_contents("msg.php");
$forward = file_get_contents("forward.php");
$midea = file_get_contents("midea.php");
$inlin = file_get_contents("inlin.php");
$photoi = file_get_contents("photoi.php");
$upq = file_get_contents("up.php");
$skor = file_get_contents("skor.php");


mkdir("data");

$channel = file_get_contents("link.php");
$link = file_get_contents("link2.php");
$ch = "$channel"; #لا تلعب هنا
$join = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=$ch&user_id=".$from_id);
if($message && (strpos($join,'"status":"left"') or strpos($join,'"Bad Request: USER_ID_INVALID"') or strpos($join,'"status":"kicked"'))!== false){
bot('sendMessage', [
'chat_id'=>$chat_id,
 'text'=>"
🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- [اضغط هنا للشتراك في القناة]($link)

‼️| اشترك ثم ارسل /start",
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
]);return false;}

$uuser = file_get_contents("uuser.php");
$join = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=$uuser&user_id=".$from_id);
if($message && (strpos($join,'"status":"left"') or strpos($join,'"Bad Request: USER_ID_INVALID"') or strpos($join,'"status":"kicked"'))!== false){
bot('sendMessage', [
'chat_id'=>$chat_id,
 'text'=>"
🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- $uuser

‼️| اشترك ثم ارسل /start",
]);return false;}

$users = explode("\n",file_get_contents("abbas.json"));

if($message){
if(!in_array($from_id,$users)){
file_put_contents("abbas.json",$from_id."\n",FILE_APPEND);}}

$tc = $message->chat->type;
$abbas09 = json_decode(file_get_contents("abbas09.json"),true);
$suodo = $abbas09['sudoarr'];
$al = $abbas09['addmessage'];
$ab = $abbas09['messagee'];
$xll = $al + $ab;
if($message and $from_id !== $admin){
$abbas09['messagee'] = $abbas09['messagee']+1;
file_put_contents("abbas09.json",json_encode($abbas09,32|128|265));
}
if($message and $from_id == $admin){
$abbas09['addmessage'] = $abbas09['addmessage']+1;
file_put_contents("abbas09.json",json_encode($abbas09,32|128|265));
}

$all = count($users)-1;

$adminss = explode("\n",file_get_contents("ad.json"));

$k088 = file_get_contents("data/k088.txt");
$q1 = file_get_contents("data/q1.txt");
$q2 = file_get_contents("q2.txt");
$q3 = file_get_contents("data/q3.txt");
$q4 = file_get_contents("q4.txt");
$q5 = file_get_contents("data/q5.txt");
$aralikan = file_get_contents("q6.txt");


if($message){
if(!in_array($admin,$adminss)){
bot('sendmessage',[
'chat_id'=>$admin,
'text'=>"
تم تحديث القائمه /start
",
]);
file_put_contents("ad.json",$admin."\n",FILE_APPEND);
}}

$d = date('D');
$day = explode("\n",file_get_contents($d.".txt"));
$todayuser = count($day);
if($d == "Sat"){
unlink("Fri.txt");
}
if($d == "Sun"){
unlink("Sat.txt");
}
if($d == "Mon"){
unlink("Sun.txt");
}
if($d == "Tue"){
unlink("Mon.txt");
}
if($d == "Wed"){
unlink("The.txt");
}
if($d == "Thu"){
unlink("Wedtxt");
}
if($d == "Fri"){
unlink("Thu.txt");
}
if($message and !in_array($from_id, $day)){ 
file_put_contents($d.".txt",$from_id. "\n",FILE_APPEND);
}

$from_id = $message->from->id;
$name = $message->from->first_name;
$id = $message->from->id;
$user = $message->from->username;
if($user){
$user = "@$user";
}
elseif(!$uaer){
$user = "بلا معرف";
}
if($text =="/start" and !in_array($from_id,$users)){
bot('sendmessage',[
'chat_id'=>$admin,
'text'=>"
٭ دخل شخص جديد الى البوت الخاص بك 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
• اسمه : ‣ $name ⌁
• يوزره : ‣ $user ⌁
• ايديه : ‣ $id ⌁
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
• عدد الاعضاء الكلي : ‣ $all ⌁
",
]);
}

$bot = file_get_contents("bot.txt");





//
if($data =="lIllabbas"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"اهلا", 
'parse_mode'=>"Markdown",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"• رفع ادمن •","callback_data"=>"adl"]],
[["text"=>"• اخر الادمن •","callback_data"=>"addmin"]],
[["text"=>"• حذف الادمنيه •","callback_data"=>"delateaddmin"]],
]])
]);   
}

if($data == "adl"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
قم بارسال ايدي العضو
 ",
]); 
file_put_contents("data/k088.txt","k088");
}
if($text !="/start" and $k088 == "k088" and !in_array($text,$adminss)){
file_put_contents("data/k088.txt","none");
file_put_contents("ad.json",$text."\n",FILE_APPEND);} 

if($text != "/start" and $k088 == "k088" and !in_array($text,$adminss)){
file_put_contents("data/k088.txt","none");
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم رفع العضو", 
]);
bot('sendmessage',[
'chat_id'=>$text,
'text'=>"تم رفعك ادمن في البوت", 
]);
}
if($text !="/start" and $k088 == "k088" and in_array($text,$adminss)){
file_put_contents("data/k088.txt","none");
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"العضو ادمن بالفعل", 
]);
}
if($data =="addmin"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"اخر خمس ادمنيه :
 1 - ".$adminss[count($adminss)-2]."
 2 - ️".$adminss[count($adminss)-3]."
 3 - ️".$adminss[count($adminss)-4]."
 4 - ️".$adminss[count($adminss)-5]."
 5 - ️".$adminss[count($adminss)-6]."
",
'parse_mode'=>"Markdown",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"- الصفحه الرئيسيه.","callback_data"=>"bak"]],
]])
]);   
}
if($data =="delateaddmin" and $chat_id2 =="$admin"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
هل انت متاكد من الحذف
",'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'لا' ,'callback_data'=>"bak"]],
[['text'=>'نعم' ,'callback_data'=>"yesaarsslan"]],
]])
]);
}
if($data =="yesaarsslan"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
تم حذف الادمنيه
",'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'الصفحه الرئيسيه' ,'callback_data'=>"bak"]],
]])
]);
unlink("ad.json");
}

if($data =="abcde"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"- اهلا بك عزيزي
- تم فتح البوت 
- /start",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'الصفحه الرئيسيه' ,'callback_data'=>"bak"]],
]])
]);
file_put_contents("bot.txt","مفتوح");
} 
if($data =="abcd"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"- اهلا بك عزيزي
- تم قفل البوت
- /start ",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'الصفحه الرئيسيه' ,'callback_data'=>"bak"]],
]])
]); 
file_put_contents("bot.txt","متوقف");
} 

if($text =="/start" and $bot =="متوقف" and $chat_id != "$admin"){
 bot("sendmessage",[
 "chat_id"=>$chat_id,
 "text"=>"عذرا البوت يخضع للتحديث الان",]);
}

if($data =="userd"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 اهلا بك عزيزي الادمن
 عدد الاعضاء : ( $all )",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'الصفحه الرئيسيه' ,'callback_data'=>"bak"]],
]])
]);
}

if($data == 'ont'){
file_put_contents("ont.php", "on");
bot('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'message_id'=>$message_id,
'text'=>"
 مرحبا عزيزي
 تم تفعيل الاشعارات في البوت
",
'show_alert'=>true
]);
}
if($data == 'oft'){
file_put_contents("ont.php", "off");
bot('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'message_id'=>$message_id,
'text'=>"
 مرحبا عزيزي
⚠ تم تعطيل الاشعارات في البوت
",
'show_alert'=>true
]);
}
$ont = file_get_contents("ont.php");
if($ont == "on"){
if($from_id != $admin){
if($message){
bot('ForwardMessage',[
'chat_id'=>$admin,
'from_chat_id'=>$chat_id,
'message_id'=>$message->message_id,
]);
}}}

if($data == "for"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم باختيار ما يناسبك",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"اذاعه صورة ",'callback_data'=>"photoi"]],
[['text' => "اذاعه رسالة ", 'callback_data' => "msg"],['text' => "اذاعه توجيه ", 'callback_data' => "forward"]],
[['text' => "اذاعه ميديا ", 'callback_data' => "midea"],['text' => "اذاعه انلاين ", 'callback_data' => "inline"]],
[['text'=>"رجوع ",'callback_data'=>"bak"]],
]])
]);
}
if($data == "msg"){
file_put_contents("msg.php", "on");
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم بأرسال رسالتك لتحويلها لجميع المشتركين",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"الغاء",'callback_data'=>"bak"]],
]])
]);
}
if($msg == "on"){
if($message){
for($i=0;$i<count($users); $i++){
bot('sendmessage',[
'chat_id'=>$users[$i],
'text'=>"$text",
]);
}
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 حسنا عزيزي
 تم عمل اذاعه بنجاح
 الى ( $all ) مشترك",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع ",'callback_data'=>"bak"]],
]])
]);
unlink("msg.php");
}}
if($data == "forward"){
file_put_contents("forward.php", "on");
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم بأرسال رسالتك لتحويلها لجميع المشتركين على شكل توجيه",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"الغاء ",'callback_data'=>"bak"]],
]])
]);
}
if($forward == "on"){
if($message){
for($i=0;$i<count($users); $i++){
bot('ForwardMessage',[
'chat_id'=>$users[$i],
'from_chat_id'=>$chat_id,
'message_id'=>$message->message_id,
]);
}
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 حسنا عزيزي
 تم عمل اذاعه توجيه بنجاح
 الى ( $all ) مشترك",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع",'callback_data'=>"bak"]],
]])
]);
unlink("forward.php");
}}
if($data == "midea"){
file_put_contents("midea.php", "on");
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 يمكنك استخدام جميع انوع الميديا ماعدى الصوره
 (ملصق - فيديو - بصمه - ملف صوتي - ملف - متحركه - جهة اتصال )",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"الغاء",'callback_data'=>"bak"]],
]])
]);
}
$up = json_decode(file_get_contents('php://input'),true);
if(!isset($message->text)){
$types = ['voice','audio','video','photo','contact','document','sticker'];
foreach($up['message'] as $key => $val){
if(in_array($key,$types) and $midea == "on"){
for($i=0;$i<count($users); $i++){
bot('send'.$key,[
'chat_id'=>$users[$i],
'caption'=>$message->caption,
$key=>$val['file_id']]);
unlink("midea.php");
}
}
}}
if($data == "photoi"){
file_put_contents("photoi.php", "on");
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم بأرسال الصورة لنشرها لجميع المشتركين",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"الغاء ",'callback_data'=>"bak"]],
]])
]);
}
if($photoi == "on"){
if($message->photo){
for($i=0;$i<count($users); $i++){
bot('sendphoto',[
'chat_id'=>$users[$i],
'photo'=>$message->photo[0]->file_id,
'caption'=>$message->caption,
]);
}
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 حسنا عزيزي
 تم نشر الصورة بنجاح
 الى ( $all ) مشترك",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع ",'callback_data'=>"bak"]],
]])
]);
unlink("photoi.php");
}}
if($data == "inline"){
file_put_contents("inlin.php", "on");
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم بتوجيه نص الانلاين لاقوم بنشره للمشتركين",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"الغاء",'callback_data'=>"bak"]],
]])
]);
}
if($inlin == "on"){
if($message->forward_from or $message->forward_from_chat){
for($i=0;$i<count($users); $i++){
bot('forwardmessage',[
'chat_id'=>$users[$i],
'from_chat_id'=>$chat_id,
'message_id'=>$message->message_id,
]);
}
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 حسنا عزيزي
 تم نشر الانلاين بنجاح
 الى ( $all ) مشترك",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع ",'callback_data'=>"bak"]],
]])
]);
unlink("inlin.php");
}}

if($data == "channel"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم بتحديد الامر لأتمكن من تنفيذه",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"قناة خاصة ",'callback_data'=>"link"]],
[['text'=>"قناة عامة ",'callback_data'=>"user"]],
[['text'=>"رجوع ",'callback_data'=>"bak"]],
]])
]);
}
if($data == "link"){
file_put_contents("link.php", "on");
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم برفع البوت ادمن في القناة
 ثم ارسل توجيه من القناة الى هنا",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع ",'callback_data'=>"bak"]],
]])
]);
}
$channel_id = $message->forward_from_chat->id;
if($channel == "on"){
if($message->forward_from_chat){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 حسنا عزيزي
 قم الان بأرسال رابط القناة هنا",
]);
file_put_contents("link.php", $channel_id);
file_put_contents("link2.php", "on");
}}
if($link == "on"){
if(preg_match('/^(.*)([Hh]ttp|[Hh]ttps|t.me)(.*)|([Hh]ttp|[Hh]ttps|t.me)(.*)|(.*)([Hh]ttp|[Hh]ttps|t.me)|(.*)[Tt]elegram.me(.*)|[Tt]elegram.me(.*)|(.*)[Tt]elegram.me|(.*)[Tt].me(.*)|[Tt].me(.*)|(.*)[Tt].me|(.*)telesco.me|telesco.me(.*)/i',$text)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 حسنا عزيزي
 تم تفعيل الاشتراك بنجاح",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"اتمام العملية",'callback_data'=>"bak"]],
]])
]);
file_put_contents("link2.php", $text);
file_put_contents("skor.php", "مفعل ✅");
}else{
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 عذرا عزيزي
 قم بأرسال الرابط بصورة صحيحه",
]);
}
}

if($data == "user"){
bot('editmessagetext',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم برفع البوت ادمن في القناة
 ثم ارسل يوزر القناة لتفعيل الاشتراك",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع ",'callback_data'=>"bak"]],
]])
]);
file_put_contents("uuser.php", "on");
}
if($uuser == "on"){
if(preg_match('/^(.*)@|@(.*)|(.*)@(.*)|(.*)#(.*)|#(.*)|(.*)#/',$text)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 حسنا عزيزي
 تم تفعيل الاشتراك بنجاح",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"اتمام العملية ⏱",'callback_data'=>"bak"]],
]])
]);
file_put_contents("skor.php", "مفعل ✅");
file_put_contents("uuser.php", $text);
}else{
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
 عذرا عزيزي
 قم بأرسال يوزر بصورة صحيحه",
]);
}
}

if($skor == "معطل ⚠️"){
if($data == 'off'){
bot('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'message_id'=>$message_id,
'text'=>'
 مرحبا عزيزي
 حالة الاشتراك الاجباري معطل
 قم بختيار - قائمةه الاشتراك .وقم بتفعيله
',
 'show_alert'=>true
 ]); 
}}
if($skor == "مفعل ✅"){
if($data == 'off'){
bot('editMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>'
 حسنا عزيزي
 حالت الاشتراك الخاص بك مفعل
 هل انت متأكد من رغبتك في تعطيل الاشتراك
',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[
['text'=>'نعم ', 'callback_data'=>'yesde2'],
['text'=>'لا ','callback_data'=>'bak'],
]
]])
]);
}}

if($data == "yesde2"){
unlink("uuser.php");
unlink("link.php");
file_put_contents("skor.php", "معطل ⚠️");
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 تم تعطيل الاشتراك في جميع القنواة
 يمكنك تفعيل الاشتراك لقناتك في مابعد",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع",'callback_data'=>"bak"]],
]])
]);
}

$bloktime = date('h:i:s A');
if($data == "file"){
$path = realpath("abbas.json");
bot('senddocument',[
'chat_id'=>$chat_id2,
'document'=>new CURLFile($path),
'caption'=>"
 نسخة لمشتركينك
 وقت الارسال : ( $bloktime )
 عدد المشتركين : ( $all )
",
]);
}

if($data == "up"){
bot('editmessagetext',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
 حسنا عزيزي
 قم بأرسال ملف الاعضاء الان
 ارسل الملف بأسم : abbas.json",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع ",'callback_data'=>"bak"]],
]])
]);
file_put_contents("up.php", "on");
}
$rep = $message->document->file_name;
if($upq == "on"){
if($message->document and $message->document->file_name == "abbas.json" ){
$file = "https://api.telegram.org/file/bot".API_KEY."/".bot('getfile',['file_id'=>$message->reply_to_message->document->file_id])->result->file_path;
file_put_contents($message->reply_to_message->document->file_name,file_get_contents($file));
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"* تم رفع الملف  : $rep*",
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
]);
unlink("up.php");
}else{
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"* لايمكن رفع الملف  : $rep*",
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"الغاء",'callback_data'=>"bak"]],
]])
]);
}
}

if($data =="pannel"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"*• اهلا بك في قسم - الاحصائيات . 📊
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
• عدد اعضاء بوتك : ‣ $all ⌁
• المتفاعلين اليوم  : ‣ $todayuser ⌁
• عدد الرسائل المرسله : ‣ ".$abbas09['addmessage']." ⌁
• عدد الرسائل المستلمه : ‣ ".$abbas09['messagee']." ⌁
• مجموع الرسائل : ‣ $xll ⌁
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳*",'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'الصفحه الرئيسيه' ,'callback_data'=>"bak"]],
]])
]);
}

if($data == "editstart"){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"
قم بارسال رسالة الاستارت الان
 ",
]); 
file_put_contents("data/q1.txt","q1");
}
if($text != "/start" and $q1 == "q1"){
file_put_contents("data/q1.txt","none");
file_put_contents("q2.txt","$text");
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم التعين بنجاح", 
]);
}

if ($data == 'bak'){
$msg = unlink("msg.php");
unlink("forward.php");
unlink("midea.php");
unlink("inlin.php");
unlink("photoi.php");
unlink("up.php");
unlink("up.php");
bot('editmessagetext',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id,
'text'=>"*- اهلا بك عزيزي المطور 
- اليك قائمه الاوامر الخاصه بك*",
'parse_mode'=>"Markdown",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>" قفل البوت ","callback_data"=>"abcd"],["text"=>" فتح البوت ","callback_data"=>"abcde"]],
[["text"=>" اعضاء البوت ","callback_data"=>"userd"]],
[["text"=>" تفعيل التنبيه ","callback_data"=>"ont"],["text"=>" تعطيل التنبيه ","callback_data"=>"oft"]],
[["text"=>" قسم الاذاعةه ","callback_data"=>"for"]],
[['text' => " قائمه الاشتراك ", 'callback_data' => "channel"],['text' => " الاشتراك ($skor) ", "callback_data" => "off"]],
[['text' => " نسخة احتياطيه ", 'callback_data' => "nnn"],['text' => " رفع نسخه ", 'callback_data' => "up"]],
[['text' => " الاحصائيات ", 'callback_data' => "pannel"],['text' => " قسم الادمن ", 'callback_data' => "lIllabbas"]],
]])
]);   
}
$update = json_decode(file_get_contents("php://input"));
file_put_contents("update.txt",json_encode($update));
$message = $update->message;
$text = $message->text;
$chat_id = $message->chat->id;
$from_id = $message->from->id;$type = $message->chat->type;
$message_id = $message->message_id;
$name = $message->from->first_name.' '.$message->from->last_name;
$user = strtolower($message->from->username);
$t =$message->chat->title; 
if(isset($update->callback_query)){
$up = $update->callback_query;
$chat_id = $up->message->chat->id;
$from_id = $up->from->id;
$user = strtolower($up->from->username); 
$name = $up->from->first_name.' '.$up->from->last_name;
$message_id = $up->message->message_id;
$mes_id = $update->callback_query->inline_message_id; 
$data = $up->data;
}
if(isset($update->inline_query)){
$chat_id = $update->inline_query->chat->id;
$from_id = $update->inline_query->from->id;
$name = $update->inline_query->from->first_name.' '.$update->inline_query->from->last_name;
$text_inline = $update->inline_query->query;
$mes_id = $update->inline_query->inline_message_id; 
$user = strtolower($update->inline_query->from->username); 
}
$update = json_decode(file_get_contents("php://input"));
file_put_contents("update.txt",json_encode($update));
$message = $update->message;
$text = $message->text;
$chat_id = $message->chat->id;
$from_id = $message->from->id;$type = $message->chat->type;
$message_id = $message->message_id;
$name = $message->from->first_name.' '.$message->from->last_name;
$user = strtolower($message->from->username);
$t =$message->chat->title;  
if(isset($update->callback_query)){
$up = $update->callback_query;
$chat_id = $up->message->chat->id;
$from_id = $up->from->id;
$user = strtolower($up->from->username); 
$name = $up->from->first_name.' '.$up->from->last_name;
$message_id = $up->message->message_id;
$mes_id = $update->callback_query->inline_message_id; 
$data = $up->data;
}




if($update->message->group_chat_created or $update->message->new_chat_member->username == bot('getme','bot')->result->username) {
	bot('sendMessage',[
       'chat_id'=>$chat_id ,
        'text'=>"ماشتغل بكروبات انا ✅" ,
    ]);
    bot('leaveChat',[ 
'chat_id'=>$chat_id, 
]);
 
	exit;
	} 
if($text and $from_id != $sudo){
bot('forwardMessage',[
'chat_id'=>$sudo,
'from_chat_id'=>$chat_id,
  'message_id'=>$update->message->message_id,
'text'=>$text,
]);
}
if($message->reply_to_message->forward_from->id and $from_id == $sudo){
    bot('sendMessage',[
       'chat_id'=>$message->reply_to_message->forward_from->id,
        'text'=>$text,
    ]);
    bot('sendmessage',[
       'chat_id'=>$sudo,
        'text'=>"
تم ارسال لرساله
",
]);
}

$ckl = $chnl; # معرف لقناة ويه @
$ch2 = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=".$ckl."&user_id=".$from_id);
$getch2 = json_decode(file_get_contents("http://api.telegram.org/bot".API_KEY."/getChat?chat_id=".$ckl))->result;
$Namech2 = $getch2->title;
$getch2li = str_replace("@","",$ckl);
if($message && (strpos($ch2,'"status":"left"') or strpos($ch2,'"Bad Request: USER_ID_INVALID"') or strpos($ch2,'"status":"kicked"'))!== false){
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>"
*
📣 ⁞ عليك الأشتراك في قناة البوت.
*
📢 ⁞ قناة البوت : [$ckl] 
*
📡 ⁞ اشترك بلقناة بعدها ارسل /start .
*
", 
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>$Namech2,'url'=>"https://t.me/$getch2li"]],
]])
]);return false;}



if(isset($update->callback_query)){

$up = $update->callback_query;
$chat_id = $up->message->chat->id;
$from_id = $up->from->id;
$user = $up->from->username;
$name = $up->from->first_name;
$message_id = $up->message->message_id;
$data = $up->data;
$tc = $up->chat->type ;
}

$rshq = json_decode(file_get_contents("rshq.json"),true);


$rsedi = json_decode(file_get_contents("https://yemenfollow.com/api/v2?key=$Api_Tok&action=balance"));
$flos = $rsedi->balance; 
$treqa = $rsedi->currency; 

if($text == "/admin") {
	if($chat_id == $admin ) {
	bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"*☆︙قسم الرشق 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
يمنك اضافه او خصم نقاط
يمكن قفل استقبال الرشق وفتحها
يمكنك صنع هدايا 
☆︙رصيدك في الموقع : ⦅ $flos$ ⦆
☆︙العمله : ⦅ $treqa ⦆*",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"اضافه او خصم نقاط",'callback_data'=>"coins" ],['text'=>"صنع كود هديه",'callback_data'=>"hdiamk" ]],
[['text'=>"فتح استقبال الرشق",'callback_data'=>"onrshq" ],['text'=>"قفل استقبال الرشق",'callback_data'=>"ofrshq" ]], 
[["text"=>" قفل البوت ","callback_data"=>"abcd"],["text"=>" فتح البوت ","callback_data"=>"abcde"]],
[["text"=>" تفعيل التنبيه ","callback_data"=>"ont"],["text"=>" تعطيل التنبيه ","callback_data"=>"oft"]],
[['text' => " قائمه الاشتراك ", 'callback_data' => "channel"],['text' => " الاشتراك ($skor) ", "callback_data" => "off"]],
[['text' => " نسخة احتياطيه ", 'callback_data' => "nnn"],['text' => " رفع نسخه ", 'callback_data' => "up"]],
[['text' => " الاحصائيات ", 'callback_data' => "pannel"],['text' => " قسم الادمن ", 'callback_data' => "lIllabbas"]],
[["text"=>" قسم الاذاعه ","callback_data"=>"for"],["text"=>" اعضاء البوت ","callback_data"=>"userd"]],
     
]
])
]);
$rshq['mode'][$from_id]  = null;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
}
}


if($data == "back") {
	if($chat_id == $admin ) {
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"*☆︙قسم الرشق 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
يمنك اضافه او خصم نقاط
يمكن قفل استقبال الرشق وفتحها
يمكنك صنع هدايا 
☆︙رصيدك في الموقع : ⦅ $flos$ ⦆
☆︙العمله : ⦅ $treqa ⦆*",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"اضافه او خصم نقاط",'callback_data'=>"coins" ],['text'=>"صنع كود هديه",'callback_data'=>"hdiamk" ]],
[['text'=>"فتح استقبال الرشق",'callback_data'=>"onrshq" ],['text'=>"قفل استقبال الرشق",'callback_data'=>"ofrshq" ]], 
[["text"=>" قفل البوت ","callback_data"=>"abcd"],["text"=>" فتح البوت ","callback_data"=>"abcde"]],
[["text"=>" تفعيل التنبيه ","callback_data"=>"ont"],["text"=>" تعطيل التنبيه ","callback_data"=>"oft"]],
[['text' => " قائمه الاشتراك ", 'callback_data' => "channel"],['text' => " الاشتراك ($skor) ", "callback_data" => "off"]],
[['text' => " نسخة احتياطيه ", 'callback_data' => "nnn"],['text' => " رفع نسخه ", 'callback_data' => "up"]],
[['text' => " الاحصائيات ", 'callback_data' => "pannel"],['text' => " قسم الادمن ", 'callback_data' => "lIllabbas"]],
[["text"=>" قسم الاذاعه ","callback_data"=>"for"],["text"=>" اعضاء البوت ","callback_data"=>"userd"]],
     
]
])
]);
$rshq['mode'][$from_id]  = null;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
}
}

if($data == "hdiamk" and $chat_id == $admin ) {
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
ارسل عدد النقاط داخل الهديه 

*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"back" ]],
       
      ]
    ])
]);
    $rshq['mode'][$from_id]  = "hdiMk";
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 


$rnd=rand(999,99999);
if($text and $rshq['mode'][$from_id] == "hdiMk") {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
   
  تم اضافة كود هدية جديد
 - - - - - - - - - - - - - - - - - - 
 الكود : `Bero". $rnd."`
 عدد النقاط : $text
 - - - - - - - - - - - - - - - - - - 
 بوت الرشق المجاني : [@".bot('getme','bot')->result->username. "] 
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"admin" ]],
       
      ]
    ])
]);
$rshq["Bero".$rnd]  = "on|$text";
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 
if($data == "onrshq") {
	if($chat_id == $admin ) {
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
تم فتح استقبال الرشق
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"rshaq" ]], 
]
])
]);
$rshq['rshaq']  = "on";
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
}
}


if($data == "ofrshq") {
	if($chat_id == $admin ) {
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
تم قفل استقبال الرشق
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"rshaq" ]], 
]
])
]);

$rshq['rshaq']  = "of";
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
}
}

if($data == "coins" and $chat_id == $admin ) {
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
ارسل ايدي الشخص الان

*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"back" ]],
       
      ]
    ])
]);
    $rshq['mode'][$from_id]  = "coins";
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 

if($text and $rshq['mode'][$from_id] == "coins") {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
   
   ارسل عدد النقاط لاضافته للشخص
   
اذا تريد تخصم كتب ويا - 
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"admin" ]],
       
      ]
    ])
]);
$rshq['mode'][$from_id]  = "coins2";
$rshq['id'][$from_id]  = "$text";
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 

if($text and $rshq['mode'][$from_id] == "coins2") {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
   
  تم اضافه $text ل". $rshq['id'][$from_id]. "
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"admin" ]],
       
      ]
    ])
]);
$rshq['mode'][$from_id]  = null;
$rshq["coin"][$rshq['id'][$from_id]] += $text;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 

$rshq = json_decode(file_get_contents("rshq.json"),true);
if(!$rshq){
	bot('sendMessage',[
   'chat_id'=>$admin,
   'text'=>"
   *
~ تم ضبط الاعدادات تلقائيا ✨
*
  ", 
  'parse_mode'=>"markdown",
]);
	$rshq['rshaq'] = "✅" ;
	$rshq= json_encode($rshq,32|128|265);
    file_put_contents("rshq.json",$rshq); 
	} 
$rshaq = $rshq['rshaq'];
if($rshaq == "on") {
	$rshaq = "✅" ;
	} else {
		$rshaq = "❌" ;
		} 
$coin = $rshq["coin"][$from_id];
$bot_tlb = $rshq['bot_tlb'];
$mytl = $rshq["cointlb"][$from_id];
$share = $rshq["mshark"][$from_id] ;
$coinss = $rshq["coinss"][$from_id];
$tlby =$rshq["tlby"][$from_id];
if($rshq["coin"][$from_id] == null) {
	$coin = 0;
	}
	if($rshq["tlby"][$from_id] == null) {
	$tlby = 0;
	}
	if($rshq["coinss"][$from_id] == null) {
	$coinss = 0;
	}
	if($rshq["mshark"][$from_id] == null) {
	$share = 0;
	}
	if($rshq["cointlb"][$from_id] == null) {
	$mytl = 0;
	}
	if($rshq['bot_tlb'] == null) {
	$bot_tlb = 0;
	}

$e=explode("|", $data) ;
$e1=str_replace("/start",null,$text); 
if($text == "/start$e1" and is_numeric($e1) and !preg_match($text,"#Bero#")) {
	if(!in_array($e1, $rshq["3thu"])){
		if($e1 != $from_id) {
			if(!in_array($from_id , $rshq["3thu"])){
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
لقد دخلت لرابط الدعوه الخاص بصديقك وحصل علي *5* نقاط

  ", 
  'parse_mode'=>"markdown",
]);
bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"*☆︙مرحبا بك ⦅* [$name](tg://user?id=$from_id) *⦆ 👋🏻. 
☆︙في بوت الرشق المتطور 🍓. 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
☆︙نقاطك : ⦅ $coin ⦆
☆︙ايديك : ⦅ $chat_id ⦆*", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"‣ نقاطك : $coin نقطه ⌁",'callback_data'=>"saleiis" ]],
     [['text'=>"‣ الخدمات ⌁",'callback_data'=>"service" ],['text'=>"‣ الحساب ⌁",'callback_data'=>"acc" ]], [['text'=>"‣ التجميع ⌁",'callback_data'=>"pluss" ]],
 [['text'=>"‣ استخدام كود ⌁",'callback_data'=>"hdia" ],['text'=>"‣ شحن نقاط ⌁",'callback_data'=>"buy" ]],
 [['text'=>"‣ الطلبات | $bot_tlb طلب ⌁",'callback_data'=>"salpes" ]],
       
      ]
    ])
]);
$rshq["3thu"][] = $from_id ;
$rshq["coin"][str_replace(" ", null, $e1)] += 5;
$rshq["mshark"][str_replace(" ", null, $e1)] += 1;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq); 
} else {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"*☆︙مرحبا بك ⦅* [$name](tg://user?id=$from_id) *⦆ 👋🏻. 
☆︙في بوت الرشق المتطور 🍓. 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
☆︙نقاطك : ⦅ $coin ⦆
☆︙ايديك : ⦅ $chat_id ⦆*", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"‣ نقاطك : $coin نقطه ⌁",'callback_data'=>"saleiis" ]],
     [['text'=>"‣ الخدمات ⌁",'callback_data'=>"service" ],['text'=>"‣ الحساب ⌁",'callback_data'=>"acc" ]], [['text'=>"‣ التجميع ⌁",'callback_data'=>"pluss" ]],
 [['text'=>"‣ استخدام كود ⌁",'callback_data'=>"hdia" ],['text'=>"‣ شحن نقاط ⌁",'callback_data'=>"buy" ]],
 [['text'=>"‣ الطلبات | $bot_tlb طلب ⌁",'callback_data'=>"salpes" ]],
      ]
    ])
]);
} 
} else {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
لايمكنك الدخول لرابط الدعوه الخاص بك✅
  ", 

]);
bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"*☆︙مرحبا بك ⦅* [$name](tg://user?id=$from_id) *⦆ 👋🏻. 
☆︙في بوت الرشق المتطور 🍓. 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
☆︙نقاطك : ⦅ $coin ⦆
☆︙ايديك : ⦅ $chat_id ⦆*", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"‣ نقاطك : $coin نقطه ⌁",'callback_data'=>"saleiis" ]],
     [['text'=>"‣ الخدمات ⌁",'callback_data'=>"service" ],['text'=>"‣ الحساب ⌁",'callback_data'=>"acc" ]], [['text'=>"‣ التجميع ⌁",'callback_data'=>"pluss" ]],
 [['text'=>"‣ استخدام كود ⌁",'callback_data'=>"hdia" ],['text'=>"‣ شحن نقاط ⌁",'callback_data'=>"buy" ]],
 [['text'=>"‣ الطلبات | $bot_tlb طلب ⌁",'callback_data'=>"salpes" ]],
       
      ]
    ])
]);
} 
} else {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"*☆︙مرحبا بك ⦅* [$name](tg://user?id=$from_id) *⦆ 👋🏻. 
☆︙في بوت الرشق المتطور 🍓. 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
☆︙نقاطك : ⦅ $coin ⦆
☆︙ايديك : ⦅ $chat_id ⦆*", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"‣ نقاطك : $coin نقطه ⌁",'callback_data'=>"saleiis" ]],
     [['text'=>"‣ الخدمات ⌁",'callback_data'=>"service" ],['text'=>"‣ الحساب ⌁",'callback_data'=>"acc" ]], [['text'=>"‣ التجميع ⌁",'callback_data'=>"pluss" ]],
 [['text'=>"‣ استخدام كود ⌁",'callback_data'=>"hdia" ],['text'=>"‣ شحن نقاط ⌁",'callback_data'=>"buy" ]],
 [['text'=>"‣ الطلبات | $bot_tlb طلب ⌁",'callback_data'=>"salpes" ]],
       
      ]
    ])
]);
} 
} 



if($text == "/start") {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"*☆︙مرحبا بك ⦅* [$name](tg://user?id=$from_id) *⦆ 👋🏻. 
☆︙في بوت الرشق المتطور 🍓. 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
☆︙نقاطك : ⦅ $coin ⦆
☆︙ايديك : ⦅ $chat_id ⦆*", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"‣ نقاطك : $coin نقطه ⌁",'callback_data'=>"saleiis" ]],
     [['text'=>"‣ الخدمات ⌁",'callback_data'=>"service" ],['text'=>"‣ الحساب ⌁",'callback_data'=>"acc" ]], [['text'=>"‣ التجميع ⌁",'callback_data'=>"pluss" ]],
 [['text'=>"‣ استخدام كود ⌁",'callback_data'=>"hdia" ],['text'=>"‣ شحن نقاط ⌁",'callback_data'=>"buy" ]],
 [['text'=>"‣ الطلبات | $bot_tlb طلب ⌁",'callback_data'=>"salpes" ]],
       
      ]
    ])
]);
 }
 
 if($data == "buy") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
⌁ لشراء نقاط من بوت رشق Namero 💲↫ ⤈ 

⌁︰1$ ↬ 1000 نقطة في البوت
⌁︰5$ ↬ 5000 نقطة في البوت
⌁︰10$ ↬ 11000 نقطة في البوت
- - - - - - - - - - - - - - -
• ⋯ • ⋯ • ⋯ • ⋯ • ⋯ •• ⋯ • ⋯ • ⋯ • ⋯ • 
⌁ للتواصل 
⌁︰@Namero  , 
- - - - - - - - - - - - - - -
⌁︙طرق الدفع 
⌁︰سبأفون , يمن موبايل , كريمي , النجم .
⌁︰سوا , موبايلي , راجحي , فودافون كاش .
⌁︰زين كاش , آسيا , رايزر , مدار , ليبيانا .
⌁︰بتك, بايير , USDT , ستيم , ايتونز .
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
} 


if($data == "tobot") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"*☆︙مرحبا بك ⦅* [$name](tg://user?id=$from_id) *⦆ 👋🏻. 
☆︙في بوت الرشق المتطور 🍓. 
ٴ𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
☆︙نقاطك : ⦅ $coin ⦆
☆︙ايديك : ⦅ $chat_id ⦆*",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"‣ نقاطك : $coin نقطه ⌁",'callback_data'=>"saleiis" ]],
     [['text'=>"‣ الخدمات ⌁",'callback_data'=>"service" ],['text'=>"‣ الحساب ⌁",'callback_data'=>"acc" ]], [['text'=>"‣ التجميع ⌁",'callback_data'=>"pluss" ]],
 [['text'=>"‣ استخدام كود ⌁",'callback_data'=>"hdia" ],['text'=>"‣ شحن نقاط ⌁",'callback_data'=>"buy" ]],
 [['text'=>"‣ الطلبات | $bot_tlb طلب ⌁",'callback_data'=>"salpes" ]],
       
      ]
    ])
]);
} 

$rshq = json_decode(file_get_contents("rshq.json"),true);
if($data == "hdia") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
ارسل رمز الهدية الان
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
    $rshq['mode'][$from_id]  = "hdia";
   
    
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 


if($data == "transer") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
ارسل عدد النقاط لتحويله 🎉
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
    $rshq['mode'][$from_id]  = $data;
   
    
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 


$MakLink = substr(str_shuffle('AbCdEfGhIjKlMnOpQrStU12345689807'),1,13);
if(is_numeric($text) and $rshq['mode'][$from_id] == "transer") {
	if($rshq["coin"][$from_id] >= $text) {
		if(!preg_match('/+/',$text) or !preg_match('/-/',$text) ){
			if($text >= 20) {
		bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
تم صنع رابط تحويل بقيمه $text نقاط 💲
- وتم استقطاع *$text* من نقاطك ➖

الرابط : https://t.me/". bot('getme','bot')->result->username. "?start=Bero$MakLink

ايدي وصل التحويل : `". base64_encode($MakLink). "`

صار عدد نقاطك : *". $rshq["coin"][$from_id]. "*
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
       
      ]
    ])
]);
$rshq["coin"][$from_id] -= $text;
$rshq['mode'][$from_id]  = null;
$rshq['thoiler'][$MakLink]["coin"] = $text;
$rshq['thoiler'][$MakLink]["to"] = $from_id;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 
else 
{
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
يمكنك تحويل نقاط اكثر من 20 فقط
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
       
      ]
    ])
]);
} 

 } 
else
 {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
لاتحاول استخدام الكلجات سيتم حظرك عام؟ 👎
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
       
      ]
    ])
]);
	} 
	} else {
		bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
نقاطك غير كافيه ❌🗣️
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
       
      ]
    ])
]);
} 
		} 
	
if($text and $rshq['mode'][$from_id] == "hdia") {
	if(explode("|", $rshq[$text])[0] == "on") {
		if($rshq['mehdia'][$from_id][$text] !="on" ) {
		bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
~ لقد حصلت علي". explode("|", $rshq[$text])[1]. " نقطه من كود الهديه
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
       
      ]
    ])
]);
bot('sendMessage',[
   'chat_id'=>$admin,
   'text'=>"
هذا اخذ كود الهديه بقيمه".explode("|", $rshq[$text])[1]."
 
 ~ [$name](tg://user?id=$chat_id) 
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
       
      ]
    ])
]);
$rshq['mode'][$from_id] = null;
$rshq['mehdia'][$from_id][$text] = "on" ;
$rshq["coin"][$from_id] += explode("|", $rshq[$text])[1];
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} else {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
   انت مستخدم الكود من قبل
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
       
      ]
    ])
]);
	} 
	} else {
		bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
كود الهدية خطأ
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
       
      ]
    ])
]);
$rshq['mode'][$from_id]  = null;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
		} 
	} 
if($data == "plus") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
💻 ┇ البوت الرشق الاول في التلجرام
⌯ يمكنك الخصول علي 5 نقاط من كل شخص يدخل رابط الدعوع
⌯ التحكم الكامل في البوت
⌯ جميع الاقسام مجانيه
⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯ الـرابــط ⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯
    
https://t.me/". bot('getme','bot')->result->username. "?start=$from_id
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
[['text'=>"⌯انـشاء اعـلان⌯",'callback_data'=>"ilan" ]],
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
} 

if($data == "info") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
البوت الاول في التليجرام لزيادة متابعين الانستقرام بشكل فوري و سريع و بنسبة ثبات 99% 

    كل ماعليك هو دعوة اصدقائك من خلال الرابط الخاص بك وستحصل على متابعين مقابل كل شخص تحصل تدعوه تحصل على 10 نقاط
    
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
} 


if($data == "mstqbll") {
	if($rshq['rshaq'] == "on") {
	$ster = "مفتوح ✅" ;
	$wsfer = "يمكنك الرشق ✅" ;
	} else {
		$ster = "مقفل ❌" ;
		$wsfer = "لايمكنك الرشق حاليا اجمع نقاط لحد ما ينفتح ❌" ;
		} 
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
استقبال الرشق $ster
- $wsfer
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);

} 

#  توم 
# @s_p_p1 - @s_p_p1 

$e1=str_replace("/start Bero",null,$text); 
if(preg_match('/start Bero/',$text)){
	if($rshq['thoiler'][$e1]["to"] != null) {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
  لقد حصلت علي *". $rshq['thoiler'][$e1]["coin"]. "* نقاط من رابط التحويل
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
bot('sendMessage',[
   'chat_id'=>$rshq['thoiler'][$e1]["to"],
   'text'=>"
   تحويل مكتمل 💯
   
   معلومات الي دخل للرابط ✅
 اسمه : [$name](tg://user?id=$chat_id)
 ايديه : `$from_id`
 
 وتم تحويل". $rshq['thoiler'][$e1]["coin"]." نقاط لحسابه
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
$rshq['thoiler'][$e1]["to"] = null;
$rshq["coin"][$from_id] += $rshq['thoiler'][$e1]["coin"];
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} else {
	bot('sendMessage',[
   'chat_id'=>$from_id, 
   'text'=>"
   رابط التحويل هذا غير صالح ❌
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
	} 
} 
if($data == "acc") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*معلومات حسابك هي👇*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
      [['text'=>"نقاطـك",'callback_data'=>"coin" ],['text'=>"".$coin."",'callback_data'=>"coin" ]],
      [['text'=>"مـشاركة الرابط",'callback_data'=>"coin" ],['text'=>"".$share."",'callback_data'=>"coin" ]],
            [['text'=>"النقاط المصروفة",'callback_data'=>"coin" ],['text'=>"".$mytl."",'callback_data'=>"coin" ]],
        [['text'=>"الايدي",'callback_data'=>"coin" ],['text'=>"".$from_id."",'callback_data'=>"coin" ]],
              [['text'=>"مـعلوماتـك ".$user."",'callback_data'=>"coin" ]],
     [['text'=>"اموالك المسترجعه جزئيا",'callback_data'=>"coin" ],['text'=>"".$coinss."",'callback_data'=>"coin" ]],
   [['text'=>"الطلبات في البوت",'callback_data'=>"coin" ],['text'=>"". $tlby."",'callback_data'=>"coin" ]],
           [['text'=>"الطلبات المكتمله",'callback_data'=>"coin" ],['text'=>"".$tlby."",'callback_data'=>"coin" ]],
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
} 

 if($data == "service") {
 	if($rshaq == "✅") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"*
اختر البرنامج  المطلوب
*",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'تيليغرام 💙' ,'callback_data'=>"tele"]], 
[['text'=>'انستغرام 💜' ,'callback_data'=>"ini"]],
[['text'=>'تيكتوك 🖤' ,'callback_data'=>"tik"]],
[['text'=>'فيسبوك 🤍' ,'callback_data'=>"face"]],
[['text'=>'تويتر 💙' ,'callback_data'=>"twi"]], 
[['text'=>'يوتيوب ❤' ,'callback_data'=>"yot"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
]])
]);
} else {
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
تم قفل استقبال الرشق عزيزي

اجمع نقاط الان بين ما ينفتح الرشق
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[

[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
]])
]);
	} 
} 


if($data == "infotlb") {
 	
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
ارسل ايدي الطلب الان
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
]])
]);
    $rshq['mode'][$from_id]  = $data;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
}

if(is_numeric($text) and $rshq['mode'][$from_id] == "infotlb"){
	if($rshq["order"][$text] != null){
		$req = json_decode(file_get_contents("https://kd1s.com/api/v2?key=$Api_Tok&action=status&order=".$rshq["order"][$text]));
$startcc = $req->start_count; //224
$status = $req->remains; 
if($status == "0"){
	$s= "طلب مكتمل 🟢";
	}else{
		$s="قيد الانتضار ....";
		}
		bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
معلومات الطلب ،
حاله الطلب : $s
العدد قبل الرشق : $startcc
  ", 
 'parse_mode'=>"markdown",
 'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>'تحديث' ,'callback_data'=>"updates|".$rshq["order"][$text]]],
     [['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
$rshq['mode'][$from_id]  = null;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
}
}

if($e[0] == "updates"){
	$req = json_decode(file_get_contents("https://kd1s.com/api/v2?key=$Api_Tok&action=status&order=".$e[1]));
$startcc = $req->start_count; 
$status = $req->remains; 
if($status == "0"){
	$sberero= "طلب مكتمل 🟢";
	}else{
		$sberero="قيد الانتضار ....";
		}
		bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
تحديث رقم (".rand(9999,999999).")
معلومات الطلب ،
حاله الطلب : $sberero
العدد قبل الرشق : $startcc
  ", 
 'parse_mode'=>"markdown",
 'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>'تحديث' ,'callback_data'=>"updates|".$e[1]]],
     [['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
	}
if($e[0] == "type"){
	
	if($e[1] == "thbt" or $e[1] == "mthbt" or $e[1] == "hq" ) {
		$typee = "متابعين" ;
		} elseif($e[1] == "view"){
			$typee = "مشاهدات";
			}elseif($e[1] == "like"){
				$typee = "لايكات";
				}
		
		if($e[1] == "thbt") {
			$s3r = 1;
			}
			if($e[1] == "mthbt") {
			$s3r = 2;
			}
			if($e[1] == "hq") {
			$s3r = 0.2;
			}
			if($e[1] == "view") {
			$s3r = 25;
			}
			
			if($e[1] == "like") {
			$s3r = 18;
			}
			if($e[1] == "likrels") {
			$s3r = 3;
			}
			if($e[1] == "vuerils") {
			$s3r = 10;
			}
			if($e[1] == "foloarb") {
			$s3r = 0.3;
			}
			if($e[1] == "likkal") {
			$s3r = 1;
			}
			if($e[1] == "commlik") {
			$s3r = 0.8;
			}
			if($e[1] == "realkil") {
			$s3r = 3;
			}
			if($e[1] == "mixfla") {
			$s3r = 2;
			}
			if($e[1] == "ralvew") {
			$s3r = 3;
			}
			if($e[1] == "spefom") {
			$s3r = 3;
			}
			if($e[1] == "qwaty") {
			$s3r = 4;
			}
			if($e[1] == "livty") {
			$s3r = 5;
			}
			if($e[1] == "peptri") {
			$s3r = 2.1;
			}
			if($e[1] == "peobsvh") {
			$s3r = 1;
			}
			if($e[1] == "pelbxsvc") {
			$s3r = 0.8;
			}
			if($e[1] == "vionew") {
			$s3r = 25;
			}
			if($e[1] == "viwefiv") {
			$s3r = 19;
			}
			if($e[1] == "commionb") {
			$s3r = 0.5;
			}
			if($e[1] == "indiaco") {
			$s3r = 0.4;
			}
			if($e[1] == "taswet") {
			$s3r = 3;
			}
			if($e[1] == "thya") {
			$s3r = 6;
			}
			if($e[1] == "nothya") {
			$s3r = 6;
			}
			if($e[1] == "hartthu") {
			$s3r = 6;
			}
			if($e[1] == "firerak") {
			$s3r = 6;
			}
			if($e[1] == "starreak") {
			$s3r = 6;
			}
			if($e[1] == "surarek") {
			$s3r = 6;
			}
			if($e[1] == "demareak") {
			$s3r = 6;
			}
			if($e[1] == "sorkre") {
			$s3r = 6;
			}
			if($e[1] == "smirseb") {
			$s3r = 6;
			}
			if($e[1] == "kakarekt") {
			$s3r = 6;
			}
			if($e[1] == "targrekt") {
			$s3r = 6;
			}
			if($e[1] == "fackyourect") {
			$s3r = 6;
			}
			if($e[1] == "facepeb") {
			$s3r = 1;
			}
			if($e[1] == "favelik") {
			$s3r = 2;
			}
			if($e[1] == "faceegbo") {
			$s3r = 2.5;
			}
			if($e[1] == "facflk") {
			$s3r = 2.5;
			}
			if($e[1] == "facharch") {
			$s3r = 4;
			}
			if($e[1] == "sminshfacwc") {
			$s3r = 2.5;
			}
			if($e[1] == "wowrafv") {
			$s3r = 2.5;
			}
			if($e[1] == "sadface") {
			$s3r = 2.5;
			}
			if($e[1] == "angrefaceb") {
			$s3r = 2.5;
			}
			if($e[1] == "carefacec") {
			$s3r = 2.5;
			}
			if($e[1] == "comlikfav") {
			$s3r = 3;
			}
			if($e[1] == "viewvidfa") {
			$s3r = 5;
			}
			if($e[1] == "actoreface") {
			$s3r = 5;
			}
			if($e[1] == "viewyoutube") {
			$s3r = 0.6;
			}
			if($e[1] == "viewralyou") {
			$s3r = 1;
			}
			if($e[1] == "vierahfyou") {
			$s3r = 0.5;
			}
			if($e[1] == "likecomyo") {
			$s3r = 3;
			}
			if($e[1] == "likeyoufa") {
			$s3r = 1;
			}
			if($e[1] == "peopltik") {
			$s3r = 0.3;
			}
			if($e[1] == "liketikbr") {
			$s3r = 3;
			}
			if($e[1] == "tikviesto") {
			$s3r = 6;
			}
			if($e[1] == "freeviewtik") {
			$s3r = 18;
			}
			if($e[1] == "livliktk") {
			$s3r = 6;
			}
			if($e[1] == "sahretik") {
			$s3r = 5;
			}
			if($e[1] == "pepltwi") {
			$s3r = 0.3;
			}
			if($e[1] == "taswttwi") {
			$s3r = 1;
			}
			if($e[1] == "vidvitwi") {
			$s3r = 6;
			}
			if($e[1] == "menhtwi") {
			$s3r = 0.8;
			}
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
🙋‍♂️︙رشق توم

🎬︙يرجى إختيار نوع الرشق من الأسفل. 👇
⌯ نقاطك ➧ $coin
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>$nm.$s3r*100,'callback_data'=>"to|100|$e[1]"], ['text'=>'➧','callback_data'=>"to|100|$e[1]"], ['text'=>'100 نقطه','callback_data'=>"to|100|$e[1]"]], 
[['text'=>$nm.$s3r*200,'callback_data'=>"to|200|$e[1]"], ['text'=>'➧','callback_data'=>"to|200|$e[1]"], ['text'=>'200 نقطه' ,'callback_data'=>"to|200|$e[1]"]],
[['text'=>$nm.$s3r*300,'callback_data'=>"to|300|$e[1]"], ['text'=>'➧','callback_data'=>"to|300|$e[1]"], ['text'=>'300 نقطه' ,'callback_data'=>"to|300|$e[1]"]],
[['text'=>$nm.$s3r*400,'callback_data'=>"to|400|$e[1]"], ['text'=>'➧','callback_data'=>"to|400|$e[1]"], 
['text'=>'400 نقطه' ,'callback_data'=>"to|400|$e[1]"]],
[['text'=>'كميات كبيره' ,'callback_data'=>"kmiat|".$e[1]]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
]])
]);
} 

if($e[0] == "kmiat"){
	
	if($e[1] == "thbt" or $e[1] == "mthbt" or $e[1] == "hq" ) {
		$typee = "متابعين" ;
		} elseif($e[1] == "view"){
			$typee = "مشاهدات";
			}elseif($e[1] == "like"){
				$typee = "لايكات";
				}
		
		if($e[1] == "thbt") {
			$s3r = 1;
			}
			if($e[1] == "mthbt") {
			$s3r = 2;
			}
			if($e[1] == "hq") {
			$s3r = 0.2;
			}
			if($e[1] == "view") {
			$s3r = 25;
			}
			
			if($e[1] == "like") {
			$s3r = 18;
			}
			if($e[1] == "likrels") {
			$s3r = 3;
			}
				if($e[1] == "vuerils") {
			$s3r = 10;
			}
			if($e[1] == "foloarb") {
			$s3r = 0.3;
			}
			if($e[1] == "likkal") {
			$s3r = 1;
			}
			if($e[1] == "commlik") {
			$s3r = 0.8;
			}
			if($e[1] == "realkil") {
			$s3r = 3;
			}
			if($e[1] == "mixfla") {
			$s3r = 2;
			}
			if($e[1] == "ralvew") {
			$s3r = 3;
			}
			if($e[1] == "spefom") {
			$s3r = 3;
			}
			if($e[1] == "qwaty") {
			$s3r = 4;
			}
			if($e[1] == "livty") {
			$s3r = 5;
			}
			if($e[1] == "peptri") {
			$s3r = 2.1;
			}
			if($e[1] == "peobsvh") {
			$s3r = 1;
			}
			if($e[1] == "pelbxsvc") {
			$s3r = 0.8;
			}
			if($e[1] == "vionew") {
			$s3r = 25;
			}
			if($e[1] == "viwefiv") {
			$s3r = 19;
			}
			if($e[1] == "commionb") {
			$s3r = 0.5;
			}
			if($e[1] == "indiaco") {
			$s3r = 0.4;
			}
			if($e[1] == "taswet") {
			$s3r = 3;
			}
			if($e[1] == "thya") {
			$s3r = 6;
			}
			if($e[1] == "nothya") {
			$s3r = 6;
			}
			if($e[1] == "hartthu") {
			$s3r = 6;
			}
			if($e[1] == "firerak") {
			$s3r = 6;
			}
			if($e[1] == "starreak") {
			$s3r = 6;
			}
			if($e[1] == "surarek") {
			$s3r = 6;
			}
			if($e[1] == "demareak") {
			$s3r = 6;
			}
			if($e[1] == "sorkre") {
			$s3r = 6;
			}
			if($e[1] == "smirseb") {
			$s3r = 6;
			}
			if($e[1] == "kakarekt") {
			$s3r = 6;
			}
			if($e[1] == "targrekt") {
			$s3r = 6;
			}
			if($e[1] == "fackyourect") {
			$s3r = 6;
			}
			if($e[1] == "facepeb") {
			$s3r = 1;
			}
			if($e[1] == "favelik") {
			$s3r = 2;
			}
			if($e[1] == "faceegbo") {
			$s3r = 2.5;
			}
			if($e[1] == "facflk") {
			$s3r = 2.5;
			}
			if($e[1] == "facharch") {
			$s3r = 3;
			}
			if($e[1] == "sminshfacwc") {
			$s3r = 2.5;
			}
			if($e[1] == "wowrafv") {
			$s3r = 2.5;
			}
			if($e[1] == "sadface") {
			$s3r = 2.5;
			}
			if($e[1] == "angrefaceb") {
			$s3r = 2.5;
			}
			if($e[1] == "carefacec") {
			$s3r = 2.5;
			}
			if($e[1] == "comlikfav") {
			$s3r = 3;
			}
			if($e[1] == "viewvidfa") {
			$s3r = 5;
			}
			if($e[1] == "actoreface") {
			$s3r = 5;
			}
			if($e[1] == "viewyoutube") {
			$s3r = 0.6;
			}
			if($e[1] == "viewralyou") {
			$s3r =1;
			}
			if($e[1] == "vierahfyou") {
			$s3r =0.5;
			}
			if($e[1] == "likecomyo") {
			$s3r =2;
			}
			if($e[1] == "likeyoufa") {
			$s3r =1;
			}
			if($e[1] == "peopltik") {
			$s3r =0.3;
			}
			if($e[1] == "liketikbr") {
			$s3r =3;
			}
			if($e[1] == "tikviesto") {
			$s3r =5;
			}
			if($e[1] == "freeviewtik") {
			$s3r =18;
			}
			if($e[1] == "livliktk") {
			$s3r =6;
			}
			if($e[1] == "sahretik") {
			$s3r =5;
			}
			if($e[1] == "pepltwi") {
			$s3r =0.3;
			}
			if($e[1] == "taswttwi") {
			$s3r =1;
			}
			if($e[1] == "vidvitwi") {
			$s3r =6;
			}
			if($e[1] == "menhtwi") {
			$s3r =0.8;
			}
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
🙋‍♂️︙رشق توم

🎬︙يرجى إختيار نوع الرشق من الأسفل. 👇
⌯ نقاطك ➧ $coin
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>$nm.$s3r*1000,'callback_data'=>"to|1000|$e[1]"],['text'=>'➧','callback_data'=>"to|1000|$e[1]"], ['text'=>'1000 نقطه' ,'callback_data'=>"to|1000|$e[1]"]],
[['text'=>$nm.$s3r*2000,'callback_data'=>"to|2000|$e[1]"], ['text'=>'➧','callback_data'=>"to|2000|$e[1]"], ['text'=>'2000 نقطه' ,'callback_data'=>"to|2000|$e[1]"]],
[['text'=>$nm.$s3r*4000,'callback_data'=>"to|4000|$e[1]"], 
['text'=>'➧','callback_data'=>"to|4000|$e[1]"], 
['text'=>'4000 نقطه' ,'callback_data'=>"to|4000|$e[1]"]],
[['text'=>$nm.$s3r*8000,'callback_data'=>"to|8000|$e[1]"], ['text'=>'➧','callback_data'=>"to|8000|$e[1]"], 
['text'=>'8000 نقطه' ,'callback_data'=>"to|8000|$e[1]"]],
[['text'=>$nm.$s3r*10000,'callback_data'=>"to|10000|$e[1]"], ['text'=>'➧','callback_data'=>"to|10000|$e[1]"],
['text'=>'10000 نقطه' ,'callback_data'=>"to|10000|$e[1]"]],
[['text'=>$nm.$s3r*20000,'callback_data'=>"to|20000|$e[1]"], ['text'=>'➧','callback_data'=>"to|20000|$e[1]"], 
['text'=>'20000 نقطه' ,'callback_data'=>"to|400|$e[1]"]],

[['text'=>'رجوع' ,'callback_data'=>"type|". $e[1]]],
]])
]);
} 


if($e[0] == "to") {
	if($coin >= $e[1]){
		if($rshaq == "✅") {
			
	if($e[2] == "thbt") {
		$tlbia = "متابعين ثابتين 📌👤" ;
			$nm = "يوزر حسابك بدون @" ;
			$s3r = $e[1]*1;
			}
			if($e[2] == "mthbt") {
			$nm = "يوزر حسابك بدون @" ;
			$tlbia = "متابعين غير ثابتين ⭐" ;
			$s3r = $e[1]*2;
			}
			if($e[2] == "hq") {
				$tlbia = "متابعين حقيقيين 👤" ;
			$nm = "يوزر حسابك بدون @" ;
			$s3r = $e[1]*0.5;
			}
			if($e[2] == "view") {
				$tlbia = "مشاهدات 👁️" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*25;
			}
			if($e[2] == "like") {
				$tlbia = "لايكات ❤️" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*15;
			}
			if($e[2] == "likrels") {
				$tlbia = "لايكات ريلز" ;
			$nm = "رابط الريلز" ;
			$s3r = $e[1]*3;
			}
			if($e[2] == "vuerils") {
				$tlbia = "مشاهدات ريلز" ;
			$nm = "رابط الريلز" ;
			$s3r = $e[1]*10;
			}
			if($e[2] == "foloarb") {
				$tlbia = "متابيعن عربي" ;
			$nm = "رابط الحساب" ;
			$s3r = $e[1]*0.5;
			}
			if($e[2] == "commlik") {
				$tlbia = "لايكات تعليقات" ;
			$nm = "رابط الكومنت" ;
			$s3r = $e[1]*0.8;
			}
			if($e[2] == "realkil") {
				$tlbia = "لايكات انستجرام صاروخ" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*3;
			}
			if($e[2] == "mixfla") {
				$tlbia = "متابعين انستجرام مكس حقيقي" ;
			$nm = "رابط الحساب" ;
			$s3r = $e[1]*2;
			}
			if($e[2] == "ralvew") {
				$tlbia = "مشاهدات حقيقي" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*3;
			}
			if($e[2] == "spefom") {
				$tlbia = "متابعين من نوع خاص" ;
			$nm = "رابط الحساب" ;
			$s3r = $e[1]*3;
			}
			if($e[2] == "qwaty") {
				$tlbia = "متابعين انستقرام جودة عالية | فوري 🚀" ;
			$nm = "رابط الحساب" ;
			$s3r = $e[1]*4;
			}
			if($e[2] == "livty") {
				$tlbia = "لايكات بث مباشر" ;
			$nm = "رابط البث" ;
			$s3r = $e[1]*5;
			}
			if($e[2] == "peptri") {
				$tlbia = "اعضاء قنوات" ;
			$nm = "رابط القناه" ;
			$s3r = $e[1]*2.1;
			}
			if($e[2] == "peobsvh") {
				$tlbia = "اعضاء قنوات مع ضمان" ;
			$nm = "رابط القناه" ;
			$s3r = $e[1]*1;
			}
			if($e[2] == "pelbxsvc") {
				$tlbia = "اعضاء قنوات فارسي بدون ضمان" ;
			$nm = "رابط القناه" ;
			$s3r = $e[1]*0.8;
			}
			if($e[2] == "vionew") {
				$tlbia = "مشاهدات 1 بوست" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*25;
			}
			if($e[2] == "viwefiv") {
				$tlbia = "مشاهدات 5 اخر بوست" ;
			$nm = "رابط القناه" ;
			$s3r = $e[1]*19;
			}
			if($e[2] == "commionb") {
				$tlbia = "تعليقات عربي" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*0.5;
			}
			if($e[2] == "indiaco") {
				$tlbia = "تعليقات هندي" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*0.4;
			}
			if($e[2] == "taswet") {
				$tlbia = "تصويتات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*3;
			}
			if($e[2] == "thya") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "nothya") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "hartthu") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "firerak") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "starreak") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "surarek") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "demareak") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "sorkre") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "smirseb") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "kakarekt") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "targrekt") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "fackyourect") {
				$tlbia = "تفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "facepeb") {
				$tlbia = "متابعين" ;
			$nm = "رابط الحساب" ;
			$s3r = $e[1]*1;
			}
			if($e[2] == "favelik") {
				$tlbia = "لايكات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*2;
			}
			if($e[2] == "faceegbo") {
				$tlbia = "لايكات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*2.5;
			}
			if($e[2] == "facflk") {
				$tlbia = "لايكات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*2.5;
			}
			if($e[2] == "facharch") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*3;
			}
			if($e[2] == "sminshfacwc") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*2.5;
			}
			if($e[2] == "wowrafv") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*2.5;
			}
			if($e[2] == "sadface") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*2.5;
			}
			if($e[2] == "angrefaceb") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*2.5;
			}
			if($e[2] == "carefacec") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*2.5;
			}
			if($e[2] == "comlikfav") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*3;
			}
			if($e[2] == "viewvidfa") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*5;
			}
			if($e[2] == "actoreface") {
				$tlbia = "نفاعلات" ;
			$nm = "رابط المنشور" ;
			$s3r = $e[1]*5;
			}
			if($e[2] == "tikviesto") {
				$tlbia = "مشاهدات" ;
			$nm = "رابط الفديو" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "viewyoutube") {
				$tlbia = "مشاهدات" ;
			$nm = "رابط الفديو" ;
			$s3r = $e[1]*0.6;
			}
			if($e[2] == "viewralyou") {
				$tlbia = "مشاهدات" ;
			$nm = "رابط الفديو" ;
			$s3r = $e[1]*1;
			}
			if($e[2] == "vierahfyou") {
				$tlbia = "مشاهدات" ;
			$nm = "رابط البث" ;
			$s3r = $e[1]*0.5;
			}
			if($e[2] == "likecomyo") {
				$tlbia = "لايكات" ;
			$nm = "رابط التعليق" ;
			$s3r = $e[1]*2;
			}
			if($e[2] == "likeyoufa") {
				$tlbia = "لايكات" ;
			$nm = "رابط الفديو" ;
			$s3r = $e[1]*1;
			}
			if($e[2] == "peopltik") {
				$tlbia = "متابعين" ;
			$nm = "رابط الحساب" ;
			$s3r = $e[1]*0.3;
			}
			if($e[2] == "liketikbr") {
				$tlbia = "لايكات" ;
			$nm = "رابط الفديو" ;
			$s3r = $e[1]*3;
			}
			if($e[2] == "freeviewtik") {
				$tlbia = "مشاهدات" ;
			$nm = "رابط الفديو" ;
			$s3r = $e[1]*18;
			}
			if($e[2] == "livliktk") {
				$tlbia = "لايكات" ;
			$nm = "رابط البث" ;
			$s3r = $e[1]*18;
			}
			if($e[2] == "sahretik") {
				$tlbia = "مشاركات" ;
			$nm = "رابط الفديو" ;
			$s3r = $e[1]*5;
			}
			if($e[2] == "pepltwi") {
				$tlbia = "متابعين" ;
			$nm = "رابط الحساب" ;
			$s3r = $e[1]*0.3;
			}
			if($e[2] == "taswttwi") {
				$tlbia = "تصويت" ;
			$nm = "رابط التصويت" ;
			$s3r = $e[1]*1;
			}
			if($e[2] == "vidvitwi") {
				$tlbia = "مشاهدات" ;
			$nm = "رابط الفديو" ;
			$s3r = $e[1]*6;
			}
			if($e[2] == "menhtwi") {
				$tlbia = "منشن" ;
			$nm = "رابط المنشن" ;
			$s3r = $e[1]*0.8;
			}
			
			bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
 ~ تم استقطاع *$e[1]* من نقاطك. 
*
ارسل $nm
*
",
'parse_mode'=>"markdown",
]);
$rshq['3dd'][$from_id][$from_id]  = $s3r;
    $rshq['mode'][$from_id]  = "to";
    $rshq["coin"][$from_id] -= $e[1];
    $rshq["tlbia"][$from_id] = $tlbia;
    $rshq["cointlb"][$from_id] += $e[1];
    $rshq["s3rltlb"][$from_id] = $e[1];
    $rshq['tp'][$from_id] = $e[2];
    $rshq['coinn'] = $s3r;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} else {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
تم قفل استقبال الرشق عزيزي

اجمع نقاط الان علماينفتح الرشق
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[

[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
]])
]);
} 

} else {
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
نقاطك غير كافية
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"جمع النقاط",'callback_data'=>"plus" ]],
       
      ]
    ])
]);
} 
} 

$rshqaft =$rshq['bot_tlb']+1;
$rnd = rand(9999999,9999999999);
if($text and $rshq['mode'][$from_id]  == "to") {
	
	if($rshq['tp'][$from_id] == "thbt") {
			$nm = "يوزر حسابك" ;
			$tp = "متابع" ;
			$inid =9650;
			}
			if($rshq['tp'][$from_id] == "mthbt") {
			$nm = "يوزر حسابك" ;
			$tp = "متابع" ;
			$inid =9650;
			}
			if($rshq['tp'][$from_id] == "hq") {
			$nm = "يوزر حسابك" ;
			$tp = "متابع" ;
			$inid =9650;
			}
			if($rshq['tp'][$from_id] == "view") {
			$nm = "رابط المنشور" ;
			$tp = "مشاهد" ;
			$inid =5132;
			}
			if($rshq['tp'][$from_id] == "like") {
			$nm = "رابط المنشور" ;
			$tp = "لايك" ;
			$inid =9168;
			}
			if($rshq['tp'][$from_id] == "likrels") {
			$nm = "رابط الريلز" ;
			$tp = "لايك" ;
			$inid =8303;
			}
				if($rshq['tp'][$from_id] == "vuerils") {
			$nm = "رابط الريلز" ;
			$tp = "مشاهدات" ;
			$inid =7921;
			}
if($rshq['tp'][$from_id] == "foloarb") {
			$nm = "رابط الحساب" ;
			$tp = "متابيعن" ;
			$inid =5166;
			}
if($rshq['tp'][$from_id] == "commlik") {
			$nm = "رابط الكومنت" ;
			$tp = "لايكات" ;
			$inid =5788;
			}
if($rshq['tp'][$from_id] == "realkil") {
			$nm = "رابط المنشور" ;
			$tp = "لايكات" ;
			$inid =5087;
			}			
if($rshq['tp'][$from_id] == "mixfla") {
			$nm = "رابط الحساب" ;
			$tp = "متابعين" ;
			$inid =5081;
			}					
if($rshq['tp'][$from_id] == "ralvew") {
			$nm = "رابط المنشور" ;
			$tp = "مشاهدات" ;
			$inid =5198;
			}						
if($rshq['tp'][$from_id] == "spefom") {
			$nm = "رابط الحساب" ;
			$tp = "متابعين" ;
			$inid =7871;
			}	
if($rshq['tp'][$from_id] == "qwaty") {
			$nm = "رابط الحساب" ;
			$tp = "متابعين" ;
			$inid =9042;
			}				
if($rshq['tp'][$from_id] == "livty") {
			$nm = "رابط البث" ;
			$tp = "لايكات" ;
			$inid =5919;
			}						if($rshq['tp'][$from_id] == "peptri") {
			$nm = "رابط القناه" ;
			$tp = "متابعين" ;
			$inid =8504;
			}				        
if($rshq['tp'][$from_id] == "peobsvh") {
			$nm = "رابط القناه" ;
			$tp = "متابعين" ;
			$inid =10266;
			}	
if($rshq['tp'][$from_id] == "pelbxsvc") {
			$nm = "رابط القناه" ;
			$tp = "متابعين" ;
			$inid =10316;
			}	
				if($rshq['tp'][$from_id] == "vionew") {
			$nm = "رابط المشور" ;
			$tp = "مشاهدات" ;
			$inid =10401;
			}	
if($rshq['tp'][$from_id] == "viwefiv") {
			$nm = "رابط القناه" ;
			$tp = "مشاهدات" ;
			$inid =10402;
			}
if($rshq['tp'][$from_id] == "commionb") {
			$nm = "رابط المنشور" ;
			$tp = "تعليقات" ;
			$inid =8584;
			}					if($rshq['tp'][$from_id] == "indiaco") {
			$nm = "رابط المنشور" ;
			$tp = "تعليقات" ;
			$inid =8587;
			}				
if($rshq['tp'][$from_id] == "taswet") {
			$nm = "رابط المنشور" ;
			$tp = "تصويتات" ;
			$inid =9481;
			}						if($rshq['tp'][$from_id] == "thya") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8593;
			}		
if($rshq['tp'][$from_id] == "nothya") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8594;
			}				
if($rshq['tp'][$from_id] == "hartthu") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8595;
			}				
if($rshq['tp'][$from_id] == "firerak") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8596;
			}			
if($rshq['tp'][$from_id] == "starreak") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8598;
			}		
if($rshq['tp'][$from_id] == "surarek") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8597;
			}		
if($rshq['tp'][$from_id] == "demareak") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8599;
			}					
if($rshq['tp'][$from_id] == "sorkre") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8600;
			}	
if($rshq['tp'][$from_id] == "smirseb") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8601;
			}		
if($rshq['tp'][$from_id] == "kakarekt") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8602;
			}		
if($rshq['tp'][$from_id] == "targrekt") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =8603;
			}		
if($rshq['tp'][$from_id] == "fackyourect") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =10559;
			}						if($rshq['tp'][$from_id] == "facepeb") {
			$nm = "رابط الحساب" ;
			$tp = "متابعين" ;
			$inid =10540;
			}			
if($rshq['tp'][$from_id] == "favelik") {
			$nm = "رابط المنشور" ;
			$tp = "لايكات" ;
			$inid =6020;
			}			
if($rshq['tp'][$from_id] == "faceegbo") {
			$nm = "رابط المنشور" ;
			$tp = "لايكات" ;
			$inid =6043;
			}					
if($rshq['tp'][$from_id] == "facflk") {
			$nm = "رابط المنشور" ;
			$tp = "لايكات" ;
			$inid =6046;
			}						if($rshq['tp'][$from_id] == "facharch") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =7094;
			}			
if($rshq['tp'][$from_id] == "sminshfacwc") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =7095;
			}			
if($rshq['tp'][$from_id] == "wowrafv") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =7098;
			}			
if($rshq['tp'][$from_id] == "sadface") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =7096;
			}						if($rshq['tp'][$from_id] == "angrefaceb") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =7097;
			}		
if($rshq['tp'][$from_id] == "carefacec") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =7099;
			}				
if($rshq['tp'][$from_id] == "comlikfav") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =6053;
			}			
if($rshq['tp'][$from_id] == "viewvidfa") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =6057;
			}					
if($rshq['tp'][$from_id] == "actoreface") {
			$nm = "رابط المنشور" ;
			$tp = "تفاعلات" ;
			$inid =10383;
			}		
if($rshq['tp'][$from_id] == "viewyoutube") {
			$nm = "رابط الفديو" ;
			$tp = "مشاهدات" ;
			$inid =6128;
			}						if($rshq['tp'][$from_id] == "viewralyou") {
			$nm = "رابط الفديو" ;
			$tp = "مشاهدات" ;
			$inid =6088;
			}				
if($rshq['tp'][$from_id] == "vierahfyou") {
			$nm = "رابط البث" ;
			$tp = "مشاهدات" ;
			$inid =6139;
			}						if($rshq['tp'][$from_id] == "likecomyo") {
			$nm = "رابط التعليق" ;
			$tp = "لايكات" ;
			$inid =8372;
			}	
if($rshq['tp'][$from_id] == "likeyoufa") {
			$nm = "رابط الفديو" ;
			$tp = "لايكات" ;
			$inid =6180;
			}						
if($rshq['tp'][$from_id] == "peopltik") {
			$nm = "رابط الحساب" ;
			$tp = "متابعين" ;
			$inid =10498;
			}			
if($rshq['tp'][$from_id] == "liketikbr") {
			$nm = "رابط الفديو" ;
			$tp = "لايكات" ;
			$inid =6267;
			}			
if($rshq['tp'][$from_id] == "tikviesto") {
			$nm = "رابط الفديو" ;
			$tp = "مشاهدات" ;
			$inid =10451;
			}						if($rshq['tp'][$from_id] == "freeviewtik") {
			$nm = "رابط الفديو" ;
			$tp = "مشاهدات" ;
			$inid =9308;
			}				
if($rshq['tp'][$from_id] == "livliktk") {
			$nm = "رابط البث" ;
			$tp = "لايكات" ;
			$inid =9619;
			}						
if($rshq['tp'][$from_id] == "sahretik") {
			$nm = "رابط الفديو" ;
			$tp = "مشاركات" ;
			$inid =6285;
			}				
if($rshq['tp'][$from_id] == "pepltwi") {
			$nm = "رابط الحساب" ;
			$tp = "متابعين" ;
			$inid =6307;
			}				
if($rshq['tp'][$from_id] == "taswttwii") {
			$nm = "رابط التصويت" ;
			$tp = "تصويتات" ;
			$inid =6336;
			}			
if($rshq['tp'][$from_id] == "vidvitwi") {
			$nm = "رابط الفديو" ;
			$tp = "مشاهدات" ;
			$inid =6349;
			}				
if($rshq['tp'][$from_id] == "menhtwi") {
			$nm = "رابط المنشن" ;
			$tp = "منشنات" ;
			$inid =8634;
			}					
			
			
			$requst = json_decode(file_get_contents("https://kd1s.com/api/v2?key=$Api_Tok&action=add&service=$inid&link=$text&quantity=". $rshq['3dd'][$from_id][$from_id]));
$idreq = $requst->order; 
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
تم ارسال طلبك بنجاح ✅
- - - - - - - - - - - - - - - - - - 
رقم طلبك : `". $rnd."`
العدد : *". $rshq['3dd'][$from_id][$from_id] . "* $tp
$nm : [$text]
- - - - - - - - - - - - - - - - - - 
سيتم ارسال ال". $tp. "ات في غصون دقائق
  ", 
 'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"طلب مراجعه الطلب ✅",'callback_data'=>"sendrq|$idreq|$rnd|". $rshq["s3rltlb"][$from_id] ]],
       
      ]
    ])
]);
bot('sendMessage',[
   'chat_id'=>$admin,
   'text'=>"
⌯طلب جديد ⌯
▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱
معلومات العضو 
ايديه : `$from_id`
يوزره : [@$user]
اسمه : [$name](tg://user?id=$chat_id)

معلومات الطلب ~
ايدي الطلب : `". $rnd. "`
". str_replace("يوزر حسابك", "يوزر", $nm). " : [$text]
العدد". $rshq['3dd'][$from_id][$from_id] . " $tp

نقاطه : ". $rshq["coin"][$from_id]. "
- - - - - - - - - - - - - - - - - - 
  ", 
 'parse_mode'=>"markdown",
 'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"ترجيع نقاطه",'callback_data'=>"ins|$from_id|". $rshq['coinn']]],
     [['text'=>"طلب تعويض تلقائيا",'callback_data'=>"tEwth|$idreq"]],
     [['text'=>"تصفير نقاطه",'callback_data'=>"msft|$from_id"]],
       
      ]
    ])
]);
bot('sendMessage',[
   'chat_id'=>$chnl,
   'text'=>"
✅ اكتمل طـلب الخدمة بنجاح .
- - - - - - - - - - - - - - - - - - 
ايدي الطلب : `". $rnd. "`
نوع الطلب :". $rshq["tlbia"][$from_id]. "
سعر الطلب :". $rshq["s3rltlb"][$from_id]. "
". str_replace("يوزر حسابك", "يوزر", $nm). " : [$text]
العدد ". $rshq['3dd'][$from_id][$from_id] . " $tp
حساب المشتري : [$name](tg://user?id=$chat_id)
الرقم التسلسلي للطلب : *". $rshqaft." * 
- - - - - - - - - - - - - - - - - - 
  ", 
 'parse_mode'=>"markdown",
 'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"Social Plus ➕",'url'=>"https://t.me/". bot('getme','bot')->result->username]],
       
      ]
    ])
]);
$rshq["order"][$rnd]= $idreq;
$rshq["tlby"][$from_id] += 1;
$rshq['3dd'][$from_id][$from_id]  = null;
    $rshq['mode'][$from_id]  = null;
    $rshq['bot_tlb']+= 1;
    
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 
 
if($e[0] == "msft" and $from_id == $admin) {
	$requst = json_decode(file_get_contents("https://kd1s.com/api/v2?key=$Api_Tok&action=refil&order=$e[1]"));
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"

تم تصفير نقاطه ✅
ايديه : [$e[1]](tg://user?id=$e[1]])

",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
$rshq["coin"][$e[1]] = 0;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq); 
	} 
	
if($e[0] == "tEwth" and $from_id == $admin) {
	$requst = json_decode(file_get_contents("https://kd1s.com/api/v2?key=$Api_Tok&action=refil&order=$e[1]"));
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"

تم طلب تعويض تلقائي للطلب
ايدي الطلب `$e[1]`

",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
	} 
	
	if($e[0] == "sendrq" and $from_id == $admin) {
	$requst = json_decode(file_get_contents("https://kd1s.com/api/v2?key=$Api_Tok&action=refil&order=$e[1]"));
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"

تم طلب مراجعه طلبك بنجاح ✅
ايدي الطلب `$e[2]`

",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);

bot('sendMessage',[
   'chat_id'=>$admin,
   'text'=>"
طلب مراجعه للطلب عزيزي المطور ✨
- - - - - - - - - - - - - - - - - - 
ايدي الطلب : `". $e[2]. "`
الي داز الطلب : [$name](tg://user?id=$chat_id)
- - - - - - - - - - - - - - - - - - 
  ", 
 'parse_mode'=>"markdown",
 'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"ترجيع نقاطه",'callback_data'=>"ins|$from_id|". $e[3]]],
       
      ]
    ])
]);
	} 

if($e[0] == "ins" and $from_id == $admin) {
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"

تم ارجاع $e[2] نقاط لحساب [$e[1]](tg://user?id=$e[1])

",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"back" ]],
       
      ]
    ])
]);
$rshq["coin"][$e[1]] += $e[2];

$rshq["coinss"][$e[1]] += $e[2];
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
	}
	
	if($data == "Asiacell") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
اهلا بك في قسم الشحن التلقائي ✨

يمكنك شحن نقاطك تلقائيا من خلال هذا القسم 🔥
    
    يمكنك شحن نقاطك من خلال (ارسال كارت اسيا، تحويل الرصيد) 
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"شحن عن طريق تحويل الرصيد",'callback_data'=>"rsedd|thoil" ], ['text'=>"شحن عن طريق كارتات",'callback_data'=>"rsedd|cart" ]],
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
} 

if($e[0] == "rsedd") {
	
	if($e[1] == "thoil") {
		$TypeShhn = "تحويل الرصيد" ;
		$ws = "
حول الرصيد الي هذا الرقم ($nmbr) 💠

في حال حولت الرصيد ارسل رقمك للبوت ليتم تأكيد طلبك ♻️
" ;
		} elseif($e[1] == "cart") {
			$TypeShhn = "كارت اسيا" ;
			$ws = "الان ارسل رقم الكارت ✴️" ;
			} 
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
  ⚡ : رائع لقد تخترت الشحن عن طريق ($TypeShhn) 
  - $ws
*

",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
$rshq['shhn'][$from_id] = $e[1];
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 
 
 
 if(is_numeric($text) and $rshq['shhn'][$from_id ] != null) {
 	if($rshq['shhn'][$from_id] == "thoil") {
		$TypeShhn = "تحويل الرصيد" ;
		$ws = "
رقمك : $text


" ;
$mshkl = "مامحول الرصيد سيتم حظرك نهائيا من البوت" ;
		} elseif($rshq['shhn'][$from_id] == "cart") {
			$TypeShhn = "ارسال كارت اسيا" ;
			$ws = "رقم الكارت : `$text`" ;
			$mshkl = "ارسلت رقم الكارت غلط سيتم حظرك نهائيا من البوت" ;
			} 
 bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
  نوع طلبك : $TypeShhn
  $ws
  سيتم مراجعه طلبك خلال 24 ساعه في حال كنت $mshkl
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);

bot('sendMessage',[
   'chat_id'=>$admin,
   'text'=>"
طلب شحن تلقائي ✅

الشحن عن طريق : $TypeShhn

". str_replace("رقمك", "رقم الشخص", $ws). "
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"تأكيد طلبه ⚡",'callback_data'=>"ok|". $from_id ]],
       
      ]
    ])
]);
$rshq['shhn'][$from_id] = null;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 

if($e[0] == "ok") {
	if($chat_id == $admin) { 
	bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
  تم تأكيد طلبه بنجاح ✅
  *
  ايدي الشخص `$e[1]`
  ~ [$e[1]](tg://user?id=$e[1])
  
  الآن ارسل عدد النقاط المراد ارسال له


",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"tobot" ]],
       
      ]
    ])
]);
$rshq['mode'][$from_id]  = "shneru" ;
$rshq['coi'][$from_id]  = $e[1] ;
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 
} 

if(is_numeric($text) and $rshq['mode'][$from_id]== "shneru" ){
	if($chat_id == $admin) {
	bot('sendMessage',[
   'chat_id'=>$chat_id,
   'text'=>"
   تم تأكيد طلبه في الشحن التلقائي و
 تم ارسال $text نقاط ل [$name](tg://user?id=$chat_id) 
  ", 
  'parse_mode'=>"markdown",
  'reply_markup'=>json_encode([
     'inline_keyboard'=>[
     [['text'=>"رجوع",'callback_data'=>"back" ]],
       
      ]
    ])
]);
bot('sendMessage',[
   'chat_id'=>$rshq['coi'][$from_id], 
   'text'=>"
~ تم تأكيد طلبك بنجاح (شحن التلقائي) ✅

وتم ارسال $text نقاط لحسابك
  ", 
  'parse_mode'=>"markdown",
  
]);
$rshq['mode'][$from_id]  = null ;
$rshq["coin"][$rshq['coi'][$from_id]] += $text;
$rshq['coi'][$from_id] = null; 
$rshq= json_encode($rshq,32|128|265);
file_put_contents("rshq.json",$rshq);
} 
} 
if($data == "ini"){ 
        bot('answercallbackquery',[
            'callback_query_id'=>$update->callback_query->id,
            'text'=>"
انتظر ثانيه جاري الدخول 🤖
",
]);
}
if($data == "ini") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
✅︙خدمات (التزويد) لـ انستجرام Instagram.
🛒︙يرجى إختيار إحدى الخدمات من الأسفل.
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'متابعين ثابتين' ,'callback_data'=>"type|thbt"],['text'=>'متابعين غير ثابتين' ,'callback_data'=>"type|mthbt"]],
[['text'=>'متابعين حقيقيين' ,'callback_data'=>"type|hq"]],
[['text'=>'لايكات' ,'callback_data'=>"type|like"], ['text'=>'مشاهدين' ,'callback_data'=>"type|view"]],
[['text'=>'لايكات ريلز' ,'callback_data'=>"type|likrels"], ['text'=>'مشاهدات ريلز' ,'callback_data'=>"type|vuerils"]],
[['text'=>'متابعين انستجرام عربي' ,'callback_data'=>"type|foloarb"], ['text'=>'لايكات انستجرام خليجي ' ,'callback_data'=>"type|likkal"]],
[['text'=>'لايكات تعليقات' ,'callback_data'=>"type|commlik"], ['text'=>'لايكات انستجرام حقيقي ' ,'callback_data'=>"type|realkil"]],
[['text'=>'متابعين انستجرام مكس حقيقي' ,'callback_data'=>"type|mixfla"]], 
[['text'=>'مشاهدات حقيقي' ,'callback_data'=>"type|ralvew"], ['text'=>'متابعين نوع خاص' ,'callback_data'=>"type|spefom"]],
[['text'=>'متابعين انستقرام جودة عالية | فوري 🚀' ,'callback_data'=>"type|qwaty"]],
[['text'=>'لايكات بث مباشر' ,'callback_data'=>"type|livty"]],
[['text'=>'معلومات طلب' ,'callback_data'=>"infotlb"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "tele"){ 
        bot('answercallbackquery',[
            'callback_query_id'=>$update->callback_query->id,
            'text'=>"
انتظر ثانيه جاري الدخول 🤖
",
]);
}
if($data == "tele") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
✅︙خدمات (التزويد) لـ تيليجرام Telegram.
🛒︙يرجى إختيار إحدى الخدمات من الأسفل.
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'اعضاء القناة العامة / المجموعة' ,'callback_data'=>"type|peptri"]],
[['text'=>'تيليجرام اعضاء [الضمان 30 يوم]' ,'callback_data'=>"type|peobsvh"]],
[['text'=>'تيليجرام اعضاء [فارسي] [بدون ضمان]' ,'callback_data'=>"type|pelbxsvc"]],
[['text'=>'مشاهدة تلي 1 بوست' ,'callback_data'=>"type|vionew"]], 
[['text'=>'مشاهدة تلي آخر 5 بوست' ,'callback_data'=>"type|viwefiv"],['text'=>'قـسم ريكشانات' ,'callback_data'=>"reakhan"]],
[['text'=>'تعليقات تيليجرام عربي عشوائية' ,'callback_data'=>"type|commionb"]], 
[['text'=>'تعليقات تلجرام هندي' ,'callback_data'=>"type|indiaco"]],
[['text'=>'تصـويت بـدون مغاديه' ,'callback_data'=>"type|taswet"]],
[['text'=>'معلومات طلب' ,'callback_data'=>"infotlb"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "reakhan") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
اهلا بك في قسم ريكشانات (تفاعلات)
اختر الريكشان الذي تريد رشقه
ملحوظه : كل رياكشن ياتي معه رشق مشاهدات
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'👍' ,'callback_data'=>"type|thya"],['text'=>'👎' ,'callback_data'=>"type|nothya"],['text'=>'❤️' ,'callback_data'=>"type|hartthu"]],
[['text'=>'🔥' ,'callback_data'=>"type|firerak"], ['text'=>'	
🎉' ,'callback_data'=>"type|surarek"],['text'=>'🤩' ,'callback_data'=>"type|starreak"]],
[['text'=>'😢' ,'callback_data'=>"type|demareak"], ['text'=>'😱' ,'callback_data'=>"type|sorkre"],['text'=>'😁' ,'callback_data'=>"type|smirseb"]],
[['text'=>'💩' ,'callback_data'=>"type|kakarekt"], ['text'=>'🤮' ,'callback_data'=>"type|targrekt"],['text'=>' 🖕' ,'callback_data'=>"type|fackyourect"]],
[['text'=>'معلومات طلب' ,'callback_data'=>"infotlb"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "sales") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
هذه هي كل عروض اليوم🚀
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
[['text'=>'مشاهدة تلي 1 بوست' ,'callback_data'=>"type|vionew"]], 
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "face"){ 
        bot('answercallbackquery',[
            'callback_query_id'=>$update->callback_query->id,
            'text'=>"
انتظر ثانيه جاري الدخول 🤖
",
]);
}
if($data == "face") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
✅︙خدمات (التزويد) لـ فيس بوك facebook.
🛒︙يرجى إختيار إحدى الخدمات من الأسفل.
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'متابعين بروفايل فيسبوك سريع 🚀' ,'callback_data'=>"type|facepeb"]],
[['text'=>'لايكات فيس بوك مكس حقيقي' ,'callback_data'=>"type|favelik"]],
[['text'=>'لايكات فيس بوك مصر فوري 🇪🇬' ,'callback_data'=>"type|faceegbo"]],
[['text'=>'لايكات فيس بوك الفلبين فوري ⭐' ,'callback_data'=>"type|facflk"]], 
[['text'=>'لايكات تعليقات فيسبوك ' ,'callback_data'=>"type|comlikfav"],['text'=>'قـسم تفاعلات' ,'callback_data'=>"facera"]],
[['text'=>'مشاهدات فيديو فيسبوك' ,'callback_data'=>"type|viewvidfa"]], 
[['text'=>'مشاهدات ستوري فيسبوك' ,'callback_data'=>"type|actoreface"]],
[['text'=>'معلومات طلب' ,'callback_data'=>"infotlb"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "facera") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
اهلا بك في قسم ريكشانات (تفاعلات)
اختر الريكشان الذي تريد رشقه
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'😲' ,'callback_data'=>"type|wowrafv"],['text'=>'😍' ,'callback_data'=>"type|facharch"],['text'=>'😀' ,'callback_data'=>"type|sminshfacwc"]],
[['text'=>'😢' ,'callback_data'=>"type|sadface"], ['text'=>'	
😡' ,'callback_data'=>"type|angrefaceb"],['text'=>'🥰' ,'callback_data'=>"type|carefacec"]],
[['text'=>'معلومات طلب' ,'callback_data'=>"infotlb"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "yot"){ 
        bot('answercallbackquery',[
            'callback_query_id'=>$update->callback_query->id,
            'text'=>"
انتظر ثانيه جاري الدخول 🤖
",
]);
}
if($data == "yot") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
✅︙خدمات (التزويد) لـ يوتيوب youtube.
🛒︙يرجى إختيار إحدى الخدمات من الأسفل.
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'مشاهدات يوتيوب بالساعات [1-12 ساعة]' ,'callback_data'=>"type|viewyoutube"]],
[['text'=>'مشاهدات يتيوب حقيقي من كل العالم' ,'callback_data'=>"type|viewralyou"]],
[['text'=>'مشاهدات يوتيوب بث مباشر حقيقي 100k 👍👌' ,'callback_data'=>"type|vierahfyou"]],
[['text'=>'لايكات تعليقات يوتيوب' ,'callback_data'=>"type|likecomyo"]], 
[['text'=>'لايكات يوتيوب فوري سريع ' ,'callback_data'=>"type|likeyoufa"]],
[['text'=>'معلومات طلب' ,'callback_data'=>"infotlb"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "tik"){ 
        bot('answercallbackquery',[
            'callback_query_id'=>$update->callback_query->id,
            'text'=>"
انتظر ثانيه جاري الدخول 🤖
",
]);
}
if($data == "tik") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
✅︙خدمات (التزويد) لـ تيك  Tik Tok.
🛒︙يرجى إختيار إحدى الخدمات من الأسفل.
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'متابعين تيك توك سريع 🚀' ,'callback_data'=>"type|peopltik"]],
[['text'=>'لايكات تيك توك حقيقي فوري البرازيل  🇧🇷' ,'callback_data'=>"type|liketikbr"]],
[['text'=>'مشاهدات تيك توك لجميع الستوريات 💩' ,'callback_data'=>"type|tikviesto"]],
[['text'=>'مشاهدات تيك توك الأرخص 🔥' ,'callback_data'=>"type|freeviewtik"]], 
[['text'=>'لايكات على بث مباشر تيك توك| سريع جداً 👍 ' ,'callback_data'=>"type|livliktk"]],
[['text'=>'تيك توك المشاركه 70k' ,'callback_data'=>"type|sahretik"]], 
[['text'=>'معلومات طلب' ,'callback_data'=>"infotlb"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "twi"){ 
        bot('answercallbackquery',[
            'callback_query_id'=>$update->callback_query->id,
            'text'=>"
انتظر ثانيه جاري الدخول 🤖
",
]);
}
if($data == "twi") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
✅︙خدمات (التزويد) لـ تويتر Twitter.
🛒︙يرجى إختيار إحدى الخدمات من الأسفل.
*
",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'متابعين تويتر حقيقي' ,'callback_data'=>"type|pepltwi"]],
[['text'=>'تصويت تويتر' ,'callback_data'=>"type|taswttwi"]],
[['text'=>'مشاهدات فيديو تويتر' ,'callback_data'=>"type|vidvitwi"]],
[['text'=>'منشن تويتر من متابعين حساب' ,'callback_data'=>"type|menhtwi"]], 
[['text'=>'معلومات طلب' ,'callback_data'=>"infotlb"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "ilan") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
⌯ بوت الرشق الاول في التلجرام📢
⌯ اسرع بوت في الرشق في التلجرام
⌯ اسهل جرق التجميع🚀
➧ ارخص الاسعار 🤩
⌯ رشق جميع مواقع التواصل 
➧⌯⌯⌯⌯⌯⌯⌯⌯⌯الاربط ⌯⌯⌯⌯⌯⌯⌯⌯⌯
*
https://t.me/". bot('getme','bot')->result->username. "?start=$from_id


",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[

[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($text == '/help' or $text == '/help'){ 
bot('sendphoto',['chat_id'=>$chat_id,
photo =>"https://www.google.com/imgres?imgurl=https%3A%2F%2Fswiftassess.com%2Fwp-content%2Fuploads%2F2020%2F08%2FSupport-21-e1598864796732.png&tbnid=2N2KpFSxhI2DRM&vet=1&imgrefurl=https%3A%2F%2Fswiftassess.com%2Far%2Fservices%2Fsupport-services&docid=8W2D6i7Z1DuJZM&w=600&h=525&hl=ar-EG&source=sh%2Fx%2Fim",
'caption'=>'
*
☆︙بوت رشق Namero < 🦈

≪━━━━━━━الشرح 🌟━━━━━━━≫
☆︙تقدر تجمع نقاط بسهوله من زر تجميع النقاط والتي تحتوي علي :
1 : دعوه الاصدقاء 🙋‍♂
2 : تسليم أرقام للبوت 📞
3 : عجله الحظ 🎡
4 : شراء نقاط من المطور 📱
≪━━━━━طريقه الرشق 👇━━━━≫
1 : اضغط على زر الخدمات
2 : اختر التطبيق 
3 : اختر الخدمة
4 : قم بإختيار العدد
5 : قم بإرسال الرابط

وسيتم الرشق تلقائياً🥱
≪━━━━━━━للتواصل━━━━━━━≫
الدعم : @Namero 

*
', 
'reply_to_message_id'=>$message->message_id,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[['text'=>'المطور','url'=>'t.me/Namero ']],
[['text'=>'قـناة المطور','url'=>'t.me/s_p_p1']], 
]])]);}

if($data == "pluss") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
مرحبا بك في قسم تجميع النقاط 💎 .

يمكنك الحصول على نقاط بـ ثلاث طرق :

• مشاركة رابط الدعوة 🫂
• تبديل نقاط تمويل 🔄
• تسليم أرقام للمطور 📞
*

",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
[['text'=>'رابـط الـدعوه' ,'callback_data'=>"plus"],['text'=>'تسليم حسابات📲' ,'callback_data'=>"abhtext"]],
[['text'=>'شراء نقاط 💰' ,'callback_data'=>"buy"],['text'=>'تبديل نقاط 🔄' ,'callback_data'=>"tabdelni"]],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "abhtext") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
مرحـبا بـك 
 يمكنك تسلــيم رقــم يدوي مــن خــلال التواصل مع بــوت الدعــم  وسيـتم تحـديد السعر بيــن 100 نقطة الى 400 نقطة حسب نوع الـدولة و الـمنصة
*

",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
[['text'=>'تواصل مع المطور','url'=>'t.me/Namero ']],
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 
if($data == "tabdelni") {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*
مرحبا بك في قسم تبديل النقاط 🔄 .

يمكنك إستبدال نقاط تمويل بدل نقاط رشق :

• كل 2000 نقطة تمويل بدل 500 نقطة في البوت 💎
• كل 10000 نقطة تمويل بدل 2500 نقطة في البوت 💎
• كل 20000 نقطة تمويل بدل 5000 نقطة في البوت 💎

- نستقبل نقاط من بوت تمويل المليار فقط ⚜

(لتبديل نقاط يرجى التواصل مع المطور) .

~ المطـور : @s_p_p1 
*

",
'parse_mode'=>"markdown",
'reply_markup'=>json_encode([
     'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"tobot"]],
       
      ]
    ])
]);
} 

?>