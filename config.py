# @Time    : 2/24/23 11:43 AM
# @Author  : Ruizhi Cheng
# @FileName: config.py.py
# @Email   : rcheng4@gmu.edu
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
import os

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
dash_line = {0:'-',1:'--',2:'-.'}
marker = {0:'o',1:'v',2:'s',3:'X',4:'p',5:'s',6:'p',7:'*',8:'h',9:'H',10:'D',11:'d',12:'P',13:'X',14:'8',15:'|',16:'_',17:'4',18:'3',19:'2',20:'1',21:'0',22:'x',23:'+','o':'o','v':'v','^':'^','<':'<','>':'>','s':'s','p':'p','*':'*','h':'h','H':'H','D':'D','d':'d','P':'P','X':'X','8':'8','|':'|','_':'_','4':'4','3':'3','2':'2','1':'1','0':'0','x':'x','+':'+'}
marker_size = 15
color=['#1f77b4','#2ca02c','#d62728','#9467bd','#ff7f0e','#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf']
FONT_SIZE = 70
LABEL_SIZE = 70
LINE_WIDTH = 7
LEGEND_FONT_SIZE = 70

def plot(data_n_label,x_label,y_label,x_ticks=None,y_ticks=None,x_lim=None,y_lim=None,bbox_to_anchor=(0.5, 1.2)):
    #x = np.arange(1, len(data_n_label[0][0]) + 1, 1)
    fig, ax1 = plt.subplots()
    ax1.set_xlabel(x_label, fontsize=FONT_SIZE)
    ax1.set_ylabel(y_label, fontsize=FONT_SIZE)
    ##linewidth = 8 or 15
    for i in range(len(data_n_label)):
        ax1.plot(x_ticks, data_n_label[i][0], label=data_n_label[i][1], linewidth=LINE_WIDTH)
        #print(x)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ### 120 or 80
    ax1.tick_params(axis='x', labelsize=LABEL_SIZE)
    ax1.tick_params(axis='y', labelsize=LABEL_SIZE)

    if x_ticks is not None:
        ax1.set_xticks(x_ticks)

    if y_ticks is not None:
        ax1.set_yticks(y_ticks)

    if x_lim is not None:
        ax1.set_xlim(x_lim)

    if y_lim is not None:
        ax1.set_ylim(y_lim)
    plt.subplots_adjust(bottom=0.18, left=0.18)
    plt.grid()
    plt.legend(fontsize=LEGEND_FONT_SIZE, loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=2, columnspacing=0.4)
    plt.show()


def plot_with_error_bar(data_n_label,x_label,y_label,x_ticks=None,y_ticks=None,x_lim=None,y_lim=None,bbox_to_anchor=(0.5, 1.2)):
    #x = np.arange(1, len(data_n_label[0][0]) + 1, 1)
    fig, ax1 = plt.subplots()
    ax1.set_xlabel(x_label, fontsize=FONT_SIZE)
    ax1.set_ylabel(y_label, fontsize=FONT_SIZE)
    ##linewidth = 8 or 15
    for i in range(len(data_n_label)):
        ax1.plot(x_ticks, data_n_label[i][0], label=data_n_label[i][1], linewidth=LINE_WIDTH)
        #print(x)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ### 120 or 80
    ax1.tick_params(axis='x', labelsize=LABEL_SIZE)
    ax1.tick_params(axis='y', labelsize=LABEL_SIZE)

    if x_ticks is not None:
        ax1.set_xticks(x_ticks)

    if y_ticks is not None:
        ax1.set_yticks(y_ticks)

    if x_lim is not None:
        ax1.set_xlim(x_lim)

    if y_lim is not None:
        ax1.set_ylim(y_lim)
    plt.subplots_adjust(bottom=0.18, left=0.18)
    plt.grid()
    plt.legend(fontsize=LEGEND_FONT_SIZE, loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=2, columnspacing=0.4)
    plt.show()