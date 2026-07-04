import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SlidingWindow } from './sliding-window';

describe('SlidingWindow', () => {
  let component: SlidingWindow;
  let fixture: ComponentFixture<SlidingWindow>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SlidingWindow],
    }).compileComponents();

    fixture = TestBed.createComponent(SlidingWindow);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
