import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin term - global minimum at origin
        quadratic = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal perturbations with multiple frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            # Multi-frequency sinusoidal components
            freq1 = 2 * np.pi * x_normalized[i]
            freq2 = 4 * np.pi * x_normalized[i]
            freq3 = 6 * np.pi * x_normalized[i]
            sinusoidal += np.exp(-0.3 * np.sum(x_normalized**2)) * (np.sin(freq1) + 0.5 * np.sin(freq2) + 0.3 * np.sin(freq3))
        
        # Modified repulsion term with sharper gradient
        repulsion = 0.0
        distance_from_origin = np.sqrt(np.sum(x_normalized**2))
        if distance_from_origin > 0:
            repulsion = 1.5 * np.exp(-distance_from_origin**2 / 0.3) * (1 + 0.5 * np.sin(5 * distance_from_origin))
        
        # Additional harmonic polynomial terms for increased complexity
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += 0.15 * x_normalized[i]**6 + 0.1 * x_normalized[i]**5
        
        # Cross-term interactions to increase dimensionality challenge
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.05 * np.sin(2 * np.pi * x_normalized[i]) * np.cos(2 * np.pi * x_normalized[j])
        
        return quadratic + sinusoidal + repulsion + harmonic + cross_term