import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.c1 = 1.2
        self.c2 = 4.5
        self.c3 = 0.25
        self.lambda_ = 3.99
        self.beta = 3.0
        self.fractal_amp = 0.4
        self.fractal_freq = 1.1
        self.gamma = 0.8
        self.delta = 1.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with fractal noise and higher dimension coupling
        chaotic = 0.0
        for i in range(self.dim):
            xi = x[i]
            for _ in range(7):
                xi = self.lambda_ * xi * (1 - xi)
            chaotic += xi**2 + self.fractal_amp * np.sin(self.fractal_freq * xi) + 0.05 * np.cos(2 * self.fractal_freq * xi)
            
        # Multi-frequency gradient terms with dynamic scaling and cross-dimensional modulation
        gradient = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            amps = [1.0, 0.7, 0.4, 0.2, 0.1]
            for f, a in zip(freqs, amps):
                gradient += a * np.sin(f * x[i]) * np.cos(f * x[i])
                
        # Enhanced saddle point structure with multiple curvature types and non-linear interactions
        saddle = 0.0
        for i in range(self.dim):
            saddle += self.c1 * x[i]**3 + self.c2 * x[i]**4 + 0.15 * x[i]**5 + 0.05 * np.sin(3 * x[i])
            
        # Advanced cross-dimensional coupling with chaotic modulation and higher-order interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                diff = x[i] - x[j]
                coupling += np.sin(diff) * np.cos(diff) * (1.0 + self.c3 * np.sin(x[i] + x[j])) * np.exp(-abs(diff)) + 0.1 * np.sin(2 * diff)
                
        # Dynamic scaling with fractal modulation and additional non-linear terms
        norm_x = np.linalg.norm(x)
        scale_factor = 1.0 + self.beta * np.exp(-norm_x**2 / (2.0 * self.dim)) + 0.05 * np.sin(self.fractal_freq * norm_x) + 0.03 * np.cos(2 * self.fractal_freq * norm_x)
        
        # Combine components with enhanced chaotic offset and non-linear transformation
        result = scale_factor * (chaotic + gradient + saddle + coupling)
        
        # Additional conditioning terms with increased complexity
        cubic_terms = np.sum(x**3) + 0.1 * np.sum(np.sin(x))
        quartic_terms = np.sum(x**4) + 0.05 * np.sum(np.cos(x))
        
        # Add fractal noise to the final result with enhanced variance
        fractal_noise = self.fractal_amp * np.sum(np.sin(self.fractal_freq * x)) + 0.1 * np.sum(np.cos(2 * self.fractal_freq * x))
        
        # Apply non-linear transformation for more complex landscape
        final_result = result + 0.1 * cubic_terms + 0.05 * quartic_terms + fractal_noise + np.random.normal(0, 0.03)
        
        # Introduce additional chaotic modulation based on gamma and delta parameters
        chaos_mod = self.gamma * np.sin(self.delta * norm_x) * np.cos(self.delta * np.mean(x))
        final_result += chaos_mod
        
        return final_result