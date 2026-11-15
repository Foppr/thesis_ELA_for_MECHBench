import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Fractal-like polynomial with varying degrees
        fractal_poly = 0.0
        for i in range(self.dim):
            degree = 3 + (i % 5)  # Varying polynomial degrees
            fractal_poly += 0.5 * (x_norm[i]**degree) * np.sin(10 * x_norm[i])
            
        # Trigonometric coupling with scale-invariant frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)  # Increasing frequency scale
            trig_coupling += 0.3 * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
            
        # Cross-dimensional interaction with fractal scaling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-invariant interaction with fractal-like decay
                scale_factor = 1.0 / (1.0 + (i + j) * 0.1)
                cross_interaction += scale_factor * np.sin(20 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(15 * np.pi * (x_norm[i] - x_norm[j]))
                
        # Multi-scale chaotic component
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.4 * np.sin(60 * x_norm[i]) * np.cos(50 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
            
        # Self-similar penalty term with multiple scales
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.25 * (x_norm[i]**8 - 4 * x_norm[i]**6 + 6 * x_norm[i]**4 - 4 * x_norm[i]**2 + 1)
            
        # Scale-invariant repulsion term
        repulsion = 0.0
        dist = np.sqrt(np.sum(x_norm**2))
        repulsion = 2.0 * np.exp(-0.5 * dist**2) * np.sin(25 * dist)
        
        # Multi-scale sinusoidal modulation
        modulation = 0.0
        for i in range(self.dim):
            modulation += 0.15 * np.sin(50 * np.pi * x_norm[i]) * np.cos(40 * np.pi * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
            
        # Asymmetric cubic interaction
        asymmetric = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asymmetric += 0.2 * (x_norm[i]**3 + x_norm[j]**3) * np.sin(10 * np.pi * (x_norm[i] - x_norm[j]))
                
        # Final combined function
        return quadratic + fractal_poly + trig_coupling + cross_interaction + chaotic + penalty + repulsion + modulation + asymmetric