import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-binary-search',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './binary-search.html',
  styleUrls: ['./binary-search.scss'],
})
export class BinarySearch {
  numbers = '';
  target = '';
  result = '';

  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef
  ) {}

  runBinarySearch(numbersInput: string, targetInput: string) {
    const array = numbersInput.split(',');
    const parsedArray = array.map(Number);
    const parsedTarget = Number(targetInput);

    this.http
      .post<{ result: number }>('https://leet-trainer.onrender.com/api/binary-search', {
        numbers: parsedArray,
        target: parsedTarget,
      })
      .subscribe({
        next: response => {
          this.result =
            response.result === -1
              ? 'Target not found in the array.'
              : `Target found at index: ${response.result}`;
          this.cdr.detectChanges();
        },
        error: err => {
          this.result = 'Request failed';
          this.cdr.detectChanges();
        },
      });
  }
}
