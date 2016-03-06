import QtQuick 2.0
Item {
    width:1272
    height:770
    
    property real tachNeedleAngle: 0
    
    property alias gear: gear.text
    property alias engineTorque: engine_torque.text
    property alias throttle: throttle_percent.text
    property alias speed: speed.text


    property alias glv_soc_green: glv_soc_green.opacity
    property alias glv_soc_red: glv_soc_red.opacity

    property alias motor_temp_red: motor_temp_red.opacity
    property alias motor_temp_yellow: motor_temp_yellow.opacity
    property alias motor_temp_green: motor_temp_green.opacity

    property alias brb_green: brb_green.opacity
    property alias brb_red: brb_red.opacity
    
    property alias ess_temp_red: ess_temp_red.opacity
    property alias ess_temp_green: ess_temp_green.opacity

    property alias tran_red: tran_red.opacity
    property alias tran_green: tran_green.opacity

    property alias soc_5: soc_5.opacity
    property alias soc_10: soc_10.opacity
    property alias soc_15: soc_15.opacity
    property alias soc_20: soc_20.opacity
    property alias soc_25: soc_25.opacity
    property alias soc_30: soc_30.opacity
    property alias soc_35: soc_35.opacity
    property alias soc_40: soc_40.opacity
    property alias soc_45: soc_45.opacity
    property alias soc_50: soc_50.opacity
    property alias soc_55: soc_55.opacity
    property alias soc_60: soc_60.opacity
    property alias soc_65: soc_65.opacity
    property alias soc_70: soc_70.opacity
    property alias soc_75: soc_75.opacity
    property alias soc_80: soc_80.opacity
    property alias soc_85: soc_85.opacity
    property alias soc_90: soc_90.opacity
    property alias soc_95: soc_95.opacity
    property alias soc_100: soc_100.opacity

    property alias fuel_5: fuel_5.opacity
    property alias fuel_10: fuel_10.opacity
    property alias fuel_15: fuel_15.opacity
    property alias fuel_20: fuel_20.opacity
    property alias fuel_25: fuel_25.opacity
    property alias fuel_30: fuel_30.opacity
    property alias fuel_35: fuel_35.opacity
    property alias fuel_40: fuel_40.opacity
    property alias fuel_45: fuel_45.opacity
    property alias fuel_50: fuel_50.opacity
    property alias fuel_55: fuel_55.opacity
    property alias fuel_60: fuel_60.opacity
    property alias fuel_65: fuel_65.opacity
    property alias fuel_70: fuel_70.opacity
    property alias fuel_75: fuel_75.opacity
    property alias fuel_80: fuel_80.opacity
    property alias fuel_85: fuel_85.opacity
    property alias fuel_90: fuel_90.opacity
    property alias fuel_95: fuel_95.opacity
    property alias fuel_100: fuel_100.opacity

    Image {
        id: background
        source: "images/background.png"
        x: 0
        y: 0
        opacity: 1
    }
    Image {
        id: brb_red
        source: "images/brb_red.png"
        x: 851
        y: 281
        opacity: 1
    }
    Image {
        id: brb_green
        source: "images/brb_green.png"
        x: 851
        y: 281
        opacity: 1
    }
    Image {
        id: motor_temp_red
        source: "images/motor_temp_red.png"
        x: 717
        y: 288
        opacity: 1
    }
    Image {
        id: motor_temp_yellow
        source: "images/motor_temp_yellow.png"
        x: 717
        y: 288
        opacity: 1
    }
    Image {
        id: motor_temp_green
        source: "images/motor_temp_green.png"
        x: 717
        y: 288
        opacity: 1
    }
    Image {
        id: glv_soc_red
        source: "images/glv_soc_red.png"
        x: 581
        y: 305
        opacity: 1
    }
    Image {
        id: glv_soc_green
        source: "images/glv_soc_green.png"
        x: 581
        y: 305
        opacity: 1
    }
    Image {
        id: tran_red
        source: "images/tran_red.png"
        x: 1133
        y: 289
        opacity: 1
    }
    Image {
        id: tran_green
        source: "images/tran_green.png"
        x: 1133
        y: 289
        opacity: 1
    }
    Image {
        id: ess_temp_red
        source: "images/ess_temp_red.png"
        x: 1033
        y: 274
        opacity: 1
    }
    Image {
        id: ess_temp_green
        source: "images/ess_temp_green.png"
        x: 1033
        y: 274
        opacity: 1
    }
    Image {
        id: fuel_5
        source: "images/fuel_5.png"
        x: 818
        y: 70
        visible: true
        opacity: 1
    }
    Image {
        id: fuel_10
        source: "images/fuel_10.png"
        x: 838
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_15
        source: "images/fuel_15.png"
        x: 857
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_20
        source: "images/fuel_20.png"
        x: 877
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_25
        source: "images/fuel_25.png"
        x: 897
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_30
        source: "images/fuel_30.png"
        x: 917
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_35
        source: "images/fuel_35.png"
        x: 936
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_40
        source: "images/fuel_40.png"
        x: 956
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_45
        source: "images/fuel_45.png"
        x: 976
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_50
        source: "images/fuel_50.png"
        x: 996
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_55
        source: "images/fuel_55.png"
        x: 1015
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_60
        source: "images/fuel_60.png"
        x: 1035
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_65
        source: "images/fuel_65.png"
        x: 1055
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_70
        source: "images/fuel_70.png"
        x: 1075
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_75
        source: "images/fuel_75.png"
        x: 1095
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_80
        source: "images/fuel_80.png"
        x: 1115
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_85
        source: "images/fuel_85.png"
        x: 1135
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_90
        source: "images/fuel_90.png"
        x: 1154
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_95
        source: "images/fuel_95.png"
        x: 1174
        y: 70
        opacity: 1
    }
    Image {
        id: fuel_100
        source: "images/fuel_100.png"
        x: 1194
        y: 70
        visible: true
        opacity: 1
    }
    Image {
        id: soc_5
        source: "images/soc_5.png"
        x: 818
        y: 17
        opacity: 1
    }
    Image {
        id: soc_10
        source: "images/soc_10.png"
        x: 838
        y: 17
        opacity: 1
    }
    Image {
        id: soc_15
        source: "images/soc_15.png"
        x: 857
        y: 17
        opacity: 1
    }
    Image {
        id: soc_20
        source: "images/soc_20.png"
        x: 877
        y: 17
        opacity: 1
    }
    Image {
        id: soc_25
        source: "images/soc_25.png"
        x: 897
        y: 17
        opacity: 1
    }
    Image {
        id: soc_30
        source: "images/soc_30.png"
        x: 917
        y: 17
        opacity: 1
    }
    Image {
        id: soc_35
        source: "images/soc_35.png"
        x: 936
        y: 17
        opacity: 1
    }
    Image {
        id: soc_40
        source: "images/soc_40.png"
        x: 956
        y: 17
        opacity: 1
    }
    Image {
        id: soc_45
        source: "images/soc_45.png"
        x: 976
        y: 17
        opacity: 1
    }
    Image {
        id: soc_50
        source: "images/soc_50.png"
        x: 996
        y: 17
        opacity: 1
    }
    Image {
        id: soc_55
        source: "images/soc_55.png"
        x: 1015
        y: 17
        opacity: 1
    }
    Image {
        id: soc_60
        source: "images/soc_60.png"
        x: 1035
        y: 17
        opacity: 1
    }
    Image {
        id: soc_65
        source: "images/soc_65.png"
        x: 1055
        y: 17
        opacity: 1
    }
    Image {
        id: soc_70
        source: "images/soc_70.png"
        x: 1075
        y: 17
        opacity: 1
    }
    Image {
        id: soc_75
        source: "images/soc_75.png"
        x: 1095
        y: 17
        opacity: 1
    }
    Image {
        id: soc_80
        source: "images/soc_80.png"
        x: 1115
        y: 17
        opacity: 1
    }
    Image {
        id: soc_85
        source: "images/soc_85.png"
        x: 1135
        y: 17
        opacity: 1
    }
    Image {
        id: soc_90
        source: "images/soc_90.png"
        x: 1154
        y: 17
        opacity: 1
    }
    Image {
        id: soc_95
        source: "images/soc_95.png"
        x: 1174
        y: 17
        opacity: 1
    }
    Image {
        id: soc_100
        source: "images/soc_100.png"
        x: 1194
        y: 17
        opacity: 1
    }
    Image {
        id: tach_needle
        objectName: "tach_needle"
        source: "images/tach_needle.png"
        x: 121
        y: 237
        opacity: 1
        transform: Rotation {
            // Transform origin is the middle point of the lower border
            origin {
                x: 167
                y: 43
            }
            //axis {x: 1; y: 0; z: 0}
            angle: tachNeedleAngle
        }
    }
    Text {
        id: engine_torque
        text: qsTr("--")
        font.bold: true
        font.family: "Tahoma"
        font.pointSize: 50
        color: "#9b8e8e"
        x: 878
        y: 151
        opacity: 1
    }
    Text {
        id: throttle_percent
        text: qsTr("--")
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        font.bold: true
        font.family: "Tahoma"
        font.pointSize: 50
        color: "#9b8e8e"
        x: 1096
        y: 151
    }
   
    Text {
        id: speed
        x: 171
        y: 405
        width: 174
        height: 109
        color: "#9b8e8e"
        text: qsTr("00")
        horizontalAlignment: Text.AlignRight
        verticalAlignment: Text.AlignVCenter
        font.bold: true
        font.family: "Arial"
        font.pixelSize: 90
    }

    Text {
        id: gear
        x: 632
        y: 46
        color: "#9b8e8e"
        text: qsTr("1")
        font.bold: true
        font.family: "Tahoma"
        font.pixelSize: 175
    }
}
