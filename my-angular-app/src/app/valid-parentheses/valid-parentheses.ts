import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-valid-parentheses',
  imports: [CommonModule, FormsModule],
  templateUrl: './valid-parentheses.html',
  styleUrl: './valid-parentheses.scss',
})
export class ValidParentheses {
  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef
  ) {}

  input = "";
  result = "";

  runValidParentheses(inputString: string) {
    this.http.post<any>(
      "http://127.0.0.1:5000/api/valid-parentheses",
      {
        string: inputString
      }
    ).subscribe({
      next: response => {
        this.result = response.result ? "Valid" : "Invalid";
        this.cdr.detectChanges();
      },
      error: err => {
        console.error('valid parentheses request failed', err);
        this.result = 'Request failed';
        this.cdr.detectChanges();
      }
    });
  }
}
