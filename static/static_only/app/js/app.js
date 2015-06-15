/**
 * Created by liulixiang on 2015/6/12.
 */
function qr(id, text){
    new QRCode(id, {
        text: text,
        width: 128,
        height: 128,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    });
}
