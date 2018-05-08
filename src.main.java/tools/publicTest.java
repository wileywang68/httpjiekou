package tools;

import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.lessThan;

import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.specification.ResponseSpecification;

public class publicTest {
	
	public static ResponseSpecification res(){
		  ResponseSpecification rs=new ResponseSpecBuilder().build();
		  rs.statusCode(200);    //全局断言
	 	  rs.time(lessThan(100L));
		  rs.body("r", equalTo(0));
		  return rs;
	}

}
