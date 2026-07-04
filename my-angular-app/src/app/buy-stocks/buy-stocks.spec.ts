import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BuyStocks } from './buy-stocks';

describe('BuyStocks', () => {
  let component: BuyStocks;
  let fixture: ComponentFixture<BuyStocks>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BuyStocks],
    }).compileComponents();

    fixture = TestBed.createComponent(BuyStocks);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
