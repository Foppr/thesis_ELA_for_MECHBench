import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic modulation
        rbf = 0
        for i in range(self.dim):
            # Chaotic sinusoidal modulation with radial basis
            rbf += np.exp(-np.sum((x - 3 * np.sin(0.5 * x))**2) / (2 * self.dim))
        
        # Sinusoidal multimodal component with dynamic frequency and polynomial coupling
        sin_mod = 0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(x[i] * 0.7)
            sin_mod += np.sin(freq * x[i])**2 + 0.5 * np.cos(4 * x[i]) * np.sin(2 * x[i])
        
        # Enhanced cross-dimensional interaction with polynomial coupling
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Polynomial decaying interaction based on distance and dimension
                dist = np.abs(x[i] - x[j])
                cross_interaction += (dist**2 + 0.5 * dist) * (x[i]**3 + x[j]**3)
        
        # Adaptive difficulty scaling with chaotic modulation
        scale_factor = 1.0 + 0.5 * np.sin(self.dim * 0.3 + np.sum(x) * 0.1)
        
        # Add higher-order polynomial terms for increased complexity
        poly_terms = np.sum(x**4) + 0.5 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        # Combine all components with dynamic weighting
        return scale_factor * (0.8 * rbf + 1.5 * sin_mod + 0.7 * cross_interaction + 0.3 * poly_terms)