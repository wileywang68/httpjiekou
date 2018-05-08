package test2;


import static io.restassured.RestAssured.given;
import static io.restassured.RestAssured.useRelaxedHTTPSValidation;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.lessThan;

import java.util.HashMap;
import java.util.Map;

import org.junit.BeforeClass;
import org.junit.Test;

import io.restassured.RestAssured;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.specification.ResponseSpecification;
import net.sf.json.JSONObject;
import tools.publicTest;

public class test2 {
	
	@BeforeClass
	public static void setup() {
		//设置默认跳过ssl验证
		useRelaxedHTTPSValidation();
		RestAssured.baseURI="https://testerhome.com";
//		ResponseSpecification rs=new ResponseSpecBuilder().build();
//		rs.statusCode(200);    //全局断言
//		rs.time(lessThan(100L));
//		rs.body("r", equalTo(0));
	//	RestAssured.proxy("127.0.0.1",8080);    设置代理
	}
	
//	@Test
//	public void gettest(){
//		
//		Map <String,Object> map = new HashMap<String,Object>();
//		map.put("topics", "topics");
//		map.put("id", 13298);
//		
//		get("https://testerhome.com/{topics}/{id}",map).prettyPeek();
//		
//	}
	/*
	@Test
	public void questinfotest(){
		
	      String  url="http://192.168.5.111:8590/quest/info";
	      Map <String,Object> map = new HashMap<String,Object>();
		  map.put("seq", "1");
		  map.put("rseq", 1);
		  map.put("t", "cbd1da997c99c99afacbb8f7bd69859f");
	      given().params(map).post(url).prettyPeek();
				
		
	}
		*/
	//断言
//	@Test
//	public void posttest(){
//	      String  url="http://192.168.5.111:8590/player";
//	      String stu = "{'plat':'WindowsEditor','flags':['lang_zh-Hans','font_FZLTH'],'capid':'d05f4c5d4a064ce68b040e59fe809cb8','jsonUpdate':{},'ver':{'editor':2147483647}}";
//		  JSONObject json_test = JSONObject.fromObject(stu);  
//	      Map <String,Object> map = new HashMap<String,Object>();
//		  map.put("seq", "1");
//		  map.put("rseq", 1);
//		  map.put("d", json_test);
//		  map.put("t", "cbd1da997c99c99afacbb8f7bd69859f");
//	      given()
//	      			.params(map)
//	      .when()
//	      			.post(url).prettyPeek()
//	      .then()
//	      			.statusCode(200)
//	      			.body("r", equalTo(0))
//	      			.body("d.info.name", equalTo("你好"))
//	      			.time(lessThan(500L))
//	      ;
//	}
//	
//	//导出数据
//		@Test
//		public void daochu(){
//		      String  url="http://192.168.5.116:8590/user/login";
//		      String d = "{'pwd':'c','capid':'d05f4c5d4a064ce68b040e59fe809cb8','name':'ccc@ccc.com','udid':'d05f4c5d4a064ce68b040e59fe809cb8'}";
//			  JSONObject json_test = JSONObject.fromObject(d);  
//		      Map <String,Object> map = new HashMap<String,Object>();
//			  map.put("seq", "1");
//			  map.put("rseq", 1);
//			  map.put("d", json_test);
//		      Response res=given()
//		      			.params(map)
//		      .when()
//		      			.post(url).prettyPeek()
//		      .then()
//		      			.statusCode(200)
//		      			.body("r", equalTo(0))
//		      			.time(lessThan(500L))
//		      .extract()
//		      			.response()
//		      ;
//		      String token=res.path("d.uinfo.token");
//		      String capstoneid=res.path("d.uinfo.capstoneID");
//		      String cuid=res.path("d.cuid");
//		      System.out.println(token);
//		      System.out.println(capstoneid);
//		      System.out.println(cuid);
//		      
//		      String  url1="http://192.168.5.111:8590/a/login";
//		      String d1 = "{'uinfo':{'token':"+token+",'capstoneID':"+capstoneid+"},'channel':'capstone','bichannel':'capstone','cuid':"+cuid+",'capid':'d05f4c5d4a064ce68b040e59fe809cb8','pf':'capstone','udid':'d05f4c5d4a064ce68b040e59fe809cb8'}";
//			  JSONObject json_test1 = JSONObject.fromObject(d1);  
//		      Map <String,Object> map1 = new HashMap<String,Object>();
//			  map1.put("seq", "2");
//			  map1.put("rseq","2");
//			  map1.put("d", json_test1);
//		      String token1=given()
//		      			.params(map1)
//		      .when()
//		      			.post(url1).prettyPeek()
//		      .then()
//		      			.statusCode(200)
//		      			.body("r", equalTo(0))
//		      			.time(lessThan(500L))
//		      .extract().path("d.servers[0].player.token")
//		      ;
//		      System.out.println(token1);
//		      
//		}
	
	
	//导出数据
//	@Test
//	public void daochu(){
//	      String  url="http://192.168.5.111:8590/a/login";
//	      String d = "{'uinfo':{'token':'sdklfjdlskfjds','capstoneID':'asfdasfdasfdas'},'channel':'capstone','bichannel':'capstone','cuid':'akasfjdkafjdasfldasfdasfdasf','capid':'d05f4c5d4a064ce68b040e59fe809cb8','pf':'capstone','udid':'d05f4c5d4a064ce68b040e59fe809cb8'}";
//		  JSONObject json_test = JSONObject.fromObject(d);  
//	      Map <String,Object> map = new HashMap<String,Object>();
//		  map.put("seq", "1");
//		  map.put("rseq", 1);
//		  map.put("d", json_test);
//	      given()
//	      			.params(map)
//	      .when()
//	      			.post(url).prettyPeek()
//	      .then()
//	      			.statusCode(200)
//	      			.body("r", equalTo(0))
//	      			.time(lessThan(500L))
//	      ;
//	}
	
//	@Test
//	public void get1test(){
//
//		 given()
//		 			.queryParam("wd", "mp3")
//		 .when()
//		 			.get("https://www.baidu.com/s").prettyPeek()
//		 .then()
//		 			.statusCode(200);
//		 
//		
//	}

//	@Test
//	public void testJsonPost(){
//		Map<String,Object> data=new HashMap<String,Object>();
//		data.put("id", 6040);
//		data.put("title", "通过代理安装testerhome");
//		data.put("name", "wiley");
//		given()
//					.contentType(ContentType.JSON)
//					.body(data)
//		.when()
//					.post("http://www.baidu.com")
//		.then().statusCode(200)
//		;
//	}
//	
//	
	
	//断言
	@Test
	public void posttest(){
//		  ResponseSpecification rs=new ResponseSpecBuilder().build();
//		  rs.statusCode(200);    //全局断言
//	 	  rs.time(lessThan(100L));
//		  rs.body("r", equalTo(0));
	      String  url="http://192.168.5.111:8590/player";
	      String stu = "{'plat':'WindowsEditor','flags':['lang_zh-Hans','font_FZLTH'],'capid':'d05f4c5d4a064ce68b040e59fe809cb8','jsonUpdate':{},'ver':{'editor':2147483647}}";
		  JSONObject json_test = JSONObject.fromObject(stu);  
	      Map <String,Object> map = new HashMap<String,Object>();
		  map.put("seq", "1");
		  map.put("rseq", 1);
		  map.put("d", json_test);
		  map.put("t", "cbd1da997c99c99afacbb8f7bd69859f");
	      given()
	      			.params(map)
	      .when()
	      			.post(url).prettyPeek()
	      .then()
	      			.spec(publicTest.res())
	      			.body("d.info.name", equalTo("你好"))
	      ;
	}
	
	
	public static void main (String args[]){
		String stu = "{'plat':'WindowsEditor','flags':['lang_zh-Hans','font_FZLTH'],'capid':'d05f4c5d4a064ce68b040e59fe809cb8','jsonUpdate':{},'ver':{'editor':2147483647}}";
		JSONObject json_test = JSONObject.fromObject(stu);  
		System.out.println(json_test);
	}

}
