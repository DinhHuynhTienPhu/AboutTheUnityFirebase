package com.nostel.parking.car.huaweiiap;

import android.content.Context;
import android.os.Bundle;
import android.os.RemoteException;
import android.util.Log;

import com.android.installreferrer.api.InstallReferrerClient;
import com.android.installreferrer.api.InstallReferrerStateListener;
import com.android.installreferrer.api.ReferrerDetails;
import com.huawei.hms.analytics.HiAnalytics;
import com.huawei.hms.analytics.HiAnalyticsInstance;
import com.huawei.hms.analytics.HiAnalyticsTools;
import com.huawei.hms.analytics.type.HAEventType;
import com.huawei.hms.analytics.type.HAParamType;
import com.huawei.hms.analytics.type.ReportPolicy;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class HuaweiAnalyticsHelper {

    public static HiAnalyticsInstance instance ;
    // Initialize Huawei Analytics
    public int initializeAnalytics(Context context,String userid) {
        try {// Enable SDK log recording for debugging purposes
            HiAnalyticsTools.enableLog();

            // Obtain a HiAnalyticsInstance instance
            HiAnalyticsInstance instance = HiAnalytics.getInstance(context);

            // (Optional) Set user attributes
            instance.setUserProfile("userKey", userid);

            // (Optional) Configure advertising ID collection
            // Note: You can also set this in AndroidManifest.xml
            instance.setCollectAdsIdEnabled(true);

            // (Optional) Disable system attribute collection
            // Note: You can also set this in AndroidManifest.xml
            //instance.setPropertyCollection(HiAnalyticsInstance.VALUES_USER_AGENT);

            // (Optional) Set event reporting policies
            setEventReportingPolicies(instance);

            // (Optional) Set custom referrer if needed
            setCustomReferrer(context, instance);

            HuaweiAnalyticsHelper.instance = instance;
        }
        catch(Error e){
            Log.i("Unity","Analytic init fail "+ e.getMessage());
            return -1;
        }
        Log.i("Unity","huawei analytic success ^^");
        return 1;
    }

    // Set event reporting policies
    private void setEventReportingPolicies(HiAnalyticsInstance instance) {
        // Create a policy that is used to report an event upon app switching to the background.
        ReportPolicy moveBackgroundPolicy = ReportPolicy.ON_MOVE_BACKGROUND_POLICY;
// Create a policy that is used to report an event at the specified interval.
        ReportPolicy scheduledTimePolicy = ReportPolicy.ON_SCHEDULED_TIME_POLICY;
// Set the event reporting interval to 600 seconds.
        scheduledTimePolicy.setThreshold(600);
        Set<ReportPolicy> reportPolicies = new HashSet<>();
// Add the ON_SCHEDULED_TIME_POLICY and ON_MOVE_BACKGROUND_POLICY policies.
        reportPolicies.add(scheduledTimePolicy);
        reportPolicies.add(moveBackgroundPolicy);
// Set the ON_MOVE_BACKGROUND_POLICY and ON_SCHEDULED_TIME_POLICY policies.
        instance.setReportPolicies(reportPolicies);
    }

    // Set custom referrer
    private void setCustomReferrer(Context context, HiAnalyticsInstance instance) {
        final InstallReferrerClient client = InstallReferrerClient.newBuilder(context).build();
        client.startConnection(new InstallReferrerStateListener() {
            @Override
            public void onInstallReferrerSetupFinished(int responseCode) {
                if (responseCode == InstallReferrerClient.InstallReferrerResponse.OK) {
                    try {
                        ReferrerDetails details = client.getInstallReferrer();
                        // Set a custom referrer.
                        instance.setCustomReferrer(details.getInstallReferrer());
                    } catch (RemoteException exception) {
                        // Capture the exception.
                    }
                }
            }
            @Override
            public void onInstallReferrerServiceDisconnected() {
                // Disconnect onInstallReferrerService.
            }
        });
    }

    // Enable event tracking
    public void trackEvents(String eventname,HashMap<String, String> eventParams) {
        // Enable tracking of custom events
        Bundle customEventBundle = new Bundle();
//        customEventBundle.putString("exam_difficulty", "high");
//        customEventBundle.putString("exam_level", "1-1");
//        customEventBundle.putString("exam_time", "20190520-08");

        for (Map.Entry<String, String> entry : eventParams.entrySet()) {
            customEventBundle.putString(entry.getKey(), entry.getValue());
            Log.i("Unity","Analytic event "+ entry.getKey() + " "+ entry.getValue());
        }
        instance.onEvent(eventname, customEventBundle);

    }
}
