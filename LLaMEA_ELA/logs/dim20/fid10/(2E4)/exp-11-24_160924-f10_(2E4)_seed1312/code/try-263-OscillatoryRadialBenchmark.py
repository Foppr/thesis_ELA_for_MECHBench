import numpy as np

class OscillatoryRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.radial_exponents = np.random.uniform(1.0, 3.0, dim)
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add radial sinusoidal components with varying conditioning
        for i in range(self.dim):
            xi = x[i]
            amp = self.amplitudes[i]
            freq = self.frequencies[i]
            phase = self.phase_shifts[i]
            exp = self.radial_exponents[i]
            cond = self.conditioning_factors[i]
            
            # Radial term with sinusoidal modulation
            radial_distance = np.sqrt(np.sum(x**2))
            radial_term = amp * np.sin(freq * radial_distance + phase) * (1.0 + 0.1 * xi**2)
            
            # Add gradient-dependent conditioning
            grad_cond = cond * (1.0 + 0.5 * np.sin(2.0 * xi))
            
            result += radial_term * grad_cond
            
        # Add cross-dimensional coupling with periodic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                
                # Periodic coupling between dimensions
                coupling = np.sin(0.5 * (xi + xj)) * np.cos(0.3 * (xi - xj))
                result += 0.5 * coupling
                
        # Add a global periodic modulation
        global_mod = np.sin(0.2 * np.sum(x))
        result += 0.3 * global_mod
        
        # Add conditioning-dependent scaling
        scaling = 1.0 + 0.2 * np.sum(self.conditioning_factors)
        result *= scaling
        
        return result