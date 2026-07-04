import { Routes } from '@angular/router';
import { Home } from './home/home';
import { BuyStocks } from './buy-stocks/buy-stocks';
import { BinarySearch } from './binary-search/binary-search';
import { TwoSum } from './two-sum/two-sum';
import { ValidParentheses } from './valid-parentheses/valid-parentheses';
import { TopKFrequency } from './top-k-frequency/top-k-frequency';
import { SlidingWindow } from './sliding-window/sliding-window';
import { Analytics } from './analytics/analytics';
import { History } from './history/history';

export const routes: Routes = [
  { path: '', component: Home },
  { path: 'buy-stocks', component: BuyStocks },
  { path: 'binary-search', component: BinarySearch },
  { path: 'two-sum', component: TwoSum },
  { path: 'valid-parentheses', component: ValidParentheses },
  { path: 'top-k-frequency', component: TopKFrequency },
  { path: 'sliding-window', component: SlidingWindow },
  { path: 'analytics', component: Analytics },
  { path: 'history', component: History }
];


