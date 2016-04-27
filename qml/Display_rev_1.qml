import QtQuick 2.0
Item {
    width:1272
    height:770

    property real tachNeedleAngle: 0

    property alias gear: gear.text
    property alias speed: speed.text
    property alias temp_text_color: tempN.color
    property alias temp_text_text: tempN.text

    property alias charging_yellow: charging_yellow.opacity
    property alias fuel_red: fuel_red.opacity
    property alias can_red: can_red.opacity
    property alias motor_temp_yellow: motor_temp_yellow.opacity
    property alias motor_temp_red: motor_temp_red.opacity
    property alias glv_soc_red: glv_soc_red.opacity
    property alias ess_temp_red: ess_temp_red.opacity
    property alias power_on: power_on.opacity

    property alias tach_shift: tach_shift.opacity
    property alias tach: tach.opacity

    property alias soc_y1: soc_y1.opacity
    property alias soc_y2: soc_y2.opacity
    property alias soc_y3: soc_y3.opacity
    property alias soc_y4: soc_y4.opacity
    property alias soc_y5: soc_y5.opacity
    property alias soc_y6: soc_y6.opacity
    property alias soc_y7: soc_y7.opacity
    property alias soc_y8: soc_y8.opacity

    property alias soc_g1: soc_g1.opacity
    property alias soc_g2: soc_g2.opacity
    property alias soc_g3: soc_g3.opacity
    property alias soc_g4: soc_g4.opacity
    property alias soc_g5: soc_g5.opacity
    property alias soc_g6: soc_g6.opacity
    property alias soc_g7: soc_g7.opacity
    property alias soc_g8: soc_g8.opacity
    property alias soc_g9: soc_g9.opacity
    property alias soc_g10: soc_g10.opacity
    property alias soc_g11: soc_g11.opacity
    property alias soc_g12: soc_g12.opacity
    property alias soc_g13: soc_g13.opacity
    property alias soc_g14: soc_g14.opacity
    property alias soc_g15: soc_g15.opacity
    property alias soc_g16: soc_g16.opacity
    property alias soc_g17: soc_g17.opacity
    property alias soc_g18: soc_g18.opacity
    property alias soc_g19: soc_g19.opacity
    property alias soc_g20: soc_g20.opacity


    property alias fuel_r1: fuel_r1.opacity
    property alias fuel_r2: fuel_r2.opacity

    property alias fuel_y1: fuel_y1.opacity
    property alias fuel_y2: fuel_y2.opacity
    property alias fuel_y3: fuel_y3.opacity
    property alias fuel_y4: fuel_y4.opacity
    property alias fuel_y5: fuel_y5.opacity
    property alias fuel_y6: fuel_y6.opacity
    property alias fuel_y7: fuel_y7.opacity
    property alias fuel_y8: fuel_y8.opacity

    property alias fuel_g1: fuel_g1.opacity
    property alias fuel_g2: fuel_g2.opacity
    property alias fuel_g3: fuel_g3.opacity
    property alias fuel_g4: fuel_g4.opacity
    property alias fuel_g5: fuel_g5.opacity
    property alias fuel_g6: fuel_g6.opacity
    property alias fuel_g7: fuel_g7.opacity
    property alias fuel_g8: fuel_g8.opacity
    property alias fuel_g9: fuel_g9.opacity
    property alias fuel_g10: fuel_g10.opacity
    property alias fuel_g11: fuel_g11.opacity
    property alias fuel_g12: fuel_g12.opacity
    property alias fuel_g13: fuel_g13.opacity
    property alias fuel_g14: fuel_g14.opacity
    property alias fuel_g15: fuel_g15.opacity
    property alias fuel_g16: fuel_g16.opacity
    property alias fuel_g17: fuel_g17.opacity
    property alias fuel_g18: fuel_g18.opacity
    property alias fuel_g19: fuel_g19.opacity
    property alias fuel_g20: fuel_g20.opacity

    property alias fuel_b1: fuel_b1.opacity
    property alias fuel_b2: fuel_b2.opacity
    property alias fuel_b3: fuel_b3.opacity
    property alias fuel_b4: fuel_b4.opacity
    property alias fuel_b5: fuel_b5.opacity
    property alias fuel_b6: fuel_b6.opacity
    property alias fuel_b7: fuel_b7.opacity
    property alias fuel_b8: fuel_b8.opacity
    property alias fuel_b9: fuel_b9.opacity
    property alias fuel_b10: fuel_b10.opacity
    property alias fuel_b11: fuel_b11.opacity
    property alias fuel_b12: fuel_b12.opacity
    property alias fuel_b13: fuel_b13.opacity
    property alias fuel_b14: fuel_b14.opacity
    property alias fuel_b15: fuel_b15.opacity
    property alias fuel_b16: fuel_b16.opacity
    property alias fuel_b17: fuel_b17.opacity
    property alias fuel_b18: fuel_b18.opacity
    property alias fuel_b19: fuel_b19.opacity
    property alias fuel_b20: fuel_b20.opacity

    Image {
        id: background
        source: "images/background.png"
        x: 0
        y: 0
        sourceSize.height: 800
        sourceSize.width: 1300
        opacity: 1
    }
    Image {
        id: power_on
        source: "images/power_on.png"
        x: 1097
        y: 609
        opacity: 1
    }
    Image {
        id: charging_yellow
        source: "images/charging_yellow.png"
        x: 1078
        y: 614
        opacity: 1
    }
    Image {
        id: fuel_red
        source: "images/fuel_red.png"
        x: 1121
        y: 615
        opacity: 1
    }
    Image {
        id: can_red
        source: "images/can_red.png"
        x: 1090
        y: 609
        opacity: 1
    }
    Image {
        id: motor_temp_yellow
        source: "images/motor_temp_yellow.png"
        x: 1095
        y: 616
        opacity: 1
    }
    Image {
        id: motor_temp_red
        source: "images/motor_temp_red.png"
        x: 1095
        y: 616
        opacity: 1
    }
    Image {
        id: glv_soc_red
        source: "images/glv_soc_red.png"
        x: 1096
        y: 638
        opacity: 1
    }
    Image {
        id: ess_temp_red
        source: "images/ess_temp_red.png"
        x: 1143
        y: 604
        opacity: 1
    }
    Image {
        id: tach_shift
        source: "images/tach_shift.png"
        x: 8
        y: 2
        opacity: 0
    }
    Image {
        id: tach
        source: "images/tach.png"
        x: 8
        y: 2
        opacity: 1
    }
    Image {
        id: fuel_b20
        source: "images/fuel_b20.png"
        x: 1213
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b19
        source: "images/fuel_b19.png"
        x: 1193
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b18
        source: "images/fuel_b18.png"
        x: 1172
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b17
        source: "images/fuel_b17.png"
        x: 1152
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b16
        source: "images/fuel_b16.png"
        x: 1132
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b15
        source: "images/fuel_b15.png"
        x: 1111
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b14
        source: "images/fuel_b14.png"
        x: 1091
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b13
        source: "images/fuel_b13.png"
        x: 1071
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b12
        source: "images/fuel_b12.png"
        x: 1051
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b11
        source: "images/fuel_b11.png"
        x: 1030
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b10
        source: "images/fuel_b10.png"
        x: 1010
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b9
        source: "images/fuel_b9.png"
        x: 990
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b8
        source: "images/fuel_b8.png"
        x: 970
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b7
        source: "images/fuel_b7.png"
        x: 949
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b6
        source: "images/fuel_b6.png"
        x: 929
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b5
        source: "images/fuel_b5.png"
        x: 909
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b4
        source: "images/fuel_b4.png"
        x: 889
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b3
        source: "images/fuel_b3.png"
        x: 868
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b2
        source: "images/fuel_b2.png"
        x: 848
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_b1
        source: "images/fuel_b1.png"
        x: 828
        y: 68
        opacity: 1
    }

    Image {
        id: fuel_r1
        source: "images/fuel_r1.png"
        x: 828
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_r2
        source: "images/fuel_r2.png"
        x: 848
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_y1
        source: "images/fuel_y1.png"
        x: 828
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_y2
        source: "images/fuel_y2.png"
        x: 848
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_y3
        source: "images/fuel_y3.png"
        x: 868
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_y4
        source: "images/fuel_y4.png"
        x: 889
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_y5
        source: "images/fuel_y5.png"
        x: 909
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_y6
        source: "images/fuel_y6.png"
        x: 929
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_y7
        source: "images/fuel_y7.png"
        x: 949
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_y8
        source: "images/fuel_y8.png"
        x: 970
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g1
        source: "images/fuel_g1.png"
        x: 828
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g2
        source: "images/fuel_g2.png"
        x: 848
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g3
        source: "images/fuel_g3.png"
        x: 868
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g4
        source: "images/fuel_g4.png"
        x: 889
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g5
        source: "images/fuel_g5.png"
        x: 909
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g6
        source: "images/fuel_g6.png"
        x: 929
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g7
        source: "images/fuel_g7.png"
        x: 949
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g8
        source: "images/fuel_g8.png"
        x: 970
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g9
        source: "images/fuel_g9.png"
        x: 990
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g10
        source: "images/fuel_g10.png"
        x: 1010
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g11
        source: "images/fuel_g11.png"
        x: 1030
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g12
        source: "images/fuel_g12.png"
        x: 1051
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g13
        source: "images/fuel_g13.png"
        x: 1071
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g14
        source: "images/fuel_g14.png"
        x: 1091
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g15
        source: "images/fuel_g15.png"
        x: 1111
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g16
        source: "images/fuel_g16.png"
        x: 1132
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g17
        source: "images/fuel_g17.png"
        x: 1152
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g18
        source: "images/fuel_g18.png"
        x: 1172
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g19
        source: "images/fuel_g19.png"
        x: 1193
        y: 68
        opacity: 1
    }
    Image {
        id: fuel_g20
        source: "images/fuel_g20.png"
        x: 1213
        y: 68
        opacity: 1
    }
    Image {
        id: soc_r1
        source: "images/soc_r1.png"
        x: 828
        y: 16
        opacity: 1
    }
    Image {
        id: soc_r2
        source: "images/soc_r2.png"
        x: 848
        y: 16
        opacity: 1
    }
    Image {
        id: soc_y1
        source: "images/soc_y1.png"
        x: 868
        y: 16
        opacity: 1
    }
    Image {
        id: soc_y2
        source: "images/soc_y2.png"
        x: 828
        y: 16
        opacity: 1
    }
    Image {
        id: soc_y3
        source: "images/soc_y3.png"
        x: 848
        y: 16
        opacity: 1
    }
    Image {
        id: soc_y4
        source: "images/soc_y4.png"
        x: 889
        y: 16
        opacity: 1
    }
    Image {
        id: soc_y5
        source: "images/soc_y5.png"
        x: 909
        y: 16
        opacity: 1
    }
    Image {
        id: soc_y6
        source: "images/soc_y6.png"
        x: 929
        y: 16
        opacity: 1
    }
    Image {
        id: soc_y7
        source: "images/soc_y7.png"
        x: 949
        y: 16
        opacity: 1
    }
    Image {
        id: soc_y8
        source: "images/soc_y8.png"
        x: 970
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g1
        source: "images/soc_g1.png"
        x: 828
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g2
        source: "images/soc_g2.png"
        x: 848
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g3
        source: "images/soc_g3.png"
        x: 868
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g4
        source: "images/soc_g4.png"
        x: 889
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g5
        source: "images/soc_g5.png"
        x: 909
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g6
        source: "images/soc_g6.png"
        x: 929
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g7
        source: "images/soc_g7.png"
        x: 949
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g8
        source: "images/soc_g8.png"
        x: 970
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g9
        source: "images/soc_g9.png"
        x: 990
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g10
        source: "images/soc_g10.png"
        x: 1010
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g11
        source: "images/soc_g11.png"
        x: 1030
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g12
        source: "images/soc_g12.png"
        x: 1051
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g13
        source: "images/soc_g13.png"
        x: 1071
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g14
        source: "images/soc_g14.png"
        x: 1091
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g15
        source: "images/soc_g15.png"
        x: 1111
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g16
        source: "images/soc_g16.png"
        x: 1132
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g17
        source: "images/soc_g17.png"
        x: 1152
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g18
        source: "images/soc_g18.png"
        x: 1172
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g19
        source: "images/soc_g19.png"
        x: 1193
        y: 16
        opacity: 1
    }
    Image {
        id: soc_g20
        source: "images/soc_g20.png"
        x: 1213
        y: 16
        opacity: 1
    }
    Image {
        id: tach_needle
        objectName: "tach_needle"
        source: "images/needle.png"
        x: 252
        y: 249
        opacity: 1
        transform: Rotation {
            // Transform origin is the middle point of the lower border
            origin {
                x: 31
                y: 29
            }
            //axis {x: 1; y: 0; z: 0}
            angle: tachNeedleAngle
        }
    }
    Text {
        id: speed
        x: 170
        y: 415
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
        x: 644
        y: 48
        color: "#9b8e8e"
        text: qsTr("1")
        font.bold: true
        font.family: "Tahoma"
        font.pixelSize: 175
    }
    Text {
        id: tempN
        x: 44
        y: 644
        width: 188
        height: 118
        color: qsTr("#ff0000")
        text: qsTr("0")
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        font.bold: true
        styleColor: "#ff0000"
        font.pixelSize: 100
    }
}
