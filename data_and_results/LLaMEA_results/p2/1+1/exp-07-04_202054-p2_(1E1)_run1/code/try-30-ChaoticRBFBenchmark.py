import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for added complexity
        self.chaos_seq = np.array([np.sin(2 * np.pi * (i * 3.569946 - np.floor(i * 3.569946))) for i in range(dim * 2)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize with quadratic base
        f_value = np.sum(x**2)
        
        # Add chaotic radial basis function components
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(min(5, self.dim)):
                center = 5.0 * np.sin(self.chaos_seq[i + j])
                rbf_sum += np.exp(-0.5 * ((x[i] - center) / (0.5 + 0.5 * np.abs(x[i])))**2)
            f_value += 0.7 * rbf_sum
            
        # Asymmetric sine-wave modulation with varying frequencies
        for i in range(self.dim):
            f_value += 0.6 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i]**2) * np.abs(x[i])
            
        # Logistic map based perturbations
        for i in range(self.dim):
            logistic_val = 4.0 * x[i] * (1.0 - x[i])
            f_value += 0.3 * np.sin(logistic_val * 10) * np.cos(logistic_val * 7)
            
        # Multi-scale radial components with dynamic centers
        for i in range(self.dim):
            f_value += 0.5 * np.sum(np.exp(-0.1 * (x[i] - self.chaos_seq[i::2])**2))
            
        # Cross-dimensional asymmetric sine interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                f_value += 0.4 * np.sin(5 * x[i]) * np.cos(8 * x[j]) * np.sin(3 * x[i] + 2 * x[j]) * np.abs(x[i] - x[j])
                
        # Polynomial chaos with sine modulation
        for i in range(self.dim):
            f_value += 0.2 * x[i]**9 * np.sin(2 * x[i])
            
        # Irregular high-frequency noise component
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.15 * np.sum(noise * np.sin(20 * x))
        
        # Add a global sine modulation to increase landscape complexity
        f_value += 0.3 * np.sin(0.5 * np.sum(x))
        
        # Add a small amount of irregular bumps
        for i in range(self.dim):
            f_value += 0.1 * np.sin(100 * x[i]) * np.cos(50 * x[i])
            
        return f_value