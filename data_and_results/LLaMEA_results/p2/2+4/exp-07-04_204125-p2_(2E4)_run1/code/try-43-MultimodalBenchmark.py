import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Exponential terms with chaotic coupling and multi-scale modulation
        for i in range(self.dim):
            # Base exponential term with variable scaling
            result += np.exp(0.4 * x[i]**2) - 1.0
            
            # Multi-frequency sinusoidal modulations with increased complexity
            result += 0.5 * (np.sin(2.0 * np.pi * x[i]) + 
                            0.6 * np.sin(5.0 * np.pi * x[i]) + 
                            0.4 * np.sin(8.0 * np.pi * x[i]) +
                            0.2 * np.sin(12.0 * np.pi * x[i]))
            
            # Chaotic coupling with varying strength and phase, enhanced coupling
            if i < self.dim - 1:
                coupling_strength = 0.4 * np.exp(-0.03 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(3.0 * (x[i] - x[i+1]) + 0.7 + 0.3 * np.sin(0.5 * x[i]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with cubic and quartic components, enhanced
            result += 0.2 * x[i]**3 * np.cos(0.4 * x[i]) + 0.08 * x[i]**4
            
            # Higher-order polynomial with random sign flips and variable exponents, more aggressive
            exponent = 6 + int(4 * np.sin(i * 1.3))
            sign = (-1)**(i % 4)
            result += 0.12 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with periodic modulation, stronger effects
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.08 * distance**2) * np.sin(0.7 * (x[i] + x[j]) + 0.3 * distance)
                result += 0.2 * coupling
        
        # Add non-smooth, non-convex perturbations with fractal-like characteristics, more aggressive
        result += 0.03 * np.sum(np.abs(x)**1.8) + 0.02 * np.sum(np.sin(15.0 * x))
        
        # Add a chaotic attractor-like component for additional complexity, enhanced
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.08 * x[i]**2)
        result += 0.15 * chaotic_component
        
        # Add new fractal-like perturbation with variable exponent
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += np.sin(20.0 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        result += 0.08 * fractal_perturbation
        
        # Add dimensionality-dependent scaling factor
        result *= (1.0 + 0.1 * self.dim)
        
        return result