
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import imageio
import cv2
import numpy as np
import math

def drawData(dataclass, BaseModel):
    prefix = 'PlotResults'
    font = {'family': 'serif', 'weight': 'normal', 'size': 12}
    matplotlib.rc('font', **font)
    LineWidth = 2
    fontsize = 10
    markersize = 3

    if dataclass == 'Kodak':
        if BaseModel == "FullRate":
            bpp = [0.11538357204861112,
                   0.18455335828993058,
                   0.300262451171875,
                   0.4586046006944445,
                   0.6429918077256943,
                   0.9030626085069445, ]
            psnr = [
                28.89405533399933,
                30.38678919426023,
                32.13403670256546,
                33.98858308377239,
                35.80802755754672,
                37.709914938896624,
            ]
            # bpp = [0.124,
            #         0.191,
            #         0.298,
            #         0.441,
            #         0.651,
            #         0.903]
            # psnr = [29.14,
            #         30.50,
            #         32.15,
            #         33.97,
            #         35.82,
            #         37.72 ]
            STF, = plt.plot(bpp, psnr, "-o", color="#95a2ff", linewidth=LineWidth,
                                  label='STF [MSE]')  ### from STF

            bpp = [0.14043511284722224,
                      0.20929294162326387,
                      0.3149041069878472,
                      0.4619310167100696,
                      0.651882595486111,
                      0.8945651584201388,
                      1.173845079210069,
                      1.405527750651042]
            psnr = [29.077883373802774,
                      30.53955663764249,
                      32.2366482625887,
                      34.03144734679171,
                      35.84216747472753,
                      37.646097058686145,
                      39.2421677850087,
                      40.276359533157496
                    ]

            STFQVRFD, = plt.plot(bpp, psnr, "-s", color="#63b2ee", linewidth=LineWidth,
                                  label='STF+QVRF (DVR)[MSE] ')

            bpp = [
                0.1580878363715278,
                0.18438042534722224,
                0.21951972113715276,
                0.2624308268229167,
                0.31270684136284727,
                0.377719455295139,
                0.43947686089409727,
                0.513092041015625,
                0.5827534993489583,
                0.609520806206597,
                0.686119927300347,
                0.781060112847222,
                0.8258768717447916,
                0.900482177734375,
                0.93084716796875,
                0.999118381076389,
                1.036231146918403,
                1.0722825792100696,
                1.1414659288194444,
                1.1662665473090277,
                1.1905517578125002,
                1.2532246907552085,
                1.2909003363715281,
                1.3627319335937502
            ]
            psnr = [
                29.49075154881946,
                30.050855259914684,
                30.72956086800414,
                31.45708664643908,
                32.20726093509745,
                33.06059824123179,
                33.78625457135397,
                34.565686267587516,
                35.22943971032149,
                35.47407880761901,
                36.12596063252735,
                36.8604606395618,
                37.18151909203548,
                37.68521485551254,
                37.881029061074095,
                38.29548134234708,
                38.510155851705925,
                38.712728440528146,
                39.07946166033019,
                39.20520754853885,
                39.324168191004375,
                39.62278784813385,
                39.792888646127686,
                40.10173618744478
                    ]
            STFQVRFC, = plt.plot(bpp, psnr, "-s", color="#e30039", linewidth=LineWidth,
                                  label='STF+QVRF (CVR)[MSE] ')




            plt.legend(handles=[STF, STFQVRFD, STFQVRFC], loc=4, fontsize=6)



    elif dataclass == 'CLIC':
        bpp = [0.124,
               0.191,
               0.298,
               0.441,
               0.651,
               0.903]
        psnr = [29.14,
                30.50,
                32.15,
                33.97,
                35.82,
                37.72]
        STF, = plt.plot(bpp, psnr, "-o", color="#95a2ff", linewidth=LineWidth,
                        label='STF [MSE]')  ### from STF

        bpp = [0.098115338,
               0.173912113,
               0.299725056,
               0.456783226,
               0.679351191,
               0.829]
        psnr = [27.98974522,
                29.82447267,
                31.8515377,
                33.87737664,
                35.62697935,
                36.654,
                ]
        STFQVRFD, = plt.plot(bpp, psnr, "-s", color="#63b2ee", linewidth=LineWidth,
                             label='STF+QVRF (DVR)[MSE] ')

        bpp = [0.098115338,
               0.173912113,
               0.299725056,
               0.456783226,
               0.679351191,
               0.829]
        psnr = [27.98974522,
                29.82447267,
                31.8515377,
                33.87737664,
                35.62697935,
                36.654,
                ]
        STFQVRFC, = plt.plot(bpp, psnr, "-s", color="#e30039", linewidth=LineWidth,
                             label='STF+QVRF (CVR)[MSE] ')

        plt.legend(handles=[STF, STFQVRFD, STFQVRFC], loc=4, fontsize=6)

    savepathpsnr = prefix + '/' + dataclass + '_psnr'  # + '.eps'
    print(prefix)
    if not os.path.exists(prefix):
        os.makedirs(prefix)


    plt.rcParams.update({'font.size': 12})

    plt.grid()
    plt.xlabel('bit per pixel (bpp)')
    plt.ylabel('PSNR (dB)')
    _, right = plt.xlim()  # return the current xlim
    plt.xlim((0, right))  # set the xlim to left, right


    bottom, top = plt.ylim()  # return the current ylim
    plt.ylim((max(24, bottom//2*2), top))  # set the xlim to left, right
    # plt.title(dataclass + ' dataset')
    # plt.savefig(savepathpsnr + '.eps', format='eps', dpi=300, bbox_inches='tight')
    plt.savefig(savepathpsnr + '.png', dpi=300)
    plt.clf()

    if dataclass == 'Kodak':
        if BaseModel == "FullRate":
            bpp = [0.11538357204861112,
                   0.18455335828993058,
                   0.300262451171875,
                   0.4586046006944445,
                   0.6429918077256943,
                0.9030626085069445,]
            msssim = [
                0.9273558557033539,
                0.9503604198495547,
                0.9675669645269712,
                0.9785798092683157,
                0.9854647070169449,
                0.9901745691895485,]
            STF, = plt.plot(bpp, -10 * np.log10(np.subtract(1, msssim)), "-o", color="#95a2ff", linewidth=LineWidth,
                            label='STF [MSE]')  ### from STF

            bpp = [0.14043511284722224,
                   0.20929294162326387,
                   0.3149041069878472,
                   0.4619310167100696,
                   0.651882595486111,
                   0.8945651584201388,
                   1.173845079210069,
                   1.405527750651042]
            msssim = [0.9320024773478508,
                      0.9515933692455292,
                      0.9673976227641106,
                      0.9783326561252276,
                      0.9854424372315407,
                      0.9900890116890272,
                      0.9928910235563914,
                      0.9942644263307253]

            STFQVRFD, = plt.plot(bpp, -10 * np.log10(np.subtract(1, msssim)), "-s", color="#63b2ee", linewidth=LineWidth,
                                 label='STF+QVRF (DVR)[MSE] ')

            bpp = [
                0.1580878363715278,
                0.18438042534722224,
                0.21951972113715276,
                0.2624308268229167,
                0.31270684136284727,
                0.377719455295139,
                0.43947686089409727,
                0.513092041015625,
                0.5827534993489583,
                0.609520806206597,
                0.686119927300347,
                0.781060112847222,
                0.8258768717447916,
                0.900482177734375,
                0.93084716796875,
                0.999118381076389,
                1.036231146918403,
                1.0722825792100696,
                1.1414659288194444,
                1.1662665473090277,
                1.1905517578125002,
                1.2532246907552085,
                1.2909003363715281,
                1.3627319335937502
            ]

            msssim = [
                0.9382740880052248,
                0.9458942512671152,
                0.9537162855267525,
                0.9609687228997549,
                0.967174286643664,
                0.9730047931273779,
                0.9771212860941887,
                0.9807775517304739,
                0.983382153014342,
                0.9842298775911331,
                0.9862969641884168,
                0.9882913678884506,
                0.9890654186407725,
                0.9901648585995039,
                0.9905528152982394,
                0.9913340533773104,
                0.9917171547810236,
                0.9920539632439613,
                0.9926423951983452,
                0.9928343643744787,
                0.9930118595560392,
                0.9934323181708654,
                0.9936605716745058,
                0.994054821630319
            ]
            STFQVRFC, = plt.plot(bpp, -10 * np.log10(np.subtract(1, msssim)), "-s", color="#e30039", linewidth=LineWidth,
                                 label='STF+QVRF (CVR)[MSE] ')

            plt.legend(handles=[STF, STFQVRFD, STFQVRFC], loc=4, fontsize=6)

    else:
        bpp = []
        msssim = []
        STF, = plt.plot(bpp, -10 * np.log10(np.subtract(1, msssim)), "-o", color="#95a2ff", linewidth=LineWidth,
                        label='STF [MSE]')  ### from STF

        bpp = []
        msssim = [
                  ]
        STFQVRFD, = plt.plot(bpp, -10 * np.log10(np.subtract(1, msssim)), "-s", color="#63b2ee", linewidth=LineWidth,
                             label='STF+QVRF (DVR)[MSE] ')

        bpp = []
        msssim = [
                  ]
        STFQVRFC, = plt.plot(bpp, 10 * np.log10(np.subtract(1, msssim)), "-s", color="#e30039", linewidth=LineWidth,
                             label='STF+QVRF (CVR)[MSE] ')

        plt.legend(handles=[STF, STFQVRFD, STFQVRFC], loc=4, fontsize=6)


    savepathmsssim = prefix + '/' + dataclass + '_msssim'  # + '.eps'

    plt.rcParams.update({'font.size': 12})
    left, right = plt.xlim()  # return the current xlim
    plt.xlim((0, right))  # set the xlim to left, right
    plt.grid()
    plt.xlabel('bit per pixel (bpp)')
    plt.ylabel('MS-SSIM (dB)')
    # plt.title(dataclass + ' dataset')
    # plt.savefig(savepathmsssim + '.eps', format='eps', dpi=300, bbox_inches='tight')
    plt.savefig(savepathmsssim + '.png', dpi=300)
    plt.clf()

    savepath = prefix + '/' + dataclass + '.png'
    img1 = cv2.imread(savepathpsnr + '.png')
    img2 = cv2.imread(savepathmsssim + '.png')

    image = np.concatenate((img1, img2), axis=1)
    cv2.imwrite(savepath, image)


drawData('Kodak', 'FullRate')



