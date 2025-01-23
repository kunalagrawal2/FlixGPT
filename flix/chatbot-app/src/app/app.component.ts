import { Component } from '@angular/core';
import { ChatComponent } from './chat/chat.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],  // Change .css to .scss
  standalone: true,
  imports: [ChatComponent]
})
export class AppComponent {
  title = 'chatbot-app';
}
