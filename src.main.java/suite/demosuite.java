package suite;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

import test2.test2;
import test2.test3;

@RunWith(Suite.class)
@Suite.SuiteClasses({
	test2.class,
	test3.class
	
})
public class demosuite {

}
