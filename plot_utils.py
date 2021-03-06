#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#******************************************************************************
#* 
#* Copyright (C) 2015  Kiran Karra <kiran.karra@gmail.com>
#*
#* This program is free software: you can redistribute it and/or modify
#* it under the terms of the GNU General Public License as published by
#* the Free Software Foundation, either version 3 of the License, or
#* (at your option) any later version.
#*
#* This program is distributed in the hope that it will be useful,
#* but WITHOUT ANY WARRANTY; without even the implied warranty of
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#* GNU General Public License for more details.
#*
#* You should have received a copy of the GNU General Public License
#* along with this program.  If not, see <http://www.gnu.org/licenses/>.
#******************************************************************************

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd

def plot_3d(X,Y,Z, titleStr):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.xlabel('U1')
    plt.ylabel('U2')
    plt.title(titleStr)
    plt.show()

def pairs(X, titleStr):
    numCols = X.shape[1]
    # generate the columns 
    colNames = []
    for col in range(0,numCols):
        colNames.append(titleStr + ' U' + str(col+1))
    
    df = pd.DataFrame(X, columns=colNames)
    axes = pd.tools.plotting.scatter_matrix(df, alpha=0.2)

    # turn grids on
    for ax1 in axes:
        for ax in ax1:
            ax.grid()
    
    plt.tight_layout()
    plt.show()