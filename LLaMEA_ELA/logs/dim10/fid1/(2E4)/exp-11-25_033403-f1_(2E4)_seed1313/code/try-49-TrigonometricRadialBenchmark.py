import numpy as np

class TrigonometricRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.amplitude = 3.0
        self.frequency = 4.0
        self.radial_decay = 0.2
        self.conditioning_factor = 2.0
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = self.radial_decay * r**3 * np.sin(self.frequency * r) * np.cos(0.7 * r)
        
        # Enhanced trigonometric components with chaotic interference
        trig_sum = 0.0
        for i in range(self.dim):
            # Chaotic combination of sine/cosine terms with different frequencies and phases
            term1 = np.sin(self.frequency * x[i])
            term2 = 0.5 * np.cos(2 * self.frequency * x[i])
            term3 = 0.3 * np.sin(0.5 * self.frequency * x[i])
            term4 = 0.1 * np.sin(3 * self.frequency * x[i])
            trig_sum += (term1 + term2 + term3 + term4)**2
            
        # Enhanced cross-dimensional coupling with chaotic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic cross-interaction with multiple harmonic components
                cross_interaction = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j])) * np.sin(0.3 * x[i])
                cross_term += cross_interaction
                
        # Enhanced adaptive conditioning with chaotic scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Chaotic non-uniform scaling with exponential growth and oscillation
            scale = self.conditioning_factor**(i / self.dim) * (1 + 0.3 * np.sin(2 * i))
            condition_term += scale * (x[i]**4 + x[i]**6 + 0.5 * x[i]**8)
            
        # Enhanced periodic valley structure with chaotic depth variations
        valley_term = 0.0
        for i in range(self.dim):
            # Create chaotic valleys with varying depths and widths
            valley_depth = 1.0 + 0.7 * np.sin(2 * self.frequency * x[i]) * np.cos(0.5 * x[i])
            valley_width = 1.0 + 0.3 * np.sin(3 * x[i])
            valley_term += valley_depth * (x[i] - np.sin(x[i]))**2 * valley_width
            
        # Additional chaotic noise components for increased complexity
        noise = 0.02 * np.sum(np.sin(15 * x)**2 + 0.5 * np.cos(7 * x)**2)
        
        return radial_term + trig_sum + cross_term + condition_term + valley_term + noise