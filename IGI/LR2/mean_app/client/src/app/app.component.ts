import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UsersComponent } from './components/users/users.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, UsersComponent],
  template: `
    <div class="app-container">
      <nav class="navbar">
        <div class="nav-content">
          <h1>👥 MEAN Stack - User Management</h1>
        </div>
      </nav>
      <main class="main-content">
        <app-users></app-users>
      </main>
    </div>
  `,
  styles: [`
    .app-container {
      min-height: 100vh;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .navbar {
      background-color: rgba(0, 0, 0, 0.3);
      padding: 20px;
      color: white;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }

    .nav-content h1 {
      margin: 0;
      font-size: 24px;
      text-align: center;
    }

    .main-content {
      padding: 30px 20px;
      max-width: 1200px;
      margin: 0 auto;
    }
  `]
})
export class AppComponent {
  title = 'MEAN Stack App';
}
