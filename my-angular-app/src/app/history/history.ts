import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';
import { HistoryService } from '../history';


@Component({
  selector: 'app-history',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './history.html',
  styleUrls: ['./history.scss'],
})
export class History implements OnInit {
  history$!: Observable<any[]>;

  constructor(private historyService: HistoryService) {}

  ngOnInit(): void {
    this.history$ = this.historyService.getHistory();
  }
}
