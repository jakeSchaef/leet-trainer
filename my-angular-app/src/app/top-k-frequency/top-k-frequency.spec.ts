import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TopKFrequency } from './top-k-frequency';

describe('TopKFrequency', () => {
  let component: TopKFrequency;
  let fixture: ComponentFixture<TopKFrequency>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TopKFrequency],
    }).compileComponents();

    fixture = TestBed.createComponent(TopKFrequency);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
