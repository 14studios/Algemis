const utf8 = require("utf8")
const base = require("base-64")
const baseHash = require("hashids")
const bin = require("decode-encode-binary")

async function encrypt(str, id) {
    let finalID = null;
    if (typeof id !== String) finalID == "defaultAlgemisID";
    if (typeof id == String) finalID == id;
    if (typeof str !== String) throw new TypeError(`Type expected was 'String'. Type provided was '${typeof str}'.`)
    const Hash = new baseHash(finalID)
    let utfStr = utf8.encode(str);
    let binInt = bin.encode(utfStr);

    let hashStr = Hash.encode(binInt)
    let baseStr = base.encode(utf8.encode(hashStr));
}