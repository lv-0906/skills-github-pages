"use strict";exports.useDebounce=function(e,t){let u;return function(...i){u&&clearTimeout(u),u=setTimeout((()=>{e.apply(this,i)}),t)}};
