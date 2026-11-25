import numpy as np

class SpectralChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map chaotic parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, size=dim)
        self.logistic_offset = np.random.uniform(-0.1, 0.1, size=dim)
        # Spectral decomposition components
        self.spectral_freq = np.random.uniform(0.5, 2.0, size=dim)
        self.spectral_amp = np.random.uniform(0.5, 2.5, size=dim)
        # Adaptive terrain scaling
        self.scaling_factors = np.random.uniform(0.5, 3.0, size=dim)
        self.scaling_centers = np.random.uniform(-4.0, 4.0, size=dim)
        # Multi-scale correlation weights
        self.correlation_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Dynamic fitness landscape parameters
        self.landscape_shifts = np.random.uniform(-1.0, 1.0, size=dim)
        self.landscape_scales = np.random.uniform(0.5, 2.0, size=dim)
        # Nonlinear frequency modulation
        self.modulation_freq = np.random.uniform(0.1, 1.0, size=dim)
        self.modulation_amp = np.random.uniform(0.1, 0.5, size=dim)
        # Basin interaction parameters
        self.basin_positions = np.random.uniform(-4.0, 4.0, size=(3, dim))
        self.basin_strengths = np.random.uniform(0.5, 2.0, size=3)
        # Periodic boundary effects
        self.periodic_freq = np.random.uniform(1.0, 5.0, size=dim)
        self.periodic_amp = np.random.uniform(0.1, 0.5, size=dim)
        
    def logistic_map(self, x, r):
        return r * x * (1 - x)
    
    def spectral_component(self, x, freq, amp):
        return amp * np.sin(freq * x) + amp * np.cos(freq * x)
    
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        logistic_component = 0.0
        for i in range(self.dim):
            logistic_val = self.logistic_map(np.abs(x[i]), self.logistic_r[i])
            logistic_component += logistic_val * np.exp(-self.logistic_offset[i] * x[i]**2)
        
        # Spectral decomposition component
        spectral_component = 0.0
        for i in range(self.dim):
            spectral_component += self.spectral_component(x[i], self.spectral_freq[i], self.spectral_amp[i])
            
        # Adaptive terrain scaling component
        scaling_component = 0.0
        for i in range(self.dim):
            scale_factor = self.scaling_factors[i]
            center = self.scaling_centers[i]
            scaling_component += scale_factor * np.exp(-((x[i] - center)**2) / (2 * 1.0**2))
            
        # Multi-scale correlation component
        correlation_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    correlation_component += self.correlation_weights[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Dynamic fitness landscape component
        dynamic_component = 0.0
        for i in range(self.dim):
            shift = self.landscape_shifts[i]
            scale = self.landscape_scales[i]
            dynamic_component += scale * np.sin(x[i] + shift) * np.cos(x[i] * scale)
            
        # Nonlinear frequency modulation component
        modulation_component = 0.0
        for i in range(self.dim):
            mod_val = self.modulation_amp[i] * np.sin(self.modulation_freq[i] * x[i])
            modulation_component += mod_val * np.exp(-x[i]**2 / 10)
            
        # Basin interaction component
        basin_component = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for k in range(3):
                dist = np.abs(x[i] - self.basin_positions[k, i])
                if dist < min_dist:
                    min_dist = dist
            basin_component += self.basin_strengths[k] * np.exp(-min_dist**2)
            
        # Periodic boundary effects component
        periodic_component = 0.0
        for i in range(self.dim):
            periodic_component += self.periodic_amp[i] * np.sin(self.periodic_freq[i] * x[i])
        
        # Combined fitness function with balanced weights
        return (1.2 * logistic_component + 
                1.5 * spectral_component + 
                1.3 * scaling_component + 
                1.7 * correlation_component + 
                1.1 * dynamic_component + 
                0.9 * modulation_component + 
                1.4 * basin_component + 
                0.8 * periodic_component)