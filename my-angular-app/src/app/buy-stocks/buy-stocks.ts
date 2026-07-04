import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-buy-stocks',
  imports: [CommonModule, FormsModule],
  templateUrl: './buy-stocks.html',
  styleUrl: './buy-stocks.scss',
})


export class BuyStocks {
  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef
  ) {}

  prices = "";
  result = "";

  runBuyStocks(pricesInput: string) {
    const array = pricesInput.split(",");
    const parsedArray = array.map(Number);

    this.http.post<any>(
      "http://127.0.0.1:5000/api/buy-stocks",
      {
        prices: parsedArray,
      }
    ).subscribe({
      next: response => {
        if (response.result === -1) {
          this.result = "No profit can be made.";
        } else {
          this.result = `Maximum profit: ${response.result}`;
        }
        this.cdr.detectChanges();
      },
      error: err => {
        console.error('buy stocks request failed', err);
        this.result = 'Request failed';
        this.cdr.detectChanges();
      }
    });
  }
}
