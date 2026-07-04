import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-top-k-frequency',
  imports: [CommonModule, FormsModule],
  templateUrl: './top-k-frequency.html',
  styleUrl: './top-k-frequency.scss',
})
export class TopKFrequency {
  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef
  ) {}

  nums = "";
  k = "";
  result = "";

  runTopKFrequency(numsInput: string, kInput: string) {
    const array = numsInput.split(",");
    const parsedArray = array.map(Number);

    const parsedK = Number(kInput);

    this.http.post<any>(
      "http://127.0.0.1:5000/api/top-k-frequency",
      {
        numbers: parsedArray,
        k: parsedK
      }
    ).subscribe({
      next: response => {
        this.result = JSON.stringify(response.result);
        this.cdr.detectChanges();
      },
      error: err => {
        console.error('top k frequency request failed', err);
        this.result = 'Request failed';
        this.cdr.detectChanges();
      }
    });
  }
}
