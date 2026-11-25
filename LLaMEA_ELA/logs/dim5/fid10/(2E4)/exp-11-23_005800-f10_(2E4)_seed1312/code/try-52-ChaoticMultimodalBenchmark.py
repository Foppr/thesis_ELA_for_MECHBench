import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.9  # Logistic map parameter
        self.alpha = 0.5  # Adaptive conditioning factor
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        chaotic = 0
        for i in range(self.dim):
            # Normalize x[i] to [0, 1] for logistic map
            norm_x = (x[i] + 5.0) / 10.0
            # Apply logistic map iteratively
            xi = norm_x
            for _ in range(10):  # Iterate to stabilize chaotic behavior
                xi = self.r * xi * (1 - xi)
            chaotic += xi
            
        # Complex harmonic interference
        harmonic = 0
        for i in range(self.dim):
            # Multiple sine/cosine waves with varying frequencies and phases
            freqs = [1.0, 2.0, 3.0, 4.0]
            phases = [0.0, np.pi/4, np.pi/2, np.pi]
            for f, p in zip(freqs, phases):
                harmonic += np.sin(f * x[i] + p) * np.cos(f * x[i] / 2.0 + p/2.0)
                
        # Adaptive conditioning based on dimension
        condition = 0
        for i in range(self.dim):
            # Dimension-specific scaling with chaotic influence
            scale_factor = 1.0 + self.alpha * np.sin(i * np.pi / self.dim)
            condition += scale_factor * (x[i]**2) * np.exp(-0.1 * abs(x[i]))
            
        # Cross-dimensional coupling with exponential decay
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                cross += np.exp(-0.5 * (diff**2)) * np.sin(2.0 * diff)
                
        # Non-linear transformation with polynomial and exponential components
        transform = 0
        for i in range(self.dim):
            # Combination of polynomial and exponential terms
            transform += (x[i]**3 + x[i]**2) * np.exp(-0.1 * abs(x[i]))
            
        # Add noise-like perturbation from chaotic system
        noise = 0
        for i in range(self.dim):
            # Use chaotic value as noise amplitude multiplier
            norm_x = (x[i] + 5.0) / 10.0
            xi = norm_x
            for _ in range(5):
                xi = self.r * xi * (1 - xi)
            noise += 0.2 * xi * np.sin(5.0 * x[i])
            
        # Combine all components with appropriate weights
        result = 1.0 * chaotic + 0.8 * harmonic + 0.6 * condition + 0.4 * cross + 0.3 * transform + 0.2 * noise
        
        return result + 5.0 * self.dim  # Add offset to ensure positive fitness