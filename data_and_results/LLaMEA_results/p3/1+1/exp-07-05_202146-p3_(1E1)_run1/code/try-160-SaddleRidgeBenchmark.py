import numpy as np

class SaddleRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for varying curvature and ridge structures
        self.curvature_coeffs = np.random.uniform(0.5, 2.0, dim)
        self.ridge_coeffs = np.random.uniform(0.1, 0.5, dim)
        self.saddle_coeffs = np.random.uniform(0.3, 1.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with varying curvature
        result = np.sum(self.curvature_coeffs * x**2)
        
        # Add ridge-like structures with varying heights
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += self.ridge_coeffs[i] * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        result += ridge_term
        
        # Introduce saddle point regions with hyperbolic tangent interactions
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle_term += self.saddle_coeffs[i] * np.tanh(x[i]) * np.tanh(x[j])
        result += saddle_term
        
        # Add multi-scale oscillatory components with varying frequencies
        oscillatory_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.5)
            oscillatory_term += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        result += 0.5 * oscillatory_term
        
        # Incorporate cross-dimensional coupling with varying strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.1 + 0.3 * np.sin(i * 0.2 + j * 0.3)
                coupling_term += strength * x[i] * x[j] * np.exp(-0.1 * (x[i] - x[j])**2)
        result += coupling_term
        
        # Add a complex multi-modal structure with asymmetric peaks
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += 0.3 * np.sin(4.0 * x[i])**2 * np.cos(2.0 * x[i])
        result += modal_term
        
        # Introduce a global minimum attractor with basin boundary complexity
        global_min = np.sum((x - 0.5)**2)
        result += 0.2 * global_min * np.exp(-0.05 * global_min)
        
        # Add noise with varying amplitude and frequency
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.02 * i)
        result += noise
        
        # Include a memory-like effect through a weighted sum of previous coordinates
        if hasattr(self, 'prev_x'):
            memory_term = 0.0
            for i in range(self.dim):
                memory_term += 0.03 * self.prev_x[i] * np.sin(x[i] * 0.7)
            result += memory_term
        self.prev_x = x.copy()
        
        return result