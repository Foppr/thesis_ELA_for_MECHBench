import numpy as np

class MultimodalFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive conditioning
        quadratic = 0.1 * np.sum(x**2)
        
        # Nested sinusoidal oscillations with varying frequencies and amplitudes
        oscillation = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * x[i])
            oscillation += np.sin(freq * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
            # Higher-order harmonic with frequency modulation
            oscillation += 0.5 * np.sin(3.0 * freq * x[i] + 0.5 * np.sin(2.0 * x[i])) * \
                          np.cos(2.0 * x[i] + 0.3 * np.cos(1.5 * x[i]))
            
            # Fractal-like interaction with recursive modulation
            oscillation += 0.3 * np.sin(5.0 * freq * x[i] + 0.2 * np.sin(3.0 * x[i]) + 
                                       0.1 * np.sin(4.0 * x[i]**2)) * \
                          np.cos(4.0 * x[i] + 0.4 * np.cos(2.5 * x[i]) + 
                                0.2 * np.cos(3.0 * x[i]**2))
        
        # Cross-dimensional coupling with fractal scaling
        coupling = 0
        for i in range(self.dim-1):
            coupling += 0.2 * np.sin(x[i] * x[i+1]) * np.cos(0.5 * (x[i] + x[i+1])) * \
                       np.exp(-0.05 * np.abs(x[i] - x[i+1]))
            
            # Multi-scale interaction with adaptive weights
            coupling += 0.1 * np.sin(2.0 * x[i] * x[i+1] + 0.3 * np.sin(x[i])) * \
                       np.cos(1.5 * x[i] + 0.4 * np.cos(x[i+1]))
        
        # Fractal basin term with gradient-based conditioning
        basin = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(8.0 * x) * (1.0 + 0.2 * np.abs(x)))
        
        # Adaptive penalty term with chaotic modulation
        penalty = 0.03 * np.sum(np.abs(np.sin(15.0 * x) + 0.3 * np.sin(30.0 * x)) * 
                               (1.0 + 0.1 * np.abs(x)))
        
        # Higher-order polynomial with fractal-like behavior
        high_order = 0.02 * np.sum(x**4) + 0.015 * np.sum(np.abs(x)**3)
        
        # Gradient complexity term with nested modulation
        gradient_complexity = 0.01 * np.sum(np.sin(20.0 * x) * np.cos(18.0 * x) * 
                                           (1.0 + 0.15 * np.abs(x)**2))
        
        return quadratic + oscillation + coupling + basin + penalty + high_order + gradient_complexity