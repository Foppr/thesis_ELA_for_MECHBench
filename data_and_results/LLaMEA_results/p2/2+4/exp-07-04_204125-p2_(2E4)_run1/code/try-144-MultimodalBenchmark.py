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
            result += 0.8 * (np.exp(0.85 * x[i]**2) - 1.0)
            
            # Multi-frequency sinusoidal modulations with altered amplitudes
            result += 0.95 * (np.sin(6.2 * np.pi * x[i]) + 
                            0.85 * np.sin(12.2 * np.pi * x[i]) + 
                            0.65 * np.sin(18.2 * np.pi * x[i]))
            
            # Chaotic coupling with modified phase relationships and stronger coupling
            if i < self.dim - 1:
                coupling_strength = 0.85 * np.exp(-0.075 * (x[i]**2 + x[i+1]**2))
                phase = np.sin(6.2 * (x[i] - x[i+1]) + 1.25 * np.cos(x[i]) + 0.55 * np.sin(x[i+1]))
                result += coupling_strength * phase
            
            # Saddle-point inducing terms with enhanced cubic and quartic components
            result += 0.42 * x[i]**3 * np.cos(0.82 * x[i]) + 0.26 * x[i]**4
            
            # Higher-order polynomial with randomized exponents and enhanced sign flips
            exponent = 8 + int(6 * np.sin(i * 0.92))
            sign = (-1)**(i % 7)
            result += 0.26 * sign * x[i]**exponent
        
        # Add long-range inter-variable coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(i - j)
                coupling = np.exp(-0.25 * distance**2) * np.sin(1.22 * (x[i] + x[j]) + 0.72 * distance)
                result += 0.42 * coupling
        
        # Add non-smooth, non-convex perturbations with stronger fractal-like characteristics
        result += 0.075 * np.sum(np.abs(x)**2.35) + 0.055 * np.sum(np.sin(22.2 * x))
        
        # Add enhanced chaotic attractor-like component for additional complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i]) * np.cos(5.2 * x[i]) * np.exp(-0.32 * x[i]**2)
        result += 0.36 * chaotic_component
        
        # Add additional fractal-like chaotic perturbations
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += np.sin(28.2 * x[i]) * np.cos(14.2 * x[i]) * np.exp(-0.125 * x[i]**2)
        result += 0.26 * fractal_perturbation
        
        # Add irregular perturbations to increase complexity
        irregular_perturbation = 0.0
        for i in range(self.dim):
            irregular_perturbation += np.sin(33.2 * x[i]) * np.cos(17.2 * x[i]) * np.exp(-0.062 * x[i]**2) + 0.062 * np.sin(55.2 * x[i])
        result += 0.19 * irregular_perturbation
        
        # Add dimensionality-dependent scaling factor
        dim_factor = 1.0 + 0.125 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result