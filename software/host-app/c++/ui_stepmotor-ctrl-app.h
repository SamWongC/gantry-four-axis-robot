/********************************************************************************
** Form generated from reading UI file 'stepmotor-ctrl-appzYgRZz.ui'
**
** Created by: Qt User Interface Compiler version 6.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef STEPMOTOR_2D_CTRL_2D_APPZYGRZZ_H
#define STEPMOTOR_2D_CTRL_2D_APPZYGRZZ_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout;
    QFrame *frame_2;
    QHBoxLayout *horizontalLayout_3;
    QGroupBox *gbDevice;
    QGridLayout *gridLayout;
    QSpacerItem *verticalSpacer_3;
    QPushButton *pbUartOpen;
    QSpacerItem *verticalSpacer_2;
    QComboBox *cbUartPort;
    QSpacerItem *verticalSpacer;
    QLabel *label;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_2;
    QSpacerItem *horizontalSpacer;
    QPushButton *pbWriteDevAdr;
    QComboBox *motor_adr;
    QComboBox *m1_pulse_cnt;
    QComboBox *run_spd;
    QLabel *label_5;
    QLabel *label_2;
    QSpacerItem *horizontalSpacer_2;
    QLabel *label_7;
    QLabel *label_3;
    QLabel *label_6;
    QLabel *label_8;
    QComboBox *m2_pulse_cnt;
    QComboBox *m3_pulse_cnt;
    QComboBox *m4_pulse_cnt;
    QPushButton *pbAllMotorRun;
    QPushButton *encoder_clear;
    QPushButton *pbGenerate;
    QPushButton *pbStop;
    QFrame *frame_3;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_4;
    QLabel *label_datetime;
    QPushButton *pbExit;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName("Dialog");
        Dialog->resize(737, 435);
        verticalLayout = new QVBoxLayout(Dialog);
        verticalLayout->setObjectName("verticalLayout");
        frame_2 = new QFrame(Dialog);
        frame_2->setObjectName("frame_2");
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(frame_2->sizePolicy().hasHeightForWidth());
        frame_2->setSizePolicy(sizePolicy);
        QFont font;
        font.setPointSize(10);
        frame_2->setFont(font);
        frame_2->setFrameShape(QFrame::WinPanel);
        frame_2->setFrameShadow(QFrame::Sunken);
        frame_2->setLineWidth(1);
        horizontalLayout_3 = new QHBoxLayout(frame_2);
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        horizontalLayout_3->setContentsMargins(0, -1, -1, -1);
        gbDevice = new QGroupBox(frame_2);
        gbDevice->setObjectName("gbDevice");
        gbDevice->setMinimumSize(QSize(160, 0));
        gbDevice->setMaximumSize(QSize(256, 16777215));
        QFont font1;
        font1.setPointSize(9);
        gbDevice->setFont(font1);
        gbDevice->setStyleSheet(QString::fromUtf8("background-color: rgb(214, 214, 214);"));
        gbDevice->setAlignment(Qt::AlignCenter);
        gridLayout = new QGridLayout(gbDevice);
        gridLayout->setObjectName("gridLayout");
        gridLayout->setContentsMargins(2, -1, 8, -1);
        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 4, 0, 1, 1);

        pbUartOpen = new QPushButton(gbDevice);
        pbUartOpen->setObjectName("pbUartOpen");
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(pbUartOpen->sizePolicy().hasHeightForWidth());
        pbUartOpen->setSizePolicy(sizePolicy1);
        pbUartOpen->setMinimumSize(QSize(100, 32));
        pbUartOpen->setCursor(QCursor(Qt::PointingHandCursor));
        pbUartOpen->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(0, 181, 80);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}"));

        gridLayout->addWidget(pbUartOpen, 3, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_2, 5, 0, 1, 1);

        cbUartPort = new QComboBox(gbDevice);
        cbUartPort->addItem(QString());
        cbUartPort->addItem(QString());
        cbUartPort->addItem(QString());
        cbUartPort->setObjectName("cbUartPort");
        sizePolicy1.setHeightForWidth(cbUartPort->sizePolicy().hasHeightForWidth());
        cbUartPort->setSizePolicy(sizePolicy1);
        cbUartPort->setMinimumSize(QSize(96, 32));

        gridLayout->addWidget(cbUartPort, 2, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 0, 0, 1, 1);

        label = new QLabel(gbDevice);
        label->setObjectName("label");
        label->setMinimumSize(QSize(64, 32));
        label->setMaximumSize(QSize(64, 32));
        label->setFont(font);
        label->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label, 1, 0, 1, 1);


        horizontalLayout_3->addWidget(gbDevice);

        groupBox_2 = new QGroupBox(frame_2);
        groupBox_2->setObjectName("groupBox_2");
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(groupBox_2->sizePolicy().hasHeightForWidth());
        groupBox_2->setSizePolicy(sizePolicy2);
        groupBox_2->setMinimumSize(QSize(0, 256));
        groupBox_2->setFont(font1);
        groupBox_2->setStyleSheet(QString::fromUtf8("background-color: rgb(214, 214, 214);"));
        groupBox_2->setAlignment(Qt::AlignCenter);
        gridLayout_2 = new QGridLayout(groupBox_2);
        gridLayout_2->setObjectName("gridLayout_2");
        gridLayout_2->setHorizontalSpacing(32);
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 2, 9, 1, 1);

        pbWriteDevAdr = new QPushButton(groupBox_2);
        pbWriteDevAdr->setObjectName("pbWriteDevAdr");
        sizePolicy1.setHeightForWidth(pbWriteDevAdr->sizePolicy().hasHeightForWidth());
        pbWriteDevAdr->setSizePolicy(sizePolicy1);
        pbWriteDevAdr->setMinimumSize(QSize(100, 32));
        pbWriteDevAdr->setMaximumSize(QSize(96, 16777215));
        pbWriteDevAdr->setCursor(QCursor(Qt::PointingHandCursor));
        pbWriteDevAdr->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(180, 80, 0);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}"));

        gridLayout_2->addWidget(pbWriteDevAdr, 0, 8, 1, 1);

        motor_adr = new QComboBox(groupBox_2);
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->addItem(QString());
        motor_adr->setObjectName("motor_adr");
        motor_adr->setMinimumSize(QSize(96, 32));
        motor_adr->setMaximumSize(QSize(96, 16777215));
        motor_adr->setEditable(true);

        gridLayout_2->addWidget(motor_adr, 0, 2, 1, 1);

        m1_pulse_cnt = new QComboBox(groupBox_2);
        m1_pulse_cnt->addItem(QString());
        m1_pulse_cnt->addItem(QString());
        m1_pulse_cnt->addItem(QString());
        m1_pulse_cnt->addItem(QString());
        m1_pulse_cnt->addItem(QString());
        m1_pulse_cnt->setObjectName("m1_pulse_cnt");
        QSizePolicy sizePolicy3(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(m1_pulse_cnt->sizePolicy().hasHeightForWidth());
        m1_pulse_cnt->setSizePolicy(sizePolicy3);
        m1_pulse_cnt->setMinimumSize(QSize(96, 32));
        m1_pulse_cnt->setMaximumSize(QSize(96, 16777215));
        m1_pulse_cnt->setEditable(true);

        gridLayout_2->addWidget(m1_pulse_cnt, 2, 2, 1, 1);

        run_spd = new QComboBox(groupBox_2);
        run_spd->addItem(QString());
        run_spd->addItem(QString());
        run_spd->addItem(QString());
        run_spd->addItem(QString());
        run_spd->setObjectName("run_spd");
        run_spd->setMinimumSize(QSize(96, 32));
        run_spd->setMaximumSize(QSize(96, 16777215));
        run_spd->setEditable(true);

        gridLayout_2->addWidget(run_spd, 1, 2, 1, 1);

        label_5 = new QLabel(groupBox_2);
        label_5->setObjectName("label_5");
        sizePolicy2.setHeightForWidth(label_5->sizePolicy().hasHeightForWidth());
        label_5->setSizePolicy(sizePolicy2);
        label_5->setMinimumSize(QSize(64, 32));
        label_5->setMaximumSize(QSize(96, 32));
        label_5->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_5, 1, 1, 1, 1);

        label_2 = new QLabel(groupBox_2);
        label_2->setObjectName("label_2");
        label_2->setMinimumSize(QSize(64, 32));
        label_2->setMaximumSize(QSize(96, 32));
        label_2->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout_2->addWidget(label_2, 2, 1, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 2, 0, 1, 1);

        label_7 = new QLabel(groupBox_2);
        label_7->setObjectName("label_7");
        sizePolicy2.setHeightForWidth(label_7->sizePolicy().hasHeightForWidth());
        label_7->setSizePolicy(sizePolicy2);
        label_7->setMinimumSize(QSize(64, 32));
        label_7->setMaximumSize(QSize(96, 32));
        label_7->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_7, 0, 1, 1, 1);

        label_3 = new QLabel(groupBox_2);
        label_3->setObjectName("label_3");
        label_3->setMinimumSize(QSize(64, 32));
        label_3->setMaximumSize(QSize(96, 32));
        label_3->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout_2->addWidget(label_3, 3, 1, 1, 1);

        label_6 = new QLabel(groupBox_2);
        label_6->setObjectName("label_6");
        label_6->setMinimumSize(QSize(64, 32));
        label_6->setMaximumSize(QSize(96, 32));
        label_6->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout_2->addWidget(label_6, 4, 1, 1, 1);

        label_8 = new QLabel(groupBox_2);
        label_8->setObjectName("label_8");
        label_8->setMinimumSize(QSize(64, 32));
        label_8->setMaximumSize(QSize(96, 32));
        label_8->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout_2->addWidget(label_8, 5, 1, 1, 1);

        m2_pulse_cnt = new QComboBox(groupBox_2);
        m2_pulse_cnt->addItem(QString());
        m2_pulse_cnt->addItem(QString());
        m2_pulse_cnt->addItem(QString());
        m2_pulse_cnt->addItem(QString());
        m2_pulse_cnt->addItem(QString());
        m2_pulse_cnt->setObjectName("m2_pulse_cnt");
        sizePolicy3.setHeightForWidth(m2_pulse_cnt->sizePolicy().hasHeightForWidth());
        m2_pulse_cnt->setSizePolicy(sizePolicy3);
        m2_pulse_cnt->setMinimumSize(QSize(96, 32));
        m2_pulse_cnt->setMaximumSize(QSize(96, 16777215));
        m2_pulse_cnt->setEditable(true);

        gridLayout_2->addWidget(m2_pulse_cnt, 3, 2, 1, 1);

        m3_pulse_cnt = new QComboBox(groupBox_2);
        m3_pulse_cnt->addItem(QString());
        m3_pulse_cnt->addItem(QString());
        m3_pulse_cnt->addItem(QString());
        m3_pulse_cnt->addItem(QString());
        m3_pulse_cnt->addItem(QString());
        m3_pulse_cnt->setObjectName("m3_pulse_cnt");
        sizePolicy3.setHeightForWidth(m3_pulse_cnt->sizePolicy().hasHeightForWidth());
        m3_pulse_cnt->setSizePolicy(sizePolicy3);
        m3_pulse_cnt->setMinimumSize(QSize(96, 32));
        m3_pulse_cnt->setMaximumSize(QSize(96, 16777215));
        m3_pulse_cnt->setEditable(true);

        gridLayout_2->addWidget(m3_pulse_cnt, 4, 2, 1, 1);

        m4_pulse_cnt = new QComboBox(groupBox_2);
        m4_pulse_cnt->addItem(QString());
        m4_pulse_cnt->addItem(QString());
        m4_pulse_cnt->addItem(QString());
        m4_pulse_cnt->addItem(QString());
        m4_pulse_cnt->addItem(QString());
        m4_pulse_cnt->setObjectName("m4_pulse_cnt");
        sizePolicy3.setHeightForWidth(m4_pulse_cnt->sizePolicy().hasHeightForWidth());
        m4_pulse_cnt->setSizePolicy(sizePolicy3);
        m4_pulse_cnt->setMinimumSize(QSize(96, 32));
        m4_pulse_cnt->setMaximumSize(QSize(96, 16777215));
        m4_pulse_cnt->setEditable(true);

        gridLayout_2->addWidget(m4_pulse_cnt, 5, 2, 1, 1);

        pbAllMotorRun = new QPushButton(groupBox_2);
        pbAllMotorRun->setObjectName("pbAllMotorRun");
        sizePolicy1.setHeightForWidth(pbAllMotorRun->sizePolicy().hasHeightForWidth());
        pbAllMotorRun->setSizePolicy(sizePolicy1);
        pbAllMotorRun->setMinimumSize(QSize(100, 32));
        pbAllMotorRun->setMaximumSize(QSize(96, 16777215));
        pbAllMotorRun->setCursor(QCursor(Qt::PointingHandCursor));
        pbAllMotorRun->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(0, 180, 180);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}"));

        gridLayout_2->addWidget(pbAllMotorRun, 4, 8, 1, 1);

        encoder_clear = new QPushButton(groupBox_2);
        encoder_clear->setObjectName("encoder_clear");
        sizePolicy1.setHeightForWidth(encoder_clear->sizePolicy().hasHeightForWidth());
        encoder_clear->setSizePolicy(sizePolicy1);
        encoder_clear->setMinimumSize(QSize(100, 32));
        encoder_clear->setMaximumSize(QSize(96, 16777215));
        encoder_clear->setCursor(QCursor(Qt::PointingHandCursor));
        encoder_clear->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(0, 181, 0);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}"));

        gridLayout_2->addWidget(encoder_clear, 5, 8, 1, 1);

        pbGenerate = new QPushButton(groupBox_2);
        pbGenerate->setObjectName("pbGenerate");
        sizePolicy1.setHeightForWidth(pbGenerate->sizePolicy().hasHeightForWidth());
        pbGenerate->setSizePolicy(sizePolicy1);
        pbGenerate->setMinimumSize(QSize(100, 32));
        pbGenerate->setMaximumSize(QSize(96, 16777215));
        pbGenerate->setCursor(QCursor(Qt::PointingHandCursor));
        pbGenerate->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(0, 181, 0);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}"));

        gridLayout_2->addWidget(pbGenerate, 1, 8, 1, 1);

        pbStop = new QPushButton(groupBox_2);
        pbStop->setObjectName("pbStop");
        sizePolicy1.setHeightForWidth(pbStop->sizePolicy().hasHeightForWidth());
        pbStop->setSizePolicy(sizePolicy1);
        pbStop->setMinimumSize(QSize(100, 32));
        pbStop->setMaximumSize(QSize(96, 16777215));
        pbStop->setCursor(QCursor(Qt::PointingHandCursor));
        pbStop->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(0, 181, 0);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 255, 0); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}"));

        gridLayout_2->addWidget(pbStop, 2, 8, 1, 1);


        horizontalLayout_3->addWidget(groupBox_2);

        horizontalLayout_3->setStretch(0, 1);
        horizontalLayout_3->setStretch(1, 4);

        verticalLayout->addWidget(frame_2);

        frame_3 = new QFrame(Dialog);
        frame_3->setObjectName("frame_3");
        frame_3->setMinimumSize(QSize(0, 40));
        frame_3->setMaximumSize(QSize(16777215, 40));
        frame_3->setFrameShape(QFrame::WinPanel);
        frame_3->setFrameShadow(QFrame::Sunken);
        horizontalLayout_2 = new QHBoxLayout(frame_3);
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        horizontalLayout_2->setContentsMargins(-1, 0, 20, 0);
        label_4 = new QLabel(frame_3);
        label_4->setObjectName("label_4");

        horizontalLayout_2->addWidget(label_4);

        label_datetime = new QLabel(frame_3);
        label_datetime->setObjectName("label_datetime");

        horizontalLayout_2->addWidget(label_datetime);

        pbExit = new QPushButton(frame_3);
        pbExit->setObjectName("pbExit");
        sizePolicy1.setHeightForWidth(pbExit->sizePolicy().hasHeightForWidth());
        pbExit->setSizePolicy(sizePolicy1);
        pbExit->setMinimumSize(QSize(96, 32));
        pbExit->setCursor(QCursor(Qt::PointingHandCursor));
        pbExit->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"  border-style: inset; border-width: 1px; \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: rgb(154, 154, 154);\n"
"  border-radius: 8px; \n"
"  border-color: beige; padding: 3px; \n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(127, 0, 20); \n"
"  color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"  background-color: #3daee9; color: #7FFF7F\n"
"}"));
        pbExit->setFlat(false);

        horizontalLayout_2->addWidget(pbExit);


        verticalLayout->addWidget(frame_3);

        verticalLayout->setStretch(0, 2);

        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QCoreApplication::translate("Dialog", "Dialog", nullptr));
        gbDevice->setTitle(QCoreApplication::translate("Dialog", "\351\251\261\345\212\250\345\231\250 - \346\234\252 \350\277\236 \346\216\245", nullptr));
        pbUartOpen->setText(QCoreApplication::translate("Dialog", "\346\211\223\345\274\200\344\270\262\345\217\243", nullptr));
        cbUartPort->setItemText(0, QCoreApplication::translate("Dialog", "com1", nullptr));
        cbUartPort->setItemText(1, QCoreApplication::translate("Dialog", "com2", nullptr));
        cbUartPort->setItemText(2, QCoreApplication::translate("Dialog", "com3", nullptr));

        label->setText(QCoreApplication::translate("Dialog", "\344\270\262\345\217\243\345\220\215\347\247\260", nullptr));
        groupBox_2->setTitle(QCoreApplication::translate("Dialog", " \347\224\265 \346\234\272 \351\251\261 \345\212\250 \345\231\250 \350\277\220 \350\241\214 \346\216\247 \345\210\266", nullptr));
        pbWriteDevAdr->setText(QCoreApplication::translate("Dialog", "\345\206\231\350\256\276\345\244\207\345\234\260\345\235\200", nullptr));
        motor_adr->setItemText(0, QCoreApplication::translate("Dialog", "1", nullptr));
        motor_adr->setItemText(1, QCoreApplication::translate("Dialog", "2", nullptr));
        motor_adr->setItemText(2, QCoreApplication::translate("Dialog", "3", nullptr));
        motor_adr->setItemText(3, QCoreApplication::translate("Dialog", "4", nullptr));
        motor_adr->setItemText(4, QCoreApplication::translate("Dialog", "5", nullptr));
        motor_adr->setItemText(5, QCoreApplication::translate("Dialog", "6", nullptr));
        motor_adr->setItemText(6, QCoreApplication::translate("Dialog", "7", nullptr));
        motor_adr->setItemText(7, QCoreApplication::translate("Dialog", "8", nullptr));
        motor_adr->setItemText(8, QCoreApplication::translate("Dialog", "9", nullptr));
        motor_adr->setItemText(9, QCoreApplication::translate("Dialog", "10", nullptr));
        motor_adr->setItemText(10, QCoreApplication::translate("Dialog", "11", nullptr));
        motor_adr->setItemText(11, QCoreApplication::translate("Dialog", "12", nullptr));
        motor_adr->setItemText(12, QCoreApplication::translate("Dialog", "13", nullptr));
        motor_adr->setItemText(13, QCoreApplication::translate("Dialog", "14", nullptr));
        motor_adr->setItemText(14, QCoreApplication::translate("Dialog", "15", nullptr));
        motor_adr->setItemText(15, QCoreApplication::translate("Dialog", "16", nullptr));
        motor_adr->setItemText(16, QCoreApplication::translate("Dialog", "17", nullptr));
        motor_adr->setItemText(17, QCoreApplication::translate("Dialog", "18", nullptr));
        motor_adr->setItemText(18, QCoreApplication::translate("Dialog", "19", nullptr));
        motor_adr->setItemText(19, QCoreApplication::translate("Dialog", "20", nullptr));

        m1_pulse_cnt->setItemText(0, QCoreApplication::translate("Dialog", "6400", nullptr));
        m1_pulse_cnt->setItemText(1, QCoreApplication::translate("Dialog", "12800", nullptr));
        m1_pulse_cnt->setItemText(2, QCoreApplication::translate("Dialog", "25600", nullptr));
        m1_pulse_cnt->setItemText(3, QCoreApplication::translate("Dialog", "51200", nullptr));
        m1_pulse_cnt->setItemText(4, QCoreApplication::translate("Dialog", "128000", nullptr));

        m1_pulse_cnt->setCurrentText(QCoreApplication::translate("Dialog", "6400", nullptr));
        run_spd->setItemText(0, QCoreApplication::translate("Dialog", "500", nullptr));
        run_spd->setItemText(1, QCoreApplication::translate("Dialog", "1000", nullptr));
        run_spd->setItemText(2, QCoreApplication::translate("Dialog", "2000", nullptr));
        run_spd->setItemText(3, QCoreApplication::translate("Dialog", "5000", nullptr));

        run_spd->setCurrentText(QCoreApplication::translate("Dialog", "500", nullptr));
        label_5->setText(QCoreApplication::translate("Dialog", "\350\277\220\350\241\214\346\227\266\351\227\264(ms)", nullptr));
        label_2->setText(QCoreApplication::translate("Dialog", "\347\224\265\346\234\2721\350\204\211\345\206\262", nullptr));
        label_7->setText(QCoreApplication::translate("Dialog", "\347\224\265\346\234\272\347\274\226\345\217\267", nullptr));
        label_3->setText(QCoreApplication::translate("Dialog", "\347\224\265\346\234\2722\350\204\211\345\206\262", nullptr));
        label_6->setText(QCoreApplication::translate("Dialog", "\347\224\265\346\234\2723\350\204\211\345\206\262", nullptr));
        label_8->setText(QCoreApplication::translate("Dialog", "\347\224\265\346\234\2723\350\204\211\345\206\262", nullptr));
        m2_pulse_cnt->setItemText(0, QCoreApplication::translate("Dialog", "6400", nullptr));
        m2_pulse_cnt->setItemText(1, QCoreApplication::translate("Dialog", "12800", nullptr));
        m2_pulse_cnt->setItemText(2, QCoreApplication::translate("Dialog", "25600", nullptr));
        m2_pulse_cnt->setItemText(3, QCoreApplication::translate("Dialog", "51200", nullptr));
        m2_pulse_cnt->setItemText(4, QCoreApplication::translate("Dialog", "128000", nullptr));

        m2_pulse_cnt->setCurrentText(QCoreApplication::translate("Dialog", "6400", nullptr));
        m3_pulse_cnt->setItemText(0, QCoreApplication::translate("Dialog", "6400", nullptr));
        m3_pulse_cnt->setItemText(1, QCoreApplication::translate("Dialog", "12800", nullptr));
        m3_pulse_cnt->setItemText(2, QCoreApplication::translate("Dialog", "25600", nullptr));
        m3_pulse_cnt->setItemText(3, QCoreApplication::translate("Dialog", "51200", nullptr));
        m3_pulse_cnt->setItemText(4, QCoreApplication::translate("Dialog", "128000", nullptr));

        m3_pulse_cnt->setCurrentText(QCoreApplication::translate("Dialog", "6400", nullptr));
        m4_pulse_cnt->setItemText(0, QCoreApplication::translate("Dialog", "6400", nullptr));
        m4_pulse_cnt->setItemText(1, QCoreApplication::translate("Dialog", "12800", nullptr));
        m4_pulse_cnt->setItemText(2, QCoreApplication::translate("Dialog", "25600", nullptr));
        m4_pulse_cnt->setItemText(3, QCoreApplication::translate("Dialog", "51200", nullptr));
        m4_pulse_cnt->setItemText(4, QCoreApplication::translate("Dialog", "128000", nullptr));

        m4_pulse_cnt->setCurrentText(QCoreApplication::translate("Dialog", "6400", nullptr));
        pbAllMotorRun->setText(QCoreApplication::translate("Dialog", "\345\271\277\346\222\255\345\220\257\345\212\250", nullptr));
        encoder_clear->setText(QCoreApplication::translate("Dialog", "\344\275\215\347\275\256\350\204\211\345\206\262\346\270\205\351\233\266", nullptr));
        pbGenerate->setText(QCoreApplication::translate("Dialog", "\347\224\265\346\234\272\345\220\257\345\212\250", nullptr));
        pbStop->setText(QCoreApplication::translate("Dialog", "\347\224\265\346\234\272\345\201\234\346\255\242", nullptr));
        label_4->setText(QCoreApplication::translate("Dialog", "\345\223\210\345\260\224\346\273\250\345\267\245\344\270\232\345\244\247\345\255\246\346\234\272\347\224\265\346\216\247\345\210\266\345\217\212\350\207\252\345\212\250\345\214\226\347\263\273", nullptr));
        label_datetime->setText(QCoreApplication::translate("Dialog", "2021-05-17", nullptr));
        pbExit->setText(QCoreApplication::translate("Dialog", "\351\200\200\345\207\272\347\250\213\345\272\217", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // STEPMOTOR_2D_CTRL_2D_APPZYGRZZ_H
