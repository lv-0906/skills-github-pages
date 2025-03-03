"use strict";const e=require("../common/vendor.js");new Proxy({},{get:(s,n)=>s=>new Promise(((o,r)=>{e.index[n]({...s,success:e=>{o(e)},fail:e=>{r(e)}})}))});
