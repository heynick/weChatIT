/**
 * 自动生成ajax请求参数，
 * key为id，radio时为name
 * @param parentDom 把parentDom元素的所有表单控件当为请求参数
 */
var _genReqData = function(parentDom){
	var obj = {};
	$(parentDom+" input").each(function(index, element){
		var el = $(element);
		var type = el.attr('type');
		if(type=="text" || type=="hidden" || type=="password" || type=="number" || type=="email"){
			var key = el.attr('id');
			if(key==undefined){
				key = el.attr('name');
			}
			if(el.val()!=undefined && el.val()!=""){
				obj[key] = el.val().trim();
			}
		}else if(type=="checkbox"){//多个checkbox用,分隔
			var key = el.attr('name');
			var val ='';
			$(parentDom+" input:checkbox[name='"+el.attr('name')+"']:checked").each(function(i, e1){
				var jE1 = $(e1);
			    val += jE1.val() ;
			    val += ',';
			});
			if(val!="" && val!=null){
				val = val.substr(0, val.length-1);
				obj[key] = val;
			}
		}else if(type=="radio"){
			var key = el.attr('name');
			var value = $('input:radio[name='+el.attr('name')+']:checked').val();
			if(value!=undefined && value!=""){
				obj[key] = value;
			}
		}
	});
	
	$(parentDom+" select").each(function(index, element){
		var el = $(element);
		var key = el.attr('name');
		var value = el.val();
		if(value!=undefined && value!=""){
			obj[key] = value.trim();
		}
	});
	
	$(parentDom+" textarea").each(function(index, element){
		var el = $(element);
		var key = el.attr('name');
		var value = el.val();
		if(value!=undefined && value!=""){
			obj[key] = value.trim();
		}
	});
	
	return obj;
}

