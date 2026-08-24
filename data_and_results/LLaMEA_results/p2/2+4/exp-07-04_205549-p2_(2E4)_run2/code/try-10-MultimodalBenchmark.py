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
            # Exponentially decaying amplitude with stronger decay
            amplitude = np.exp(-0.3 * np.sum(x_normalized**2))
            # Multiple sinusoidal components for increased complexity
            sinusoidal += amplitude * (np.sin(2 * np.pi * x_normalized[i]) + 
                                     0.5 * np.sin(5 * np.pi * x_normalized[i]) + 
                                     0.3 * np.sin(8 * np.pi * x_normalized[i]))
        
        # Modified central repulsion term with sharper gradient
        repulsion = 0.0
        distance_from_origin = np.sqrt(np.sum(x_normalized**2))
        if distance_from_origin > 0:
            repulsion = 1.5 * np.exp(-distance_from_origin**2 / 0.3)
        
        # Additional harmonic polynomial terms for increased multimodality
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += 0.1 * (x_normalized[i]**6 + 0.5 * x_normalized[i]**5 + 0.3 * x_normalized[i]**4)
        
        # Cross-term interactions to increase problem difficulty
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.05 * np.sin(np.pi * (x_normalized[i] + x_normalized[j]))
        
        return quadratic + sinusoidal + repulsion + harmonic + cross_terms