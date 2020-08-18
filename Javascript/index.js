var inc=(function(){
	return function sum(...ar){
		// const ar=[a,b,c,d];
		return ar.reduce((a,b)=>a+b,0)
	}
})();
console.log(inc(1,2,3,4))