import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ValidParentheses } from './valid-parentheses';

describe('ValidParentheses', () => {
  let component: ValidParentheses;
  let fixture: ComponentFixture<ValidParentheses>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ValidParentheses],
    }).compileComponents();

    fixture = TestBed.createComponent(ValidParentheses);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
