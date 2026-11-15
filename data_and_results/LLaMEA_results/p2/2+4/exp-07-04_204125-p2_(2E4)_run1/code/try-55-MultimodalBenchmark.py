import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Enhanced exponential terms with chaotic coupling and multi-scale modulation
        for i in range(self.dim):
            # Base exponential term with variable scaling
            result += 0.45 * (np.exp(0.55 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with varying amplitudes
            result += 0.65 * (np.sin(3.2 * np.pi * x[i]) + 
                            0.55 * np.sin(7.2 * np.pi * x[i]) + 
                            0.35 * np.sin(10.2 * np.pi * x[i]))
            
            # Chaotic coupling with stronger and more complex phase relationships
            if i < self.dim - 1:
                coupling_strength = 0.55 * np.exp(-0.045 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(4.2 * (x[i] - x[i+1]) + 0.85 * np.cos(x[i]) + 0.35 * np.sin(x[i+1]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.27 * x[i]**3 * np.cos(0.55 * x[i]) + 0.11 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 5 + int(3.2 * np.sin(i * 0.62))
            sign = (-1)**(i % 4)
            result += 0.16 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.11 * distance**2) * np.sin(0.72 * (x[i] + x[j]) + 0.42 * distance)
                result += 0.27 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.042 * np.sum(np.abs(x)**1.92) + 0.022 * np.sum(np.sin(15.2 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(3.2 * x[i]) * np.exp(-0.16 * x[i]**2)
        result += 0.22 * chaotic_component
        
        # Add dimensionality-dependent scaling factor
        result *= (1.0 + 0.11 * np.log(self.dim + 1))
        
        # Add cross-dimensional interaction terms with fractal characteristics
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(2.2 * x[i] * x[j]) * np.exp(-0.055 * (x[i]**2 + x[j]**2))
                result += 0.11 * interaction
        
        return result