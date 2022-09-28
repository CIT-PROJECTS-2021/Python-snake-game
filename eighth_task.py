#background render method
def image_display(self):
        bg_img = pygame.image.load(" ")
        self.surface.blit(bg_img, (0,0))

#play_method
def play(self):
        self.image_display()
        self.snake.walk()
        self.food.eat()
        self.display_score()
        pygame.display.flip()

        # snake eating food 
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.food.x, self.food.y):
                self.play_sound(" ")
                self.snake.increase_length()
                self.food.random_shift()

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound(' ')
                raise "Snake collided with self"

        # snake colliding with the boundaries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.play_sound(' ')
            raise "You hit the boundary"
            
            
 
