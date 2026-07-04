import { Component } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  title = 'Leet-Trainer Home Page';
  welcomeMessage = 'Select the algorithm you wish to test.';
  currentAlgorithmCount = 5;

  constructor(private router: Router) {}

  algorithms = [
   {
    name: "Two Sum",
    difficulty: "Easy",
    description: "Return the indices of the two numbers that add up to a specific target"
   },
   {
    name: "Binary Search",
    difficulty: "Easy",
    description: "Locate a target inside a sorted array"
   },
   {
    name: "Buy Stocks",
    difficulty: "Medium",
    description: "Determine the maximum profit from buying and selling a stock"
   },
   {
    name: "Top K Frequency",
    difficulty: "Medium",
    description: "Return the k most frequent elements in an array"
   },
   {
    name: "Valid Parentheses",
    difficulty: "Easy",
    description: "Check if the input string has valid parentheses"
   },
  ];

  selectedAlgorithm: any = null;

  runAlgorithm(algo: any){
    this.selectedAlgorithm = algo;
    const routeMap: any = {
      "Two Sum": 'two-sum',
      "Binary Search": 'binary-search',
      "Buy Stocks": 'buy-stocks',
      "Top K Frequency": 'top-k-frequency',
      "Valid Parentheses": 'valid-parentheses'
    };

    const route = routeMap[algo.name];
    if (route) {
      this.router.navigate([route]);
    }
  }
}