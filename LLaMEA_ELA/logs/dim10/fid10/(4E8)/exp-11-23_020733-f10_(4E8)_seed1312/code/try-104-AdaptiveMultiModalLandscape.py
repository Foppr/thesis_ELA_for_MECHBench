import numpy as np

class AdaptiveMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive centers and weights for radial basis functions
        np.random.seed(42)  # For reproducibility
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.exponential(1.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive centers
        rbf_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            diff = x - center
            distance_sq = np.sum(diff**2)
            rbf_sum += self.weights[i] * np.exp(-distance_sq / (2.0 * (i + 1)**2))
        
        # Asymmetric gradient field component
        grad_field = 0.0
        for i in range(self.dim):
            if x[i] > 0:
                grad_field += 0.5 * x[i]**3
            else:
                grad_field += 0.3 * x[i]**4
                
        # Dynamic conditioning based on dimension
        cond_factor = np.sum(np.abs(x)) / self.dim
        
        # Multi-modal harmonic component
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 * (1.0 + 0.3 * np.sin(i * np.pi / self.dim))
            harmonic += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
            
        # Cross-dimensional coupling with dynamic weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.1 * (i + j + 1) / (self.dim + 1)
                coupling += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Asymmetric penalty for boundary violations
        penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.5:
                penalty += 2.0 * (abs(x[i]) - 4.5)**2
            elif x[i] > 4.5:
                penalty += 1.5 * (x[i] - 4.5)**2
                
        # Combine all components
        result = rbf_sum + grad_field + cond_factor * harmonic + coupling + penalty
        
        return result