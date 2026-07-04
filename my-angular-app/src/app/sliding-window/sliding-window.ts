import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-sliding-window',
  imports: [CommonModule, FormsModule],
  templateUrl: './sliding-window.html',
  styleUrl: './sliding-window.scss',
})
export class SlidingWindow {
  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef
  ) {}

  input = "";
  result = "";

  runSlidingWindow(inputString: string) {
    this.http.post<any>(
      "http://127.0.0.1:5000/api/sliding-window",
      {
        string: inputString
      }
    ).subscribe({
      next: response => {
        this.result = response.result;
        this.cdr.detectChanges();
      },
      error: err => {
        console.error('sliding window request failed', err);
        this.result = 'Request failed';
        this.cdr.detectChanges();
      }
    });
  }
}
