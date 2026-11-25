import numpy as np

class SinusoidalRBFNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Sinusoidal parameters
        self.sin_freq = np.random.uniform(1.0, 10.0, size=dim)
        self.sin_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.sin_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Radial Basis Functions parameters
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=(dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=10)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=10)
        # Adaptive noise parameters
        self.noise_scale = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 3.0, size=dim)
        # Multi-scale interaction terms
        self.interaction_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Basin-like regions
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=5)
        self.basin_radii = np.random.uniform(0.5, 2.0, size=5)
        self.basin_depths = np.random.uniform(1.0, 5.0, size=5)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            
        # Radial Basis Functions component
        rbf_component = 0.0
        for j in range(10):
            rbf_val = 0.0
            for i in range(self.dim):
                rbf_val += (x[i] - self.rbf_centers[i, j])**2
            rbf_component += self.rbf_weights[j] * np.exp(-rbf_val / (2 * self.rbf_widths[j]**2))
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_scale[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Multi-scale interaction terms
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_weights[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Basin-like regions component
        basin_component = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for k in range(5):
                dist = np.abs(x[i] - self.basin_centers[k])
                if dist < min_dist:
                    min_dist = dist
            if min_dist <= self.basin_radii[k]:
                basin_component += self.basin_depths[k] * (1 - min_dist / self.basin_radii[k])
            
        # Combined fitness function with balanced weights
        return (1.2 * sin_component + 
                1.5 * rbf_component + 
                0.8 * noise_component + 
                1.3 * interaction_component + 
                0.7 * basin_component)