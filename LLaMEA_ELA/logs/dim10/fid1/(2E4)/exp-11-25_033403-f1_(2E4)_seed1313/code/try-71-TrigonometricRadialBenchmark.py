import numpy as np

class TrigonometricRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.amplitude = 4.0
        self.frequency = 5.0
        self.radial_decay = 0.3
        self.conditioning_factor = 3.0
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = self.radial_decay * r**4 * np.sin(self.frequency * r) * np.cos(0.8 * r)
        
        # Enhanced trigonometric components with chaotic interference
        trig_sum = 0.0
        for i in range(self.dim):
            # Chaotic combination of sine/cosine terms with different frequencies and phases
            term1 = np.sin(self.frequency * x[i])
            term2 = 0.6 * np.cos(2 * self.frequency * x[i])
            term3 = 0.4 * np.sin(0.5 * self.frequency * x[i])
            term4 = 0.2 * np.sin(3 * self.frequency * x[i])
            trig_sum += (term1 + term2 + term3 + term4)**3
            
        # Enhanced cross-dimensional coupling with chaotic interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic cross-interaction with multiple harmonic components
                cross_interaction = np.sin(x[i] * x[j]) * np.cos(0.6 * (x[i] + x[j])) * np.sin(0.4 * x[i])
                cross_term += cross_interaction
                
        # Enhanced adaptive conditioning with chaotic scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Chaotic non-uniform scaling with exponential growth and oscillation
            scale = self.conditioning_factor**(i / self.dim) * (1 + 0.4 * np.sin(3 * i))
            condition_term += scale * (x[i]**5 + x[i]**7 + 0.6 * x[i]**9)
            
        # Enhanced periodic valley structure with chaotic depth variations
        valley_term = 0.0
        for i in range(self.dim):
            # Create chaotic valleys with varying depths and widths
            valley_depth = 1.0 + 0.8 * np.sin(2 * self.frequency * x[i]) * np.cos(0.6 * x[i])
            valley_width = 1.0 + 0.4 * np.sin(4 * x[i])
            valley_term += valley_depth * (x[i] - np.sin(x[i]))**3 * valley_width
            
        # Novel harmonic barrier structures for increased complexity
        barrier_term = 0.0
        for i in range(self.dim):
            # Add exponential barrier terms with chaotic modulation
            barrier = np.exp(3 * np.abs(x[i])) * (1 + 0.6 * np.sin(6 * x[i]))
            barrier_term += barrier
            
        # Additional chaotic noise components for increased complexity
        noise = 0.03 * np.sum(np.sin(20 * x)**2 + 0.6 * np.cos(8 * x)**2)
        
        # Improved fitness calculation with better balance of components
        total = radial_term + trig_sum + cross_term + condition_term + valley_term + barrier_term + noise
        
        # Add a global scaling factor to improve conditioning and prevent premature convergence
        scaling_factor = 1.0 + 0.15 * np.sin(0.6 * r)
        
        return total * scaling_factor