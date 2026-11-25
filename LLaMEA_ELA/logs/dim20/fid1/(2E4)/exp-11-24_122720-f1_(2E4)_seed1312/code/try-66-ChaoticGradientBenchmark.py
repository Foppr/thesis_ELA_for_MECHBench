import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient component with modified sine modulation
        grad_component = 0.0
        for i in range(self.dim):
            # Enhanced chaotic behavior with multiple sine modulations
            base = np.sin(x[i] * (1.0 + 0.3 * np.sin(0.5 * x[i]) + 0.2 * np.cos(0.3 * x[i])))
            # Enhanced periodic forcing with phase shifts
            forcing = np.sin(0.8 * x[i] + i * 0.25) * np.cos(0.5 * x[i] + i * 0.15) * np.sin(0.6 * x[i] + i * 0.3)
            grad_component += base * forcing
            
        # Improved adaptive conditioning with exponential scaling
        cond_component = 0.0
        for i in range(self.dim):
            # Exponential scaling factor based on dimension
            scale = 1.0 + 0.4 * np.exp(-0.1 * i) * np.sin(i * np.pi / self.dim)
            # Modified quadratic term with higher-order polynomial
            quad_term = scale * (x[i]**2) * (1.0 + 0.15 * np.sin(3.0 * x[i]) + 0.05 * np.cos(2.0 * x[i]))
            cond_component += quad_term
            
        # Enhanced periodic interaction component between dimensions
        periodic_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced interaction term with multiple modulation frequencies
                interaction = np.sin(0.6 * (x[i] + x[j]) * (1.0 + 0.3 * np.cos(i * x[j] + j * x[i])))
                interaction += 0.5 * np.cos(0.4 * (x[i] - x[j]) * (1.0 + 0.2 * np.sin(i * x[i] + j * x[j])))
                periodic_component += interaction
                
        # Multi-scale oscillation with enhanced frequency components
        oscillation_component = 0.0
        for i in range(self.dim):
            # Multiple frequency components with dynamic amplitudes
            freq1 = 2.5 + 0.4 * np.sin(i * 0.3) + 0.2 * np.cos(i * 0.2)
            freq2 = 3.5 + 0.3 * np.cos(i * 0.4) + 0.1 * np.sin(i * 0.3)
            freq3 = 1.5 + 0.2 * np.sin(i * 0.5) + 0.1 * np.cos(i * 0.4)
            oscillation_component += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.sin(freq3 * x[i])
            
        # Enhanced dynamic weights with more complex modulation
        weight1 = 0.35 + 0.15 * np.sin(self.dim * 0.12)
        weight2 = 0.45 + 0.1 * np.cos(self.dim * 0.18)
        weight3 = 0.15 + 0.1 * np.sin(self.dim * 0.22)
        weight4 = 0.05 + 0.05 * np.cos(self.dim * 0.28)
        
        # Add enhanced noise for additional complexity
        noise = 0.03 * np.random.normal(0, 1)
        
        return (weight1 * grad_component + 
                weight2 * cond_component + 
                weight3 * periodic_component + 
                weight4 * oscillation_component + 
                self.dim * 0.35 + noise)