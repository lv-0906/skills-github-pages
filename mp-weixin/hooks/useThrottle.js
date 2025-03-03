"use strict";exports.useThrottle=function(t,e){let u;return function(...i){u||(t.apply(this,i),u=setTimeout((()=>{clearTimeout(u),u=null}),e))}};
