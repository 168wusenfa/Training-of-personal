package edu.com.wusenfa

import android.app.Instrumentation;
import android.os.RemoteException;

import androidx.test.platform.app.InstrumentationRegistry;
import androidx.test.uiautomator.By;
import androidx.test.uiautomator.UiDevice;

import org.junit.Before;
import org.junit.Test;

public class Xuanxuan_uiautomator {
    Instrumentation mInstrumentation;
    UiDevice mDevice;
    @Before
    public void startup() throws RemoteException, InterruptedException {
        //��ȡ�豸
        mInstrumentation = InstrumentationRegistry.getInstrumentation();
        mDevice = UiDevice.getInstance(mInstrumentation);
        //����home
        mDevice.pressHome();
        //�ж��Ƿ�����
        boolean status = mDevice.isScreenOn();
        if (!status) {
            mDevice.wakeUp();
        }
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }


    //1.������죬�����飬��ϵ�ˣ��ҵ�
    @Test
    public void test1() throws InterruptedException {
        mDevice.findObject(By.text("����\n"+"�� 1 ����ǩ���� 4 ��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������\n"+"�� 2 ����ǩ���� 4 ��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ϵ��\n"+"�� 3 ����ǩ���� 4 ��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("�ҵ�\n"+"�� 4 ����ǩ���� 4 ��")).click();
        Thread.sleep(1000);
    }

    //2.���wsf168������
    @Test
    public void test2() throws InterruptedException {
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //3.���xit1-������-�ղ�-����
    @Test
    public void test3() throws InterruptedException{
        mDevice.findObject(By.text("w\n"+"xit 1\n"+"3��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("�ղ�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //4.���xit1-������-��Ա�б�-����-����
    @Test
    public void test4() throws InterruptedException{
        mDevice.findObject(By.text("w\n"+"xit 1\n"+"3��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��Ա�б�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //5.���xit1-������-������-������-����
    @Test
    public void test5() throws InterruptedException{
        mDevice.findObject(By.text("w\n"+"xit 1\n"+"3��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //6.���xit1-������-������-ȡ��-����
    @Test
    public void test6() throws InterruptedException{
        mDevice.findObject(By.text("w\n"+"xit 1\n"+"3��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("ȡ��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //7.���xit1-������-ͬ���������Ϣ-����
    @Test
    public void test7() throws InterruptedException{
        mDevice.findObject(By.text("w\n"+"xit 1\n"+"3��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("ͬ���������Ϣ")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //8.���wsf168-������-�ղ�-����
    @Test
    public void test8() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("�ղ�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //9.�����wsf168-������-����-����-����
    @Test
    public void test9() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //10.���wsf168-������-����-����-����-����
    @Test
    public void test10() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("�ղ�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //11.���wsf168-������-ͬ���������Ϣ-����
    @Test
    public void test11() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("ͬ���������Ϣ")).click();
        Thread.sleep(1000);
    }

    //12.���wsf168-ͼƬ-����-����-���
    @Test
    public void test12() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.res("com.android.camera2:id/shutter_button")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.res("com.android.camera2:id/cancel_button")).click();
        Thread.sleep(1000);
    }

    //13.���wsf168-ͼƬ-����-����-�Թ�
    @Test
    public void test13() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.res("com.android.camera2:id/shutter_button")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.res("com.android.camera2:id/done_button")).click();
        Thread.sleep(1000);
    }

    //14.�����wsf168-ͼƬ-����-����-��������
    @Test
    public void test14() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.res("com.android.camera2:id/shutter_button")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.res("com.android.camera2:id/retake_button")).click();
        Thread.sleep(1000);
    }

    //15.���wsf168-ͼƬ-��Ƭ-���-ѡ��ͼƬ
    @Test
    public void test15() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��Ƭ")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.clazz("android.widget.ImageButton")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("���")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.res("com.android.documentsui:id/icon_mime")).click();
        Thread.sleep(1000);
    }

    //16.���wsf168-ͼƬ-��Ƭ-����
    @Test
    public void test16() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��Ƭ")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.clazz("android.widget.ImageButton")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //17.���wsf168-ͼƬ-��Ƭ-ͼ��-ȡ��
    @Test
    public void test17() throws InterruptedException{
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��Ƭ")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.clazz("android.widget.ImageButton")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("ͼ��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("ȡ��")).click();
        Thread.sleep(1000);
    }

    //18.�����ϵ��-�����һ��-����-����
    @Test
    public void test18() throws InterruptedException{
        mDevice.findObject(By.text("��ϵ��\n"+"�� 3 ����ǩ���� 4 ��")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("w\n" + "wsf168\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("�ղ�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }

    //19.�Ӻ�-ѡ���һ����ϵ��-����
    @Test
    public void test19() throws InterruptedException{
        mDevice.findObject(By.text("��������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("w\n" + "wsf168" )).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }
    
    //  20.admin��ϵ�ˣ�����
    @Test
    public void test20() throws InterruptedException {
      mDevice.findObject(By.text("A\n" + "admin\n" + "[����]")).click();
      Thread.sleep(1000);
      mDevice.findObject(By.text("��ʾ�˵�")).click();
      Thread.sleep(1000);
      mDevice.findObject(By.text("����")).click();
      Thread.sleep(1000);
      mDevice.findObject(By.text("����")).click();
      Thread.sleep(1000);
      mDevice.findObject(By.text("����")).click();
      Thread.sleep(1000);
    }
    
//    21.admin��ϵ�ˣ���Ƭ
    @Test
    public void test21() throws InterruptedException {
        mDevice.findObject(By.text("A\n" + "admin\n" + "[����]")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("������������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��Ƭ")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.res("com.android.documentsui:id/line2")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }
    
    //    22.�����飬ϵͳ,��Ա�б�

    @Test
    public void test22() throws InterruptedException {
        mDevice.findObject(By.text("ϵͳ\n" + "������")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��ʾ�˵�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("��Ա�б�")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
        mDevice.findObject(By.text("����")).click();
        Thread.sleep(1000);
    }
    
//  23.�鿴���������
    @Test
    public void test23() throws InterruptedException, UiObjectNotFoundException {
    	mDevice.findObject(By.text("����\n" + "�� 1 ����ǩ���� 4 ��")).click();
        Thread.sleep(1000);
    }
    
    

}
