import numpy as np

class TrigonometricRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.amplitude = 2.0
        self.frequency = 3.0
        self.radial_decay = 0.1
        self.conditioning_factor = 1.5
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with periodic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = self.radial_decay * r**2 * np.sin(self.frequency * r)
        
        # Trigonometric components in each dimension
        trig_sum = 0.0
        for i in range(self.dim):
            # Multiple sine/cosine terms with different frequencies and phases
            term1 = np.sin(self.frequency * x[i])
            term2 = 0.5 * np.cos(2 * self.frequency * x[i])
            term3 = 0.3 * np.sin(0.5 * self.frequency * x[i])
            trig_sum += (term1 + term2 + term3)**2
            
        # Cross-dimensional coupling with radial interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                cross_term += cross_interaction
                
        # Adaptive conditioning based on dimension position
        condition_term = 0.0
        for i in range(self.dim):
            # Non-uniform scaling with exponential growth
            scale = self.conditioning_factor**(i / self.dim)
            condition_term += scale * (x[i]**4 + x[i]**6)
            
        # Periodic valley structure with multiple local minima
        valley_term = 0.0
        for i in range(self.dim):
            # Create periodic valleys with varying depths
            valley_depth = 1.0 + 0.5 * np.sin(2 * self.frequency * x[i])
            valley_term += valley_depth * (x[i] - np.sin(x[i]))**2
            
        # Add noise-like perturbations for increased complexity
        noise = 0.01 * np.sum(np.sin(10 * x)**2)
        
        return radial_term + trig_sum + cross_term + condition_term + valley_term + noise