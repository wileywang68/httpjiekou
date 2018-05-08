package test2;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.lessThan;
import java.util.HashMap;
import java.util.Map;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import net.sf.json.JSONObject;


public class test3 {
	
	@BeforeClass
	public static void beforeclass(){
		System.out.println("这是beforeclass方法，开始测试用例之前会执行一次");
	}
	
	@Before
	public void before(){
		System.out.println("这是before方法，每次用例之前都会执行");
	}
	
	@Test
	public void posttest(){
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
	      			.statusCode(200)
	      			.body("r", equalTo(0))
	      			.body("d.info.name", equalTo("你好"))
	      			.time(lessThan(500L))
	      ;
	}
	
	@After
	public void after(){
		System.out.println("这是after方法，每次执行用例后会执行");
	}
	
	@AfterClass
	public static void afterclass(){
		System.out.println("这是afterclass方法，测试用例之后会执行一次");
	}
}
