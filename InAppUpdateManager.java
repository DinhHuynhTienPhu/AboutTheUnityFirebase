package com.nostel.parking.car.huaweiiap;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import com.huawei.hms.common.internal.AnyClient;
import com.huawei.hms.jos.AppUpdateClient;
import com.huawei.hms.jos.JosApps;

import com.huawei.updatesdk.service.appmgr.bean.ApkUpgradeInfo;
import com.huawei.updatesdk.service.otaupdate.*;
import java.lang.ref.WeakReference;
import java.io.Serializable;

public class InAppUpdateManager {

    private static final String TAG = "InAppUpdateManager";
    private Context mContext;

    public InAppUpdateManager(Context context) {
        this.mContext = context;
    }

    public void checkUpdate() {
        AppUpdateClient client = JosApps.getAppUpdateClient(mContext);
        Callback callBack = new Callback(mContext);
        client.checkAppUpdate(mContext, callBack);
    }

    private static class Callback implements CheckUpdateCallBack {
        private WeakReference<Context> mContextWeakReference;

        public Callback(Context context) {
            mContextWeakReference = new WeakReference<>(context);
        }

        @Override
        public void onUpdateInfo(Intent intent) {
            if (intent != null) {
                int status = intent.getIntExtra(UpdateKey.STATUS, -99);
                Log.i(TAG, "check update status is:" + status);

                int rtnCode = intent.getIntExtra(UpdateKey.FAIL_CODE, -99);
                String rtnMessage = intent.getStringExtra(UpdateKey.FAIL_REASON);

                boolean isExit = intent.getBooleanExtra(UpdateKey.MUST_UPDATE, false);
                Log.i(TAG, "rtnCode = " + rtnCode + " rtnMessage = " + rtnMessage);

                Serializable info = intent.getSerializableExtra(UpdateKey.INFO);

                if (info instanceof ApkUpgradeInfo) {
                    Context context = mContextWeakReference.get();
                    if (context != null) {
                        JosApps.getAppUpdateClient(context)
                                .showUpdateDialog(context, (ApkUpgradeInfo) info, false);
                    }
                    Log.i(TAG, "check update success and there is a new update");
                }

                Log.i(TAG, "check update isExit=" + isExit);
                if (isExit) {
                    // Handle the logic for the user exiting the app due to a forced update.
                    System.exit(0);
                }
            }
        }

        @Override
        public void onMarketInstallInfo(Intent intent) {
            // Handle market install information if needed.
        }

        @Override
        public void onMarketStoreError(int i) {
            // Handle market store errors if needed.
        }

        @Override
        public void onUpdateStoreError(int i) {
            // Handle update store errors if needed.
        }
    }
}
