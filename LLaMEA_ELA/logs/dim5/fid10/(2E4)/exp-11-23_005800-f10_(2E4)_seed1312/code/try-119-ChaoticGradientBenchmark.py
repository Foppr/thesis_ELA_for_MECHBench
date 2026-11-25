import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 0.5  # Increased cubic coefficient for stronger saddle points
        self.c2 = 2.3  # Increased quartic coefficient for more complex curvature
        self.c3 = 0.4  # Increased coupling modulation strength
        self.lambda_ = 3.98  # Slight increase in chaotic map parameter
        self.beta = 2.7  # Increased exponential scaling factor
        self.gamma = 0.7  # Increased polynomial scaling factor
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with logistic map and sinusoidal modulation
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            for _ in range(5):
                xi = self.lambda_ * xi * (1 - xi)
            chaotic += xi**2 * np.sin(xi)
            
        # Modified gradient terms with multi-scale harmonic structure
        gradient = 0.0
        for i in range(self.dim):
            freqs = [1.0, 3.0, 5.0]
            amps = [1.0, 0.7, 0.2]
            for f, a in zip(freqs, amps):
                gradient += a * np.sin(f * x[i]) * np.cos(f * x[i] + np.pi/6)
                
        # Enhanced saddle point structure with asymmetric curvature
        saddle = 0.0
        for i in range(self.dim):
            # Asymmetric cubic and quartic terms to create complex landscape
            if x[i] >= 0:
                saddle += self.c1 * x[i]**3 + self.c2 * x[i]**4
            else:
                saddle += self.c1 * x[i]**3 - self.c2 * x[i]**4
                
        # Improved cross-dimensional coupling with fractal-like interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                diff = x[i] - x[j]
                coupling += (np.sin(diff) * np.cos(diff) + 
                           0.6 * np.sin(2*diff)) * (1.0 + self.c3 * np.tanh(x[i] + x[j]))
                
        # Adaptive scaling with exponential and polynomial components
        norm_x = np.linalg.norm(x)
        scale_factor = 1.0 + self.beta * np.exp(-norm_x**2 / (2.0 * self.dim)) + \
                      self.gamma * (norm_x / self.dim)**2
        
        # Combine all components with enhanced weighting
        result = scale_factor * (chaotic + gradient + saddle + coupling)
        
        # Add higher-order polynomial terms for improved conditioning
        cubic_terms = np.sum(x**3)
        quartic_terms = np.sum(x**4)
        
        # Return final value with controlled noise and bias adjustment
        return result + 0.2 * cubic_terms + 0.08 * quartic_terms + np.random.normal(0, 0.003)