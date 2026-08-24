import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        self.delayed_feedback = np.random.uniform(-0.3, 0.3, dim)
        self.saddle_points = np.random.uniform(-5.0, 5.0, (10, dim))
        self.time_delay = 3
        self.chaos_parameter = 3.8
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        x_norm = x / 5.0
        
        # Chaotic component with delayed feedback
        chaotic = 0.0
        for i in range(self.dim):
            delayed_idx = (i - self.time_delay) % self.dim
            chaotic += (self.chaos_parameter * x_norm[i] * 
                       (1 - x_norm[i]**2) + 
                       self.delayed_feedback[i] * x_norm[delayed_idx])
        
        # Saddle-point attraction terms
        saddle_sum = 0.0
        for i in range(10):
            diff = x_norm - self.saddle_points[i]
            distance = np.sqrt(np.sum(diff**2))
            # Saddle point with repulsive and attractive components
            saddle_sum += 1.0 / (1.0 + distance**2) * np.sin(distance * 2)
        
        # Coupled oscillatory terms
        oscillatory = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    oscillatory += (self.coupling_weights[i, j] * 
                                  np.sin(x_norm[i] - x_norm[j]) * 
                                  np.cos(x_norm[i] + x_norm[j]))
        
        # Polynomial and interaction terms for complexity
        poly_term = 0.1 * np.sum(x_norm**4)
        interaction_term = 0.05 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Gradient-based landscape with local maxima
        gradient_term = 0.0
        for i in range(self.dim):
            gradient_term += (x_norm[i]**3 - 3 * x_norm[i])**2
        
        # Combine all terms with global minimum at origin
        return chaotic + saddle_sum + oscillatory + poly_term + interaction_term + gradient_term