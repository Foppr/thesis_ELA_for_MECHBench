import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.frequency_range = np.random.uniform(1.0, 5.0, dim)
        self.amplitude_range = np.random.uniform(0.5, 2.0, dim)
        self.chaos_factor = np.random.uniform(0.1, 0.9, dim)
        self.radial_decay = np.random.uniform(0.1, 0.5, dim)
        self.cross_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        self.dynamic_conditioning = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric component with dynamic frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.frequency_range[i] * (1.0 + 0.2 * np.sin(x[i]))
            amp = self.amplitude_range[i] * (1.0 + 0.1 * np.cos(x[i]))
            trig_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Radial component with decay and chaotic modulation
        radial_term = 0.0
        center = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sqrt(np.sum((x - center)**2))
            radial_term += self.radial_decay[i] * np.exp(-dist**2 / (2.0 * self.dynamic_conditioning[i]**2)) * np.sin(dist * self.chaos_factor[i])
            
        # Chaotic component using logistic map dynamics
        chaotic_term = 0.0
        for i in range(self.dim):
            # Initialize chaotic sequence with small perturbation
            x_chaos = 0.5 + 0.1 * np.sin(i)
            for _ in range(10):
                x_chaos = 4.0 * x_chaos * (1.0 - x_chaos)
            chaotic_term += np.sin(x_chaos * x[i]) * self.chaos_factor[i]
            
        # Cross-dimensional coupling with dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = self.cross_coupling[i, j] * np.cos(x[i] - x[j])
                    cross_term += weight * np.sin(0.5 * (x[i]**2 + x[j]**2))
                    
        # Dynamic conditioning with time-varying parameters
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = self.dynamic_conditioning[i] * (1.0 + 0.3 * np.sin(x[i]))
            cond_term += cond_factor * x[i]**4 * np.cos(0.2 * x[i])
            
        # Boundary attraction term to encourage convergence
        boundary_term = 0.0
        for i in range(self.dim):
            boundary_term += 5.0 * (1.0 / (1.0 + np.exp(-2.0 * (x[i] - 4.0))) + 
                                  1.0 / (1.0 + np.exp(2.0 * (x[i] + 4.0))))
            
        # Combined fitness function with adaptive weighting
        total = 0.7 * trig_term + 0.8 * radial_term + 0.6 * chaotic_term + 0.5 * cross_term + 0.9 * cond_term + 0.3 * boundary_term
        
        return total