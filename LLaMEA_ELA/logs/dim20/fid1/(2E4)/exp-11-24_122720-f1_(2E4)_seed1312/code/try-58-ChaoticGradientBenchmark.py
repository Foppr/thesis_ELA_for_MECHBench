import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with periodic forcing
        grad_component = 0.0
        for i in range(self.dim):
            # Base chaotic behavior with sine modulation
            base = np.sin(x[i] * (1.0 + 0.5 * np.sin(0.3 * x[i])))
            # Add periodic forcing with varying frequency
            forcing = np.sin(0.7 * x[i] + i * 0.2) * np.cos(0.4 * x[i] + i * 0.1)
            grad_component += base * forcing
            
        # Adaptive conditioning with dimension-dependent scaling
        cond_component = 0.0
        for i in range(self.dim):
            # Dynamic scaling factor based on dimension
            scale = 1.0 + 0.3 * np.sin(i * np.pi / self.dim)
            # Quadratic term with adaptive coefficients
            quad_term = scale * (x[i]**2) * (1.0 + 0.1 * np.sin(2.0 * x[i]))
            cond_component += quad_term
            
        # Periodic interaction component between dimensions
        periodic_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction term with periodic modulation
                interaction = np.sin(0.5 * (x[i] + x[j]) * (1.0 + 0.2 * np.cos(i * x[j])))
                periodic_component += interaction
                
        # Multi-scale oscillation with varying amplitudes
        oscillation_component = 0.0
        for i in range(self.dim):
            # Multiple frequency components
            freq1 = 2.0 + 0.5 * np.sin(i * 0.3)
            freq2 = 3.0 + 0.3 * np.cos(i * 0.4)
            oscillation_component += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            
        # Combine all components with dynamic weights
        weight1 = 0.3 + 0.2 * np.sin(self.dim * 0.1)
        weight2 = 0.4 + 0.1 * np.cos(self.dim * 0.15)
        weight3 = 0.2 + 0.15 * np.sin(self.dim * 0.2)
        weight4 = 0.1 + 0.05 * np.cos(self.dim * 0.25)
        
        # Add noise for additional complexity
        noise = 0.02 * np.random.normal(0, 1)
        
        return (weight1 * grad_component + 
                weight2 * cond_component + 
                weight3 * periodic_component + 
                weight4 * oscillation_component + 
                self.dim * 0.3 + noise)