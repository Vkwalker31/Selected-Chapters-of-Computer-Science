import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UserService } from '../../services/user.service';

interface User {
  _id?: string;
  name: string;
  email: string;
  createdAt?: string;
}

@Component({
  selector: 'app-users',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
  users: User[] = [];
  newUser: User = { name: '', email: '' };
  editingId: string | null = null;
  editingUser: User | null = null;
  errorMessage = '';
  successMessage = '';

  constructor(private userService: UserService) {}

  ngOnInit() {
    this.loadUsers();
  }

  loadUsers() {
    this.userService.getUsers().subscribe(
      (response: any) => {
        this.users = response.data;
        this.errorMessage = '';
      },
      (error) => {
        this.errorMessage = 'Failed to load users';
        console.error(error);
      }
    );
  }

  createUser() {
    if (!this.newUser.name || !this.newUser.email) {
      this.errorMessage = 'Name and email are required';
      return;
    }

    this.userService.createUser(this.newUser).subscribe(
      (response: any) => {
        this.users.push(response.data);
        this.newUser = { name: '', email: '' };
        this.successMessage = 'User created successfully!';
        setTimeout(() => this.successMessage = '', 3000);
      },
      (error) => {
        this.errorMessage = 'Failed to create user';
        console.error(error);
      }
    );
  }

  startEdit(user: User) {
    this.editingId = user._id || null;
    this.editingUser = { ...user };
  }

  cancelEdit() {
    this.editingId = null;
    this.editingUser = null;
  }

  updateUser() {
    if (!this.editingId || !this.editingUser) return;
    if (!this.editingUser.name || !this.editingUser.email) {
      this.errorMessage = 'Name and email are required';
      return;
    }

    this.userService.updateUser(this.editingId, this.editingUser).subscribe(
      (response: any) => {
        const index = this.users.findIndex(u => u._id === this.editingId);
        if (index !== -1) {
          this.users[index] = response.data;
        }
        this.editingId = null;
        this.editingUser = null;
        this.successMessage = 'User updated successfully!';
        setTimeout(() => this.successMessage = '', 3000);
      },
      (error) => {
        this.errorMessage = 'Failed to update user';
        console.error(error);
      }
    );
  }

  deleteUser(id: string | undefined) {
    if (!id || !confirm('Are you sure?')) return;

    this.userService.deleteUser(id).subscribe(
      () => {
        this.users = this.users.filter(u => u._id !== id);
        this.successMessage = 'User deleted successfully!';
        setTimeout(() => this.successMessage = '', 3000);
      },
      (error) => {
        this.errorMessage = 'Failed to delete user';
        console.error(error);
      }
    );
  }
}
