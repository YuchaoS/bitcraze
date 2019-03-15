LOCODECK_TS_FREQ=499.2e6*128;
SPEED_OF_LIGHT=299792458;
data=dlmread('lps_twr.log');
tround1=data(:,1);
tround2=data(:,2);
treply1=data(:,3);
treply2=data(:,4);
dround1=data(:,1)/ LOCODECK_TS_FREQ*SPEED_OF_LIGHT;
dround2=data(:,2)/ LOCODECK_TS_FREQ*SPEED_OF_LIGHT;
dreply1=data(:,3)/ LOCODECK_TS_FREQ*SPEED_OF_LIGHT;
dreply2=data(:,4)/ LOCODECK_TS_FREQ*SPEED_OF_LIGHT;
tprop_ctn = ((tround1.*tround2)-(treply1.*treply2))./(tround1 + tround2 + treply1 + treply2);
tprop = tprop_ctn / LOCODECK_TS_FREQ;
distance = SPEED_OF_LIGHT * tprop;
distance_quter=0.25*(tround1-treply1+tround2-treply2)/ LOCODECK_TS_FREQ*SPEED_OF_LIGHT;
[data(:,5) distance distance_quter (dround1-dreply1)/2 (dround2-dreply2)/2 (dround1-dreply1)/2-(dround2-dreply2)/2]

