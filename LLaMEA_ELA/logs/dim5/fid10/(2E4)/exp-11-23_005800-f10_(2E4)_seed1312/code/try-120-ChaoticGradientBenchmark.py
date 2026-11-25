import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 0.8  # Stronger cubic coefficient for enhanced saddle points
        self.c2 = 3.5  # Increased quartic coefficient for greater curvature complexity
        self.c3 = 0.7  # Higher coupling modulation strength for stronger interactions
        self.lambda_ = 4.0  # Increased chaotic map parameter for more instability
        self.beta = 3.2  # Stronger exponential scaling factor
        self.gamma = 0.9  # Increased polynomial scaling factor
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Intensified chaotic component with multiple logistic maps and complex modulation
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            for _ in range(6):
                xi = self.lambda_ * xi * (1 - xi)
            chaotic += xi**3 * np.sin(xi) + 0.5 * xi**2 * np.cos(xi)
            
        # Enhanced gradient terms with multi-scale harmonic and fractal structure
        gradient = 0.0
        for i in range(self.dim):
            freqs = [1.0, 3.0, 6.0, 8.0]
            amps = [1.5, 0.8, 0.4, 0.2]
            for f, a in zip(freqs, amps):
                gradient += a * np.sin(f * x[i]) * np.cos(f * x[i] + np.pi/6)
                
        # Intensified saddle point structure with multi-scale asymmetry
        saddle = 0.0
        for i in range(self.dim):
            # Multi-scale asymmetric terms to create extreme landscape complexity
            if x[i] >= 0:
                saddle += self.c1 * x[i]**3 + self.c2 * x[i]**4 + 0.5 * x[i]**5
            else:
                saddle += self.c1 * x[i]**3 - self.c2 * x[i]**4 - 0.3 * x[i]**5
                
        # Enhanced cross-dimensional coupling with fractal-like interaction and dynamic scaling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                diff = x[i] - x[j]
                coupling += (np.sin(diff) * np.cos(diff) + 
                           0.7 * np.sin(2*diff) + 
                           0.3 * np.sin(3*diff)) * (1.0 + self.c3 * np.tanh(x[i] + x[j]) + 
                                                   0.5 * np.sin(x[i] * x[j]))
                
        # Adaptive scaling with enhanced exponential and polynomial components
        norm_x = np.linalg.norm(x)
        scale_factor = 1.0 + self.beta * np.exp(-norm_x**2 / (2.0 * self.dim)) + \
                      self.gamma * (norm_x / self.dim)**3 + 0.5 * np.log(1 + norm_x)
        
        # Combine all components with enhanced weighting
        result = scale_factor * (chaotic + gradient + saddle + coupling)
        
        # Add higher-order polynomial terms for improved conditioning
        cubic_terms = np.sum(x**3)
        quartic_terms = np.sum(x**4)
        quintic_terms = np.sum(x**5)
        
        # Return final value with controlled noise and bias adjustment
        return result + 0.2 * cubic_terms + 0.1 * quartic_terms + 0.05 * quintic_terms + np.random.normal(0, 0.01)