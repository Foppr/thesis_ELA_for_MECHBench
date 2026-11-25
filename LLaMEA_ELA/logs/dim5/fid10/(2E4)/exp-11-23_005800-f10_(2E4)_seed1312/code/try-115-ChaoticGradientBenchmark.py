import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 0.9
        self.c2 = 3.5
        self.c3 = 0.2
        self.lambda_ = 3.98
        self.beta = 2.5
        self.fractal_amp = 0.4
        self.fractal_freq = 0.8
        self.nonlinear_factor = 1.2
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with fractal noise and non-linear transformations
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            for _ in range(7):
                xi = self.lambda_ * xi * (1 - xi)
            chaotic += xi**2 + self.fractal_amp * np.sin(self.fractal_freq * xi) + self.nonlinear_factor * np.tanh(xi)
            
        # Multi-frequency gradient terms with dynamic scaling and cross-dimensional modulation
        gradient = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            amps = [1.0, 0.7, 0.4, 0.2, 0.1]
            for f, a in zip(freqs, amps):
                gradient += a * np.sin(f * x[i]) * np.cos(f * x[i]) * (1.0 + 0.1 * np.sin(f * x[i]))
                
        # Enhanced saddle point structure with multiple curvature types and non-linear coupling
        saddle = 0.0
        for i in range(self.dim):
            saddle += self.c1 * x[i]**3 + self.c2 * x[i]**4 + 0.15 * x[i]**5 + 0.05 * np.sin(x[i]**2)
            
        # Advanced cross-dimensional coupling with chaotic modulation and higher-order interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                diff = x[i] - x[j]
                coupling += np.sin(diff) * np.cos(diff) * (1.0 + self.c3 * np.sin(x[i] + x[j])) * np.exp(-abs(diff)) * np.log(1 + abs(diff))
                
        # Dynamic scaling with fractal modulation and additional non-linear factors
        norm_x = np.linalg.norm(x)
        scale_factor = 1.0 + self.beta * np.exp(-norm_x**2 / (2.0 * self.dim)) + 0.05 * np.sin(self.fractal_freq * norm_x) + 0.02 * np.cos(norm_x)
        
        # Combine components with enhanced chaotic offset and non-linear transformations
        result = scale_factor * (chaotic + gradient + saddle + coupling)
        
        # Additional conditioning terms with higher-order polynomials
        cubic_terms = np.sum(x**3)
        quartic_terms = np.sum(x**4)
        quintic_terms = np.sum(x**5)
        
        # Add fractal noise to the final result and include non-linear scaling
        fractal_noise = self.fractal_amp * np.sum(np.sin(self.fractal_freq * x)) + 0.03 * np.sum(np.cos(self.fractal_freq * x**2))
        
        return result + 0.15 * cubic_terms + 0.08 * quartic_terms + 0.03 * quintic_terms + fractal_noise + np.random.normal(0, 0.03)