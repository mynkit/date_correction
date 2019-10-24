'''日付をフォーマット化して返すクラスの作成
'''


import re
import traceback
import datetime


class date_correction(object):
    @staticmethod
    def jap_to_west(date, remove_day=False):
        '''令和平成昭和大正明治,RHSTM表記の和暦を含めて西暦に変換する関数(西暦そのものをつっこんでもよい)

        Args:
            date (datetime.datetime or int or str): 変換したい日付文字列
            remove_day (bool): 日付まで返すか，月までで十分か

        Returns:
            str : 'yyyy/mm/dd' or 'yyyy/mm'

        Examples:
            >>> from date_correction import date_correction
            >>> corrector = date_correction()
            >>> corrector.jap_to_west(1991)
            '1991'
            >>> corrector.jap_to_west('令和元年6月')
            '2019/06/01'
            >>> corrector.jap_to_west('1991/12/25', remove_day=True)
            '1991/12'
            >>> import datetime
            >>> corrector.jap_to_west(datetime.datetime(2000,1,15))
            '2000/01/15'

        '''
        try:
            if date is not None and date == date:
                y, m, d = None, None, None  # 初期化

                ''' datetime型のときはdate型の文字列に変更 '''
                if type(date) is datetime.datetime:
                    date = str(date.date())
                date = str(date)
                # datetime型を文字列にしてあった場合に対応
                date = re.sub(r'\d+:\d+:\d+', '', date)

                date = date.replace('元', '1')  # 元年は1年に変換
                date = re.sub(r'\s', '', date)  # 空欄は消す
                ymd = re.split(r'\D', date)
                ymd = [v for v in ymd if v != '']
                if sum([int(v in date) for v in ['令和', '平成', '昭和', '大正', '明治', 'R', 'H', 'S', 'T', 'M', 'r', 'h', 's', 't', 'm']]) == 1:
                    ''' dateが和暦だった場合の処理 '''
                    if sum([int(v in date) for v in ['令和', 'R', 'r']]) == 1:  # 令和のとき
                        if len(ymd) == 3:  # 年月日まで存在する場合
                            [y, m, d] = ymd
                            d = '%02d' % int(d)
                        elif len(ymd) == 2:  # 年月まで存在する場合
                            [y, m] = ymd
                        elif len(ymd) == 1:
                            [y] = ymd
                            m = 1
                        y = '%04d' % (int(y) + 2018)
                        m = '%02d' % int(m)
                    if sum([int(v in date) for v in ['平成', 'H', 'h']]) == 1:  # 平成のとき
                        if len(ymd) == 3:  # 年月日まで存在する場合
                            [y, m, d] = ymd
                            d = '%02d' % int(d)
                        elif len(ymd) == 2:  # 年月まで存在する場合
                            [y, m] = ymd
                        elif len(ymd) == 1:
                            [y] = ymd
                            m = 1
                        y = '%04d' % (int(y) + 1988)
                        m = '%02d' % int(m)
                    if sum([int(v in date) for v in ['昭和', 'S', 's']]) == 1:  # 昭和のとき
                        if len(ymd) == 3:  # 年月日まで存在する場合
                            [y, m, d] = ymd
                            d = '%02d' % int(d)
                        elif len(ymd) == 2:  # 年月まで存在する場合
                            [y, m] = ymd
                        elif len(ymd) == 1:
                            [y] = ymd
                            m = 1
                        y = '%04d' % (int(y) + 1925)
                        m = '%02d' % int(m)
                    if sum([int(v in date) for v in ['大正', 'T', 't']]) == 1:  # 大正のとき
                        if len(ymd) == 3:  # 年月日まで存在する場合
                            [y, m, d] = ymd
                            d = '%02d' % int(d)
                        elif len(ymd) == 2:  # 年月まで存在する場合
                            [y, m] = ymd
                        elif len(ymd) == 1:
                            [y] = ymd
                            m = 1
                        y = '%04d' % (int(y) + 1911)
                        m = '%02d' % int(m)
                    if sum([int(v in date) for v in ['明治', 'M', 'm']]) == 1:  # 明治のとき
                        if len(ymd) == 3:  # 年月日まで存在する場合
                            [y, m, d] = ymd
                            d = '%02d' % int(d)
                        elif len(ymd) == 2:  # 年月まで存在する場合
                            [y, m] = ymd
                        elif len(ymd) == 1:
                            [y] = ymd
                            m = 1
                        y = '%04d' % (int(y) + 1867)
                        m = '%02d' % int(m)

                else:
                    ''' dateが西暦表記だったとき '''
                    if re.match(r'\d{6}', date):
                        y = date[0:4]
                        m = date[4:6]
                        if re.match(r'\d{8}', date):
                            d = date[6:8]
                    if len(ymd) == 3:  # 年月日まで存在する場合
                        [y, m, d] = ymd
                        d = '%02d' % int(d)
                    elif len(ymd) == 2:  # 年月まで存在する場合
                        [y, m] = ymd
                    elif len(ymd) == 1:
                        [y] = ymd
                        m = 1
                    y = '%04d' % int(y)
                    m = '%02d' % int(m)

                if remove_day == True:
                    return y + '/' + m
                else:
                    if d is not None:
                        return y + '/' + m + '/' + d
                    else:
                        return y + '/' + m + '/01'

        except:
            traceback.print_exc()
            print(date)
            return None

