import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 0.5
        self.c2 = 2.5
        self.c3 = 0.3
        self.lambda_ = 4.0
        self.beta = 3.0
        self.gamma = 0.7
        self.fractal_amp = 1.5
        self.saddle_strength = 2.0
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with logistic map and sinusoidal modulation
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            for _ in range(6):
                xi = self.lambda_ * xi * (1 - xi)
            chaotic += xi**2 * np.sin(xi) + 0.3 * np.sin(5*xi)
            
        # Modified gradient terms with multi-scale harmonic structure
        gradient = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.5, 4.0, 6.0]
            amps = [1.5, 0.8, 0.4, 0.2]
            for f, a in zip(freqs, amps):
                gradient += a * np.sin(f * x[i]) * np.cos(f * x[i] + np.pi/4)
                
        # Enhanced saddle point structure with asymmetric curvature and higher-order terms
        saddle = 0.0
        for i in range(self.dim):
            # Asymmetric cubic and quartic terms to create complex landscape
            if x[i] >= 0:
                saddle += self.c1 * x[i]**3 + self.c2 * x[i]**4 + self.saddle_strength * x[i]**5
            else:
                saddle += self.c1 * x[i]**3 - self.c2 * x[i]**4 - self.saddle_strength * x[i]**5
                
        # Improved cross-dimensional coupling with fractal-like interaction and additional noise
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                diff = x[i] - x[j]
                coupling += (np.sin(diff) * np.cos(diff) + 
                           0.5 * np.sin(2*diff) + 
                           0.3 * np.sin(3*diff)) * (1.0 + self.c3 * np.tanh(x[i] + x[j])) * \
                           (1.0 + self.fractal_amp * np.sin(0.5 * (x[i] + x[j])))
                
        # Adaptive scaling with exponential and polynomial components
        norm_x = np.linalg.norm(x)
        scale_factor = 1.0 + self.beta * np.exp(-norm_x**2 / (2.0 * self.dim)) + \
                      self.gamma * (norm_x / self.dim)**2 + 0.5 * np.sin(norm_x)
        
        # Combine all components with enhanced weighting
        result = scale_factor * (chaotic + gradient + saddle + coupling)
        
        # Add higher-order polynomial terms for improved conditioning
        cubic_terms = np.sum(x**3)
        quartic_terms = np.sum(x**4)
        quintic_terms = np.sum(x**5)
        
        # Return final value with controlled noise and bias adjustment
        return result + 0.2 * cubic_terms + 0.1 * quartic_terms + 0.05 * quintic_terms + \
               np.random.normal(0, 0.01)