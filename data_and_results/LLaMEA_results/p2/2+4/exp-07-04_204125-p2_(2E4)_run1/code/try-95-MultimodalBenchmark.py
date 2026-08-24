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
            result += 0.7 * (np.exp(0.85 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with altered amplitudes
            result += 0.85 * (np.sin(5.5 * np.pi * x[i]) + 
                            0.75 * np.sin(11.0 * np.pi * x[i]) + 
                            0.55 * np.sin(16.5 * np.pi * x[i]))
            
            # Chaotic coupling with modified phase relationships and stronger coupling
            if i < self.dim - 1:
                coupling_strength = 0.75 * np.exp(-0.06 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(5.5 * (x[i] - x[i+1]) + 1.1 * np.cos(x[i]) + 0.45 * np.sin(x[i+1]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.35 * x[i]**3 * np.cos(0.75 * x[i]) + 0.2 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 7 + int(5 * np.sin(i * 0.85))
            sign = (-1)**(i % 6)
            result += 0.23 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.23 * distance**2) * np.sin(1.1 * (x[i] + x[j]) + 0.65 * distance)
                result += 0.38 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.075 * np.sum(np.abs(x)**2.2) + 0.055 * np.sum(np.sin(24.0 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(4.5 * x[i]) * np.exp(-0.28 * x[i]**2)
        result += 0.33 * chaotic_component
        
        # Add additional fractal-like chaotic perturbations
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += np.sin(28.0 * x[i]) * np.cos(14.0 * x[i]) * np.exp(-0.14 * x[i]**2)
        result += 0.23 * fractal_perturbation
        
        # Add irregular perturbations to increase complexity
        irregular_perturbation = 0.0
        for i in range(self.dim):
            irregular_perturbation += np.sin(33.0 * x[i]) * np.cos(17.0 * x[i]) * np.exp(-0.05 * x[i]**2) + 0.065 * np.sin(58.0 * x[i])
        result += 0.18 * irregular_perturbation
        
        # Add dimensionality-dependent scaling factor with increased impact
        dim_factor = 1.0 + 0.14 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result