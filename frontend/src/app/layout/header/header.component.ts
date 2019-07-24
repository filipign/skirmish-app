import { Component, OnInit } from '@angular/core';

import { AppService } from '../../service/app.service'

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class AppHeaderComponent implements OnInit {

  constructor(private appService: AppService) { }

  ngOnInit() {
  }

}
