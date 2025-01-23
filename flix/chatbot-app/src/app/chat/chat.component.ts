import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatService } from '../services/chat.service';

interface MovieRecommendation {
  movie: string;
  description: string;
}

interface ChatMessage {
  text: string;
  isUser: boolean;
  recommendations?: MovieRecommendation[];
}

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class ChatComponent {
  messages: ChatMessage[] = [];
  newMessage: string = '';

  constructor(private chatService: ChatService) {}

  sendMessage() {
    if (this.newMessage.trim() === '') return;
    
    this.messages.push({text: this.newMessage, isUser: true});
    
    this.chatService.sendMessage(this.newMessage).subscribe(response => {
      this.messages.push({
        text: 'Here are some movie recommendations for you:',
        isUser: false,
        recommendations: response.recommendations
      });
    });

    this.newMessage = '';
  }
}
