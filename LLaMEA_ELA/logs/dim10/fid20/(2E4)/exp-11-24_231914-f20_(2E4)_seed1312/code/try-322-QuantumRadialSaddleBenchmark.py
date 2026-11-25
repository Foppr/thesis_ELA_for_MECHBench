import numpy as np

class QuantumRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired oscillation parameters
        self.oscillation_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.oscillation_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.oscillation_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        
        # Saddle-point attractor parameters
        self.saddle_centers = np.random.uniform(-4.0, 4.0, size=(8, dim))
        self.saddle_strengths = np.random.uniform(1.0, 5.0, size=8)
        self.saddle_curvatures = np.random.uniform(0.5, 2.0, size=8)
        
        # Cross-dimensional interaction terms
        self.interaction_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        
        # Noise modulation parameters
        self.noise_level = np.random.uniform(0.1, 1.5, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 4.0, size=dim)
        
        # Basin depth variation
        self.basin_depths = np.random.uniform(0.5, 4.0, size=12)
        self.basin_centers = np.random.uniform(-4.2, 4.2, size=(12, dim))
        self.basin_radii = np.random.uniform(0.3, 2.5, size=12)

    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum oscillation component
        quantum_component = 0.0
        for i in range(self.dim):
            oscillation_val = self.oscillation_amp[i] * np.sin(self.oscillation_freq[i] * x[i] + self.oscillation_phase[i])
            quantum_component += oscillation_val
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(15):
            dist_sq = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_val = np.exp(-dist_sq / (2 * self.rbf_widths[i] ** 2))
            rbf_component += rbf_val
            
        # Saddle-point attractor component
        saddle_component = 0.0
        for i in range(8):
            dist_sq = np.sum((x - self.saddle_centers[i]) ** 2)
            curvature = self.saddle_curvatures[i]
            strength = self.saddle_strengths[i]
            saddle_val = strength * np.exp(-dist_sq / (2 * curvature ** 2))
            saddle_component += saddle_val
            
        # Cross-dimensional interaction
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_weights[i, j] * x[i] * x[j]
                    
        # Basin component with varying depths
        basin_component = 0.0
        for i in range(12):
            dist_sq = np.sum((x - self.basin_centers[i]) ** 2)
            if dist_sq <= self.basin_radii[i] ** 2:
                basin_val = self.basin_depths[i] * (1 - dist_sq / (self.basin_radii[i] ** 2))
                basin_component += basin_val
                
        # Noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_level[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Combine all components with appropriate weights
        return (1.5 * quantum_component + 
                1.3 * rbf_component + 
                1.2 * saddle_component + 
                0.8 * interaction_component + 
                1.0 * basin_component + 
                0.6 * noise_component)