import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Enhanced exponential terms with modified scaling and chaotic coupling
        for i in range(self.dim):
            # Base exponential term with adjusted scaling
            result += 0.65 * (np.exp(0.7 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with altered amplitudes
            result += 0.8 * (np.sin(5.0 * np.pi * x[i]) + 
                            0.7 * np.sin(10.0 * np.pi * x[i]) + 
                            0.5 * np.sin(15.0 * np.pi * x[i]))
            
            # Chaotic coupling with modified phase relationships and stronger coupling
            if i < self.dim - 1:
                coupling_strength = 0.7 * np.exp(-0.06 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(5.0 * (x[i] - x[i+1]) + 1.0 * np.cos(x[i]) + 0.4 * np.sin(x[i+1]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.35 * x[i]**3 * np.cos(0.7 * x[i]) + 0.2 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 7 + int(5 * np.sin(i * 0.8))
            sign = (-1)**(i % 5)
            result += 0.2 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.2 * distance**2) * np.sin(1.0 * (x[i] + x[j]) + 0.6 * distance)
                result += 0.35 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.06 * np.sum(np.abs(x)**2.2) + 0.04 * np.sum(np.sin(20.0 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.25 * x[i]**2)
        result += 0.3 * chaotic_component
        
        # Add additional fractal-like chaotic perturbations
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += np.sin(25.0 * x[i]) * np.cos(12.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        result += 0.22 * fractal_perturbation
        
        # Add irregular perturbations to increase complexity
        irregular_perturbation = 0.0
        for i in range(self.dim):
            irregular_perturbation += np.sin(30.0 * x[i]) * np.cos(15.0 * x[i]) * np.exp(-0.05 * x[i]**2) + 0.05 * np.sin(50.0 * x[i])
        result += 0.15 * irregular_perturbation
        
        # Add dimensionality-dependent scaling factor
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result