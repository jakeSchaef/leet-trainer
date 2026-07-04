import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwoSum } from './two-sum';

describe('TwoSum', () => {
  let component: TwoSum;
  let fixture: ComponentFixture<TwoSum>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TwoSum],
    }).compileComponents();

    fixture = TestBed.createComponent(TwoSum);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
