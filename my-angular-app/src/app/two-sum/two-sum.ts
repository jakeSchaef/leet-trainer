import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-two-sum',
  imports: [CommonModule, FormsModule],
  templateUrl: './two-sum.html',
  styleUrl: './two-sum.scss',
})
export class TwoSum {
  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef
  ) {}

  nums = "";
  target = "";
  result = "";

  runTwoSum(numsInput: string, targetInput: string) {
    const array = numsInput.split(",");
    const parsedArray = array.map(Number);

    const parsedTarget = Number(targetInput);

    this.http.post<any>(
      "http://127.0.0.1:5000/api/two-sum",
      {
        nums: parsedArray,
        target: parsedTarget
      }
    ).subscribe({
      next: response => {
        this.result = JSON.stringify(response.result);
        this.cdr.detectChanges();
      },
      error: err => {
        console.error('two sum request failed', err);
        this.result = 'Request failed';
        this.cdr.detectChanges();
      }
    });
  }
}
