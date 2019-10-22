
![](./DocResources/2.png)
# VSTA
### Virtual Stock Trade Agent

#### The trade system base on the three basic model:
* Data Module
* Analysis Module
* Automatic Trade Client


#### First dev stage , we ready to build the dataIO module basic on the [tushare](https://github.com/waditu/tushare) & MYSQL like database API in python.

#### Second dev stage , we start build basic data analysis function base on pandas & so on.

#### Third dev stage , we use the standard XGBoost, GDBT , LSTM , GRU class & independent dataloader to train different Sub-Model ，the Multi-Model Fusion to predict in Long & Short term trade. The Fusion Model could be face to individual stock or group stock ,even whole market.

#### Fourth dev stage ，we use the Virtual Trade API to simulate the daily trade process，and design the Whole Trade Loss Function to eval the PROFIT of different fusion model.

#### Fifth dev stage ，we build Fusion Model support class to generate trade strategy template config file . We could modified it by some prior knowledge . Then use the simulate trade module to verify the trade strategy.

#### In the last version of this project , we will use the [Stock Trade Client Project](https://github.com/shidenggui/easytrader) to build a market monitoring auto-trade system.



### **Make Stock Trade Intelligence,Easy,& Fast**





Update Log:

> Oct.23.2019

First Init Work , Introduction ,Doc;







![](./DocResources/1.jpg)




#### Contributor：

####  [Tom Winshare](https://github.com/OOXXXXOO) ; [Peng jun]();
