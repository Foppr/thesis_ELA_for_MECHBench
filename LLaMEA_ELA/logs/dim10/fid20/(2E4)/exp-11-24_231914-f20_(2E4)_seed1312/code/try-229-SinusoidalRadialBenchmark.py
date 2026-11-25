import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Sinusoidal perturbation parameters
        self.sin_freq = np.random.uniform(1.0, 10.0, size=dim)
        self.sin_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.sin_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=(dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 2.0, size=10)
        # Adaptive noise parameters
        self.noise_level = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_decay = np.random.uniform(0.1, 0.9, size=dim)
        # Multi-scale harmonic components
        self.harmonic_freqs = np.random.uniform(0.5, 5.0, size=(dim, 3))
        self.harmonic_amps = np.random.uniform(0.2, 1.5, size=(dim, 3))
        # Basin-like attraction wells
        self.well_centers = np.random.uniform(-4.0, 4.0, size=(dim, 4))
        self.well_strengths = np.random.uniform(1.0, 3.0, size=4)
        # Exponential decay terms
        self.decay_rates = np.random.uniform(0.1, 0.5, size=dim)
        # Cross-term interaction weights
        self.cross_weights = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal perturbation component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(10):
            dist = np.sum((x - self.rbf_centers[:, i])**2)
            rbf_component += np.exp(-dist / (2 * self.rbf_widths[i]**2))
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_level = self.noise_level[i] * np.exp(-self.noise_decay[i] * np.abs(x[i]))
            noise_component += noise_level * np.random.uniform(-1, 1)
            
        # Harmonic interaction component
        harmonic_component = 0.0
        for i in range(self.dim):
            for j in range(3):
                harmonic_component += self.harmonic_amps[i, j] * np.cos(self.harmonic_freqs[i, j] * x[i])
                
        # Basin attraction component
        basin_component = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for k in range(4):
                dist = np.abs(x[i] - self.well_centers[i, k])
                if dist < min_dist:
                    min_dist = dist
            basin_component += self.well_strengths[k] * np.exp(-min_dist**2 / 2)
            
        # Exponential decay component
        decay_component = 0.0
        for i in range(self.dim):
            decay_component += np.exp(-self.decay_rates[i] * np.abs(x[i]))
            
        # Cross-term interaction
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_component += self.cross_weights[i, j] * x[i] * x[j]
                    
        # Combined fitness function
        return (1.2 * sin_component + 
                1.5 * rbf_component + 
                0.8 * noise_component + 
                1.3 * harmonic_component + 
                1.0 * basin_component + 
                0.7 * decay_component + 
                0.9 * cross_component)