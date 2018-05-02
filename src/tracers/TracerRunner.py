#coding:utf-8
#!/usr/bin/env python
import os
import re
import requests,time
import shutil
import sys
import threading
import time
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

rootPath = sys.path[0][0:sys.path[0].index('StockParser')]+'/StockParser'
sys.path.append(rootPath+'/src') 
from common import Tools
from parsers import BaseParser



if __name__ == '__main__':
  # config ==========================================================================
  parserList = [
    #'BaldRiseLineAndVolumeReduceParser',
    #'GoldenPinBottomParser',
    #'MacdReverseParser',
    #'MaConvergenceParser',
    #'MaPenetrateParser',
    #'MaTrendParser',
    #'MaxPriceParser',
    #'OneLimitsParser',
    #'PenetrateUpwardMa60Parser',
    #'RgbParser',
    #'StandOn60Parser',
    #'SwallowUpParser',
    #'ThreeLimitsParser',
    #'TriangularSupportParser',
    #'TwoLimitsParser',
    #'VenusParser',
    #'VolumeMutationParser',
    'WJParser'
  ]

  beginDate = '2017-01-17'
  #beginDate = '2018-03-01'
  traceDays = 71 # 统计天数

  isNew = False if (len(sys.argv) <= 1) else ('new' ==sys.argv[1])
  if isNew:
    Tools.initDir('enterList')

    for parser in parserList:
      # run parser ======================================================================
      print parser,beginDate,traceDays
      dayList = BaseParser.BaseParser.getNextTradingDayList(beginDate,traceDays-1)
      dayList.insert(0,beginDate)
      print dayList

      dayList2 = [
        '2018-03-26',
      ]

      for parseDay in dayList:
        print parseDay
        cmd = 'python '+Tools.getParsersDirPath() + '/'+ parser +'.py ' + parseDay
        print cmd
        os.system(cmd)

  cmd = 'python '+Tools.getTracersDirPath() + '/WJTracer.py'
  os.system(cmd)
  
  cmd = 'python '+Tools.getTracersDirPath() + '/TracerReport.py'
  os.system(cmd)


   













