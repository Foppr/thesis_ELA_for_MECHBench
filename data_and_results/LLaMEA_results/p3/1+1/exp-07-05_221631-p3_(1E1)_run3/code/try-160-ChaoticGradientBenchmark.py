import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.5, 2.0, dim)
        self.attractor_centers = np.random.uniform(-3.0, 3.0, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
        # Saddle point configuration
        self.saddle_points = np.random.uniform(-4.0, 4.0, (5, dim))
        self.saddle_weights = np.random.uniform(0.1, 0.5, 5)
        # Periodic modulation
        self.period = np.random.uniform(1.0, 3.0, dim)
        # Noise scaling
        self.noise_level = 0.05
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        f_val = 0.0
        
        # Attractor basin contribution
        for i in range(10):
            dist = np.sum((x - self.attractor_centers[i])**2)
            f_val += self.weights[i] * np.exp(-dist / (2.0 * self.chaos_params[0]**2))
            
        # Saddle point contribution
        for i in range(5):
            dist = np.sum((x - self.saddle_points[i])**2)
            f_val -= self.saddle_weights[i] * np.exp(-dist / (2.0 * self.chaos_params[1]**2))
            
        # Chaotic gradient term
        grad_term = 0.0
        for i in range(self.dim):
            # Periodic chaotic modulation
            mod = np.sin(2.0 * np.pi * x[i] / self.period[i])
            grad_term += mod * x[i]**3
            
        f_val += 0.5 * grad_term
        
        # Cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(self.chaos_params[i] * x[i] + self.chaos_params[j] * x[j])
                f_val += 0.1 * x[i] * x[j] * coupling
                
        # Add noise
        noise = np.random.normal(0, self.noise_level, self.dim)
        f_val += np.sum(noise * x)
        
        # Ensure positive fitness
        f_val = max(0.01, f_val)
        
        return f_val