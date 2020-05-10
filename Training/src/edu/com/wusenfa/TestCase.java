package edu.com.wusenfa;

import org.testng.annotations.Test;
public class TestCase extends Pages{
		@Test
		public void test01() {
			chat().click();
		}

		@Test
		public void test02() {
			creat().click();
		}

		@Test
		public void test03() {
			my().click();
		}

		@Test
		public void test04() {
			my().click();
			list().click();
			about().click();
			close().click();
		}

		@Test
		public void test05() {
			my().click();
			list().click();
			about().click();
			private1().click();
		}

		@Test
		public void test06() {
			my().click();
			cancel().click();
			nochose().click();
		}
		
		@Test
		public void test07() {
			my().click();
			cancel().click();
			enter1().click();
		}
		
		@Test
		public void test08() throws InterruptedException{
			Pages submit = new Pages();
			submit.addWhite();
		}
		@Test
		public void test09() throws InterruptedException{
			Pages submit = new Pages();
			submit.add("hello");
		}
		
		@Test
		public void test10() throws InterruptedException{
			Pages submit = new Pages();
			submit.addWhite();
		}
		
		@Test
		public void test11() throws InterruptedException{
			Pages submit = new Pages();
			submit.add("world");
		}
		
		@Test
		public void test12() throws InterruptedException{
			Pages submit = new Pages();
			submit.add("168");
		}
		
		@Test
		public void test13() throws InterruptedException{
			Pages submit = new Pages();
			submit.add("");
		}
		
		@Test
		public void test14() throws InterruptedException{
			Pages submit = new Pages();
			submit.add("你好");
		}
		
		@Test
		public void test15() throws InterruptedException{
			Pages submit = new Pages();
			submit.freshen();
		}
		
		@Test
		public void test16() throws InterruptedException{
			Pages submit = new Pages();
			submit.rename("是讨论组吗");
		}
		
		@Test
		public void test17() throws InterruptedException{
			Pages submit = new Pages();
			submit.renameWhite();
		}
		
		@Test
		public void test18() throws InterruptedException{
			Pages submit = new Pages();
			submit.rename("shide");
		}
		
		@Test
		public void test19() throws InterruptedException{
			Pages submit = new Pages();
			submit.rename("16888");
		}
		
		@Test
		public void test20() throws InterruptedException{
			Pages submit = new Pages();
			submit.rename("shiy");
		}
		
		@Test
		public void test21() throws InterruptedException{
			Pages submit = new Pages();
			submit.collect();
		}
		
		@Test
		public void test22() throws InterruptedException{
			Pages submit = new Pages();
			submit.deleteCollect();
		}
		
		@Test
		public void test23() throws InterruptedException{
			Pages submit = new Pages();
			submit.viewList();
		}
		
		@Test
		public void test24() throws InterruptedException{
			Pages submit = new Pages();
			submit.collectPerson();
		}

		@Test
		public void test25() throws InterruptedException{
			Pages submit = new Pages();
			submit.deletePerson();
		}

}