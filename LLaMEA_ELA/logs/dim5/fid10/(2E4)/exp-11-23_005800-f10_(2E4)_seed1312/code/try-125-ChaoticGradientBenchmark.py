import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 1.2
        self.c2 = 4.5
        self.c3 = 0.25
        self.lambda_ = 3.99
        self.beta = 3.0
        self.fractal_amp = 0.5
        self.fractal_freq = 1.2
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with fractal noise
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            for _ in range(7):
                xi = self.lambda_ * xi * (1 - xi)
            chaotic += xi**2 + self.fractal_amp * np.sin(self.fractal_freq * xi)
            
        # Multi-frequency gradient terms with dynamic scaling
        gradient = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.5, 3.5, 4.5]
            amps = [1.2, 0.8, 0.5, 0.3]
            for f, a in zip(freqs, amps):
                gradient += a * np.sin(f * x[i]) * np.cos(f * x[i])
                
        # Enhanced saddle point structure with multiple curvature types
        saddle = 0.0
        for i in range(self.dim):
            saddle += self.c1 * x[i]**3 + self.c2 * x[i]**4 + 0.15 * x[i]**5
            
        # Advanced cross-dimensional coupling with chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                diff = x[i] - x[j]
                coupling += np.sin(diff) * np.cos(diff) * (1.0 + self.c3 * np.sin(x[i] + x[j])) * np.exp(-abs(diff))
                
        # Dynamic scaling with fractal modulation
        norm_x = np.linalg.norm(x)
        scale_factor = 1.0 + self.beta * np.exp(-norm_x**2 / (2.0 * self.dim)) + 0.1 * np.sin(self.fractal_freq * norm_x)
        
        # Combine components with enhanced chaotic offset
        result = scale_factor * (chaotic + gradient + saddle + coupling)
        
        # Additional conditioning terms
        cubic_terms = np.sum(x**3)
        quartic_terms = np.sum(x**4)
        
        # Add fractal noise to the final result
        fractal_noise = self.fractal_amp * np.sum(np.sin(self.fractal_freq * x))
        
        return result + 0.15 * cubic_terms + 0.1 * quartic_terms + fractal_noise + np.random.normal(0, 0.03)