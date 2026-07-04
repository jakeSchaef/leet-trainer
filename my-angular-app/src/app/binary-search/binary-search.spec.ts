import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BinarySearch } from './binary-search';

describe('BinarySearch', () => {
  let component: BinarySearch;
  let fixture: ComponentFixture<BinarySearch>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BinarySearch],
    }).compileComponents();

    fixture = TestBed.createComponent(BinarySearch);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
