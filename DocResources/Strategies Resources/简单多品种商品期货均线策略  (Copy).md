
> 策略名称

简单多品种商品期货均线策略  (Copy)

> 策略作者

ktz

> 策略描述

商品期货类库实现了$.CTA函数的策略框架，借助该策略框架, 可以短短几十行实现一个并发稳定可实盘的多品种策略

 https://dn-filebox.qbox.me/21384f4e53937bc1dd252ff478ff08e5b4d52e71.png

> 策略参数



|参数|默认值|描述|
|----|----|----|
|Symbols|rb000,MA000|操作品种|
|FastPeriod|5|快线周期|
|SlowPeriod|20|慢线周期|
|ConfirmPeriod|2|确认周期|
|Lots|true|开仓手数|


> 源码 (javascript)

``` javascript
/*backtest
start: 2017-06-01 00:00:00
end: 2017-10-01 00:00:00
period: 1d
*/
function main() {
    // 使用了商品期货类库的CTA策略框架
    $.CTA(Symbols, function(st) {
        var r = st.records
        var mp = st.position.amount
        var symbol = st.symbol
        /*
        r为K线, mp为当前品种持仓数量, 正数指多仓, 负数指空仓, 0则不持仓, symbol指品种名称
        返回值如为n: 
            n = 0 : 指全部平仓(不管当前持多持空)
            n > 0 : 如果当前持多仓，则加n个多仓, 如果当前为空仓则平n个空仓,如果n大于当前持仓, 则反手开多仓
            n < 0 : 如果当前持空仓，则加n个空仓, 如果当前为多仓则平n个多仓,如果-n大于当前持仓, 则反手开空仓
            无返回值表示什么也不做
        */
        if (r.length < SlowPeriod) {
            return
        }
        var cross = _Cross(TA.EMA(r, FastPeriod), TA.EMA(r, SlowPeriod));
        if (mp <= 0 && cross > ConfirmPeriod) {
            Log(symbol, "金叉周期", cross, "当前持仓", mp);
            return Lots * (mp < 0 ? 2 : 1)
        } else if (mp >= 0 && cross < -ConfirmPeriod) {
            Log(symbol, "死叉周期", cross, "当前持仓", mp);
            return -Lots * (mp > 0 ? 2 : 1)
        }
    });
}
```

> 策略出处

https://www.fmz.com/strategy/159506

> 更新时间

2019-07-30 22:26:44
